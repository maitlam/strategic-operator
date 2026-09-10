---
name: competitive-intel
description: Build a read on a competitor — what they're actually doing versus what they say, where they're strong, where they're exposed, and what their recent moves imply about their strategy. Use whenever the user is assessing a rival, preparing for a competitive situation, sees a competitor announcement they need to interpret, or asks what a competitor is up to. Trigger on a named competitor plus any strategic, positioning, or threat context.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Competitive Intelligence

A competitor in. A read on their strategy and exposure, out.

## The framework behind this

Competitive analysis fails in two directions, and both are common.

It over-reads announcements — treating a press release as a strategy, when a launch is frequently a defensive reaction, a recruiting signal, or an investor story. Or it under-reads them, cataloguing features and producing a comparison grid that tells you nothing about what the competitor will do next.

The corrective: **weight behavior over messaging.** What a company hires for, where it opens offices, what it acquires, and what it quietly stops doing are far more reliable indicators than what it announces. Job postings in particular are among the most honest public artifacts a company produces — nobody writes a requisition for a strategy they've abandoned.

Two more.

**Find the exposure, not just the strength.** A strengths-and-weaknesses list is a static object. What's actionable is structural exposure: a business model that can't absorb a price move, a customer concentration, an architecture that makes a category of feature expensive for them and cheap for you.

**Separate the read from the evidence, always.** Competitive work circulates widely and gets quoted at levels where the caveats fall off. If the inference isn't clearly labeled, it will eventually be repeated as fact in a room where nobody can check it.

## Process

1. **Gather observable behavior first** — hiring, acquisitions, pricing changes, departures, deprecations, published roadmap.
2. **Note the messaging separately**, and flag where it diverges from behavior. The divergence is usually the most interesting finding.
3. **Assess strength honestly**, including where they're genuinely better. A competitive read that flatters is worse than none.
4. **Identify structural exposure** — what they can't easily change.
5. **State the strategic read** as inference, labeled.
6. **Name what to watch** — specific, observable signals that would confirm or kill the read.

## Output format

```markdown
# Competitive Read: [Company] — [date]
*Sources: [public] · Confidence: [high / mixed / thin]*

## The read — *inference*
[Three or four sentences on what they appear to be doing and why.]

## Observed behavior
| Signal | Date | What it suggests |
|---|---|---|
[Hiring, acquisitions, pricing, departures, deprecations.]

## Messaging vs. behavior
[Where what they say and what they do diverge.]

## Where they're genuinely strong
- [Be honest. This section is what makes the rest credible.]

## Structural exposure
- [What they can't easily change. Model, concentration, architecture,
  installed base.]

## What to watch
| Signal | Would confirm | Would kill the read |
|---|---|---|

## Not established
- [What you'd want and couldn't find.]
```

## Hold the line on

- **Never state inference as observation.** This material circulates and loses its caveats.
- **Never fabricate metrics** — revenue, headcount, customer counts. "Not public" is correct.
- **Include their real strengths.** A read that only finds weakness will be discounted entirely, and rightly.
- **Do not build a feature grid.** If the user wants one, say it's a different artifact and offer it separately; it answers a different question.
