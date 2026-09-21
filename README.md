# Strategic Operator

Open-source Claude skills, subagents, and automations for Biz Ops, Strategy, Program Management, and Communications.

[![Validate](https://github.com/maitlam/strategic-operator/actions/workflows/validate.yml/badge.svg)](https://github.com/maitlam/strategic-operator/actions/workflows/validate.yml)

The best way I know to learn something is to build it. So as I dig into agentic Biz Ops and Program Management, that's exactly what I'm doing, one skill at a time.

Early on, I stumbled on two generous open-source collections: Anthropic's [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) and Amin Borghei's [Claude-Skills](https://github.com/borghei/Claude-Skills). Rather than start from a blank page, I used them as my baseline and my guide. From there, I'm applying my own knowledge and experience: tweaking skills to fit how strategic ops work actually gets done, and building new skills and agents where I see gaps.

This repo is part learning project, part working Strategic Ops toolkit, and part reference architecture for anyone curious about agentic workflows. If you're a chief of staff or strategic generalist exploring how AI agents fit into your workflow, clone this and experiment. If you're building your own skill system, steal whatever's useful.

---

## Quick Start

**Install (Claude Code).**

```bash
claude plugin marketplace add maitlam/strategic-operator
claude plugin install bizops@strategic-operator
claude plugin install programs@strategic-operator
claude plugin install operating-model@strategic-operator
claude plugin install portfolio@strategic-operator
claude plugin install intelligence@strategic-operator
claude plugin install discovery@strategic-operator
claude plugin install positioning@strategic-operator
claude plugin install product-planning@strategic-operator
claude plugin install communications@strategic-operator
```

**Claude Cowork.** Add `maitlam/strategic-operator` as a marketplace from the plugins directory.

**Try it.** Skills activate on their own when you describe what you need — no invocation ceremony. Try:

```
Help me define a north star metric for [your product].
Map the ecosystem for [an unfamiliar market].
Draft a positioning brief for [our team].
Review this PRD I've written.
Turn this brief into a deck for leadership.
```

Prefer explicit invocation? Every skill is directly callable — `/discovery:jtbd-workshop`, `/portfolio:opportunity-scoring`, `/positioning:positioning-brief`.

**Connectors are optional.** Some skills can pull from Slack, Notion, or Jira if you've connected them (each plugin's `CONNECTORS.md` explains how). Every skill also works if you just paste in the context.

---

## Architecture

Three extension types, each earning its place for a different problem shape.

### Skills — atomic capabilities

The unit of work. A markdown file (`SKILL.md`) with frontmatter declaring what it does and when to trigger, and a body describing the method. Skills auto-fire when Claude matches an intent against the description.

Use skills for **one bounded job** — draft an OKR, score an opportunity, synthesize interviews.

Location: `plugins/<plugin>/skills/<skill-name>/SKILL.md`

### Subagents — persona-driven workflows

Delegated Claude sub-instances with a system prompt, tool restrictions, and a focused role. Claude routes to them when a task fits their scope.

Use subagents for **multi-step work with a distinct voice** — heavy web research (context isolation), a chained workflow (portfolio review across four skills), or an opinionated persona (a critic vs. an author).

Location: `plugins/<plugin>/agents/<agent-name>.md`

### Automations — user-invoked shortcuts

Commands the user calls explicitly (`/plugin:command`). Unlike skills, no matching ambiguity — the command runs the exact template every time.

Use automations for **recurring rituals** — the Monday morning beat, the Friday status, the pre-launch sweep.

Location: `plugins/<plugin>/commands/<command>.md`

### How they compose

```
   Skills ──► atomic jobs (one job per skill)
     ▲
     │
     │ invoked by
     │
   Subagents ──► multi-step workflows with a voice
     ▲
     │
     │ optionally kicked off by
     │
   Automations ──► explicit, deterministic entry points
```

A user request usually enters via **description matching a skill** or **describing intent that routes to a subagent**. Automations are the shortcut layer on top — nothing is done that couldn't be reached by describing intent, but muscle memory works faster.

### Repo layout

```
strategic-operator/
├── .claude-plugin/marketplace.json   # the marketplace: lists the nine plugins
├── plugins/
│   ├── bizops/                       # each plugin has the same shape:
│   ├── programs/                     #   .claude-plugin/plugin.json  manifest
│   ├── operating-model/              #   skills/<name>/SKILL.md      one folder per skill
│   ├── portfolio/                    #   agents/<name>.md            one file per agent
│   ├── intelligence/                 #   commands/<name>.md          one file per command
│   ├── discovery/                    #   hooks/hooks.json + *.sh     event-triggered, ship with the plugin
│   ├── positioning/                  #   README.md, CONNECTORS.md, LICENSES/
│   ├── product-planning/
│   └── communications/               #   (deck skill also carries assets/, scripts/, references/, examples/)
├── templates/                        # starting points for original and adapted skills
├── scripts/
│   ├── catalog.py                    # builds the catalog, checks labels, removes skills
│   └── check_upstream.py             # tracks and pulls upstream changes
├── sources.json                      # where every borrowed item came from
├── docs/skill-review.md              # curation checklist: overlaps and fit questions
└── .github/workflows/validate.yml    # runs the checks on every push
```

---

## Skill Reference

<!-- catalog:start -->
| Plugin | Focus | Skills | Original | Adapted | Included |
|---|---|---|---|---|---|
| [Biz Ops](plugins/bizops/README.md) | Run the business: operating rhythm, planning and OKRs, metrics, processes, vendors, compliance, and meetings that actually decide things. | 15 | 1 | 3 | 11 |
| [Discovery](plugins/discovery/README.md) | Continuous customer discovery: interview design, transcript synthesis, JTBD workshops, opportunity ideation, and the disciplines that keep discovery signal over noise. | 13 | 3 | 0 | 10 |
| [Positioning](plugins/positioning/README.md) | Decide where to play and how to win: market frameworks (Porter's, SWOT, Ansoff), business-model canvases, ICP, and go-to-market strategy. | 9 | 1 | 0 | 8 |
| [Product Planning](plugins/product-planning/README.md) | Turn strategy into product direction: PRDs, product vision, prioritization frameworks, and outcome-driven roadmaps. | 10 | 1 | 0 | 9 |
| [Programs](plugins/programs/README.md) | Deliver cross-functional work: programs and portfolios, launches, dependencies, decisions, risk, agile delivery, and the tools teams run on. | 38 | 4 | 1 | 33 |
| [Operating Model](plugins/operating-model/README.md) | Design how a team runs: the operating model itself, decision rights, governance forums, and OKRs. For teams with no existing process to inherit. | 6 | 6 | 0 | 0 |
| [Portfolio](plugins/portfolio/README.md) | Run a portfolio: intake, scoring against declared criteria, whole-portfolio health, and matching demand against real capacity. | 6 | 6 | 0 | 0 |
| [Intelligence](plugins/intelligence/README.md) | Build a standing market intelligence function: map and size a market, run the loop from signal to research to pattern, and read specific partners and competitors. | 12 | 12 | 0 | 0 |
| [Communications](plugins/communications/README.md) | Turn any analysis into something an audience can act on: slide decks built from a fixed slide grammar, rendered from markdown, shaped differently for executives, the internal team, and external stakeholders. | 2 | 2 | 0 | 0 |
| **Total** | | **111** | **36** | **4** | **71** |

Counts include 95 skills, 7 commands, and 9 agents.

### My original and adapted work

- [`/meeting-prep`](plugins/bizops/commands/meeting-prep.md) (command) · Original · bizops: Prep for a meeting — its purpose and the decision it needs, open items from last time, who's in the room and what they care about, the questions to ask, and a time-boxed…
- [`deck`](plugins/communications/skills/deck/SKILL.md) · Original · communications: Build a slide deck from an existing analysis — a brief, a status report, a portfolio read, a roadmap — using a fixed slide grammar and an audience profile, and render it…
- [`/deck`](plugins/communications/commands/deck.md) (command) · Original · communications: Build and render a slide deck from an existing artifact for a named audience — exec, internal, or external — using the deck skill's slide grammar and audience profiles
- [`discovery-cadence`](plugins/discovery/skills/discovery-cadence/SKILL.md) · Original · discovery: Design or diagnose the operating rhythm of continuous customer discovery — the weekly beat that produces learning, not the one-off "round of interviews" that produces a…
- [`/feedback-weekly`](plugins/discovery/commands/feedback-weekly.md) (command) · Original · discovery: Weekly customer-feedback analysis — gather the week's inbound from every channel, triage and deduplicate it, count independent sources per theme, show what moved since…
- [`product-discovery-researcher`](plugins/discovery/agents/product-discovery-researcher.md) (agent) · Original · discovery: Run customer discovery workflows — plan interview scripts, run interviews, synthesize transcripts, facilitate JTBD workshops, and ideate opportunities from evidence
- [`competitive-intel`](plugins/intelligence/skills/competitive-intel/SKILL.md) · Original · intelligence: Build a read on a competitor — what they're actually doing versus what they say, where they're strong, where they're exposed, and what their recent moves imply about…
- [`ecosystem-map`](plugins/intelligence/skills/ecosystem-map/SKILL.md) · Original · intelligence: Segment an unfamiliar market or ecosystem into its structural parts — who the actors are, how value and money move between them, and where the pain concentrates
- [`intelligence-brief`](plugins/intelligence/skills/intelligence-brief/SKILL.md) · Original · intelligence: Produce a recurring market intelligence brief — daily or weekly signals filtered for what actually matters to this team, with the "so what" attached
- [`lens-researcher`](plugins/intelligence/agents/lens-researcher.md) (agent) · Original · intelligence: Research one lens of a larger topic — money, operations, players and moves, technology, evidence, or constraints — against a short list of sub-questions, writing sourced…
- [`market-landscape-analyzer`](plugins/intelligence/agents/market-landscape-analyzer.md) (agent) · Original · intelligence: Map an unfamiliar market, space, vertical, or ecosystem — segment the actors, trace value and money flow, identify pain concentration, and flag white space
- [`market-sizing`](plugins/intelligence/skills/market-sizing/SKILL.md) · Original · intelligence: Size a market with a defensible range rather than a single number — TAM, SAM, and SOM built bottom-up and top-down, reconciled, with every assumption visible and the one…
- [`partner-intelligence`](plugins/intelligence/agents/partner-intelligence.md) (agent) · Original · intelligence: Research and profile a named company or organization as a potential partner, vendor, channel, or acquirer target
- [`partner-scan`](plugins/intelligence/skills/partner-scan/SKILL.md) · Original · intelligence: Profile a specific company as a potential partner — what they do, who they serve, how they make money, what they'd want from a partnership, and what would have to be…
- [`pattern-analysis`](plugins/intelligence/skills/pattern-analysis/SKILL.md) · Original · intelligence: Read across a whole corpus of conversations — meeting notes, interviews, customer calls, briefs — and report what recurs, what conflicts, what is newly emerging, and how…
- [`research-agenda`](plugins/intelligence/skills/research-agenda/SKILL.md) · Original · intelligence: Turn a pile of open questions, graduated signals, and untested assumptions into a prioritized research roadmap — each item framed by the decision it feeds and what…
- [`research-brief`](plugins/intelligence/skills/research-brief/SKILL.md) · Original · intelligence: Produce a deep, sourced research brief on a single topic — scope confirmed first, the topic decomposed into lenses so coverage is systematic, every fact sourced and…
- [`signal-scan`](plugins/intelligence/skills/signal-scan/SKILL.md) · Original · intelligence: Sweep the team's own recent conversations — meeting notes, customer calls, interviews, internal briefs — for research signals, deduplicate them against a running signal…
- [`decision-memo`](plugins/operating-model/agents/decision-memo.md) (agent) · Original · operating-model: Turn evidence, options, and stakeholder input into a structured decision memo — context, options, tradeoffs, recommendation, risks, and a clear decision request
- [`decision-rights`](plugins/operating-model/skills/decision-rights/SKILL.md) · Original · operating-model: Map who decides what on a team or program — the authority to approve, to break a tie, to spend, and to stop — and surface where that authority is currently undefined
- [`governance-design`](plugins/operating-model/skills/governance-design/SKILL.md) · Original · operating-model: Design the review and forum layer for a team or portfolio — which recurring meetings exist, what each one decides, what artifact it requires as input, and which existing…
- [`okr-tracking`](plugins/operating-model/skills/okr-tracking/SKILL.md) · Original · operating-model: Draft, review, or check in on objectives and key results — including diagnosing OKRs that are really task lists in disguise
- [`operating-model-builder`](plugins/operating-model/skills/operating-model-builder/SKILL.md) · Original · operating-model: Design an operating model for a team from scratch — purpose, cadence, artifacts, roles, and the decisions the model exists to make possible
- [`operating-model-designer`](plugins/operating-model/agents/operating-model-designer.md) (agent) · Original · operating-model: Design a team's operating model from ambiguous inputs — purpose, cadence, artifacts, roles, decision rights, governance forums, and OKRs
- [`opportunity-scoring`](plugins/portfolio/skills/opportunity-scoring/SKILL.md) · Original · portfolio: Score an opportunity, proposal, vendor, or investment candidate against explicit criteria and produce a comparable, defensible read
- [`portfolio-health`](plugins/portfolio/skills/portfolio-health/SKILL.md) · Original · portfolio: Produce a whole-portfolio read — where the money and people actually are, what has stalled, what should be killed, and whether the mix matches the stated strategy
- [`portfolio-intake`](plugins/portfolio/skills/portfolio-intake/SKILL.md) · Original · portfolio: Design or run the front door for a portfolio — how opportunities enter, what information is required before anything is evaluated, and what happens to things that don't…
- [`portfolio-manager`](plugins/portfolio/agents/portfolio-manager.md) (agent) · Original · portfolio: Track and manage active initiatives across a portfolio — status, resources, dependencies, risks, executive sponsorship — and flag what's at risk or should be killed
- [`portfolio-prioritizer`](plugins/portfolio/agents/portfolio-prioritizer.md) (agent) · Original · portfolio: Score new opportunities against declared strategic criteria and recommend invest / pause / kill / investigate
- [`resource-allocation`](plugins/portfolio/skills/resource-allocation/SKILL.md) · Original · portfolio: Match a portfolio's demands against a team's real capacity and show where it is oversubscribed, including the person-level constraints that determine dates
- [`positioning-brief`](plugins/positioning/skills/positioning-brief/SKILL.md) · Original · positioning: Write or stress-test a one-page positioning brief — who we're for, what we do, why it's different, what we deliberately are not
- [`prd-quality-gate`](plugins/product-planning/skills/prd-quality-gate/SKILL.md) · Original · product-planning: Review a draft PRD against a short quality checklist before it goes to a stakeholder — is a decision actually being requested, is success measurable, are assumptions…
- [`launch-readiness`](plugins/programs/agents/launch-readiness.md) (agent) · Original · programs: Evaluate readiness across cross-functional teams before a launch — Product, Engineering, Legal/Privacy, Security, Operations, GTM, Support — and surface blockers,…
- [`/retro`](plugins/programs/commands/retro.md) (command) · Original · programs: Run a sprint or milestone retrospective — data first, then the team's read, then one to three owned actions — and file the durable lessons somewhere they'll be read again
- [`/sprint-kickoff`](plugins/programs/commands/sprint-kickoff.md) (command) · Original · programs: Run the sprint kickoff — real capacity, a readiness check on candidate stories, a commit-versus-stretch split, dependencies and risks named, and a one-sentence sprint…
- [`/standup`](plugins/programs/commands/standup.md) (command) · Original · programs: Prep the daily standup — what moved since yesterday, what's aging, what's blocked, and the one or two things the standup actually needs to decide
- [`metrics-dashboard`](plugins/bizops/skills/metrics-dashboard/SKILL.md) · Adapted · bizops: Design the whole product metrics dashboard SYSTEM: layers, owners, review cadence, and visualization — the board a team actually reviews on a weekly or monthly rhythm
- [`north-star-metric`](plugins/bizops/skills/north-star-metric/SKILL.md) · Adapted · bizops: Define the North Star Metric spec: the single number, its input metric tree, leading indicators, anti-metrics, and counter-metrics — with a Python tool that renders it…
- [`risk-assessment`](plugins/bizops/skills/risk-assessment/SKILL.md) · Adapted · bizops: Identify, assess, and mitigate ongoing operational risks — the standing risk register that lives across a program or team
- [`pre-mortem`](plugins/programs/skills/pre-mortem/SKILL.md) · Adapted · programs: Pre-launch imagined-failure exercise: classify risks as Tigers, Paper Tigers, and Elephants to surface launch-blocking issues before they happen
<!-- catalog:end -->

Everything above is auto-generated from each item's frontmatter by `scripts/catalog.py`. The counts can't drift out of date — a GitHub Action re-runs the check on every push.

---

## Subagents

Nine agents wrap the multi-step workflows and personas. Skills are what agents call.

| Agent | Plugin | Wraps | Job |
|---|---|---|---|
| [partner-intelligence](plugins/intelligence/agents/partner-intelligence.md) | intelligence | ecosystem-map, partner-scan, competitive-intel | Named-company research; ends in a discovery list, not a verdict |
| [market-landscape-analyzer](plugins/intelligence/agents/market-landscape-analyzer.md) | intelligence | ecosystem-map + others | Whole-market mapping; ecosystem is the deliverable |
| [lens-researcher](plugins/intelligence/agents/lens-researcher.md) | intelligence | research-brief (one lens per instance) | Parallel per-lens research with write-as-you-go findings and stuck-detection |
| [product-discovery-researcher](plugins/discovery/agents/product-discovery-researcher.md) | discovery | customer-interview-script, interview-synthesis, jtbd-workshop, brainstorm-ideas | Customer-side research cycle — behavior over opinion, jobs not personas |
| [operating-model-designer](plugins/operating-model/agents/operating-model-designer.md) | operating-model | operating-model-builder, decision-rights, governance-design, okr-tracking | Zero-to-one team design; anti-ceremony, authority explicit |
| [decision-memo](plugins/operating-model/agents/decision-memo.md) | operating-model | decision-rights + novel content | Options-first decision packets; reversibility framing (T1/T2 doors) |
| [portfolio-manager](plugins/portfolio/agents/portfolio-manager.md) | portfolio | portfolio-health, resource-allocation, dependency-map, risk-assessment | Active-work tracking; kill discipline, no watermelon status |
| [portfolio-prioritizer](plugins/portfolio/agents/portfolio-prioritizer.md) | portfolio | portfolio-intake, opportunity-scoring | Pipeline scoring; criteria declared before scoring, invest/pause/kill/investigate |
| [launch-readiness](plugins/programs/agents/launch-readiness.md) | programs | launch-playbook, dependency-map, risk-assessment, pre-mortem | Cross-team readiness sweep with a defensible GO / CONDITIONAL GO / NO-GO |

Research agents restrict tools to `WebSearch, WebFetch, Read, Grep, Glob` (no Edit/Write); lens-researcher adds `Write` for its append-only findings file. Orchestrators restrict to `Read, Grep, Glob`. Launch-readiness adds `WebFetch` for Confluence/Notion pulls.

---

## Automations

Two flavors of automation live in this repo: **slash commands** (user-invoked) and **hooks** (event-triggered).

### Slash commands

Deterministic — same input, same execution, every time.

| Command | Plugin | What it does |
|---|---|---|
| [`/discovery:brainstorm`](plugins/discovery/commands/brainstorm.md) | discovery | Brainstorm a product idea, problem space, or strategic question with a sharp thinking partner (borrowed from Anthropic's plugins) |
| [`/programs:standup`](plugins/programs/commands/standup.md) | programs | Daily standup prep — delta since yesterday, aging work, blocked items, and the one or two decisions the standup needs |
| [`/programs:sprint-kickoff`](plugins/programs/commands/sprint-kickoff.md) | programs | Sprint kickoff — measured capacity, readiness check, commit vs stretch, dependencies, one-sentence goal, meeting agenda |
| [`/programs:retro`](plugins/programs/commands/retro.md) | programs | Retrospective — follow-through check, data first, ≤3 owned actions, durable lessons filed separately; `--incident` routes to post-mortem |
| [`/bizops:meeting-prep`](plugins/bizops/commands/meeting-prep.md) | bizops | Meeting prep — purpose and decision sought, open items from last time, the room, questions, time-boxed agenda; or a recommendation to cancel |
| [`/discovery:feedback-weekly`](plugins/discovery/commands/feedback-weekly.md) | discovery | Weekly customer-feedback digest — triage, independent-source counts per theme, trend vs last week, routing to roadmap / bug / research |
| [`/communications:deck`](plugins/communications/commands/deck.md) | communications | Build and render a deck from an existing artifact for a named audience — exec, internal, or external |

### Hooks

Event-triggered — they fire *because something happened*, not on a schedule. Two scopes:

| | Lives in | Fires for |
|---|---|---|
| **Plugin hooks** | `plugins/<plugin>/hooks/hooks.json` + scripts | anyone who installs that plugin |
| **Repo hooks** | [`.claude/settings.json`](.claude/settings.json) + [`.claude/hooks/`](.claude/hooks/) | anyone working inside this repo |

**Plugin hooks** ship with the plugin. A hook can't reason — it detects an event and either does something deterministic (recount a table) or injects an instruction so Claude does the reasoning in the same turn. Anything that writes on Claude's behalf asks first.

| Event | Plugin | Hook | What it does | Off switch |
|---|---|---|---|---|
| `SessionStart` | programs | [`standup-nudge.sh`](plugins/programs/hooks/standup-nudge.sh) | Sprint plan present and no standup prep today → one-line reminder to run `/programs:standup` | `SO_STANDUP_NUDGE=off` |
| `PostToolUse` (Write/Edit) | bizops | [`note-actions.sh`](plugins/bizops/hooks/note-actions.sh) | A note landed in the notes folder → run `meeting-analyzer`, present decisions and actions **for confirmation**, then append to the register | `SO_NOTE_ACTIONS=off` |
| `PostToolUse` (Write/Edit) | bizops | [`refresh-status.sh`](plugins/bizops/hooks/refresh-status.sh) | The action register changed → recount open / overdue / due-soon / by-owner and rewrite the status block. Deterministic, idempotent. | `SO_REFRESH_STATUS=off` |
| `PostToolUse` (Write/Edit) | intelligence | [`note-signals.sh`](plugins/intelligence/hooks/note-signals.sh) | A note landed in the notes folder → run `signal-scan` on it, show candidates **for confirmation**, then update the signal log | `SO_NOTE_SIGNALS=off` |

Paths are conventions with env-var overrides — `SO_NOTES_DIR` (`meetings/`), `SO_ACTION_REGISTER` (`actions.md`), `SO_SIGNAL_LOG` (`signal-log.md`), `SO_SPRINT_PLAN` (`sprint.md`), `SO_STANDUP_DIR` (`standups/`). Each plugin's README documents the ones it uses.

**Repo hooks** are for maintaining this repo itself.

| Event | Hook | What it does |
|---|---|---|
| `PostToolUse` (Edit / Write) | [`refresh-catalog.sh`](.claude/hooks/refresh-catalog.sh) | Auto-runs `scripts/catalog.py` whenever a plugin file (SKILL.md, agent, or command) is edited — the catalog and READMEs never drift. Silent on success; warns on missing PyYAML. |
| `UserPromptSubmit` | [`log-prompt.sh`](.claude/hooks/log-prompt.sh) | Appends every user prompt to `.claude/sessions/YYYY-MM-DD.md` — a running log of what you asked Claude, per day. Session logs are gitignored (personal record, not shared). |

**Requirements.** All hooks need `python3` on your PATH. The catalog-refresh hook also expects PyYAML. `pip install pyyaml` (or the equivalent for your environment) once, and it works forever.

**Opt out.** Plugin hooks: set the env var shown in the table. Repo hooks: edit `.claude/settings.json` or override with a `.claude/settings.local.json` (gitignored).

### MCP servers

Not yet configured. Some of the borrowed skills gesture at MCP integrations in their CONNECTORS.md — Slack, Notion, Jira, Confluence, Linear — but I haven't installed and documented these yet. That's the next automation layer.

---

## Sources & Attribution

### Provenance conventions

Every skill, agent, and command is labeled with one of three provenance types:

- **Original** — I wrote it from scratch. Author: `maitlam`.
- **Adapted** — Started from someone else's work and meaningfully reshaped. Each has a `CHANGES.md` explaining what changed and why. `metadata.adapted-from` points to the source.
- **Included** — Someone else's work, brought in as-is and credited. `metadata.source` points to the upstream file. The only edit is the provenance label in the frontmatter.

Labels live in each item's frontmatter (`metadata.provenance`). The catalog above is generated from them, so it can't drift out of date. CI enforces every item to be labeled and every non-original item to link back to its upstream source.

### Upstream sources

Borrowed work keeps its original license, noted in each item's frontmatter:

- **Anthropic** · [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) · Apache License 2.0
- **Amin Borghei** · [Claude-Skills](https://github.com/borghei/Claude-Skills) · MIT + Commons Clause — use, modify, share; do not sell.

Full license texts are in each plugin's `LICENSES/` folder. [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) describes exactly what changed from the originals.

My original work is released under the [MIT License](LICENSE).

### Keeping in sync with upstream

Nothing here is a fork, so upstream changes never arrive automatically and nothing flows back. [`sources.json`](sources.json) records the exact upstream commit each borrowed item came from.

```bash
python3 scripts/check_upstream.py                      # what changed upstream since I copied?
python3 scripts/check_upstream.py --diff pre-mortem    # see the changes for one item
python3 scripts/check_upstream.py --merge pre-mortem   # merge them in (or --merge all)
```

Merging is three-way: it compares upstream's old version, upstream's new version, and my copy — my edits and provenance labels are preserved. If upstream changed the same lines I did, the file gets standard `<<<<<<<` conflict markers to resolve; nothing is marked synced until I do.

---

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
