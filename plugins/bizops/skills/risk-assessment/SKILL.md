---
name: risk-assessment
description: Identify, assess, and mitigate ongoing operational risks — the standing risk register that lives across a program or team. Trigger with "risk register", "operational risks", "compliance risks", "vendor risk review", "process risks", or ongoing risk work. For pre-launch imagined-failure exercises, use `pre-mortem` instead.
license: Apache-2.0
metadata:
  provenance: adapted
  author: maitlam
  adapted-from: https://github.com/anthropics/knowledge-work-plugins/tree/main/operations/skills/risk-assessment
  changes: Sharpened description to trigger on ongoing operational risk registers, disambiguating from pre-mortem's pre-launch imagined-failure scope.
---

# Risk Assessment

Systematically identify, assess, and plan mitigations for operational risks.

## Risk Assessment Matrix

| | Low Impact | Medium Impact | High Impact |
|---|-----------|---------------|-------------|
| **High Likelihood** | Medium | High | Critical |
| **Medium Likelihood** | Low | Medium | High |
| **Low Likelihood** | Low | Low | Medium |

## Risk Categories

- **Operational**: Process failures, staffing gaps, system outages
- **Financial**: Budget overruns, vendor cost increases, revenue impact
- **Compliance**: Regulatory violations, audit findings, policy breaches
- **Strategic**: Market changes, competitive threats, technology shifts
- **Reputational**: Customer impact, public perception, partner relationships
- **Security**: Data breaches, access control failures, third-party vulnerabilities

## Risk Register Format

For each risk, document:
- **Description**: What could happen
- **Likelihood**: High / Medium / Low
- **Impact**: High / Medium / Low
- **Risk Level**: Critical / High / Medium / Low
- **Mitigation**: What we're doing to reduce likelihood or impact
- **Owner**: Who is responsible for managing this risk
- **Status**: Open / Mitigated / Accepted / Closed

## Output

Produce a prioritized risk register with specific, actionable mitigations. Focus on risks that are controllable and material.
