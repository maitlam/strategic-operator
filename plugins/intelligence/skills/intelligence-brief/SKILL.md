---
name: intelligence-brief
description: Produce a recurring market intelligence brief — daily or weekly signals filtered for what actually matters to this team, with the "so what" attached. Use whenever the user needs a news or signals digest, is setting up a standing market-monitoring function, has a pile of headlines to filter, or asks what happened in their space this week. Trigger on "news brief," "what's happening in the market," "weekly signals," or any recurring monitoring need.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Intelligence Brief

Raw signals in. A short brief the team reads because it's worth reading, out.

## The framework behind this

A recurring brief has exactly one failure mode, and it's fatal: it becomes a link dump. Once it does, people stop opening it, and the standing intelligence function quietly dies while continuing to be produced.

The thing that prevents it is aggressive filtering plus one line of interpretation. **A signal without a "so what" is noise with a source attached.** If you can't say why an item matters to this specific team, it doesn't go in — and that judgment is the entire value of the brief. Anyone can aggregate headlines; an aggregator is not an intelligence function.

Two disciplines.

**Filter against a declared thesis.** A brief needs a stated set of things the team cares about — its segments, its bets, its named watchlist. Without that, relevance is decided ad hoc and drifts toward whatever is loudest that week. With it, the brief can be checked and improved.

**Five items, maximum.** The discipline of choosing is what makes it worth reading. A brief with fifteen items has outsourced the filtering back to the reader, which is the job it existed to do.

Silence is a legitimate output. A brief that says "nothing material this week, here's the one thing worth watching" preserves credibility. One that manufactures five items every week to justify itself is training the team to skim.

## Process

1. **Confirm the thesis** — the segments, bets, and watchlist this brief filters against. If not defined, establish it first; everything downstream depends on it.
2. **Gather signals**, then discard aggressively.
3. **Rank by relevance to the thesis**, not by how big the news is.
4. **Write one "so what" per item**, specific to this team.
5. **Flag anything that challenges a current assumption.** This is the highest-value category and the easiest to skip past.
6. **Say when there's nothing.**

## Output format

```markdown
# [Team] Intelligence — [date]

## Bottom line
[One or two sentences. If nothing material happened, say that.]

## Signals
**1. [Headline in your own words]** · [source, date]
*So what:* [One line. Specific to this team. Not a summary of the article.]

[Maximum five.]

## Challenges an assumption we hold
- [Signal] → [the assumption it puts pressure on]

## Watchlist movement
| Company / segment | What moved | Implication |
|---|---|---|

## Quiet this period
- [Named watchlist items with no activity. Sustained silence is a signal.]
```

## Hold the line on

- **Five items maximum.** The filtering is the product.
- **Every item carries a "so what" specific to this team.** No exceptions; an item that can't get one gets cut.
- **Never pad a slow week.** "Nothing material" is a credible output and protects the brief's signal value.
- **Summarize in your own words, briefly, and link out.** Never reproduce article text.
- **Flag assumption-challenging signals separately.** Confirming news is comfortable and less useful.
