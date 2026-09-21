---
name: pattern-analysis
description: Read across a whole corpus of conversations — meeting notes, interviews, customer calls, briefs — and report what recurs, what conflicts, what is newly emerging, and how the evidence stacks up for and against the team's stated hypotheses, with every claim cited and every theme carrying its independent-source count. Use whenever someone asks what the team is hearing overall, wants to check whether a belief is actually supported, needs a periodic cross-conversation read, or when individual notes have been synthesized but the corpus hasn't. Trigger on "what patterns," "what are we hearing across," "does the evidence support," "themes across conversations," or any request to connect dots across many sources rather than summarize one.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Pattern Analysis

A corpus of conversations and a set of working hypotheses in. What genuinely recurs, what conflicts, and how the evidence stands — counted and cited — out.

## The framework behind this

Individual conversations get written up. The corpus almost never does, and that's where the patterns live: a theme is invisible inside any one note and obvious across twenty. The failure mode of reading across a corpus is the opposite one — a vivid remark from a single conversation gets remembered as "what people are saying," and the team's picture of its market comes to rest on one anecdote.

**The central discipline is counting independent sources.** One person saying something three times is one source. Three people from the same organization may be one source. A theme is a claim about frequency, and frequency has to be counted, not felt.

That gives a vocabulary that must be used precisely:

- **Convergent theme** — three or more independent sources, unprompted, saying materially the same thing.
- **Emerging signal** — two independent sources, typically recent. Worth watching; not yet a theme.
- **Single-source signal** — one source. Reported as exactly that, with its source, and never promoted to a theme by strength of phrasing.
- **Contradiction** — independent sources disagreeing on a point that matters. Named and left standing. The analysis surfaces contradictions; it does not resolve them by picking the more articulate side.

**Hypotheses get a ledger, not a verdict.** For each working hypothesis, list the evidence for and against, each item cited, and rate confidence by the count rule: high needs multiple independent supporting sources and no unaddressed contradiction; medium has support but thin or contested; low is one source or less. The rating comes from the tally, not from how much the team wants it to be true.

**Name the corpus bias.** What the team has heard depends on who it talked to. Every analysis says which segments, roles, and perspectives are over- and under-represented in the corpus, because a theme that's convergent among the people the team happened to reach may be absent among the people it hasn't.

## Gather first

- The corpus, or the subset in scope. Note what's excluded and why.
- The team's stated hypotheses. If none are written down, ask for them or extract the implicit ones from strategy documents and label them as such.
- Prior pattern analyses, so this one can say what changed.
- An optional focus — a theme, segment, or hypothesis to narrow to.

## Process

1. **Read the whole corpus.** Not summaries of it. For each source, extract claims with the source identity (person, organization, role, date).
2. **Cluster claims** that say materially the same thing. Be strict: "wants faster onboarding" and "onboarding is confusing" are related, not identical.
3. **Count independent sources per cluster.** Merge sources that aren't independent. Classify each cluster as convergent, emerging, or single-source.
4. **Find contradictions.** Where independent sources disagree on the same point, record both sides with their sources.
5. **Tally the hypotheses.** For each: supporting citations, contradicting citations, confidence by the count rule, and what evidence would move it.
6. **Map coverage.** Who has been heard from, by segment and role, and who hasn't.
7. **Compare with the prior analysis.** What was emerging and is now convergent? What faded? What's new?
8. **Cite everything.** Every claim in the output points at its sources.

## Output format

```markdown
# Pattern Analysis — [date]
*Corpus: [N sources, date range, what's excluded]. Focus: [none / theme]. Prior analysis: [date or none]*

## Read in one paragraph
[What the corpus says, at the confidence the counts support.]

## Convergent themes (3+ independent sources)
### [Theme]
- **Sources (N):** [source; source; source]
- **What they say:** [in the sources' terms, briefly]
- **What it doesn't establish:** [the overreach to avoid]

## Emerging signals (2 independent sources)
| Signal | Sources | First seen | Watch for |
|---|---|---|---|

## Single-source signals
| Signal | Source | Why it's noted |
|---|---|---|

## Contradictions
### [Point of disagreement]
- **Position A:** [claim] — [sources]
- **Position B:** [claim] — [sources]
- **What would resolve it:** [evidence or conversation]

## Hypothesis ledger
### H[n]: [hypothesis]
- **Confidence:** High / Medium / Low
- **For (N):** [citation; citation]
- **Against (N):** [citation]
- **Would move it:** [what evidence]

## Who we've heard from
| Segment / role | Sources | Note |
|---|---|---|
[Include rows with zero. Absence is the point.]

## Since last analysis
- [Emerging → convergent / faded / new]
```

## Hold the line on

- **Never promote a single-source signal to a theme.** However memorable the quote.
- **Source count next to every theme.** A theme without a count is an opinion.
- **Independence is judged, not assumed.** Same person, same organization, same meeting — usually one source.
- **Contradictions stay open.** Surface them; don't adjudicate.
- **Cite every claim.** An uncited pattern can't be checked and shouldn't be repeated.
- **Always report coverage gaps.** The corpus is a sample; say what it's a sample of.
