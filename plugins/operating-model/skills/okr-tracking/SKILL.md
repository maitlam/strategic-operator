---
name: okr-tracking
description: Draft, review, or check in on objectives and key results — including diagnosing OKRs that are really task lists in disguise. Use whenever the user is writing goals for a quarter or year, asks whether their OKRs are any good, needs a mid-cycle or end-of-cycle check-in, is grading results, or is trying to connect team goals to company ones. Trigger on "OKRs," "quarterly goals," "key results," "am I on track," or any goal-setting and goal-review conversation.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# OKR Tracking

Goals in. Key results that measure outcomes rather than activity — or an honest diagnosis of why the current ones don't.

## The framework behind this

The overwhelming majority of OKRs in the wild are project plans wearing a costume. "Launch the new portal" is a task. It has a completion date, not a measurement. Written as a key result, it guarantees a green score for shipping something nobody used.

The distinction the whole method rests on: **an objective is a direction, a key result is evidence you moved.** If a key result can be satisfied by completing an activity regardless of its effect, it isn't one.

Three things follow.

**Leading and lagging must coexist.** Lagging KRs measure what you actually care about but arrive too late to steer by. Leading KRs move early but only proxy the real thing. A set with only lagging indicators can't be managed mid-cycle; a set with only leading ones can be gamed. Label each.

**The mid-cycle check is the point.** Grading at the end is bookkeeping. The value of the method is the conversation at week six, when a KR sits at 20% and there's still time to change what the team is doing.

**Confidence beats percentage.** "40%, confidence dropping" is far more useful than "40%." Trajectory is the signal, and it's what the check-in conversation actually runs on.

## Process

1. **Check the objective is a direction, not a deliverable.** If it contains a ship date, it's a project.
2. **Test each KR against the activity trap:** could this be fully satisfied without the objective being any more true? If yes, rewrite it.
3. **Label each KR leading or lagging**, and flag a set that's all one kind.
4. **For check-ins, capture trajectory and confidence**, not just current value.
5. **Say what changes.** A check-in producing no decision was a status meeting.

## Output format

```markdown
# OKRs: [Team] — [Cycle]

## Objective: [Direction. Qualitative. No dates.]
*Why this matters now: [one line]*

| Key result | Baseline | Target | Current | Type | Confidence |
|---|---|---|---|---|---|
| | | | | Leading / Lagging | High / Med / Low ↑↓ |

## Check-in read
[What the trajectory says, not what the numbers say.]

## What we're changing
- [Concrete and owned. If nothing changes, say why that's the right call.]

## Flagged
- [KRs that are activity in disguise, missing baselines, or unmeasurable
  as written.]
```

## Hold the line on

- **Refuse the activity trap.** "Ship X" is not a key result. Offer the outcome version — but if the user genuinely needs to track deliverables, tell them that's a project plan, which is a legitimate thing to want and not this.
- **A KR without a baseline is not measurable.** Flag it rather than scoring it.
- **Never invent a current value.** Unknown is a finding.
- **Never grade without trajectory.** A number alone hides whether the team is gaining or losing ground.
