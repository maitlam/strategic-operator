#!/usr/bin/env python3
"""
Build and check the skill catalog from each skill's own frontmatter.

Every skill, command, and agent declares where it came from in its frontmatter
(metadata.provenance: original | adapted | included). This script turns that into
the catalog tables in the READMEs, so the READMEs can never drift from the files.

Usage (from the repo root; requires PyYAML: pip install pyyaml):
  python3 scripts/catalog.py                     # rebuild the catalog sections in all READMEs
  python3 scripts/catalog.py --check             # validate labels, sources.json, and READMEs (used by CI)
  python3 scripts/catalog.py --remove pm-interview-prep   # delete a skill and clean up after it
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skillmeta  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"
LABEL = {"original": "Original", "adapted": "Adapted", "included": "Included"}
ORDER = {"original": 0, "adapted": 1, "included": 2}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def load_json(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return json.load(f)


def plugins():
    return sorted(p for p in os.listdir(os.path.join(ROOT, "plugins"))
                  if os.path.isdir(os.path.join(ROOT, "plugins", p)))


def discover():
    """Every skill, command, and agent in every plugin."""
    entries = []
    for plugin in plugins():
        base = os.path.join(ROOT, "plugins", plugin)
        for f in sorted(glob.glob(os.path.join(base, "skills", "*", "SKILL.md"))):
            d = os.path.dirname(f)
            entries.append(dict(plugin=plugin, kind="skill", name=os.path.basename(d), file=f, local=rel(d)))
        for kind in ("commands", "agents"):
            for f in sorted(glob.glob(os.path.join(base, kind, "*.md"))):
                name = os.path.splitext(os.path.basename(f))[0]
                entries.append(dict(plugin=plugin, kind=kind[:-1], name=name, file=f, local=rel(f)))
    for e in entries:
        e["fm"], e["error"] = skillmeta.load_frontmatter(e["file"])
        meta = e["fm"].get("metadata") or {}
        e["meta"] = meta if isinstance(meta, dict) else {}
        e["provenance"] = str(e["meta"].get("provenance", "")).lower()
    return entries


def summary_line(description, limit=170):
    text = " ".join(str(description or "").split())
    m = re.search(r"(?<=[a-z0-9)])\.\s", text)
    if m and m.start() < limit:
        text = text[:m.start()]
    elif len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0] + "…"
    return text.rstrip(".").replace("|", "\\|")


def display(e, link_from):
    label = f"/{e['name']}" if e["kind"] == "command" else e["name"]
    suffix = "" if e["kind"] == "skill" else f" ({e['kind']})"
    return f"[`{label}`]({os.path.relpath(e['file'], link_from).replace(os.sep, '/')}){suffix}"


def plugin_table(plugin, entries):
    rows = sorted((e for e in entries if e["plugin"] == plugin),
                  key=lambda e: (ORDER.get(e["provenance"], 9), e["kind"] != "skill", e["name"]))
    base = os.path.join(ROOT, "plugins", plugin)
    out = ["| Skill | Type | What it does |", "|---|---|---|"]
    for e in rows:
        out.append(f"| {display(e, base)} | {LABEL.get(e['provenance'], '⚠ unlabeled')} | "
                   f"{summary_line(e['fm'].get('description'))} |")
    return "\n".join(out)


def root_summary(entries):
    out = ["| Plugin | Focus | Skills | Original | Adapted | Included |", "|---|---|---|---|---|---|"]
    totals = [0, 0, 0, 0]
    market_order = [p["name"] for p in load_json(".claude-plugin/marketplace.json")["plugins"]]
    ordered = [p for p in market_order if p in plugins()] + [p for p in plugins() if p not in market_order]
    for plugin in ordered:
        manifest = load_json(f"plugins/{plugin}/.claude-plugin/plugin.json")
        mine = [e for e in entries if e["plugin"] == plugin]
        counts = [len(mine)] + [sum(e["provenance"] == p for e in mine) for p in skillmeta.PROVENANCE]
        totals = [a + b for a, b in zip(totals, counts)]
        name = manifest.get("displayName", plugin)
        out.append(f"| [{name}](plugins/{plugin}/README.md) | {manifest.get('description', '')} | "
                   + " | ".join(map(str, counts)) + " |")
    out.append("| **Total** | | " + " | ".join(f"**{n}**" for n in totals) + " |")

    kinds = {k: sum(e["kind"] == k for e in entries) for k in ("skill", "command", "agent")}
    out.append("")
    out.append(f"Counts include {kinds['skill']} skills, {kinds['command']} "
               f"command{'s' if kinds['command'] != 1 else ''}, and {kinds['agent']} "
               f"agent{'s' if kinds['agent'] != 1 else ''}.")
    out.append("")
    out.append("### My original and adapted work")
    out.append("")
    mine = sorted((e for e in entries if e["provenance"] in ("original", "adapted")),
                  key=lambda e: (ORDER[e["provenance"]], e["plugin"], e["name"]))
    if not mine:
        out.append("_Nothing here yet. My own skills and agents will show up here as I build them._")
    for e in mine:
        out.append(f"- {display(e, ROOT)} · {LABEL[e['provenance']]} · {e['plugin']}: "
                   f"{summary_line(e['fm'].get('description'))}")
    return "\n".join(out)


def render_into(path, content):
    """Return the file text with the catalog section replaced, or None if markers are missing."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if START not in text or END not in text:
        return None, text
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{content}\n{END}{tail}", text


def targets(entries):
    yield os.path.join(ROOT, "README.md"), root_summary(entries)
    for plugin in plugins():
        yield os.path.join(ROOT, "plugins", plugin, "README.md"), plugin_table(plugin, entries)


def build(entries=None, quiet=False):
    entries = entries if entries is not None else discover()
    for path, content in targets(entries):
        if not os.path.exists(path):
            continue
        new, old = render_into(path, content)
        if new is not None and new != old:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new)
            if not quiet:
                print(f"updated {rel(path)}")
    return entries


def check():
    entries = discover()
    errors = []
    sources = load_json("sources.json")
    tracked = {i["local"]: i for i in sources["items"]}

    for e in entries:
        where = rel(e["file"])
        if e["error"]:
            errors.append(f"{where}: {e['error']}")
            continue
        fm, meta, prov = e["fm"], e["meta"], e["provenance"]
        if e["kind"] == "skill":
            if fm.get("name") != e["name"]:
                errors.append(f"{where}: frontmatter name '{fm.get('name')}' must match folder name '{e['name']}'")
            if not NAME_RE.match(e["name"]):
                errors.append(f"{where}: skill names must be lowercase letters, numbers, and hyphens")
        if not fm.get("description"):
            errors.append(f"{where}: missing description")
        if prov not in skillmeta.PROVENANCE:
            errors.append(f"{where}: metadata.provenance must be one of original, adapted, included")
            continue
        if not meta.get("author"):
            errors.append(f"{where}: metadata.author is required")
        if not fm.get("license"):
            errors.append(f"{where}: license is required")
        if prov == "original" and e["local"] in tracked:
            errors.append(f"{where}: marked original but listed in sources.json (original work has no upstream)")
        if prov in ("adapted", "included") and e["local"] not in tracked:
            errors.append(f"{where}: marked {prov} but not tracked in sources.json")
        if prov == "included" and not meta.get("source"):
            errors.append(f"{where}: included items need metadata.source (link to the original)")
        if prov == "adapted":
            if not meta.get("adapted-from"):
                errors.append(f"{where}: adapted items need metadata.adapted-from (link to the original)")
            if not meta.get("changes"):
                errors.append(f"{where}: adapted items need metadata.changes (one-line summary of what you changed)")
            if e["kind"] == "skill" and not os.path.exists(os.path.join(os.path.dirname(e["file"]), "CHANGES.md")):
                errors.append(f"{where}: adapted skills need a CHANGES.md in the skill folder explaining what and why")

    for local in tracked:
        if not os.path.exists(os.path.join(ROOT, local)):
            errors.append(f"sources.json: '{local}' no longer exists (run: python3 scripts/catalog.py --remove <name>, or delete the entry)")

    market = load_json(".claude-plugin/marketplace.json")
    listed = {p["name"]: p.get("source") for p in market["plugins"]}
    for plugin in plugins():
        if plugin not in listed:
            errors.append(f"marketplace.json: plugins/{plugin} exists but isn't listed")
        elif listed[plugin] != f"./plugins/{plugin}":
            errors.append(f"marketplace.json: '{plugin}' source should be ./plugins/{plugin}")
        manifest = load_json(f"plugins/{plugin}/.claude-plugin/plugin.json")
        if manifest.get("name") != plugin:
            errors.append(f"plugins/{plugin}/.claude-plugin/plugin.json: name must be '{plugin}'")
    for name in listed:
        if name not in plugins():
            errors.append(f"marketplace.json: lists '{name}' but plugins/{name} doesn't exist")

    for path, content in targets(entries):
        if not os.path.exists(path):
            errors.append(f"{rel(path)}: missing")
            continue
        new, old = render_into(path, content)
        if new is None:
            errors.append(f"{rel(path)}: missing {START} / {END} markers")
        elif new != old:
            errors.append(f"{rel(path)}: catalog is out of date (run: python3 scripts/catalog.py)")

    counts = {p: sum(e["provenance"] == p for e in entries) for p in skillmeta.PROVENANCE}
    if errors:
        print(f"✗ {len(errors)} problem(s) found:\n")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    print(f"✓ {len(entries)} items checked: {counts['original']} original, "
          f"{counts['adapted']} adapted, {counts['included']} included. READMEs are up to date.")


def remove(target):
    entries = discover()
    matches = [e for e in entries if target in (e["name"], f"{e['plugin']}/{e['name']}", e["local"])]
    if not matches:
        data = load_json("sources.json")
        stale = [i for i in data["items"] if not os.path.exists(os.path.join(ROOT, i["local"]))
                 and target in (i["local"], os.path.basename(i["local"].rstrip("/")))]
        if stale:
            data["items"] = [i for i in data["items"] if i not in stale]
            with open(os.path.join(ROOT, "sources.json"), "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                f.write("\n")
            print(f"'{target}' was already deleted; removed its leftover sources.json entry")
            build(entries)
            return
        sys.exit(f"No skill, command, or agent named '{target}'.")
    if len(matches) > 1:
        options = ", ".join(f"{e['plugin']}/{e['name']}" for e in matches)
        sys.exit(f"'{target}' matches more than one item. Use one of: {options}")
    e = matches[0]
    if e["kind"] == "skill":
        shutil.rmtree(os.path.dirname(e["file"]))
    else:
        os.remove(e["file"])
    path = os.path.join(ROOT, "sources.json")
    data = load_json("sources.json")
    before = len(data["items"])
    data["items"] = [i for i in data["items"] if i["local"] != e["local"]]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"removed {e['local']}" + (" and its sources.json entry" if len(data["items"]) < before else ""))
    build([x for x in entries if x is not e])


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="validate everything; exit 1 on problems")
    parser.add_argument("--remove", metavar="NAME", help="delete a skill/command/agent and update sources.json and READMEs")
    opts = parser.parse_args()
    if opts.check:
        check()
    elif opts.remove:
        remove(opts.remove)
    else:
        build()


if __name__ == "__main__":
    main()
