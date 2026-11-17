# Identity Governance Automation

## Project summary

This project documents an access-review workflow built with Python, Microsoft Entra ID, SQL, and Power BI. It focuses on identifying identity risks and giving reviewers a traceable way to assign and follow remediation.

## Demonstration workflow

- Review a synthetic population of 1,200 identities.
- Use SQL checks to flag dormant accounts, excessive privileges, and segregation-of-duties conflicts.
- Use Python to organize findings for review and remediation tracking.
- Present the findings in a Power BI dashboard.

The accompanying resume reports a reduction from a three-hour manual review to 17 minutes for this demonstration. Treat those timings as scenario-specific results, not as a guaranteed outcome for another environment.

## Review considerations

- Verify source data, account ownership, and exception handling before acting on a finding.
- Confirm privilege conflicts with application owners and business context.
- Require a human reviewer to approve changes before disabling accounts or removing access.
- Keep an audit trail for evidence, decisions, exceptions, and remediation status.

## Scope

This GitHub page summarizes the project described in the resume. The source pipeline, sample identity dataset, SQL checks, and Power BI file were not available in the supplied project files, so they are not included here. The summary does not claim a live Entra tenant assessment or compliance certification.
