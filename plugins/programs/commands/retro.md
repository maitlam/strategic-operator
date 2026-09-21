---
description: Run a sprint or milestone retrospective — data first, then the team's read, then one to three owned actions — and file the durable lessons somewhere they'll be read again
argument-hint: "<sprint, milestone, or period> [--incident]"
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: "0.1.0"
---

# /retro

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Run a retrospective that produces two different outputs and keeps them separate: **actions** (specific, owned, due next sprint) and **lessons** (durable, reusable, filed in a log that outlives the sprint). Most retros produce a wall of sticky notes and neither. This command sequences the data, the discussion, and the filing — and starts by checking whether last retro's actions actually happened.

For an incident, outage, or failed launch, pass `--incident`; the command routes to the blameless `post-mortem` method instead of the sprint retro.

## Usage

```
/retro $ARGUMENTS
```

## How It Works

```
┌────────────────────────────────────────────────────────────────┐
│                          RETRO                                 │
├────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                     │
│  ✓ Check last retro's actions — done, not done, why            │
│  ✓ Build the data view: planned vs delivered, cycle time,      │
│    churn, carry-over                                           │
│  ✓ Structure the team's discussion around what the data shows  │
│  ✓ Separate actions from lessons; file both                    │
├────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                    │
│  + Project tracker: Pull planned vs delivered directly         │
│  + Code hosting: Velocity, cycle time, and churn from history  │
│  + Knowledge base: Read and append the lessons log             │
└────────────────────────────────────────────────────────────────┘
```

## Workflow

### 1. Close the loop on last time

Pull the previous retro's actions. For each: done, partly, or not — and if not, why. A retro that doesn't check its own follow-through is theater, and the team knows it.

### 2. Build the data view

Run `sprint-retrospective` on the period: planned vs delivered, velocity trend, cycle and lead time, carry-over, churn hotspots, where the time actually went. If **~~project tracker** or **~~code hosting** is connected, pull it; otherwise work from exports. The data goes first so the discussion argues with facts rather than impressions.

### 3. Gather the team's read

Three questions, answered before the meeting if possible so quiet people get equal weight:
- What went well that we should keep doing deliberately?
- What got in the way?
- What surprised us?

Cluster the answers. Where the team's read and the data disagree, that's the first thing to discuss.

### 4. Choose the actions

One to three. Each has an owner, a due date inside the next sprint, and a way to tell it happened. If the list is longer than three, the retro is expressing frustration rather than choosing; cut it.

### 5. Extract the lessons

Separately from actions: what did this sprint teach that will still be true in six months? A lesson is a generalization ("estimates for integration work run 2× when the partner API isn't sandboxed") — not a task. Append to the lessons log. If no lessons log exists, create one.

### 6. File and share

The retro doc, the actions into the tracker, the lessons into the log.

## Output

```markdown
# Retro — [sprint or period] · [date]

## Last retro's actions
| Action | Owner | Status | If not done, why |
|---|---|---|---|

## The data
- **Planned / delivered:** [n / n] · **Carry-over:** [n]
- **Cycle time:** [median, and trend]
- **Where the time went:** [top three, with share]
- **Churn hotspots:** [files, areas, or stories reworked most]

## What the team said
### Keep doing
### Got in the way
### Surprised us
### Where the read and the data disagree

## Actions (max 3)
| Action | Owner | Due | How we'll know |
|---|---|---|---|

## Lessons filed
| Lesson | Applies when | Source sprint |
|---|---|---|
```

Lessons log format (one file, append-only):

```markdown
| Date | Lesson | Applies when | Source | Still true? |
|---|---|---|---|---|
```

## Rules

- **Follow-through check comes first.** Every time.
- **Data before opinions.** The team argues with the numbers, not with each other.
- **Actions ≤ 3, each owned and dated.**
- **Lessons ≠ actions.** Lessons go in the log; actions go in the tracker. Never mix them.
- **Blameless.** The question is what the system made easy or hard, not who did what.

## Skills this command uses

- `sprint-retrospective` — the data-driven retro method
- `post-mortem` — when `--incident` is passed
- `cycle-time-analyzer` — flow metrics for the data view
