---
name: ecosystem-map
description: Segment an unfamiliar market or ecosystem into its structural parts — who the actors are, how value and money move between them, and where the pain concentrates. Use whenever the user is entering a space they don't yet understand, needs a landscape view rather than a company profile, is planning discovery conversations, or asks who the players are in a market. Trigger on "map this space," "landscape," "who's in this market," or any request to understand a market's structure before evaluating anyone in it.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Ecosystem Map

An unfamiliar market in. Its structure, and where to point discovery next, out.

## The framework behind this

The instinct on entering a new space is to start profiling companies. That produces a pile of profiles and no understanding, because a company only makes sense relative to the structure it sits in — and you can't see the structure from inside a list of vendors.

Segment first. **The segments that matter are defined by role in the value chain, not by product category.** In healthcare, "payers, providers, clinicians, pharma, health tech" is a structural segmentation: each has different incentives, different buying behavior, and different pain. "Analytics companies, workflow companies, AI companies" is a product taxonomy — it looks like a segmentation and explains nothing, because the incentives inside each bucket are unrelated.

Two more.

**Follow the money separately from the value.** Who benefits and who pays are frequently different parties, and that gap is where most of the interesting structural pain lives. Any segment where the party experiencing the pain isn't the party with the budget is worth flagging loudly.

**The map's job is to direct discovery, not to conclude.** A landscape map ends in a ranked list of who to go talk to and what to ask them. If it ends in a conclusion about the market, it was built on desk research pretending to be knowledge.

Most of what an ecosystem map produces is negative information — segments that turned out not to matter. That's not waste; that's the map working. Say so explicitly, because it protects the effort from being judged on how many partners it produced.

## Process

1. **Identify segments by role**, not category. Aim for four to six; more means the segmentation isn't doing work.
2. **For each: who they are, what they optimize for, who pays them, what they buy.**
3. **Trace value and money flows between segments**, and note where they diverge.
4. **Locate pain by segment**, distinguishing observed from assumed.
5. **Name the structural constraints** — regulation, incumbency, procurement cycles, switching costs — that shape what's possible for anyone here.
6. **Produce a discovery list:** who to talk to, in what order, and the specific question each conversation answers.

## Output format

```markdown
# Ecosystem Map: [Market] — [date]
*Confidence: [desk research / partial discovery / N conversations]*

## Structure in one paragraph
[How this market is organized and what governs it.]

## Segments
### [Segment] — [rough size or count]
- **Optimizes for:** [their actual incentive, not their mission statement]
- **Paid by:** [who]
- **Buys:** [what, and through what process]
- **Pain observed:** [with source]
- **Pain assumed:** [labeled clearly]

## Value and money flows
[Where they diverge. Any segment feeling pain without holding budget.]

## Structural constraints
- [Regulation, incumbency, procurement, switching costs.]

## Where the opportunity concentrates
[2–4 sentences of judgment. Labeled as inference.]

## Discovery list
| Who | Segment | Question this answers | Priority |
|---|---|---|---|

## Ruled out
- [Segments examined and set aside, with the reason. Negative findings
  are findings.]
```

## Hold the line on

- **Never segment by product category.** If the segments don't have distinct incentives, re-segment.
- **Separate observed pain from assumed pain** in every segment. This is the discipline that keeps a map honest.
- **Never fabricate counts or market sizes.** "Not established from public sources" is correct and usable.
- **End in a discovery list, not a conclusion.** A map that concludes is over-claiming what desk research supports.
