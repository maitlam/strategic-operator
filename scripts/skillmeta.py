"""
Shared helpers for reading SKILL.md / command / agent frontmatter and stamping
provenance labels (original / adapted / included) into it.

Stamping edits the text directly instead of re-writing the YAML, so the original
author's formatting, comments, and key order stay exactly as they were.
"""
import json
import re

PROVENANCE = ("original", "adapted", "included")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
PLAIN_SAFE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_./:+()@-]*( [A-Za-z0-9_./:+()@,-]+)*$")


def require_yaml():
    try:
        import yaml  # noqa: F401
        return yaml
    except ImportError:
        raise SystemExit("PyYAML is required for this command. Install it with:  pip install pyyaml")


def split_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def load_frontmatter(path):
    """Return (dict, error). dict is {} when the file has no frontmatter."""
    yaml = require_yaml()
    with open(path, encoding="utf-8") as f:
        fm, _ = split_frontmatter(f.read())
    if fm is None:
        return {}, "missing YAML frontmatter (the file must start with ---)"
    try:
        data = yaml.safe_load(fm) or {}
    except yaml.YAMLError as e:
        return {}, f"frontmatter is not valid YAML: {e}"
    if not isinstance(data, dict):
        return {}, "frontmatter must be a YAML mapping"
    return data, None


def _scalar(value):
    value = str(value)
    if PLAIN_SAFE.match(value) and ": " not in value and " #" not in value:
        return value
    return json.dumps(value)  # a JSON string is always a valid YAML string


def stamp(path, license_name=None, meta=None):
    """
    Add `license` (if missing) and `metadata` keys (if missing) to a file's frontmatter.
    Existing keys are never overwritten. Returns True if the file changed.
    """
    meta = meta or {}
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm, body = split_frontmatter(text)
    if fm is None:
        raise ValueError(f"{path}: no frontmatter to stamp")
    lines = fm.split("\n")
    changed = False

    top_keys = {m.group(1) for m in (re.match(r"^([A-Za-z0-9_-]+):", l) for l in lines) if m}
    meta_idx = next((i for i, l in enumerate(lines) if re.match(r"^metadata:\s*$", l)), None)

    if license_name and "license" not in top_keys:
        insert_at = meta_idx if meta_idx is not None else len(lines)
        lines.insert(insert_at, f"license: {_scalar(license_name)}")
        if meta_idx is not None:
            meta_idx += 1
        changed = True

    if meta:
        if meta_idx is None:
            lines.append("metadata:")
            meta_idx = len(lines) - 1
            indent, existing = "  ", set()
        else:
            nxt = lines[meta_idx + 1] if meta_idx + 1 < len(lines) else ""
            indent = re.match(r"^(\s*)", nxt).group(1) or "  "
            existing, j = set(), meta_idx + 1
            while j < len(lines) and (lines[j].startswith(indent) or not lines[j].strip()):
                m = re.match(r"^\s+([A-Za-z0-9_-]+):", lines[j])
                if m and len(re.match(r"^(\s*)", lines[j]).group(1)) == len(indent):
                    existing.add(m.group(1))
                j += 1
        new = [f"{indent}{k}: {_scalar(v)}" for k, v in meta.items() if k not in existing]
        if new:
            lines[meta_idx + 1:meta_idx + 1] = new
            changed = True

    if changed:
        new_fm = "\n".join(lines)
        try:
            import yaml
            before, after = yaml.safe_load(fm) or {}, yaml.safe_load(new_fm)
            for k, v in before.items():
                if k == "metadata":
                    for mk, mv in (v or {}).items():
                        assert after["metadata"][mk] == mv, f"metadata.{mk} changed"
                else:
                    assert after[k] == v, f"{k} changed"
        except ImportError:
            pass
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"---\n{new_fm}\n---\n{body}")
    return changed


def set_metadata_values(path, values):
    """Change the value of existing metadata keys in place (text edit, formatting preserved)."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm, body = split_frontmatter(text)
    if fm is None or not values:
        return False
    lines = fm.split("\n")
    meta_idx = next((i for i, l in enumerate(lines) if re.match(r"^metadata:\s*$", l)), None)
    if meta_idx is None:
        return False
    changed = False
    j = meta_idx + 1
    while j < len(lines) and (lines[j][:1] in (" ", "\t") or not lines[j].strip()):
        m = re.match(r"^(\s+)([A-Za-z0-9_-]+):(.*)$", lines[j])
        if m and m.group(2) in values:
            lines[j] = f"{m.group(1)}{m.group(2)}: {_scalar(values[m.group(2)])}"
            changed = True
        j += 1
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"---\n{chr(10).join(lines)}\n---\n{body}")
    return changed


def upstream_url(upstream_cfg, path, is_file=False):
    web = upstream_cfg["web"].rstrip("/")
    return f"{web}/{'blob' if is_file else 'tree'}/{upstream_cfg.get('branch', 'main')}/{path}"


def stamp_included(target_file, upstream_cfg, upstream_path, is_file=False):
    return stamp(
        target_file,
        license_name=upstream_cfg["license"],
        meta={
            "provenance": "included",
            "author": upstream_cfg["author"],
            "source": upstream_url(upstream_cfg, upstream_path, is_file),
        },
    )
