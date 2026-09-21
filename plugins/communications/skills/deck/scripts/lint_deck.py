#!/usr/bin/env python3
"""Lint a deck written in the operator slide grammar. Deterministic; no model.

Usage: lint_deck.py <deck.md> [--audience exec|internal|external|board]

Audience defaults to the theme in frontmatter (operator-<audience>).
Exit 0 with no findings, 1 with findings. Checks only what a script can check;
the deck-critic agent does the rest (argument, fidelity, tone).

Checks
  frontmatter   marp: true, theme: operator-<audience>, header, footer
  types         every `_class` is one of the ten grammar types
  cap           main slides (before the Appendix section) within the profile cap
  bullets       point slides <= 3 bullets; answer slides 2-4 support lines
  headlines     claim types (answer/point/evidence/options/ask) have a headline
                that reads as a sentence (ends in . ? or ! and has a verb-ish
                shape); label types are exempt
  point-two     point headline joined by " and " -> possible two ideas (warn)
  evidence      evidence slides carry a .source element; evidence not
                free-standing (previous slide is a point)
  ask           ask slide has Decider, By (ISO date), Scope, If not decided
  answer        present, and second in the deck
  next          present when an ask is present
"""
import re
import sys
from pathlib import Path

TYPES = {"title", "answer", "agenda", "section", "point", "evidence", "options", "ask", "next", "appendix"}
CLAIM = {"answer", "point", "evidence", "options", "ask"}
CAPS = {"exec": 10, "internal": 25, "external": 12, "board": 8}
CLASS_RE = re.compile(r"^\s*<!--\s*_class:\s*([a-z-]+)\s*-->\s*$", re.M)


def parse(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
        text = text[m.end():]
    raw = re.split(r"\n---\n", "\n" + text.strip("\n") + "\n")
    slides = []
    for i, s in enumerate(raw):
        s = s.strip("\n")
        if not s.strip():
            continue
        cm = CLASS_RE.search(s)
        stype = cm.group(1) if cm else None
        body = CLASS_RE.sub("", s).strip("\n")
        hm = re.search(r"^#\s+(.+)$", body, re.M)
        headline = hm.group(1).strip() if hm else ""
        bullets = [l for l in body.splitlines() if re.match(r"^\s*[-*]\s+", l)]
        slides.append({"n": len(slides) + 1, "type": stype, "headline": headline, "bullets": bullets, "body": body})
    return fm, slides


def is_sentence(h):
    return bool(h) and h[-1] in ".?!" and len(h.split()) >= 5


def lint(path, audience=None):
    text = Path(path).read_text()
    fm, slides = parse(text)
    F = []  # (severity, slide, message)

    theme = fm.get("theme", "")
    aud = audience or (theme.split("operator-")[-1] if theme.startswith("operator-") else None)
    if fm.get("marp") != "true":
        F.append(("error", 0, "frontmatter: `marp: true` missing"))
    if not theme.startswith("operator-"):
        F.append(("error", 0, f"frontmatter: theme should be operator-<audience>, got '{theme}'"))
    if aud not in CAPS:
        F.append(("error", 0, f"audience unknown ('{aud}'); pass --audience or set theme: operator-<audience>"))
    for k in ("header", "footer"):
        if k not in fm:
            F.append(("warn", 0, f"frontmatter: `{k}` missing"))

    # infer effective type: untyped slides are points, except "Appendix" section handling
    appendix_at = None
    for s in slides:
        if s["type"] and s["type"] not in TYPES:
            F.append(("error", s["n"], f"unknown slide type `{s['type']}` — grammar types: {', '.join(sorted(TYPES))}"))
        s["eff"] = s["type"] or ("next" if s["headline"].lower().startswith("what happens next") else "point")
        if s["eff"] == "section" and s["headline"].strip().lower() == "appendix" and appendix_at is None:
            appendix_at = s["n"]

    main = [s for s in slides if appendix_at is None or s["n"] < appendix_at]
    if aud in CAPS and len(main) > CAPS[aud]:
        F.append(("error", 0, f"cap: {len(main)} main slides, profile '{aud}' allows {CAPS[aud]}"))

    types_main = [s["eff"] for s in main]
    if "answer" not in types_main:
        F.append(("error", 0, "no `answer` slide"))
    elif types_main.index("answer") != 1:
        F.append(("warn", types_main.index("answer") + 1, "`answer` should be the second slide"))
    if "ask" in types_main and "next" not in types_main:
        F.append(("warn", 0, "`ask` present but no `next` slide"))

    for i, s in enumerate(slides):
        t, n, h = s["eff"], s["n"], s["headline"]
        if t in CLAIM and not is_sentence(h):
            F.append(("error", n, f"{t} headline is a label, not a claim: \"{h}\""))
        if t == "point":
            if len(s["bullets"]) > 3:
                F.append(("error", n, f"point slide has {len(s['bullets'])} bullets (max 3)"))
            if re.search(r"\band\b", h) and h.count(",") >= 1 and len(h.split()) > 14:
                F.append(("warn", n, "point headline joined by 'and' — check it isn't two ideas"))
            if "|" in s["body"] and s["bullets"]:
                F.append(("warn", n, "point slide has both a table and bullets — pick one, or make the table an evidence slide"))
        if t == "answer":
            if not (2 <= len(s["bullets"]) <= 4):
                F.append(("error", n, f"answer slide has {len(s['bullets'])} support lines (2–4)"))
        if t == "evidence":
            if 'class="source"' not in s["body"]:
                F.append(("error", n, "evidence slide has no `.source` element (source, date, boundary)"))
            prev = slides[i - 1]["eff"] if i > 0 else None
            in_appendix = appendix_at is not None and n > appendix_at
            if prev != "point" and not in_appendix:
                F.append(("error", n, f"evidence slide is free-standing (previous slide is `{prev}`, must be a point)"))
        if t == "ask":
            b = s["body"]
            for key in ("Decider:", "By:", "Scope:", "If not decided:"):
                if key not in b:
                    F.append(("error", n, f"ask slide missing `**{key}**`"))
            if not re.search(r"\*\*By:\*\*\s*\d{4}-\d{2}-\d{2}", b):
                F.append(("warn", n, "ask `By:` is not an ISO date"))
            if re.search(r"\*\*Decider:\*\*\s*(leadership|the team|everyone|tbd)\b", b, re.I):
                F.append(("error", n, "ask decider is not a person or role"))
        if t == "appendix" and 'class="source"' not in s["body"] and ("|" in s["body"] or re.search(r"\d", s["body"])):
            F.append(("warn", n, "appendix slide with numbers has no `.source` element"))

    return aud, len(main), F


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(2)
    path = args[0]
    aud = args[args.index("--audience") + 1] if "--audience" in args else None
    aud, nmain, F = lint(path, aud)
    errs = [f for f in F if f[0] == "error"]
    print(f"{path}: audience={aud} main-slides={nmain}/{CAPS.get(aud, '?')} findings={len(F)} ({len(errs)} errors)")
    for sev, n, msg in F:
        where = f"slide {n}" if n else "deck"
        print(f"  [{sev}] {where}: {msg}")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
