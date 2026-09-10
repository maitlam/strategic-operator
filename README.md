# Strategic Operator

Open-source Claude skills for Biz Ops, Strategy, and Program Management.

[![Validate](https://github.com/maiiioi/strategic-operator/actions/workflows/validate.yml/badge.svg)](https://github.com/maiiioi/strategic-operator/actions/workflows/validate.yml)

## Why I built this

The best way I know to learn something is to build it. So as I dig into agentic Biz Ops and Program Management, that's exactly what I'm doing, one skill at a time.

Early on, I stumbled on two generous open-source collections: Anthropic's [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) and Amin Borghei's [Claude-Skills](https://github.com/borghei/Claude-Skills). Rather than start from a blank page, I used them as my baseline and my guide. From there, I'm applying my own knowledge and experience: tweaking skills to fit how strategic ops work actually gets done, and building new skills and agents where I see gaps. Huge thanks to both for sharing their work in the open.

This repo is part learning project, part working Strategic Ops toolkit, and part reference architecture for anyone curious about agentic workflows. If you're a chief of staff or strategic generalist exploring how AI agents fit into your workflow, clone this and experiment. If you're building your own skill system, steal whatever's useful. Just keep the original authors' license notes with anything you take.

## What's inside

Three plugins, one for each area I work in. Every skill is labeled so you can see exactly what I wrote, what I adapted, and what I brought in from others.

<!-- catalog:start -->
| Plugin | Focus | Skills | Original | Adapted | Included |
|---|---|---|---|---|---|
| [Biz Ops](plugins/bizops/README.md) | Run the business: operating rhythm, planning and OKRs, metrics, processes, vendors, compliance, and meetings that actually decide things. | 18 | 0 | 0 | 18 |
| [Strategy](plugins/strategy/README.md) | Decide where to play and how to win: markets, competition, business models, go-to-market, pricing, discovery, and product direction. | 30 | 0 | 0 | 30 |
| [Programs](plugins/programs/README.md) | Deliver cross-functional work: programs and portfolios, launches, dependencies, decisions, risk, agile delivery, and the tools teams run on. | 38 | 0 | 0 | 38 |
| **Total** | | **86** | **0** | **0** | **86** |

Counts include 85 skills, 1 command, and 0 agents.

### My original and adapted work

_Nothing here yet. My own skills and agents will show up here as I build them._
<!-- catalog:end -->

## How to read the labels

**Original** skills are ones I wrote from scratch.

**Adapted** skills started from someone else's work and were meaningfully reshaped. Each has a `CHANGES.md` in its folder explaining what I changed and why.

**Included** skills are someone else's work, brought in as-is and credited because they round out the toolkit. The only edit is the provenance label in their frontmatter.

The labels live in each skill's frontmatter (`metadata.provenance`), and the catalog above is generated from them, so it can't drift out of date. A GitHub Action checks every push: every item must be labeled, adapted and included work must link back to its source, and the catalog must match the files.

## Try it

**Browse.** Every skill is a readable markdown file. Start with a plugin README ([Biz Ops](plugins/bizops/README.md), [Strategy](plugins/strategy/README.md), [Programs](plugins/programs/README.md)) and open whatever catches your eye.

**Claude Code.**

```bash
claude plugin marketplace add maiiioi/strategic-operator
claude plugin install bizops@strategic-operator
claude plugin install strategy@strategic-operator
claude plugin install programs@strategic-operator
```

Skills activate on their own when a request matches, or you can call one directly, like `/programs:dependency-map`.

**Claude Cowork.** Add `maiiioi/strategic-operator` as a marketplace from the plugins directory.

**Connectors are optional.** Some skills can pull from tools like Slack, Notion, or Jira if you've connected them, and each plugin's `CONNECTORS.md` explains how. Every skill also works if you just paste in the context.

## Build on it

You'll need Python 3.8+, git, and PyYAML (`pip install pyyaml`).

**Write an original skill.** Copy `templates/original-skill/` to `plugins/<plugin>/skills/<skill-name>/`, rename the `name` field to match the folder, and write it. Then run `python3 scripts/catalog.py` to refresh the catalog.

**Adapt an included skill.** In its frontmatter, set `provenance: adapted`, set `author` to yourself, rename `source` to `adapted-from`, and add a one-line `changes` summary. Keep the original `license`. Copy `templates/adapted-skill/CHANGES.md` into the skill folder and explain what you changed and why.

**Bring in a skill from upstream.** This copies it, labels it as Included, tracks it for updates, and refreshes the catalog:

```bash
python3 scripts/check_upstream.py --add borghei business-operations/process-mapper plugins/bizops/skills/process-mapper
```

**Remove a skill.** This deletes it, drops its tracking entry, and refreshes the catalog:

```bash
python3 scripts/catalog.py --remove pm-interview-prep
```

**Before you push:** `python3 scripts/catalog.py --check`. CI runs the same check, plus Claude Code's own plugin validator.

## Staying in sync with upstream

Nothing here is a fork, so upstream changes never arrive automatically, and nothing flows back. `sources.json` records the exact upstream commit each borrowed item came from.

```bash
python3 scripts/check_upstream.py                      # what changed upstream since I copied?
python3 scripts/check_upstream.py --diff pre-mortem    # see the changes for one item
python3 scripts/check_upstream.py --merge pre-mortem   # merge them in (or --merge all)
```

Merging is three-way: it compares upstream's old version, upstream's new version, and my copy, so my edits and provenance labels are kept. If upstream changed the same lines I did, the file gets standard `<<<<<<<` conflict markers for me to resolve, and nothing is marked synced until I do. Review with `git diff` before committing.

## How it's organized

```
strategic-operator/
├── .claude-plugin/marketplace.json   # the marketplace: lists the three plugins
├── plugins/
│   ├── bizops/                       # each plugin has the same shape:
│   ├── strategy/                     #   .claude-plugin/plugin.json  manifest
│   └── programs/                     #   skills/<name>/SKILL.md      one folder per skill
│                                     #   README.md, CONNECTORS.md, LICENSES/
├── templates/                        # starting points for original and adapted skills
├── scripts/
│   ├── catalog.py                    # builds the catalog, checks labels, removes skills
│   └── check_upstream.py             # tracks and pulls upstream changes
├── sources.json                      # where every borrowed item came from
├── docs/skill-review.md              # curation checklist: overlaps and fit questions
└── .github/workflows/validate.yml    # runs the checks on every push
```

## Credits and licenses

My original work is released under the [MIT License](LICENSE).

Borrowed work keeps its original license, noted in each skill's frontmatter:

- **Anthropic** · [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) · Apache License 2.0
- **Amin Borghei** · [Claude-Skills](https://github.com/borghei/Claude-Skills) · MIT + Commons Clause. You can use, modify, and share these skills, but not sell them or a paid product built substantially on them.

Full license texts are in each plugin's `LICENSES/` folder, and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) describes exactly what was changed from the originals.
