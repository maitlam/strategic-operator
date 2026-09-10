#!/usr/bin/env python3
"""
Check whether Anthropic or borghei changed anything you copied into this repo.

Your own edits are never touched. This script only looks at the *upstream*
repos and compares the commit you last synced from (recorded in sources.json)
with their latest commit.

Usage (run from the repo root):
  python3 scripts/check_upstream.py                  # summary of what changed upstream
  python3 scripts/check_upstream.py --verbose        # ...and list everything that's up to date too
  python3 scripts/check_upstream.py --diff pre-mortem   # show the full upstream diff for one item
  python3 scripts/check_upstream.py --merge pre-mortem  # merge upstream changes into your copy (keeps your edits)
  python3 scripts/check_upstream.py --merge all
  python3 scripts/check_upstream.py --patch          # alternative: write .patch files for every changed item
  python3 scripts/check_upstream.py --mark-synced pre-mortem   # record that you've pulled in the changes
  python3 scripts/check_upstream.py --mark-synced all
  python3 scripts/check_upstream.py --add borghei business-operations/process-mapper plugins/bizops/skills/process-mapper

Items can be named by skill name (pre-mortem), plugin/name (bizops/SHARED_OUTPUT_SCHEMA.md), or full path.

Requires: git and Python 3.8+. --add and --merge also need PyYAML (pip install pyyaml).
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(ROOT, "sources.json")
CACHE = os.path.join(ROOT, ".cache")
PATCHES = os.path.join(ROOT, ".upstream-patches")


def git(repo_dir, *args, check=True):
    result = subprocess.run(
        ["git", "-C", repo_dir, *args], capture_output=True, text=True
    )
    if check and result.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{result.stderr.strip()}")
    return result.stdout


def refresh_upstream(name, cfg):
    """Keep a lightweight copy of each upstream repo in .cache/ (history only, files fetched on demand)."""
    path = os.path.join(CACHE, name)
    if not os.path.isdir(os.path.join(path, ".git")):
        os.makedirs(CACHE, exist_ok=True)
        print(f"Downloading history for '{name}' (first run only)...")
        subprocess.run(
            ["git", "clone", "--quiet", "--filter=blob:none", "--no-checkout",
             "--branch", cfg["branch"], cfg["repo"], path],
            check=True,
        )
    else:
        git(path, "fetch", "--quiet", "origin", cfg["branch"])
    return path, git(path, "rev-parse", f"origin/{cfg['branch']}").strip()


def item_name(item):
    """Short display name: plugin/name, e.g. programs/dependency-map."""
    parts = item["local"].rstrip("/").split("/")
    return f"{parts[1]}/{parts[-1]}" if len(parts) > 2 and parts[0] == "plugins" else parts[-1]


def matches(item, which):
    local = item["local"].rstrip("/")
    return which in (local, item_name(item), os.path.basename(local))


def find_items(data, which):
    if which == "all":
        return data["items"]
    found = [i for i in data["items"] if matches(i, which)]
    if not found:
        sys.exit(f"No tracked item named '{which}'. Try the skill name (e.g. pre-mortem) "
                 f"or plugin/name (e.g. programs/pre-mortem). Tracked items are listed in sources.json.")
    return found


def is_file(repo, sha, path):
    return git(repo, "cat-file", "-t", f"{sha}:{path}", check=False).strip() == "blob"


def upstream_commits(repo, item, head):
    return git(repo, "log", "--oneline", f"{item['synced_sha']}..{head}", "--", item["path"]).strip()


def upstream_diff(repo, item, head, rewrite_paths=False):
    args = ["diff", item["synced_sha"], head]
    single_file = False
    if rewrite_paths:
        # Rewrite upstream paths to where the files live in *this* repo, so `git apply` works.
        single_file = is_file(repo, item["synced_sha"], item["path"]) or is_file(repo, head, item["path"])
        if single_file:
            up_dir, local_dir = os.path.dirname(item["path"]), os.path.dirname(item["local"])
        else:
            up_dir, local_dir = item["path"].rstrip("/"), item["local"].rstrip("/")
        args += [f"--relative={up_dir}/" if up_dir else "--relative",
                 f"--src-prefix=a/{local_dir}/", f"--dst-prefix=b/{local_dir}/"]
    out = git(repo, *args, "--", item["path"])
    if single_file:
        # Handle a locally renamed file: point the patch at the local filename.
        up_name = os.path.join(os.path.dirname(item["local"]), os.path.basename(item["path"]))
        for prefix in ("a/", "b/", "diff --git a/", " b/"):
            out = out.replace(prefix + up_name, prefix + item["local"])
    return out


def git_bytes(repo_dir, *args):
    return subprocess.run(["git", "-C", repo_dir, *args], capture_output=True, check=True).stdout


LABEL_KEYS = ("provenance", "author", "source", "adapted-from", "changes")


def mirror_labels(local_file, upstream_copies):
    """
    Copy the provenance labels from your file into temporary copies of upstream's
    versions, in the same positions, so labels never show up as a merge conflict.
    """
    import skillmeta
    local_fm, err = skillmeta.load_frontmatter(local_file)
    if err or not local_fm:
        return
    local_meta = local_fm.get("metadata") or {}
    for path in upstream_copies:
        up_fm, up_err = skillmeta.load_frontmatter(path)
        if up_err or not up_fm:
            continue
        up_meta = up_fm.get("metadata") or {}
        added = {k: v for k, v in local_meta.items() if k in LABEL_KEYS and k not in up_meta}
        edited = {k: v for k, v in local_meta.items() if k in LABEL_KEYS and k in up_meta and up_meta[k] != v}
        license_name = local_fm.get("license") if "license" not in up_fm else None
        if edited:
            skillmeta.set_metadata_values(path, edited)
        if added or license_name:
            skillmeta.stamp(path, license_name=license_name, meta=added)


def merge_item(repo, item, head):
    """
    Three-way merge upstream's changes into the local copy, file by file:
    base = upstream at synced_sha, theirs = upstream at head, ours = your file.
    Returns (clean, notes). Conflicts are written into files with <<<<<<< markers.
    """
    single = git(repo, "cat-file", "-t", f"{head}:{item['path']}", check=False).strip() == "blob" or \
        git(repo, "cat-file", "-t", f"{item['synced_sha']}:{item['path']}", check=False).strip() == "blob"
    changes = git(repo, "diff", "--name-status", "--no-renames", item["synced_sha"], head, "--", item["path"]).split("\n")
    clean, notes = True, []
    for line in filter(None, changes):
        status, up_file = line.split("\t", 1)
        if single:
            local_file = os.path.join(ROOT, item["local"])
        else:
            local_file = os.path.join(ROOT, item["local"], os.path.relpath(up_file, item["path"]))
        shown = os.path.relpath(local_file, ROOT)
        base = git_bytes(repo, "show", f"{item['synced_sha']}:{up_file}") if status != "A" else b""
        theirs = git_bytes(repo, "show", f"{head}:{up_file}") if status != "D" else None
        exists = os.path.exists(local_file)

        if status == "D":
            if exists and open(local_file, "rb").read() == base:
                os.remove(local_file)
                notes.append(f"deleted  {shown} (removed upstream)")
            elif exists:
                clean = False
                notes.append(f"KEPT     {shown} (removed upstream, but you've changed it; decide by hand)")
            continue
        if not exists:
            os.makedirs(os.path.dirname(local_file), exist_ok=True)
            with open(local_file, "wb") as f:
                f.write(theirs)
            notes.append(f"added    {shown}")
            continue
        if b"\0" in theirs or b"\0" in base:
            clean = False
            notes.append(f"SKIPPED  {shown} (binary file changed upstream; copy it by hand if you want it)")
            continue
        with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as b, \
                tempfile.NamedTemporaryFile(delete=False, suffix=".md") as t:
            b.write(base)
            t.write(theirs)
        if local_file.endswith(".md"):
            mirror_labels(local_file, [b.name, t.name])
        result = subprocess.run(["git", "merge-file", "-L", "yours", "-L", "upstream (before)", "-L", "upstream (now)",
                                 local_file, b.name, t.name], capture_output=True)
        os.unlink(b.name)
        os.unlink(t.name)
        if result.returncode == 0:
            notes.append(f"merged   {shown}")
        else:
            clean = False
            notes.append(f"CONFLICT {shown} (look for <<<<<<< markers)")
    return clean, notes


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--diff", metavar="ITEM", help="show the full upstream diff for one item")
    parser.add_argument("--merge", metavar="ITEM", help="three-way merge upstream changes into an item (or 'all')")
    parser.add_argument("--patch", action="store_true", help="write .patch files for changed items")
    parser.add_argument("--mark-synced", metavar="ITEM", help="record an item (or 'all') as synced to upstream's latest")
    parser.add_argument("--verbose", action="store_true", help="also list items that are up to date")
    parser.add_argument("--add", nargs=3, metavar=("UPSTREAM", "UPSTREAM_PATH", "LOCAL_PATH"),
                        help="copy a new folder from an upstream and track it, e.g. "
                             "--add borghei project-management/senior-pm plugins/program-management/skills/senior-pm")
    opts = parser.parse_args()

    with open(SOURCES) as f:
        data = json.load(f)

    heads = {}
    for name, cfg in data["upstreams"].items():
        heads[name] = refresh_upstream(name, cfg)

    if opts.add:
        upstream, up_path, local = opts.add
        up_path, local = up_path.strip("/"), local.strip("/")
        if upstream not in heads:
            sys.exit(f"Unknown upstream '{upstream}'. Choices: {', '.join(heads)}")
        repo, head = heads[upstream]
        dest = os.path.join(ROOT, local)
        if os.path.exists(dest):
            sys.exit(f"{local} already exists. Delete it first or pick another LOCAL_PATH.")
        if git(repo, "cat-file", "-t", f"{head}:{up_path}", check=False).strip() != "tree":
            sys.exit(f"'{up_path}' isn't a folder in {upstream}'s latest commit. Check the path on GitHub.")
        os.makedirs(dest)
        archive = subprocess.run(["git", "-C", repo, "archive", head, up_path], capture_output=True, check=True)
        strip = str(len(up_path.split("/")))
        subprocess.run(["tar", "-x", f"--strip-components={strip}", "-C", dest], input=archive.stdout, check=True)
        data["items"].append({"local": local, "upstream": upstream, "path": up_path, "synced_sha": head})
        with open(SOURCES, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        print(f"Copied {upstream}:{up_path} -> {local} and recorded it in sources.json")
        skill_file = os.path.join(dest, "SKILL.md")
        if os.path.exists(skill_file):
            import skillmeta
            skillmeta.stamp_included(skill_file, data["upstreams"][upstream], up_path)
            print("Labeled it as Included (author, license, and source link added to its frontmatter)")
            import catalog
            catalog.build()
        return

    if opts.mark_synced:
        for item in find_items(data, opts.mark_synced):
            item["synced_sha"] = heads[item["upstream"]][1]
            print(f"Marked {item_name(item)} as synced to {item['synced_sha'][:10]}")
        with open(SOURCES, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        return

    if opts.merge:
        items = [i for i in find_items(data, opts.merge)
                 if upstream_commits(heads[i["upstream"]][0], i, heads[i["upstream"]][1])]
        if not items:
            print("Nothing to merge: upstream hasn't changed these items since you synced.")
            return
        conflicted = []
        for item in items:
            repo, head = heads[item["upstream"]]
            clean, notes = merge_item(repo, item, head)
            print(f"{item_name(item)}:")
            for note in notes:
                print(f"  {note}")
            if clean:
                item["synced_sha"] = head
            else:
                conflicted.append(item_name(item))
        with open(SOURCES, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        print()
        print("Review everything with `git diff` before committing.")
        if conflicted:
            print(f"Resolve the flagged files, then run: python3 scripts/check_upstream.py --mark-synced <item>")
            print(f"Needs attention: {', '.join(conflicted)}")
        else:
            print("All merges were clean and are marked as synced.")
        return

    if opts.diff:
        for item in find_items(data, opts.diff):
            repo, head = heads[item["upstream"]]
            print(upstream_diff(repo, item, head) or "No upstream changes.")
        return

    changed = 0
    for item in data["items"]:
        repo, head = heads[item["upstream"]]
        log = upstream_commits(repo, item, head)
        if not log:
            if opts.verbose:
                print(f"  up to date   {item_name(item)}  ({item['upstream']})")
            continue
        changed += 1
        stat = git(repo, "diff", "--shortstat", item["synced_sha"], head, "--", item["path"]).strip()
        print(f"* CHANGED      {item_name(item)}  ({item['upstream']}): {stat}")
        for line in log.splitlines()[:5]:
            print(f"               {line}")
        if opts.patch:
            os.makedirs(PATCHES, exist_ok=True)
            out = os.path.join(PATCHES, item_name(item).replace("/", "__") + ".patch")
            with open(out, "w") as f:
                f.write(upstream_diff(repo, item, head, rewrite_paths=True))
            print(f"               patch written: {os.path.relpath(out, ROOT)}")

    up_to_date = len(data["items"]) - changed
    print()
    if changed == 0:
        print(f"All {up_to_date} items you copied match upstream's latest. Nothing to do.")
    else:
        print(f"{changed} item(s) changed upstream ({up_to_date} up to date). Next steps:")
        print("  1. Review:  python3 scripts/check_upstream.py --diff <item>")
        print("  2. Merge:   python3 scripts/check_upstream.py --merge <item>   (your edits are kept)")
        print("  3. Review with `git diff`, resolve any conflict markers, and commit.")


if __name__ == "__main__":
    main()
