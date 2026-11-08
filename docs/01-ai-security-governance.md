# Project 1 — AI Security Governance Simulator

## Executive summary

A company wants to introduce a generative AI assistant, but deployment, data sensitivity, and connected tools change the risk picture. This simulator turns those decisions into a starting checklist for governance and security review.

## Inputs and logic

Inputs include deployment model, highest data sensitivity, personal data processing, and whether the model can call tools or take external actions. Outputs prompt review of provider retention and training terms, identity boundaries, sensitive-data minimization, privacy, incident ownership, prompt injection, unsafe outputs, and tool safeguards.

The simulator references the NIST AI RMF Govern, Map, Measure, and Manage functions and broad ISO/IEC 42001 topics. These are discussion topics to validate, not a control-by-control mapping.

## Demonstration scenario

**Scenario:** a public-cloud assistant processes confidential information and can call tools.

**Review prompts:** verify provider handling and retention; minimize sensitive inputs; test prompt-injection paths; constrain tool permissions; require human approval for consequential actions; log tool calls; assign an owner and incident process.

## Why it matters

It translates an architecture choice into concrete questions for security, privacy, legal, and business owners, focusing discussion on data flows, evidence, ownership, testing, and risk acceptance.

## Limitations

- Not a security scanner or model evaluation harness.
- Does not inspect provider contracts, cloud configurations, prompts, or model behavior.
- Framework references are high-level and need qualified review for the applicable scope.

## Interview explanation

**Executive:** “I built a small governance simulator that makes AI adoption discussions concrete. It connects deployment and data-sensitivity choices to safeguards teams should validate.”

**Plain language:** “It asks where the AI runs, what information it sees, and whether it can take actions, then offers protections to verify before use.”
