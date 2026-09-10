---
name: positioning-brief
description: Write or stress-test a one-page positioning brief — who we're for, what we do, why it's different, what we deliberately are not. The artifact that positioning frameworks (SWOT, Porter's, canvases) are all trying to converge on. Use when the user is defining positioning for a new product or company, feels their positioning is fuzzy, is drafting messaging or a homepage, or has been running frameworks and needs to turn the outputs into a stateable, testable page. Trigger on "our positioning," "positioning statement," "who are we for," "why us," "how do we describe ourselves," or when frameworks have run and the answer still isn't crisp.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Positioning Brief

The one-page artifact positioning work is trying to produce. Not another framework — the output frameworks feed. If you can't fit your positioning on a page a stranger can describe back to you, the frameworks were rehearsal.

## The framework behind this

Most positioning fails at the same step. The team runs frameworks (SWOT, Porter's, business-model canvas, ICP work), produces slides, everyone nods, and the actual homepage still reads like the last homepage. Frameworks are analysis; positioning is a commitment. The commitment lives in one page — or it doesn't live.

The distinction the whole method rests on: **positioning is what you deliberately give up.** Everyone can say who they're for and what they do. The load-bearing question is: who are you deliberately NOT for, and what are you deliberately NOT doing? A positioning brief that has no explicit "not for" section is a marketing brochure.

Three things follow.

**Positioning is stateable, not implied.** If a new hire, a prospect, and a partner can't independently produce roughly the same sentence about who you are, you don't have positioning — you have hope. The brief exists to make the sentence a fact.

**Language belongs to the customer.** How you describe yourselves internally is not positioning. Positioning is the language a customer uses about you when you're not in the room. Test the brief by looking for phrases customers have actually said back to you.

**Positioning is time-stamped.** Markets shift. Positioning should be re-checked when strategy changes, when the customer base shifts, or annually — whichever comes first. A positioning brief without a review date is a fossil in six months.

## The brief

Fill in these five blocks. Total length: one page, tops. Anything longer is a strategy doc, not a positioning brief.

### 1. Who we're for

- The primary customer segment, in one sentence.
- What's specifically true about them (a firmographic + a behavior + a job they're trying to do).
- Not "SMBs" or "PMs" — sharp enough to exclude the majority of people who might casually fit.

**Test:** if the answer includes "and also," rewrite. Positioning has one primary.

### 2. What we do

- One line, in the customer's language, not yours.
- Avoid: "platform," "solution," "empower," "seamless," "next-generation."
- Aim for: what the customer would tell their peer at lunch about you.

**Test:** would a stranger reading this line know what button they'd click?

### 3. Why it's different

- 2-3 reasons, framed as tradeoffs, not features.
- Each reason must be something a competitor could name too — and choose against. If nobody could reasonably disagree, it's not differentiation.
- Prefer reasons customers actually cite over reasons your team believes are important.

**Test:** could you cross out our name and paste in a competitor's? If yes, it's not differentiation.

### 4. What we're NOT

- 2-3 things you deliberately give up. Segments not served. Use cases actively excluded. Features you won't build.
- The point isn't false modesty; it's clarity about the tradeoff.

**Test:** does this exclude at least 60% of the people who might casually consider you? If everyone could still be a customer, you don't have positioning.

### 5. The evidence

- Customer quotes, sales data, product usage patterns that support the four sections above.
- If any section rests on internal belief without customer evidence, mark it `[unverified]`.

**Test:** can you name a specific customer conversation from the last 90 days that supports each claim?

## Process

1. **Draft each block cold.** Fifteen minutes each, no committee. Write from what you know.
2. **Test with three real interactions.** Show it to a recent customer, a recent prospect who didn't buy, and a partner. Watch which lines they can repeat back and which they paraphrase into something else.
3. **Rewrite the sections they paraphrased.** Their paraphrase is the truth about how the market hears you.
4. **Kill anything unverified.** Every claim needs evidence or a label.
5. **Date it and set a review.** Six months from now, or when strategy shifts — whichever first.

## Common failure modes

**"For everyone."** Positioning without an "and NOT" section. Rewrite Section 4 or the whole brief is decoration.

**Feature lists as differentiation.** "We have integrations with X, Y, Z" is not why customers pick you — the reasons they cite are usually about how it feels, what it lets them stop doing, or who else is on board.

**Aspirational voice.** Where the brief describes a company that doesn't exist yet. Fine as a strategic vision, fatal as positioning. Positioning is about the company you are right now.

**One customer's quote as universal truth.** One person said it doesn't mean it's the positioning. Look for the phrase multiple customers use independently.

**No review date.** Positioning without a review date drifts. Set one before the brief goes anywhere.

## Output format

```markdown
# Positioning Brief — [product/company], [date]

**Review by:** [date, ~6 months out]

## Who we're for
[One sentence. Firmographic + behavior + job. Sharp enough to exclude most.]

## What we do
[One line. Customer's language. What they'd tell a peer at lunch.]

## Why it's different
1. [Reason, framed as tradeoff]
2. [Reason, framed as tradeoff]
3. [Reason, framed as tradeoff]

## What we're NOT
1. [Segment / use case / feature we deliberately give up]
2. [...]

## Evidence
- **Who we're for:** [customer/data reference]
- **What we do:** [customer/data reference]
- **Why it's different:** [customer/data reference per point]
- **What we're not:** [rationale + evidence]

[Mark anything without customer evidence `[unverified]` and flag as work to do.]
```

## When to hand off

- **You don't yet know who you're for** → `ideal-customer-profile` (positioning)
- **You need a full go-to-market plan around this** → `gtm-strategy` (positioning)
- **You're stress-testing against competition** → `porters-five-forces` or `swot-analysis` (positioning)
- **You're translating the brief into product decisions** → `product-vision` or `outcome-roadmap` (product-planning)
