---
description: Build and render a slide deck from an existing artifact for a named audience — exec, internal, external, or board — using the deck skill's slide grammar and audience profiles
argument-hint: "<source file or artifact> --audience exec|internal|external|board [--engine marp|slidev] [--pdf|--html|--pptx|--all]"
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: "0.1.0"
---

# /deck

Shape an existing analysis into a deck for one audience and render it. This is the explicit entry point to the `deck` skill: source in, audience named, rendered file out.

## Usage

```
/deck $ARGUMENTS
```

Examples:

```
/deck research/market-brief.md --audience exec
/deck status/2026-09-week-38.md --audience internal --html
/deck partners/proposal-draft.md --audience external --all
```

## Workflow

### 1. Resolve the inputs

- **Source:** the file or pasted artifact. If none is given, ask. If the user has an idea but no artifact, point them at the skill that produces one — this command shapes, it doesn't analyze.
- **Audience:** `exec`, `internal`, `external`, or `board`. If missing, ask; don't default.
- **Engine:** `marp` unless `--engine slidev` is passed. Slidev's first run installs a workspace (a few minutes).
- **Format:** `--pdf` unless told otherwise.

### 2. Run the deck skill

Follow the `deck` skill in full: answer sentence → audience profile from `references/audience-<name>.md` → headline outline → bodies → ask → appendix → `deck.md`.

### 3. Render

```bash
<plugin-root>/skills/deck/scripts/render.sh <name>-<audience>.md --pdf [--engine slidev]
```

Requires Node. Uses a global `marp` if present, otherwise `npx @marp-team/marp-cli` (network on first run).

### 4. Hand back

- The answer sentence
- Slide count vs. the profile's cap
- The ask (or "informational — no ask")
- What the profile stripped that the user may want to know about
- Paths to the `.md` source and the rendered file

## Rules

- **Never default the audience.** Exec and internal decks from the same source look nothing alike; guessing wrong wastes the whole run.
- **Never invent an ask.** If the profile requires one and the source has none, ask the user.
- **Over the cap means cut points, not shrink type.**
- **Headline test before handing back.** Headlines only, top to bottom; if the argument doesn't hold, it isn't done.

## Skills this command uses

- `deck` — the grammar, the process, the profiles, the renderer
