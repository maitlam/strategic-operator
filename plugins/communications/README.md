# communications

Shaping analysis for a room. One skill, one command, three audiences.

## The domain view

Every other plugin in this collection produces an analysis — a brief, a portfolio read, a research finding, a status. None of that is finished until someone who can act on it has seen it in a form they'll actually read. That last step is where the work most often fails: a good analysis becomes a forty-slide document deck, and the decision it was meant to enable doesn't happen.

The corrective is to treat a deck as an **argument built from a fixed grammar**. Ten slide types — title, answer, agenda, section, point, evidence, options, ask, next, appendix — and every deck is a sequence of them. An audience is then a *profile*: which types, in what order, under what cap, with what stripped and what added. The same source becomes a ten-slide answer-first deck for executives, a twenty-five-slide show-the-work deck for the team, and a twelve-slide what's-in-it-for-you deck for a partner.

Two disciplines. **Every headline is a sentence that claims something** — read down the outline, the headlines alone make the case, or the deck isn't done. And **the audience decides the sequence, not the content** — evidence is shared across audiences; order, length, and framing are what change.

| Skill | In → Out |
|---|---|
| `deck` | An analysis + an audience → a rendered deck that makes one argument to that room |

The three audience profiles live in the skill's `references/` folder and are the extension point: add a fourth (board, all-hands, customer training) by writing one file in the same shape.

## Engine

Markdown in, [Marp](https://marp.app) out — PDF, HTML, or PPTX (image-based). The `operator` theme is built from scratch in `skills/deck/assets/`; each audience is a theme variant that imports it. `scripts/render.sh` wraps the CLI and uses a global `marp` if installed, otherwise `npx @marp-team/marp-cli` (Node required, network on first run).

The content contract is deliberately plain — frontmatter, `---` separators, `<!-- _class: type -->` — so a second renderer (Slidev is the planned next one) can sit behind the same source.

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
| [`/deck`](commands/deck.md) (command) | Original | Build and render a slide deck from an existing artifact for a named audience — exec, internal, or external — using the deck skill's slide grammar and audience profiles |
<!-- catalog:end -->

## Try the example

```bash
plugins/communications/skills/deck/scripts/render.sh \
  plugins/communications/skills/deck/examples/example-exec.md --pdf
```
