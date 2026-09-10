---
name: resource-allocation
description: Match a portfolio's demands against a team's real capacity and show where it is oversubscribed, including the person-level constraints that determine dates. Use whenever the user is staffing initiatives, asks whether the team can absorb something new, is building a resourcing plan, or wonders why everything is late. Trigger on "do we have bandwidth," "can we take this on," "how should I staff this," or any allocation conversation.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Resource Allocation

A portfolio and a team in. An honest read on what actually fits, out.

## The framework behind this

Allocation planning fails on one arithmetic error repeated everywhere: treating headcount as capacity.

A person is not a unit of delivery capacity. Between meetings, interviews, on-call, support, onboarding, and keeping existing things running, the fraction of a week available for new committed work is usually 50–70% — and it is never 100%, though nearly every plan implicitly assumes it. **A plan built on full allocation is not aggressive, it is arithmetically wrong**, and it produces the same slip every quarter while everyone wonders why.

Two further disciplines.

**Overhead gets named, not absorbed.** If a support rotation eats a day a week, that day is a line item. Hiding it inside optimism means it gets paid for out of committed work, silently, and the shortfall surfaces as individual underperformance rather than a planning error.

**The output is a constraint, not a schedule.** The useful result is "you are oversubscribed by 1.5 people, and here are the three things that could give." A tidy allocation table that happens to fit is usually a sign the numbers were bent until it did.

The binding constraint is almost never total capacity. It's one person or one skill that four initiatives all need, and team-level averages conceal it perfectly.

## Process

1. **Establish real available capacity.** Headcount, minus known time off, minus a named overhead percentage. Make the user state the overhead figure; if never measured, use 30% and label it an assumption.
2. **List demands with their claim**, including run-the-business work nobody counts.
3. **State the gap in both directions** — oversubscribed by how much, or genuinely available.
4. **Find the person-level constraint.**
5. **Give options, not a verdict.** What could be cut, deferred, sequenced differently, or resourced from outside.

## Output format

```markdown
# Resource Allocation: [Team] — [period]

## The read
[Oversubscribed, balanced, or available — and by how much.]

## Available capacity
| Person / role | Nominal | Time off | Overhead % | Available |
|---|---|---|---|---|
**Total available: X person-weeks**
*Overhead assumption: N% — [measured / estimated / unvalidated]*

## Demand
| Initiative | Claim | Owner | Fixed or flexible? |
|---|---|---|---|
**Total demand: Y person-weeks**

## Gap: [±Z person-weeks]

## Binding constraint
[The specific person or skill that sets the dates.]

## Options
1. [What gives, what it costs, who decides.]

## Assumptions
- [Anything unvalidated, especially the overhead figure.]
```

## Hold the line on

- **Never plan at 100% allocation.** If the user insists, state what it implies: zero absorption of anything unplanned, and slip as the only release valve.
- **Count run-the-business work.** Support, maintenance, and interviews are capacity even when they're on nobody's roadmap.
- **Never pad silently.** Named buffer survives scrutiny; hidden buffer destroys trust in the whole plan when found.
- **Always name the person-level constraint.** Team averages hide the one bottleneck that determines the date.
