---
name: understand-and-extend-an-inherited-spreadsheet
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Understand and extend an inherited spreadsheet."
metadata:
  status: template — resolve every TODO before use
  category: Finance
  recommended_model: Opus 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/understand-and-extend-an-inherited-spreadsheet
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Understand and extend an inherited spreadsheet — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Understand existing formulas and structure then add new data while preserving the original logic.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I inherited this SaaS revenue model when Marcus left. Finance needs Q1-Q3 2026 projections by Thursday. There's a Legend tab with some basics, and a few cell comments on formulas. Can you read through those, then help me understand the rest? Specifically:

- How the four tabs connect to each other
- What the seasonality adjustment and CAC Payback formulas are actually doing
- Anything important that isn't documented

Add some visual elements so I can see the trends at a glance—data bars on the margins, or a column showing growth from baseline. And add comments explaining any complex formulas. Then extend the model through Q3 2026, following Marcus's patterns.
```

## Inputs

- File creation must be enabled in settings
- Extended Thinking (recommended)
- Spreadsheet file upload required
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

1. Give Claude context (upload spreadsheet)
2. Review what Claude creates
3. Follow up with additional prompts (changelog, variance analysis)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- All figures reconcile to source statements/workbooks; totals recomputed programmatically, not by eye
- Flag (never silently correct) discrepancies between model and source data
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Understand and extend an inherited spreadsheet](https://claude.com/resources/use-cases/understand-and-extend-an-inherited-spreadsheet) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
