---
name: research-brief
description: Produce a deep, sourced research brief on a single topic — scope confirmed first, the topic decomposed into lenses so coverage is systematic, every fact sourced and dated, observation kept separate from inference, and the brief ending in what is still unknown. Runs the lenses in parallel through the lens-researcher agent when it is available and sequentially otherwise. Use whenever the user needs to understand a topic, market, practice, or technology deeply enough to make a decision or teach it to others, or asks for "research on," "a brief on," "a deep dive on," "help me understand," or "what do we know about" anything.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Research Brief

One topic and a purpose in. A brief someone can make a decision from, and a list of what it couldn't settle, out.

## The framework behind this

Unscoped research produces whatever the first few searches happened to return, written up at whatever length felt like enough. It reads fine and answers nothing in particular, because nothing in particular was asked.

**Scope before search.** Three questions change the entire shape of the work: what matters most about this topic, how deep to go, and who will read it. A leadership readout and a working-notes deep dive on the same topic share almost nothing. Ask, then research.

**Decompose into lenses, then cover each one.** A topic looked at through one lens gives a partial view that feels complete. The standing set — not all apply to every topic — is:

- **Money** — who pays whom, for what, at what margins; how the economics actually work.
- **Operations** — what this looks like day to day, where it breaks, and the specific failures with names and numbers attached.
- **Players and moves** — who does this, who's winning, what recent deals, exits, and entries say about where it's going.
- **Technology and infrastructure** — what it runs on, what's missing, who supplies it.
- **Evidence** — what outcomes are actually documented, by whom, and how strong the data is.
- **Constraints** — regulation, standards, procurement, and incumbency that shape what's possible.

Each lens gets its own sub-questions and its own pass. Then the lenses are read against each other: where do they agree, where do they disagree, and what does the disagreement mean?

**Sourcing is the product.** Every fact carries a source and a date. Every number carries the boundary the source used. Claims are tagged as `observed` (sourced), `inferred` (reasoning from evidence, with the evidence named), or `unknown` (looked for, not found — which is itself a finding). A brief that reads confidently and can't be checked is worse than no brief, because it will be believed.

**Parallel when possible, honest when not.** The lenses are independent, which makes them a natural fan-out: one researcher per lens, each writing findings to a file as it goes so nothing is lost mid-run, then a synthesis pass. Where parallel agents aren't available, run the lenses in sequence with the same discipline and the same output shape. Say which mode was used.

## Gather first

Ask these, unless the user has already answered them or says to proceed on defaults — in which case state the defaults at the top of the brief.

1. **Focus** — which lens matters most, or all of them?
2. **Depth** — quick read (a few pages: framing and key facts), standard (solid coverage of the main lenses), or deep dive (all lenses, operational detail, case examples, sourced tables)?
3. **Audience** — working notes for one person, a team learning document, or a leadership readout?

Also check what the team already has on the topic, so the brief extends it rather than repeating it.

## Process

1. **Confirm scope** and restate the question the brief answers in one sentence.
2. **Decompose.** Choose the lenses that apply; write two to four sub-questions under each. This list is the research plan and goes in the brief's appendix.
3. **Research each lens.**
   - If the `lens-researcher` agent is available: launch one per lens in parallel using the template below — fill the brackets, change nothing else. Collect the files.
   - Otherwise: work the lenses in sequence, writing findings to a file as you go.
   Either way, every finding is a sourced, dated, tagged statement.

   **Lens-researcher launch template** (one per lens, all launched in the same turn):

   ```
   You are the `lens-researcher` agent. Read your instructions first at
   [path to lens-researcher.md] and follow them exactly.

   TOPIC: [topic]
   BOUNDARY: [what's in, what's out, geography]
   QUESTION THE BRIEF ANSWERS: [the one sentence from step 1]
   YOUR LENS: **[Lens name]** — [one-line description of the lens's job]
   DEPTH TARGET: [quick | standard | deep]
   FINDINGS FILE: [absolute path]/findings/[lens].md

   SUB-QUESTIONS:
   1. [sub-question]
   2. [sub-question]
   3. [sub-question]
   4. [sub-question]

   Prefer primary sources: [name the kinds that matter for this topic —
   filings, official statistics, published studies with methodology, dated
   announcements]. Label company self-reported figures as such. Date
   everything. Do not fabricate — `unknown` is a valid entry.

   When done, return: the findings file path, the two or three most
   load-bearing findings, and the unknowns.
   ```
4. **Synthesize across lenses.** Where do they agree? Where does the money lens contradict the players lens, or the evidence lens undercut the operations story? Disagreement between lenses is usually the most useful paragraph in the brief.
5. **Write** to the depth and audience agreed. Lead with the answer; support it; end with what remains open.
6. **List sources and gaps.** Every source with its date. Every sub-question that couldn't be answered from public material, and what would answer it.

## Output format

```markdown
# [Topic] — Research Brief
*[date] · Depth: [quick / standard / deep] · Audience: [who] · Mode: [parallel / sequential]*
*Question: [the one sentence this brief answers]*

## Bottom line
[The answer in one paragraph, for the stated audience. Tag the load-bearing claims.]

## What we found
### [Lens]
[Findings. Each fact sourced and dated inline. Tagged `observed` / `inferred` / `unknown`.]

### [Lens]
…

## Where the lenses disagree
[What one view says that another contradicts, and what that implies.]

## Numbers worth keeping
| Figure | Value | Boundary / definition | Source | Date |
|---|---|---|---|---|

## What this doesn't settle
- [Sub-question] — [why public material couldn't answer it] — [what would]

## Sources
[Numbered. Title, publisher, date, URL.]

## Appendix: research plan
[The lenses and sub-questions as decomposed in step 2.]
```

Depth guides length: quick reads stay to a few pages; standard briefs cover the main lenses fully; deep dives add operational detail, case examples, and sourced tables. Never pad to reach a target; a shorter brief that says what it couldn't find is better than a longer one that hides it.

## Hold the line on

- **Scope first.** No research before the three questions are answered or defaults are stated.
- **No unsourced numbers, and no numbers without their boundary.**
- **Every claim tagged** `observed`, `inferred`, or `unknown`.
- **Date every source.** Undated evidence can't be weighed.
- **Report the mode used.** If the lenses ran sequentially, say so; don't imply parallel coverage that didn't happen.
- **End in gaps.** A brief with no "doesn't settle" section didn't look hard enough.
