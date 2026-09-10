# Changes from the original

**Adapted from:** [Anthropic knowledge-work-plugins / risk-assessment](https://github.com/anthropics/knowledge-work-plugins/tree/main/operations/skills/risk-assessment)
**Original author and license:** Anthropic, Apache-2.0

## Why I adapted it

The original description triggered on "what could go wrong," which collides with `pre-mortem`. In practice both would match a user asking about launch risks, and the pick was unpredictable.

## What I changed

| Date | Change | Why |
|------|--------|-----|
| 2026-09-10 | Rewrote the description to emphasize ongoing operational risk registers, compliance work, and standing risk reviews. Explicitly redirected pre-launch imagined-failure to `pre-mortem`. | Reduce trigger collision with `pre-mortem`. |

## What I kept

The whole skill body — the risk matrix, the assessment method, and mitigation planning were already right. Only the description trigger surface changed.
