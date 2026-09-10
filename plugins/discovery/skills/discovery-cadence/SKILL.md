---
name: discovery-cadence
description: Design or diagnose the operating rhythm of continuous customer discovery — the weekly beat that produces learning, not the one-off "round of interviews" that produces a report. Use when the user is setting up discovery for the first time, when their existing discovery has stalled, when they're trying to decide how much time to spend talking to customers, or when they ask "how often should we be doing this." Trigger on "discovery cadence," "continuous discovery," "how often should we talk to customers," or diagnosing why a discovery function has quietly stopped producing signal.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Discovery Cadence

Not another discovery activity — the rhythm underneath. Small samples run weekly beat large studies run rarely, and most discovery functions die from cadence collapse long before they run out of things to learn.

## The framework behind this

The dominant failure mode in customer discovery isn't bad interviews or weak synthesis. It's that discovery gets treated as a project — "we're doing a round of interviews before Q3 planning" — instead of a rhythm. A round ends. A rhythm doesn't.

The distinction the whole method rests on: **discovery is a beat, not a batch.** Torres's continuous-discovery framing is right on this — the goal isn't to run five great interviews once; it's to run two okay interviews every week for a year and let the compounding do the work. What you learn in week 34 is not what you would have learned in week 4 no matter how many interviews you crammed in.

Three things follow.

**Small samples, high frequency.** Two interviews this week beats twenty next quarter. The value of an interview is in the next hypothesis it triggers, and that only happens if you're back in the chair the following week. Twenty interviews in a burst are twenty answers to the same question you had at the start.

**Cadence collapses quietly.** No one announces "we've stopped doing discovery." The calendar just fills. Interviews get pushed one week, then two, then quietly deleted. By the time anyone notices, it's been a quarter. The absence of noise is the failure signal.

**The beat has to survive priority shifts.** If discovery is the first thing dropped when the team is busy, it will always be dropped, because the team is always busy. Discovery has to be scheduled as if it were a customer commitment — because it is.

## Process

Use this to design a new cadence, or diagnose one that's stalled.

1. **Pick the beat.** Weekly is the default and usually the right answer. Bi-weekly is acceptable only if the team is <3 people. Monthly is not discovery — it's research projects.
2. **Assign the seats.** Who's in each interview? Torres says trio (PM + designer + engineer). Solo works too if the team is small; the constraint is that whoever's in the room is also in the roadmap conversation.
3. **Book two weeks of interviews at once.** Cadence dies at the scheduling step. Standing recruiting on autopilot — a rolling pool, a booking link, a weekly slot — is the single largest determinant of whether the rhythm survives.
4. **Set the weekly artifact.** Not a report; a running log. Three bullets per interview at most: what surprised you, what confirmed a hypothesis, what new question opened up. If the log takes more than 30 minutes to write, you're doing it wrong.
5. **Set the weekly conversation.** 30 minutes, same day of the week, with the roadmap owner in the room. If nobody in the roadmap conversation was in an interview this month, the cadence has already broken.
6. **Set the review trigger.** After 6-8 weeks of running, look back: are you learning things that change what you're building? If no, either the questions are wrong or the customers are wrong. Adjust one; don't quit.

## Diagnose a stalled cadence

Score honestly:

- [ ] At least one interview happened this week
- [ ] At least one interview is booked for next week
- [ ] The last synthesis touched the roadmap in some concrete way
- [ ] The team members in the roadmap conversation have been in an interview this month
- [ ] The recruiting pool has fresh contacts (not just the same friendly customers)

Fewer than 3 checked → cadence has collapsed. Restart with step 1, not by trying harder inside the current broken rhythm.

## Common failure modes

**"Big study, then implementation."** The batch mindset. Produces a slide deck and stops. Rewrite as a weekly beat.

**"We talked to X customers this quarter."** The vanity-metric trap. Count of interviews without a follow-up hypothesis is theater. Track "hypotheses tested" instead.

**"Discovery is the research team's job."** Firewalls between discovery and building. The roadmap owner has to be in the beat.

**Only-your-favorite-customers.** The recruiting pool calcifies around three people who always say yes. Ask "did anything a stranger say surprise us this month?"

## Output format

```markdown
# Discovery Cadence — [team, month/quarter]

## Current state
- Beat: [weekly / bi-weekly / broken]
- Standing slot: [day, time, participants]
- Interviews in the last 4 weeks: [count]
- Interviews booked in the next 2 weeks: [count]

## Health check
[Five checkboxes above, with a one-line note on each]

## What's producing signal
- [What the team has actually learned in the last month that changed a decision]

## Where the cadence is fragile
- [Where the beat is likely to skip a week — the scheduling gap, the recruiting drought, the missing participant]

## Adjustments for next month
- [1-3 specific changes]

## Next review date
[6-8 weeks out]
```

## When to hand off

- **New insights arrived, need to be organized** → `interview-synthesis`
- **The interviews themselves need better questions** → `customer-interview-script`
- **You're not sure what you're trying to learn** → step back; this is a strategy question, not a cadence one
- **A specific job-to-be-done needs deep exploration** → `jtbd-workshop`
