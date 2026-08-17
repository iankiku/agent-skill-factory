---
name: organize-your-business-finances
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Organize your business finances."
metadata:
  status: template — resolve every TODO before use
  category: Finance
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/organize-your-business-finances
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Organize your business finances — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Create spreadsheets that bring clarity to your finances. Spot trends, filter what matters, and understand what your numbers are telling you.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need help organizing my freelance invoices from this year. I'm uploading my invoice file. It has the date, client name, what the project was, and how much I invoiced. Formatting is inconsistent because I've been adding to it all year.

Can you create a cleaner version with a dashboard that shows my total income, breaks it down by month, and lists my clients by who's paid me the most. Add sparklines and data visualizations showing trends over time at a glance. I want to be able to filter and sort to find specific invoices when I need them. If you notice nuance in the data, leave cell comments for more context.

Make this a sophisticated financial dashboard with a 'quiet luxury', editorial aesthetic—muted sage green accent, abundant whitespace, restrained typography. You may need to write a Python script using xlsxwriter to get the sparklines and advanced features working.
```

## Inputs

- Invoice spreadsheet or CSV file upload
- Optional: Extended Thinking (recommended)
- Python/xlsxwriter capability for advanced features
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

1. Give Claude context (upload spreadsheet/CSV with invoice data)
2. What Claude creates (organized data with spreadsheet features)
3. Follow-up prompts (request additions/revisions; update with new data)

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

Derived from [Organize your business finances](https://claude.com/resources/use-cases/organize-your-business-finances) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
