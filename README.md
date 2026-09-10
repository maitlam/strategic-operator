# Strategic Operator

Open-source Claude skills for Biz Ops, Strategy, and Program Management.

[![Validate](https://github.com/maitlam/strategic-operator/actions/workflows/validate.yml/badge.svg)](https://github.com/maitlam/strategic-operator/actions/workflows/validate.yml)

## Why I built this

The best way I know to learn something is to build it. So as I dig into agentic Biz Ops and Program Management, that's exactly what I'm doing, one skill at a time.

Early on, I stumbled on two generous open-source collections: Anthropic's [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) and Amin Borghei's [Claude-Skills](https://github.com/borghei/Claude-Skills). Rather than start from a blank page, I used them as my baseline and my guide. From there, I'm applying my own knowledge and experience: tweaking skills to fit how strategic ops work actually gets done, and building new skills and agents where I see gaps. Huge thanks to both for sharing their work in the open.

This repo is part learning project, part working Strategic Ops toolkit, and part reference architecture for anyone curious about agentic workflows. If you're a chief of staff or strategic generalist exploring how AI agents fit into your workflow, clone this and experiment. If you're building your own skill system, steal whatever's useful. Just keep the original authors' license notes with anything you take.

## What's inside

Three plugins, one for each area I work in. Every skill is labeled so you can see exactly what I wrote, what I adapted, and what I brought in from others.

<!-- catalog:start -->
| Plugin | Focus | Skills | Original | Adapted | Included |
|---|---|---|---|---|---|
| [Biz Ops](plugins/bizops/README.md) | Run the business: operating rhythm, planning and OKRs, metrics, processes, vendors, compliance, and meetings that actually decide things. | 14 | 0 | 3 | 11 |
| [Strategy](plugins/strategy/README.md) | Decide where to play and how to win: markets, competition, business models, go-to-market, pricing, discovery, and product direction. | 27 | 0 | 0 | 27 |
| [Programs](plugins/programs/README.md) | Deliver cross-functional work: programs and portfolios, launches, dependencies, decisions, risk, agile delivery, and the tools teams run on. | 34 | 0 | 1 | 33 |
| [Operating Model](plugins/operating-model/README.md) | Design how a team runs: the operating model itself, decision rights, governance forums, and OKRs. For teams with no existing process to inherit. | 4 | 4 | 0 | 0 |
| [Portfolio](plugins/portfolio/README.md) | Run a portfolio: intake, scoring against declared criteria, whole-portfolio health, and matching demand against real capacity. | 4 | 4 | 0 | 0 |
| [Intelligence](plugins/intelligence/README.md) | Build a standing market intelligence function: ecosystem mapping, partner scans, competitive reads, and a recurring signals brief. | 4 | 4 | 0 | 0 |
| **Total** | | **87** | **12** | **4** | **71** |

Counts include 86 skills, 1 command, and 0 agents.

### My original and adapted work

- [`competitive-intel`](plugins/intelligence/skills/competitive-intel/SKILL.md) · Original · intelligence: Build a read on a competitor — what they're actually doing versus what they say, where they're strong, where they're exposed, and what their recent moves imply about…
- [`ecosystem-map`](plugins/intelligence/skills/ecosystem-map/SKILL.md) · Original · intelligence: Segment an unfamiliar market or ecosystem into its structural parts — who the actors are, how value and money move between them, and where the pain concentrates
- [`intelligence-brief`](plugins/intelligence/skills/intelligence-brief/SKILL.md) · Original · intelligence: Produce a recurring market intelligence brief — daily or weekly signals filtered for what actually matters to this team, with the "so what" attached
- [`partner-scan`](plugins/intelligence/skills/partner-scan/SKILL.md) · Original · intelligence: Profile a specific company as a potential partner — what they do, who they serve, how they make money, what they'd want from a partnership, and what would have to be…
- [`decision-rights`](plugins/operating-model/skills/decision-rights/SKILL.md) · Original · operating-model: Map who decides what on a team or program — the authority to approve, to break a tie, to spend, and to stop — and surface where that authority is currently undefined
- [`governance-design`](plugins/operating-model/skills/governance-design/SKILL.md) · Original · operating-model: Design the review and forum layer for a team or portfolio — which recurring meetings exist, what each one decides, what artifact it requires as input, and which existing…
- [`okr-tracking`](plugins/operating-model/skills/okr-tracking/SKILL.md) · Original · operating-model: Draft, review, or check in on objectives and key results — including diagnosing OKRs that are really task lists in disguise
- [`operating-model-builder`](plugins/operating-model/skills/operating-model-builder/SKILL.md) · Original · operating-model: Design an operating model for a team from scratch — purpose, cadence, artifacts, roles, and the decisions the model exists to make possible
- [`opportunity-scoring`](plugins/portfolio/skills/opportunity-scoring/SKILL.md) · Original · portfolio: Score an opportunity, proposal, vendor, or investment candidate against explicit criteria and produce a comparable, defensible read
- [`portfolio-health`](plugins/portfolio/skills/portfolio-health/SKILL.md) · Original · portfolio: Produce a whole-portfolio read — where the money and people actually are, what has stalled, what should be killed, and whether the mix matches the stated strategy
- [`portfolio-intake`](plugins/portfolio/skills/portfolio-intake/SKILL.md) · Original · portfolio: Design or run the front door for a portfolio — how opportunities enter, what information is required before anything is evaluated, and what happens to things that don't…
- [`resource-allocation`](plugins/portfolio/skills/resource-allocation/SKILL.md) · Original · portfolio: Match a portfolio's demands against a team's real capacity and show where it is oversubscribed, including the person-level constraints that determine dates
- [`metrics-dashboard`](plugins/bizops/skills/metrics-dashboard/SKILL.md) · Adapted · bizops: Design the whole product metrics dashboard SYSTEM: layers, owners, review cadence, and visualization — the board a team actually reviews on a weekly or monthly rhythm
- [`north-star-metric`](plugins/bizops/skills/north-star-metric/SKILL.md) · Adapted · bizops: Define the North Star Metric spec: the single number, its input metric tree, leading indicators, anti-metrics, and counter-metrics — with a Python tool that renders it…
- [`risk-assessment`](plugins/bizops/skills/risk-assessment/SKILL.md) · Adapted · bizops: Identify, assess, and mitigate ongoing operational risks — the standing risk register that lives across a program or team
- [`pre-mortem`](plugins/programs/skills/pre-mortem/SKILL.md) · Adapted · programs: Pre-launch imagined-failure exercise: classify risks as Tigers, Paper Tigers, and Elephants to surface launch-blocking issues before they happen
<!-- catalog:end -->

## How to read the labels

**Original** skills are ones I wrote from scratch.

**Adapted** skills started from someone else's work and were meaningfully reshaped. Each has a `CHANGES.md` in its folder explaining what I changed and why.

**Included** skills are someone else's work, brought in as-is and credited because they round out the toolkit. The only edit is the provenance label in their frontmatter.

The labels live in each skill's frontmatter (`metadata.provenance`), and the catalog above is generated from them, so it can't drift out of date. A GitHub Action checks every push: every item must be labeled, adapted and included work must link back to its source, and the catalog must match the files.

## Try it

**Browse.** Every skill is a readable markdown file. Start with a plugin README ([Biz Ops](plugins/bizops/README.md), [Strategy](plugins/strategy/README.md), [Programs](plugins/programs/README.md), [Operating Model](plugins/operating-model/README.md), [Portfolio](plugins/portfolio/README.md), [Intelligence](plugins/intelligence/README.md)) and open whatever catches your eye.

**Claude Code.**

```bash
claude plugin marketplace add maitlam/strategic-operator
claude plugin install bizops@strategic-operator
claude plugin install strategy@strategic-operator
claude plugin install programs@strategic-operator
claude plugin install operating-model@strategic-operator
claude plugin install portfolio@strategic-operator
claude plugin install intelligence@strategic-operator
```

Skills activate on their own when a request matches, or you can call one directly, like `/programs:dependency-map`.

**Claude Cowork.** Add `maitlam/strategic-operator` as a marketplace from the plugins directory.

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
├── .claude-plugin/marketplace.json   # the marketplace: lists the six plugins
├── plugins/
│   ├── bizops/                       # each plugin has the same shape:
│   ├── strategy/                     #   .claude-plugin/plugin.json  manifest
│   ├── programs/                     #   skills/<name>/SKILL.md      one folder per skill
│   ├── operating-model/              #   README.md, CONNECTORS.md, LICENSES/
│   ├── portfolio/
│   └── intelligence/
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
