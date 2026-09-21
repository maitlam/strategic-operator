---
name: market-sizing
description: Size a market with a defensible range rather than a single number — TAM, SAM, and SOM built bottom-up and top-down, reconciled, with every assumption visible and the one that drives the answer named. Use whenever the user asks how big a market is, needs a TAM/SAM/SOM for a plan, deck, or investment case, wants to check a number someone else produced, or is deciding whether an opportunity is large enough to pursue. Trigger on "how big is this market," "TAM," "market size," "is this worth going after," or any request to put a number on an opportunity.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Market Sizing

A market and a boundary in. A range, the assumptions that produce it, and the one assumption that matters most, out.

## The framework behind this

Most market sizes are a single large number with no visible reasoning, produced to make a slide work. They can't be checked, can't be argued with, and can't be improved — which is why the same "$40B market" survives for years after everyone stopped believing it.

The number is not the deliverable. **The assumptions are the deliverable.** Any market size is a function of four or five inputs, and the decision it feeds usually turns on one of them. A sizing that exposes those inputs can be tightened by discovery; one that hides them is a guess wearing a suit.

Three disciplines.

**Fix the boundary before touching a number.** What is being counted — which buyers, which geography, which unit of sale, over what period? Two people who disagree about a market's size almost always disagree about its boundary and don't know it. Write the boundary down first, and every step-down from TAM to SAM to SOM is a stated boundary decision, not a percentage pulled from the air.

**Build it two ways and make them fight.** Top-down (start from a published figure and narrow) is fast and inherits someone else's boundary and method. Bottom-up (count buyers × adoption × frequency × price) is slower and makes every assumption visible. Run both. If they land within a factor of two or three, the range is credible. If they don't, the disagreement is the finding — one of the boundaries is wrong, and finding out which teaches more about the market than either number.

**Ranges, never points.** A point estimate claims a precision the inputs don't have. Give the low, the base, and the high, and say which input moves it most.

## Gather first

- The boundary: buyer type, geography, unit of sale, time period.
- What decision the size feeds. "Is it big enough to bother" needs a different precision than "how much to raise."
- Any published estimates already in circulation, with their sources — these are inputs to check, not answers to adopt.

## Process

1. **Write the boundary.** One paragraph. Who is counted, where, buying what, over what period. Everything after this is relative to it.
2. **Build bottom-up.** Choose the counting unit (accounts, sites, users, transactions). For each factor — count, adoption or penetration, frequency, price — record the value, its source, and a confidence label. Where no source exists, label the factor `assumed` and give the reasoning. Multiply through for low, base, and high.
3. **Build top-down.** Find one to three published figures. For each, record its boundary and method as best it can be determined. Narrow each to your boundary with explicit step-downs and note where you had to guess at the source's scope.
4. **Reconcile.** Compare the two. Within ~3×: report the overlap as the working range. Outside it: identify which boundary or factor explains the gap. Do not average them to make the tension go away.
5. **Run sensitivity.** Vary each bottom-up factor across its plausible range, holding the others at base. Name the factor that moves the total most. That factor is what discovery should go tighten.
6. **Step down to SAM and SOM.** Each step is a boundary decision — a segment you can actually reach, a share you can plausibly win given competition and capacity — stated in words, not as a percentage of the previous line.
7. **Say what would change the number.** Which conversation, dataset, or pilot would narrow the range, and by how much.

## Output format

```markdown
# Market Sizing: [Market] — [date]
*Purpose: [the decision this feeds]*

## Boundary
[Who is counted, where, buying what, over what period. One paragraph.]

## Working range
| | Low | Base | High |
|---|---|---|---|
| TAM | | | |
| SAM | | | |
| SOM | | | |

**Driven most by:** [the one factor from sensitivity]

## Bottom-up
| Factor | Low | Base | High | Source | Confidence |
|---|---|---|---|---|---|
| [Counting unit] | | | | | observed / assumed |
| Adoption | | | | | |
| Frequency | | | | | |
| Price | | | | | |

## Top-down
| Published figure | Their boundary | Their method | Narrowed to ours | Notes |
|---|---|---|---|---|

## Reconciliation
[Do the methods agree? If not, which boundary or factor explains the gap.]

## Sensitivity
| Factor | Range tested | Effect on base TAM |
|---|---|---|

## Step-downs
- **TAM → SAM:** [the boundary decision, in words]
- **SAM → SOM:** [the boundary decision, in words]

## What would tighten this
- [Conversation, dataset, or pilot] → [which factor it narrows]
```

## Hold the line on

- **Never a point estimate without a range.** The range is the honest answer; the point is a convenience.
- **Never cite a published number without its boundary and method.** If they can't be determined, say so and weight it accordingly.
- **Never derive SOM as a percentage of TAM.** "1% of a big number" is not a plan; SOM is a boundary decision about reach and share.
- **Every bottom-up factor is sourced or labeled `assumed`.** No unlabeled numbers.
- **Report disagreement between methods; don't smooth it.** The gap is information.
