#!/usr/bin/env python3
"""Convert a deck written in the operator slide grammar (Marp source) to Slidev.

Usage: to_slidev.py <deck.md> [-o out.md]

The grammar source is canonical. This translates:
  - deck frontmatter: theme: operator-<audience>  ->  theme: ./theme, audience: <audience>
    header/footer                                   ->  kept as frontmatter for the layouts
  - per-slide `<!-- _class: type -->`                ->  per-slide frontmatter `layout: op-<type>`
  - slides without a type                           ->  layout: op-point
  - <p class="source">…</p>                         ->  <div class="source">…</div>

Everything else (headings, lists, tables, `---` separators) is common markdown
and passes through untouched.
"""
import re
import sys
from pathlib import Path

CLASS_RE = re.compile(r"^\s*<!--\s*_class:\s*([a-z-]+)\s*-->\s*$", re.M)
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, text[m.end():]


def split_slides(body):
    # Marp separates slides with a line that is exactly `---`.
    return re.split(r"\n---\n", "\n" + body.strip("\n") + "\n")


def convert(text):
    fm, body = parse_frontmatter(text)
    theme = fm.get("theme", "operator")
    audience = theme.split("operator-")[-1] if theme.startswith("operator-") else "internal"

    head = ["---", "theme: ./theme", f"audience: {audience}", "aspectRatio: 16/9", "canvasWidth: 1280"]
    for key in ("title", "header", "footer"):
        if key in fm:
            head.append(f'{key}: "{fm[key]}"')
    head.append("---")

    out = []
    for i, slide in enumerate(split_slides(body)):
        slide = slide.strip("\n")
        if not slide.strip():
            continue
        m = CLASS_RE.search(slide)
        stype = m.group(1) if m else "point"
        slide = CLASS_RE.sub("", slide).strip("\n")
        slide = slide.replace('<p class="source">', '<div class="source">').replace("</p>", "</div>")
        block = [] if i == 0 else ["---"]
        block += [f"layout: op-{stype}", "---", "", slide, ""]
        out.append("\n".join(block))

    # First slide: merge its layout into the deck frontmatter (Slidev convention).
    first = out[0].split("\n", 2)  # ["layout: op-x", "---", rest]
    head.insert(-1, first[0])
    return "\n".join(head) + "\n" + first[2] + "\n" + "\n".join(out[1:]) + "\n"


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(1)
    src = Path(args[0])
    out = Path(args[args.index("-o") + 1]) if "-o" in args else src.with_suffix(".slidev.md")
    out.write_text(convert(src.read_text()))
    print(out)


if __name__ == "__main__":
    main()
