---
name: develop-a-program-toolkit
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Develop a program toolkit."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/develop-a-program-toolkit
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Develop a program toolkit — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Generate complete program design frameworks for new initiatives with logic models, evaluation plans, and resource guides that transform concepts into implementation-ready programs.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm designing a tech workforce preparation program for young adults ages 18-26 from underserved Detroit communities. We'll serve 120 participants annually, helping them prepare for entry-level IT careers.

Program Structure:

- 6-hour virtual course covering IT career pathways, resume building, interview skills, and professional networking
- 4 one-on-one career coaching sessions to support job search and applications

Target Outcomes: 80% course completion, 60% job placement within 90 days, $40K average starting salary.

Create a comprehensive program design toolkit in Excel with: program description with mission and goals, logic model (inputs → activities → outputs → outcomes), SWOT analysis with recommendations, evaluation framework with indicators and data collection methods, resource planning (staffing, budget), and executive dashboard.

Make this consulting-grade with premium formatting, sophisticated design, and advanced Excel features. Use a professional color scheme—avoid default Excel colors.
```

## Inputs

- Extended Thinking feature (recommended to enable in conversation settings)
- Excel software (for the output file)
- Theory of Change documentation, current program materials, organizational strategy documents (optional)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- No connectors detected on the source page; base Claude capabilities only
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Develop a program toolkit](https://claude.com/resources/use-cases/develop-a-program-toolkit) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
