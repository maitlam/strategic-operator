---
description: Prep the daily standup — what moved since yesterday, what's aging, what's blocked, and the one or two things the standup actually needs to decide
argument-hint: "[team or sprint] [--since yesterday|<date>]"
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: "0.1.0"
---

# /standup

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Prepare the daily standup so it runs in ten minutes and decides something. This command produces the prep, not the meeting: a one-page read of what changed, what's stuck, and what needs a call — so the standup skips status recitation and goes straight to the two things worth discussing.

## Usage

```
/standup $ARGUMENTS
```

Defaults to the active sprint and the delta since yesterday. Pass a team or sprint name to narrow, or `--since <date>` after a weekend or a skipped day.

## How It Works

```
┌────────────────────────────────────────────────────────────────┐
│                        STANDUP                                 │
├────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                     │
│  ✓ Read a pasted board export or yesterday's notes             │
│  ✓ Compute the delta: done, moved, new, blocked                │
│  ✓ Flag aging work-in-progress and dependencies at risk        │
│  ✓ Name what the standup needs to decide                       │
├────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                    │
│  + Project tracker: Pull the board state directly              │
│  + Chat: Catch blockers raised in channels overnight           │
│  + Calendar: Note who's out and what's colliding today         │
└────────────────────────────────────────────────────────────────┘
```

## Workflow

### 1. Establish the window

Since yesterday's standup unless told otherwise. If there was no standup yesterday, say which window is being used.

### 2. Pull the state

If **~~project tracker** is connected, pull the sprint board. Otherwise ask for an export or work from yesterday's prep plus whatever the user pastes. If **~~chat** is connected, scan the team channel for blockers or asks raised since the last standup. If **~~calendar** is connected, note who's out today.

### 3. Compute the delta

Using the `sprint-plan` commitment as the baseline:
- **Done** since the window opened
- **Moved** — anything that changed state without finishing (in review, in test, back to in-progress)
- **New** — scope that appeared mid-sprint
- **Blocked** — and by what, and since when

### 4. Flag what's aging

Apply the `cycle-time-analyzer` lens: anything in progress longer than the team's typical cycle time gets flagged with its age. Aging work is the earliest signal a sprint is slipping and the one standups most reliably ignore.

### 5. Check dependencies

From the `dependency-map`, if one exists: any cross-team dependency due in the next few days that hasn't moved.

### 6. Name the decisions

At most two. What does this standup need to decide — a re-prioritization, a swarm on a blocker, a scope cut, an escalation? If nothing needs deciding, say so; the standup can be short.

## Output

```markdown
# Standup prep — [date] · [sprint], day [n] of [N]
*Window: since [when]. Out today: [names or none]*

## Needs a decision
1. [The call, who makes it, and what happens if it isn't made today]
2. …

## Since last standup
- **Done:** [items]
- **Moved:** [item → state]
- **New:** [items, and whether they displaced anything]
- **Blocked:** [item — blocked by — since]

## Aging
| Item | Owner | In progress for | Typical |
|---|---|---|---|

## Dependencies due this week
| Dependency | Owning team | Due | Moved? |
|---|---|---|---|

## Suggested order
[The two or three items to talk about, in order. Everything else is on the board.]
```

## Rules

- **Prep, not minutes.** This is read before the standup, not written after it.
- **Decisions first.** If the prep leads with status, it has failed.
- **Aging is always reported**, even when nobody wants to hear it.
- **Say "nothing to decide" when true.** Manufacturing urgency trains the team to skim.

## Skills this command uses

- `sprint-plan` — the commitment baseline
- `cycle-time-analyzer` — aging and flow signals
- `dependency-map` — cross-team risk
