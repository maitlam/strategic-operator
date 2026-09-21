---
name: research-agenda
description: Turn a pile of open questions, graduated signals, and untested assumptions into a prioritized research roadmap — each item framed by the decision it feeds and what "answered" looks like. Use whenever the team has more questions than research capacity, when signals have graduated from a signal log and need a home, when someone asks what we should research next, or when research keeps going to whoever asked loudest. Trigger on "research roadmap," "what should we look into," "research priorities," "research agenda," or any request to organize and rank open questions.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Research Agenda

Open questions from everywhere in. A ranked list of what to research, why, and what it will change, out.

## The framework behind this

Without an agenda, research is allocated by recency and volume: the last question asked, or the one asked most often, gets the time. That's how teams end up with a deep brief on something nobody needed and no answer to the question a decision was actually waiting on.

**A research item is a question attached to a decision.** The framing is not optional context; it is the reason the item exists. Every entry on the agenda states the question, the decision that depends on the answer, and what the team would do differently depending on how it comes out. A question with no decision behind it is curiosity, and curiosity gets parked, not scheduled.

Priority comes from four things, in roughly this order:

- **Decision proximity** — is a decision waiting on this now, or eventually, or never?
- **Evidence gap** — how little does the team actually know, versus how much it believes it knows?
- **Cost of being wrong** — what happens if the current assumption holds and is false?
- **Answerability** — can desk research answer this, or does it need conversations, a pilot, or data the team doesn't have? Research time spent on a question that only a customer can answer is wasted.

And one more rule: **"answered" must be defined before the work starts.** A brief that could go on forever will. Each item says what evidence would settle it, at what depth, so the research knows when to stop.

## Gather first

- The candidate questions: graduated signals from a signal log, assumptions surfaced in strategy or discovery work, questions raised in reviews, anything a stakeholder has asked for.
- The decisions on the team's horizon and their rough timing.
- What has already been researched, so the agenda doesn't re-ask answered questions.
- Research capacity — how many briefs, at what depth, in the period.

## Process

1. **Collect and phrase as questions.** Every candidate becomes a question someone could answer. "Competitor pricing" is a topic; "Is competitor X's per-seat price below ours for teams under fifty, and does it include the features buyers compare us on?" is a question.
2. **Attach a decision.** For each: which decision does this feed, when is it being made, and what changes depending on the answer? No decision → park it with that reason.
3. **Score** on the four criteria. Keep it coarse — high, medium, low — and be honest about answerability. Route anything that needs a conversation to discovery instead.
4. **Define "answered."** What evidence, at what depth (quick read, standard brief, deep dive), settles it.
5. **Rank and group** by theme so related questions can share a brief.
6. **Check against prior work.** Link anything already partly answered; narrow the question to the gap.
7. **Set the review trigger.** The agenda gets refreshed when a signal graduates, a decision closes, or a brief comes back — not on a fixed calendar alone.

## Output format

```markdown
# Research Agenda — [date]
*Capacity this period: [N briefs / depth mix]. Next review: [trigger or date]*

## Now
| # | Question | Decision it feeds | Due by | Depth | Status |
|---|---|---|---|---|---|

## Next
| # | Question | Decision it feeds | Depth | Status |
|---|---|---|---|---|

## Parked
| Question | Why parked |
|---|---|

## Routed elsewhere
| Question | Needs | Where it went |
|---|---|---|
| [Question] | conversations / pilot / internal data | discovery / ops |

## Answered this period
| Question | Answer in one line | Brief |
|---|---|---|

---

### Item detail
#### [#] [Question]
- **Decision it feeds:** [which, and when]
- **If the answer is X we would:** …  **If Y we would:** …
- **What we believe now:** [the current assumption and where it came from]
- **Evidence gap:** [what's actually known vs. assumed]
- **"Answered" means:** [the evidence and depth that settles it]
- **Source of the question:** [signal log row / review / person]
```

Statuses: **Open**, **In progress**, **Answered** (with link), **Parked** (with reason).

## Hold the line on

- **No item without a decision it feeds.** This is the whole filter.
- **Phrase every item as a question.** Topics can't be answered; questions can.
- **Route un-researchable questions out, don't rank them low.** A question that needs a customer conversation belongs in discovery, not at the bottom of this list forever.
- **Define "answered" before starting.** Open-ended research doesn't end.
- **Parked items carry a reason.** So they can be revisited when the reason changes.
- **Answered items link to the brief.** The agenda is also the index of what the team knows.
