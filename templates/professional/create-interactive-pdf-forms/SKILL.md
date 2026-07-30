---
name: create-interactive-pdf-forms
description: "Turn forms from static documents into professional, interactive forms that people fill out right in their PDF reader. Use for tasks like “Create interactive PDF forms” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-interactive-pdf-forms
  source_title: Create interactive PDF forms
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create interactive PDF forms — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Turn forms from static documents into professional, interactive forms that people fill out right in their PDF reader.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- Extended Thinking (optional)
- Brand materials or style preference files (optional)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- No connectors detected on the source page; base Claude capabilities only
- TODO: confirm which connectors are enabled in the runtime that will execute this skill
- Authentication: connectors authenticate via their own OAuth flows — this skill must
  NEVER ask for, store, or echo credentials, tokens, or API keys. If auth is missing,
  stop and tell the user which connector to enable.

## Permissions and sensitive actions

- Reads: TODO (folders, channels, records this skill may read)
- Writes: TODO (what it may create/modify, and where)
- Held back for the primary agent / human: sending external communications, financial
  transactions, deleting or overwriting originals, submitting web forms

## Workflow

1. Describe the task
2. Give Claude context
3. What Claude creates
4. Follow up prompts

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Apply the repo's delegation policy (`docs/delegation-policy.md` — bundle or restate
it if you install this skill outside the repo). Defaults for this template:

- Run single-agent unless a step fans out over independent items (files, records,
  vendors, channels). Only independent work parallelizes.
- Each delegated task must ship with: the minimal context slice it needs, an explicit
  output contract, a validation check the primary agent runs on the result, and a
  fallback if it returns empty or fails.
- Final review, synthesis, and every sensitive action listed above stay with the
  primary agent.
- TODO: name the concrete subtasks (if any) that qualify for delegation here.

## Attribution

Derived from [Create interactive PDF forms](https://claude.com/resources/use-cases/create-interactive-pdf-forms) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
