---
name: partner-scan
description: Profile a specific company as a potential partner — what they do, who they serve, how they make money, what they'd want from a partnership, and what would have to be true for it to work. Use whenever the user is evaluating a company for partnership, preparing for a partner conversation, doing build/buy/partner analysis, or asks to look into a specific company. Trigger on a named company plus any partnership, vendor, or collaboration context.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Partner Scan

A named company in. A profile that ends in what would have to be true, out.

## The framework behind this

A partner scan is not a company research report. It's a structured read aimed at one question: **is there a version of this partnership that both sides would actually want?**

That reframe changes what goes in it. A research report describes a company. A partner scan describes a company *and* models their side of the deal — because the most common failure in partnership work is a thoroughly researched target who has no reason to say yes. Understanding what they need is the difference between a first conversation that goes somewhere and one that doesn't.

Two disciplines.

**Separate observation from inference, visibly.** Everything about what they do is reporting. Everything about what they'd want is inference, and mislabeling the second as the first is how a scan becomes a bad basis for a conversation someone else has to have.

**End in falsifiable conditions, not a recommendation.** "What would have to be true" converts the scan into a set of questions for the first call. A recommendation short-circuits that and rests on information desk research can't supply.

Also worth stating plainly: most scans should end in no. A scan function that produces partners from every target isn't screening.

## Process

1. **Establish what's actually known.** Search if tools allow; otherwise work from what's supplied and mark thin sections.
2. **Profile the five dimensions** below. Don't skip one for lack of information — write "unclear from public sources" and move it to open questions.
3. **Model their side:** what they need, who they already work with, what a partnership would cost them.
4. **State the fit hypothesis** as inference, labeled.
5. **Write the conditions** — what would have to be true, each answerable in a conversation.

## The five dimensions

**What they do** — the actual product or service in two sentences. Not the mission statement.
**Who they serve** — the specific buyer and the specific user, often different people.
**How they make money** — model, pricing shape if public, who signs. Opaque pricing is itself a signal.
**How they're positioned** — what they claim to be better at, against whom, and whether it holds up.
**Where they sit** — dependencies, existing partners, and what would put them in trouble.

## Output format

```markdown
# Partner Scan: [Company]
*[date] · Sources: [public sources] · Confidence: [high / mixed / thin]*

## In one line
[The sentence you'd say in a hallway.]

## What they do
## Who they serve
## How they make money
## How they're positioned
## Where they sit in the ecosystem

## Signals
- [Observed: funding, hiring, launches, departures, published roadmap.]

## Their side of the deal — *inference*
- **What they need:** [what a partnership would solve for them]
- **Who they already work with:** [and what that implies]
- **What this would cost them:** [attention, exclusivity, roadmap]

## Fit hypothesis — *inference*
[2–4 sentences. Labeled as judgment.]

## What would have to be true
1. [Answerable in a conversation. Ordered by how much it changes the read.]

## Recommended next step
[Specific: a conversation with a role, a demo, a document to request —
or no further pursuit, with the reason.]
```

## Hold the line on

- **Never invent specifics.** A fabricated funding round or customer count destroys the credibility of the scan and the person circulating it.
- **Marketing language doesn't survive.** If a company says it's "AI-native," write what that means operationally or write that it's unclear.
- **Label the inference sections.** Everything above them is reporting; blurring the two makes the scan unusable to a second reader.
- **Conditions must be answerable.** "Are they a good fit?" is not one. "Do they sell to the clinical team or to procurement?" is.
