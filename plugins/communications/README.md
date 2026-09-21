# communications

Shaping analysis for a room. One skill, one agent, one command, four audiences.

## The domain view

Every other plugin in this collection produces an analysis — a brief, a portfolio read, a research finding, a status. None of that is finished until someone who can act on it has seen it in a form they'll actually read. That last step is where the work most often fails: a good analysis becomes a forty-slide document deck, and the decision it was meant to enable doesn't happen.

The corrective is to treat a deck as an **argument built from a fixed grammar**. Ten slide types — title, answer, agenda, section, point, evidence, options, ask, next, appendix — and every deck is a sequence of them. An audience is then a *profile*: which types, in what order, under what cap, with what stripped and what added. The same source becomes a ten-slide answer-first deck for executives, a twenty-five-slide show-the-work deck for the team, a twelve-slide what's-in-it-for-you deck for a partner, and an eight-slide same-shape-every-quarter deck for the board.

Two disciplines. **Every headline is a sentence that claims something** — read down the outline, the headlines alone make the case, or the deck isn't done. And **the audience decides the sequence, not the content** — evidence is shared across audiences; order, length, and framing are what change.

| Skill | In → Out |
|---|---|
| `deck` | An analysis + an audience → a rendered deck that makes one argument to that room |
| `deck-critic` (agent) | A draft deck + its profile → located findings: where the headline test breaks, what the profile forbids, whether the ask is decidable |

The four audience profiles (`exec`, `internal`, `external`, `board`) live in the skill's `references/` folder and are the extension point: add another (all-hands, customer training) by writing one file in the same shape plus a small theme variant.

## Engines

One source, two renderers. The deck is written once in the grammar (Marp-flavoured markdown: frontmatter, `---` separators, `<!-- _class: type -->`); `scripts/render.sh --engine marp|slidev` does the rest.

| | Marp (default) | Slidev |
|---|---|---|
| Good for | Fast PDF, sending, low friction | Presenting live: animations, presenter notes, a real HTML site |
| Setup | none — `npx` on first run | first run installs a workspace in `assets/slidev/` (Slidev + headless Chromium, ~600 MB, a few minutes) |
| Output | pdf · html · pptx (image-based) | pdf · pptx · html (static site) |
| Theme | `assets/operator*.css` — base + one variant per audience | `assets/slidev/theme/` — one Vue layout per grammar type, same tokens and variants |

`scripts/lint_deck.py` runs before every render: unknown slide types, cap, bullets, label headlines on claim slides, evidence without a source, ask without decider/date/scope. It checks what a script can check; `deck-critic` does the rest. `scripts/to_slidev.py` translates grammar source to Slidev source (`_class` → `layout: op-<type>`, audience → deck config); the theme's `global-top.vue` draws header, footer, and page numbers. Both engines produce the same slide for the same source — that's the test.

## Install

```
/plugin marketplace add maitlam/strategic-operator
/plugin install communications@strategic-operator
```

Then, from any analysis:

```
/communications:deck research/market-brief.md --audience exec
```

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`deck`](skills/deck/SKILL.md) | Original | Build a slide deck from an existing analysis — a brief, a status report, a portfolio read, a roadmap — using a fixed slide grammar and an audience profile, and render it… |
| [`/deck`](commands/deck.md) (command) | Original | Build and render a slide deck from an existing artifact for a named audience — exec, internal, external, or board — using the deck skill's slide grammar and audience… |
| [`deck-critic`](agents/deck-critic.md) (agent) | Original | Review a draft deck against its audience profile before it goes to the room — run the headline test, check the sequence and cap, find the slides carrying two ideas or… |
<!-- catalog:end -->

## Try the example

```bash
plugins/communications/skills/deck/scripts/render.sh \
  plugins/communications/skills/deck/examples/example-exec.md --pdf
# same deck through Slidev
plugins/communications/skills/deck/scripts/render.sh \
  plugins/communications/skills/deck/examples/example-exec.md --engine slidev --pdf
```

Then have the critic read it: "review this deck against the exec profile" routes to `deck-critic`.
