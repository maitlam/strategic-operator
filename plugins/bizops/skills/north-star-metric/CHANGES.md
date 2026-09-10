# Changes from the original

**Adapted from:** [borghei Claude-Skills / north-star-metric](https://github.com/borghei/Claude-Skills/tree/main/project-management/execution/north-star-metric)
**Original author and license:** borghei, MIT + Commons Clause

## Why I adapted it

The original description covered "the NSM and its input metric tree, with leading indicators, anti-metrics, and counter-metrics" — accurate, but overlapping with `metrics-dashboard`, which also names "North Star, input metrics, and guardrails" in its description. Both would trigger on metrics work.

## What I changed

| Date | Change | Why |
|------|--------|-----|
| 2026-09-10 | Rewrote the description to emphasize this is the METRIC-SPEC artifact — the single number and its tree — with explicit trigger phrases like "what's our north star." Redirected wider dashboard architecture work to `metrics-dashboard`. | Reduce trigger collision with `metrics-dashboard`. |

## What I kept

The full method (five tests, Amplitude archetypes, input math, leading indicators, anti/counter-metrics) and the `metric_tree_builder.py` renderer. Only the description trigger surface changed.
