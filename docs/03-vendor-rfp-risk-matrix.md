# Project 3 — Vendor RFP and SOW Risk Matrix

## Executive summary

This matrix gives procurement and security reviewers a repeatable first-pass score across five risk dimensions, then turns weak evidence areas into contract discussion topics.

## Scoring model

Each dimension is scored from 0 to 5, from absent or poor evidence to strong verified evidence. The weighted result is normalized to 100.

| Dimension | Weight |
| --- | ---: |
| Data transit protection | 25% |
| IAM boundaries | 25% |
| External certifications | 20% |
| Log isolation and access | 15% |
| Data residency and deletion | 15% |

**Pass ≥ 80; Conditional ≥ 60 and < 80; Fail < 60.** Conditional results call for documented risk-owner approval and time-bound remediation. A fail pauses onboarding pending material remediation and evidence.

## Demonstration scenario

| Dimension | Score |
| --- | ---: |
| Data transit protection | 4/5 |
| IAM boundaries | 5/5 |
| External certifications | 3/5 |
| Log isolation and access | 2/5 |
| Data residency and deletion | 3/5 |
| **Weighted result** | **72/100 — Conditional** |

The weakest area prompts SOW discussion on log ownership, tenant separation, access restrictions, retention, export, and incident access procedures.

## Why it matters

A consistent matrix helps reviewers compare vendors, focus evidence requests, and make a conditional decision actionable. The score is a triage aid, not a substitute for reviewing evidence, contract, service scope, or subprocessors.

## Interview explanation

**Executive:** “I designed a weighted vendor review that makes criteria explicit and connects weak evidence to practical SOW protections. A human risk owner decides whether residual risk is acceptable.”

**Plain language:** “It grades vendors on a shared scorecard and identifies what proof or contract terms to resolve before onboarding.”
