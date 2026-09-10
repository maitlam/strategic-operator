---
name: portfolio-intake
description: Design or run the front door for a portfolio — how opportunities enter, what information is required before anything is evaluated, and what happens to things that don't qualify. Use whenever ideas arrive through side channels, the user needs an intake process or request form, a team is drowning in unsorted requests, or someone asks how work should get proposed. Trigger on "intake," "request process," "how do ideas get in," or a backlog that arrived without structure.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Portfolio Intake

Unsorted incoming requests in. A front door with a defined bar, out.

## The framework behind this

Every team without an intake process has one anyway — it's just informal, and it runs on proximity to whoever is loudest. The result isn't an absence of prioritization. It's prioritization by access, which is the worst available algorithm and the hardest to see.

A designed front door does three things the informal one can't.

**It sets a minimum submission bar.** The single highest-leverage element of any intake process is the list of things a submitter must supply before evaluation happens. Not because paperwork is good, but because **the bar filters.** Requiring a stated problem, an affected population, and a rough size kills a meaningful fraction of requests at zero cost to the receiving team — the submitter discovers they don't have an answer.

**It makes rejection legible.** "No" delivered without a reason generates a second attempt through a different channel. "No, because it doesn't clear the strategic-fit bar, and here's what would change that" ends the loop, and occasionally produces a better resubmission.

**It gives everything a disposition.** The failure mode of intake is the silent queue: items that were never accepted and never rejected, which the submitter still believes are alive. Every item leaves with a state and a date.

Intake is deliberately separate from scoring. Intake decides whether something is *complete enough to evaluate*; `opportunity-scoring` decides whether it's *good*. Merging them means the team ends up debating merit on half-specified requests.

## Process

1. **Define the minimum submission set.** Problem, who has it, evidence, rough size, requester, and the sponsor if there is one.
2. **Set the qualification bar** — the conditions for entering evaluation at all.
3. **Define dispositions:** accepted for scoring, returned for more information, rejected with reason, or parked with a revisit date.
4. **Set a response SLA.** An intake process with no turnaround commitment gets routed around within a month.
5. **Name the intake owner**, and how often the queue is reviewed.
6. **Decide where it lives** so submitters can see status without asking.

## Output format

```markdown
# Portfolio Intake: [Team]
*Owner: [name] · Reviewed: [cadence] · Response SLA: [N days]*

## Required to submit
| Field | Why it's required |
|---|---|
| Problem statement | |
| Who has this problem, and how we know | |
| Rough size | |
| Requester and sponsor | |

## Qualification bar
An item enters evaluation only if:
- [Condition]

## Dispositions
| Disposition | Meaning | What the submitter gets |
|---|---|---|
| Accepted | Enters scoring | Date it will be scored |
| Returned | Incomplete | What's missing |
| Rejected | Doesn't clear the bar | The reason, and what would change it |
| Parked | Right idea, wrong time | Revisit date |

## Current queue
| Item | Received | Disposition | Owner | Next step |
|---|---|---|---|---|

## Routed around
- [Items that arrived outside this process, and where the gap is.]
```

## Hold the line on

- **Never leave an item without a disposition.** The silent queue is what destroys trust in intake.
- **Always give a reason with a rejection**, and what would change it.
- **Don't score at intake.** Completeness and merit are separate gates; blending them produces arguments about half-specified ideas.
- **Enforce the SLA or lower it.** A missed turnaround teaches people to go around the process, and they will not come back.
