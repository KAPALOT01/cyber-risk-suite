# AI Risk and Control Monitor

## Project summary

This project documents a governance and testing workflow for generative AI systems. It combines control tracking with prompt-based checks for sensitive-data leakage and unsafe outputs.

## Demonstration workflow

- Map 28 control considerations to the NIST AI Risk Management Framework.
- Test a set of 500 generative AI prompts for sensitive-data leakage and unsafe responses.
- Use Python to organize risk findings and scores.
- Use Power BI to report test coverage, findings, and governance follow-up.
- Include Azure OpenAI in the documented technology stack.

## Review considerations

- Define the intended use, data sensitivity, test population, and acceptance criteria before testing.
- Review prompt and response samples with authorized data owners.
- Treat scores as test evidence for human review; they do not prove that a model is safe or compliant.
- Re-run tests when the model, prompts, data, configuration, or connected tools change.

## Scope

This GitHub page summarizes the project described in the resume. The prompt corpus, control register, evaluation scripts, Azure configuration, and Power BI file were not available in the supplied project files, so they are not included here. The summary does not claim a production security assessment or certification.
