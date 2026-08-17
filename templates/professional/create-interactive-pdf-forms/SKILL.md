---
name: create-interactive-pdf-forms
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create interactive PDF forms."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-interactive-pdf-forms
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create interactive PDF forms — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn forms from static documents into professional, interactive forms that people fill out right in their PDF reader.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm organizing a three-day conference in June (Innovation Summit 2025) and need a professional registration form that attendees can fill out digitally.

Create an interactive PDF registration form with these sections:

- Attendee Information: Full name, email (required fields), company/organization and job title (optional)
- Registration Details: Dropdown for ticket type: Full Conference Pass ($899), Single Day Pass ($349), Virtual Access ($199), Student Pass ($99); Dietary preferences with checkboxes: Vegetarian, Vegan, Gluten-Free, Other; Text field for additional dietary requirements
- Session Interests: Checkboxes for conference tracks (AI & Machine Learning, Sustainability, Leadership, Product Innovation, Design & UX, Data Science)
- Communication Preferences: Checkbox for event updates, checkbox for sharing info with sponsors

Use a professional color scheme with a branded header. The event is "2025 Innovation Summit" at San Francisco Convention Center, June 15-17. Include contact info: [email protected].
```

## Inputs

- Extended Thinking (optional)
- Brand materials or style preference files (optional)
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
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Create interactive PDF forms](https://claude.com/resources/use-cases/create-interactive-pdf-forms) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
