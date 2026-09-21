---
description: Run the sprint kickoff — real capacity, a readiness check on candidate stories, a commit-versus-stretch split, dependencies and risks named, and a one-sentence sprint goal
argument-hint: "<sprint name or dates>"
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: "0.1.0"
---

# /sprint-kickoff

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Take a team from "the sprint starts Monday" to a sprint plan the team can actually hold itself to. This command sequences the pieces — capacity, readiness, commitment, dependencies, goal — and produces the kickoff document plus the meeting agenda. It does not pick the work; the team does that in the room, with this as the input.

## Usage

```
/sprint-kickoff $ARGUMENTS
```

## How It Works

```
┌────────────────────────────────────────────────────────────────┐
│                      SPRINT KICKOFF                            │
├────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                     │
│  ✓ Compute real capacity from headcount, time off, and         │
│    standing commitments                                        │
│  ✓ Check candidate stories for readiness before they're        │
│    committed to                                                │
│  ✓ Split commit from stretch and name the dependencies         │
│  ✓ Draft the sprint goal and the kickoff agenda                │
├────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                    │
│  + Project tracker: Pull the candidate backlog and last        │
│    sprint's actuals                                            │
│  + Calendar: Pull time off and recurring meeting load          │
│  + Knowledge base: Link the roadmap item each story serves     │
└────────────────────────────────────────────────────────────────┘
```

## Workflow

### 1. Establish capacity

People × working days, minus time off, minus standing meetings, minus support or on-call rotation. If **~~calendar** is connected, pull it; otherwise ask. Compare against last sprint's actual throughput if **~~project tracker** has it — planned capacity that consistently exceeds delivered capacity is the first thing to correct.

### 2. Pull the candidates

The stories being considered, from the tracker or pasted. Note which roadmap outcome each one serves; a story that serves none is a candidate for the "why is this here" conversation.

### 3. Check readiness

Run the `backlog-refinement` check on each candidate: is it INVEST-shaped, does it meet the Definition of Ready, is it small enough to finish inside the sprint? Anything that fails is either refined before kickoff or excluded — it doesn't get committed to on the promise of being refined later.

### 4. Split commit from stretch

Using `sprint-plan`: the commit set fits inside capacity with margin; stretch is what the team picks up if the commit lands early. Be explicit about the margin — a sprint planned to 100% of capacity is planned to fail.

### 5. Name dependencies and risks

From `dependency-map`: what does this sprint need from other teams, by when, and who has confirmed it? What's the risk that shows up mid-sprint, and what's the fallback?

### 6. Draft the sprint goal

One sentence. What will be true at the end of the sprint that isn't true now? If the committed stories can't be summarized in one sentence, the sprint has no goal — it has a list.

### 7. Produce the kickoff pack

The document below, plus a 45-minute agenda for the kickoff meeting.

## Output

```markdown
# Sprint [name] — [start] to [end]

## Goal
[One sentence.]

## Capacity
| Person | Days available | Notes |
|---|---|---|
**Total:** [n] person-days · **Last sprint delivered:** [n] · **Planning to:** [n] ([margin]%)

## Commit
| Story | Serves | Size | Owner | Ready? |
|---|---|---|---|---|

## Stretch
| Story | Serves | Size | Condition to pull in |
|---|---|---|---|

## Not ready — refined or excluded
| Story | What's missing |
|---|---|

## Dependencies
| Need | From | By | Confirmed by |
|---|---|---|---|

## Risks
| Risk | Signal it's happening | Fallback |
|---|---|---|

## Kickoff agenda (45 min)
1. Goal — 5 min
2. Capacity and margin — 5 min
3. Commit set, story by story — 20 min
4. Dependencies and risks — 10 min
5. Confirm and close — 5 min
```

## Rules

- **Capacity is measured, not assumed.** Time off and meeting load come off the top.
- **Nothing unready gets committed.** "We'll refine it during the sprint" is how sprints slip.
- **Plan with margin.** State the margin as a number.
- **One-sentence goal or no goal.** A list is not a goal.

## Skills this command uses

- `sprint-plan` — capacity, commit vs stretch, risk identification
- `backlog-refinement` — INVEST and Definition of Ready checks
- `dependency-map` — cross-team dependencies and critical path
