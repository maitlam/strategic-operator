# Operator

The strategic operator's own toolkit. Weekly rhythm rituals and exec comms craft — the connective-tissue work a generalist, chief of staff, or biz-ops lead does on top of the function-centered plugins.

## The domain view

Everywhere else in this repo is organized by *function* — bizops, programs, portfolio, intelligence. This plugin is organized by *role*. The operator is the person who connects those functions, writes the memo that lands, runs the Monday that sets the week, and reshapes the status update into something an exec will actually act on.

Two threads here:

**The weekly rhythm.** A Monday packet that frames the week in advance of it happening, and a Friday wrap that closes the loop. Both force a top-3 synthesis — not a dump — because the point of the ritual is a decision about where attention goes, not a transcript of what happened.

**Exec comms craft.** A memo rewriter that picks the right pattern (BLUF, SCQA, Amazon-narrative) and enforces house-style defaults a tech-startup CoS would recognize: TL;DR up front, decision ask explicit, DRI named, reversibility called out, confidence stated. A talking-points skill that refuses to produce ten — three max, each with anticipated pushback and the response.

Both threads will grow. Decision log, stakeholder profiles kept across weeks, 1:1 prep — those live here when they land.

| Item | In → Out |
|---|---|
| `/operator:monday-packet` | Your inputs for the week → the three things that matter |
| `/operator:friday-wrap` | What happened → 3 wins, 3 misses, 3 to watch |
| `/operator:one-on-one-prep` | A person + current context → three to raise, three to listen for |
| `/operator:setup-scheduling` | OS + workflow tool + timing → scheduler config + setup walkthrough written to disk |
| `exec-memo` | A draft + audience + the ask → a reshape with the pattern labeled |
| `talking-points` | A meeting + the outcome you want → three points with pushback and response |
| `decision-log` | A decision → appended to a running, searchable log |
| `stakeholder-profile` | A person + an interaction → living profile that persists across weeks |
| `red-team-critic` (agent) | An artifact + its audience → steelman critique, named pushback, ranked fixes |

## Install

```
/plugin marketplace add maitlam/strategic-operator
/plugin install operator@strategic-operator
```

## State: the one convention

Two skills in this plugin — `decision-log` and `stakeholder-profile` — maintain state across sessions. They're the first *living* artifacts in the repo. The convention:

- Default base path: **`~/.claude/operator/`**
- Decision log: `~/.claude/operator/decisions.md` (single file, newest-first)
- Stakeholder profiles: `~/.claude/operator/stakeholders/<slug>.md` (one file per person)
- Override: set `OPERATOR_STATE_DIR` to a different base (e.g., `~/work/acme/.operator` for a per-client workspace)

User-global by default because the operator's attention isn't scoped to a project — Sarah the CFO shows up across every initiative. Override when confidentiality or per-client isolation matters.

The files are yours. Commit them to a private repo if you want version history; keep them local if you don't. The skills don't care, and neither does the repo.

## Scheduling the rituals

The Monday and Friday rituals can run on a schedule — fed by a staging folder (`~/.claude/operator/inbox/`) that any workflow tool (Power Automate, Apps Script, bash cron, or hand-dropped files) can write into.

Set it up by running `/operator:setup-scheduling` — a four-question wizard that writes the right scheduler config and a tool-specific setup walkthrough. See [`scheduling/README.md`](scheduling/README.md) for the loose contract and manual-setup path.

## Skills and commands

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`decision-log`](skills/decision-log/SKILL.md) | Original | Maintain a running log of decisions — append new ones, query the history, mark pending items as decided, flag supersessions |
| [`exec-memo`](skills/exec-memo/SKILL.md) | Original | Rewrite a draft memo, update, or doc for an exec audience — pick the right pattern (BLUF for decision asks, SCQA for analytical framing, Amazon-narrative for… |
| [`stakeholder-profile`](skills/stakeholder-profile/SKILL.md) | Original | Maintain a living profile for a specific person — their role, what they care about, how they want information, prior positions and pushback, recent touchpoints, and open… |
| [`talking-points`](skills/talking-points/SKILL.md) | Original | Prepare three talking points for a specific meeting — each point with a one-line "say this," the supporting evidence, the anticipated pushback, and the response |
| [`/friday-wrap`](commands/friday-wrap.md) (command) | Original | Close the week — 3 wins, 3 misses, 3 to watch, plus a decision log of what actually got decided, what shipped vs |
| [`/monday-packet`](commands/monday-packet.md) (command) | Original | Produce the Monday morning packet — the three things that matter this week, high-stakes meetings and prep gaps, pending decisions, at-risk items you own, overnight asks… |
| [`/one-on-one-prep`](commands/one-on-one-prep.md) (command) | Original | Prep for a specific 1:1 — reads the stakeholder's profile, surfaces open asks in both directions, drafts three things to raise with anticipated pushback, three things to… |
| [`red-team-critic`](agents/red-team-critic.md) (agent) | Original | Stress-test an artifact before it ships — argue the strongest version of the counter-case, surface hidden assumptions, name who will push back on what, identify concrete… |
| [`/setup-scheduling`](commands/setup-scheduling.md) (command) | Original | One-time interactive wizard to set up scheduled Monday-packet and Friday-wrap rituals |
<!-- catalog:end -->

## How this plugin is different

Most of the repo is function-centered — someone running Programs reaches for `/programs:*`, someone running Portfolio reaches for `/portfolio:*`. The operator reaches across all of those plus their own inbox and calendar, and the deliverable is a weekly cadence of their own attention. These skills and commands are built around that cadence rather than around a function's artifacts.
