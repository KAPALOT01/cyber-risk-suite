# Project 1 — AI Security Governance Simulator

## Executive summary

A company wants to introduce a generative AI assistant, but the deployment model, data sensitivity, and connected tools change the risk picture. This simulator turns those decisions into a starting checklist for governance and security review.

## Inputs

- Deployment: public cloud endpoint, isolated cloud VPC, or local model deployment
- Highest data sensitivity: public, internal, confidential, or restricted
- Whether personal data is processed
- Whether the model can call tools or take external actions

## Logic and outputs

The simulator combines the selected inputs with review prompts covering provider retention and training terms, identity boundaries, sensitive-data minimization, privacy review, incident ownership, prompt injection, unsafe outputs, and tool-use safeguards. It names the NIST AI RMF's Govern, Map, Measure, and Manage functions and points to broad ISO/IEC 42001 topics.

These are framework topics and safeguards to validate, not an asserted control-by-control mapping. The app does not decide whether a specific organization may use a particular dataset.

## Demonstration scenario

**Scenario:** a public-cloud assistant processes confidential information and can call tools.

**Decision support:** verify provider handling and retention terms; minimize sensitive inputs; test prompt injection paths; constrain tool permissions; require human approval for consequential external actions; log tool calls; assign an owner and incident process.

## Why it matters to a consulting conversation

The output helps translate an architecture choice into concrete questions for security, privacy, legal, and business owners. The discussion can then focus on data-flow evidence, ownership, testing, and risk acceptance.

## Limitations

- This is not a security scanner or a model evaluation harness.
- It does not inspect provider contracts, cloud configurations, prompts, or model behavior.
- Framework references are high-level; scope and applicable requirements need qualified review.

## Interview explanation

**Executive version:** “I built a small governance simulator that makes AI adoption discussions more concrete. It connects deployment and data-sensitivity choices to safeguards teams should validate, and it makes tool-use and data-leak concerns visible early.”

**Plain-language version:** “It asks where the AI runs, what kind of information it sees, and whether it can take actions. Then it gives the team a checklist of protections to verify before use.”
