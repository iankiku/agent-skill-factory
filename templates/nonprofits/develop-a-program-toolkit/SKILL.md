---
name: develop-a-program-toolkit
description: "Generate complete program design frameworks for new initiatives with logic models, evaluation plans, and resource guides that transform concepts into implementation-ready programs. Use for tasks like “Develop a program toolkit” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/develop-a-program-toolkit
  source_title: Develop a program toolkit
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Develop a program toolkit — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Generate complete program design frameworks for new initiatives with logic models, evaluation plans, and resource guides that transform concepts into implementation-ready programs.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- Extended Thinking feature (recommended to enable in conversation settings)
- Excel software (for the output file)
- Theory of Change documentation, current program materials, organizational strategy documents (optional)
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
5. Tricks, tips, and troubleshooting

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
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

Derived from [Develop a program toolkit](https://claude.com/resources/use-cases/develop-a-program-toolkit) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
