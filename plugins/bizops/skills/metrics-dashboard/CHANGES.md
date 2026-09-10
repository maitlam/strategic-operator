# Changes from the original

**Adapted from:** [borghei Claude-Skills / metrics-dashboard](https://github.com/borghei/Claude-Skills/tree/main/project-management/discovery/metrics-dashboard)
**Original author and license:** borghei, MIT + Commons Clause

## Why I adapted it

The original description named "North Star, input metrics, and guardrails" — the same content as `north-star-metric`'s description. Both would match a user asking about their headline metric, and the pick was unpredictable.

## What I changed

| Date | Change | Why |
|------|--------|-----|
| 2026-09-10 | Rewrote the description to emphasize this is the WHOLE DASHBOARD SYSTEM — layers, owners, review cadence — with explicit trigger phrases like "design our dashboard." Redirected the single-metric spec to `north-star-metric`. | Reduce trigger collision with `north-star-metric`. |

## What I kept

The whole dashboard-design method — hexagonal metrics, layered architecture, owner assignment, cadence rules, and the `dashboard_designer.py` renderer. Only the description trigger surface changed.
