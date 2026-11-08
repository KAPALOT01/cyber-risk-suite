# Cyber Risk Suite

**Practical, explainable decision support for AI governance, GRC financial risk, and third-party security reviews.**

This portfolio brings three complementary consulting workflows into one small Python application. Each engine turns a business question into documented assumptions, structured findings, and a decision-oriented report.

> **Portfolio demonstration only.** The results are illustrative, depend on user-entered assumptions, and do not establish compliance, provide legal advice, or replace an independent assessment.

## The three projects

| Project | Business question | What the tool produces |
| --- | --- | --- |
| [AI Security Governance Simulator](docs/01-ai-security-governance.md) | What safeguards should we validate before adopting this AI deployment for this data? | Risk-aware safeguard checklist, prompt-injection and data-leak warnings, and framework topics to review |
| [Quantitative GRC Risk Engine](docs/02-quantitative-grc-risk.md) | How large is the modeled annual loss, and how might a proposed control change the business case? | SLE, ALE, estimated loss reduction, annual net benefit, ROI, payback, and SOC 2 control status/gaps |
| [Vendor RFP Risk Matrix](docs/03-vendor-rfp-risk-matrix.md) | What evidence and contract protections should procurement resolve before onboarding a vendor? | Weighted 0–100 score, pass/conditional/fail outcome, evidence gaps, and SOW topics |

## Run locally

Requires Python 3.9 or later. No third-party packages are used.

```bash
python3 cyber_risk_suite.py
```

Choose a project from the menu, enter the assumptions, and review the results. The application keeps all processing local and does not make network requests.

## Example results

### Financial risk scenario

For a sample asset valued at `$100,000`, an exposure factor of `0.50`, and an annualized occurrence rate of `0.20`:

- SLE: `$50,000`
- ALE: `$10,000` per year
- At an assumed `60%` risk reduction, modeled annual loss reduction: `$6,000`
- At an annual control cost of `$5,000`, estimated net benefit: `$1,000` and ROI: `20%`

These are scenario calculations, not forecasts. The output is only as useful as the owner's asset valuation, event frequency, and control-effectiveness assumptions.

### Vendor scoring scenario

A demonstration vendor with dimension scores `4, 5, 3, 2, 3` receives `72/100` and a **conditional** outcome. The low score for log isolation prompts contract language about tenant separation, log access, retention, and export.

## Design choices

- **Transparent math:** formulas, weights, rating scales, and decision thresholds are visible in the code and documentation.
- **Human review:** the app records assumptions and evidence gaps rather than presenting its output as an automatic approval.
- **Bounded framework language:** framework names guide the review. The simulator does not claim clause-level ISO/IEC 42001 mapping or certify NIST AI RMF / SOC 2 compliance.
- **Useful adverse outcomes:** a control investment can have negative estimated ROI, and a vendor can fail the score threshold; neither result is hidden.
- **No fabricated impact metrics:** the portfolio does not claim a percentage reduction in review effort. Add measured outcomes only after running and documenting a real evaluation.

## Repository map

```text
cyber_risk_suite.py       Interactive three-engine application
README.md                 Portfolio overview and quick start
docs/                     Individual case studies and interview notes
```

## Roadmap

- Add exportable executive reports with assumptions and evidence references.
- Add configurable scoring weights and thresholds with versioned decision records.
- Add a small reviewed control crosswalk before making clause-level framework claims.

## References

- [NIST AI Risk Management Framework Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [ISO/IEC 42001:2023](https://www.iso.org/standard/42001.html)
- [AICPA 2017 Trust Services Criteria (2022 revised points of focus)](https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022)

## About this portfolio

This project is intended to demonstrate a consulting-oriented approach to cyber risk: state the business question, show the assumptions, connect the findings to useful control topics, and give stakeholders a clear next step. It complements a separate security-operations detection lab in the account's portfolio.
