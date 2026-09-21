---
marp: true
theme: operator-exec
paginate: true
header: "Onboarding churn · Exec readout"
footer: "2026-09-21 · Source: research brief, onboarding churn"
---

<!-- _class: title -->
# Onboarding churn

A decision on where to spend Q4 engineering to stop first-month churn.

2026-09-21 · Product team · For: leadership

---

<!-- _class: answer -->
# Most churn happens in the first 30 days, and it's caused by setup — not by the product.

- 62% of churned accounts never completed data connection
- Accounts that connect data in week one retain at 91%
- Fixing setup is a six-week project; fixing "the product" isn't a project

---

# Churn is front-loaded: the first 30 days account for most of it.

- Day 0–30: **58%** of all churn
- Day 31–90: 27%
- Day 91+: 15%

---

<!-- _class: evidence -->
# Accounts that connect data in week one almost never churn.

| Cohort | Connected data by day 7 | 90-day retention |
|---|---|---|
| Q1 signups | Yes | 91% |
| Q1 signups | No | 34% |
| Q2 signups | Yes | 89% |
| Q2 signups | No | 31% |

<p class="source">Source: product analytics, Q1–Q2 2026 cohorts. Boundary: paid accounts, self-serve signup only.</p>

---

# Setup fails because it assumes a data engineer the customer doesn't have.

- 71% of stalled accounts have no technical owner assigned
- Median time to first connection when it succeeds: 4 days; when it fails, it's never attempted
- Support tickets in the first week are 3× more likely to be about connection than anything else

---

# We're asking for a six-week guided-setup project, not a redesign.

- Guided connection flow with a non-technical path
- A setup owner assigned on the customer side during sales handoff
- Scope is setup only; the in-product experience isn't the problem

---

<!-- _class: ask -->
# We're asking for six weeks of one squad in Q4, starting the first sprint.

**Decider:** VP Product · **By:** 2026-09-30
**Scope:** one squad, six weeks, no new headcount
**If not decided:** Q4 planning locks without it, and first-month churn continues at the current rate through Q1

---

# What happens next

| Step | Owner | When |
|---|---|---|
| Decision | VP Product | 2026-09-30 |
| Scope and staffing confirmed | Eng lead | 2026-10-07 |
| First guided-setup cohort live | Squad | 2026-11-18 |
| Retention read on that cohort | Product | 2027-01-15 |

---

<!-- _class: section -->
# Appendix

---

<!-- _class: appendix -->
# Method

- Cohorts: all self-serve paid signups Q1–Q2 2026 (n = 1,840)
- Churn defined as cancellation or non-renewal within 90 days
- "Connected data" = at least one source integration completed
- Support ticket classification: manual review of a 200-ticket sample
