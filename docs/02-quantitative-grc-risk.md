# Project 2 — Quantitative GRC Risk Engine

## Executive summary

This engine models a financial risk scenario using Single Loss Expectancy (SLE) and Annualized Loss Expectancy (ALE), then compares estimated control benefit with annual cost.

## Formulas

```text
SLE = asset value × exposure factor
ALE = SLE × annualized rate of occurrence
Estimated annual loss reduction = ALE × estimated risk reduction
Estimated net annual benefit = loss reduction − annual control cost
Estimated ROI = net annual benefit ÷ annual control cost × 100
Estimated payback = annual control cost ÷ annual loss reduction
```

A rate of occurrence is entered as events per year. The tool labels zero-cost or zero-benefit cases without dividing by zero.

## Demonstration scenario

| Assumption or result | Value |
| --- | ---: |
| Asset value | $100,000 |
| Exposure factor | 0.50 |
| Annualized occurrence rate | 0.20 |
| SLE / ALE | $50,000 / $10,000 per year |
| Assumed risk reduction | 60% |
| Modeled loss reduction | $6,000 per year |
| Annual control cost | $5,000 |
| Modeled net benefit / ROI | $1,000 / 20% |
| Modeled payback | 0.83 years |

All figures are illustrative. The model does not discount future cash flows, account for multiple loss types, or quantify uncertainty.

## Control review prompts

- **SOC 2 CC6.1:** record implementation status and evidence gaps for logical access safeguards.
- **SOC 2 CC7.5:** record status and evidence gaps for recovery from identified security incidents, including recovery testing.

These prompts are not an audit opinion or complete SOC 2 assessment.

## Why it matters

The model shows a visible chain from business assumptions to a proposed control's estimated economics and encourages owners to challenge assumptions before using them in a budget case.

## Interview explanation

**Executive:** “I built a quantitative risk register that shows its inputs and formulas, then compares estimated annual loss reduction with control cost.”

**Plain language:** “It estimates what an event could cost and compares that scenario with a proposed protection's yearly cost.”
