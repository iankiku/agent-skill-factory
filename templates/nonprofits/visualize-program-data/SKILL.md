---
name: visualize-program-data
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Visualize program data."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/visualize-program-data
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Visualize program data — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Transform spreadsheets of program statistics into presentation-ready charts, infographics, and dashboards that tell your impact story visually and help demonstrate program satisfaction to stakeholders.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
The uploaded CSV contains quarterly metrics for six programs: Youth Nutrition Workshop, Adult Wellness Seminar, Senior Health Education, Community CPR Training, Mental Health First Aid, and Diabetes Prevention Program.

The data includes: participants enrolled and completed, completion rates, satisfaction scores (1-5 scale), Net Promoter Scores, pre/post-test averages, knowledge gains, repeat participants, referrals, volunteer hours, and cost per participant.

I need to create a comprehensive visualization suite for our board meeting next week. Create:

1. An Excel dashboard with multiple analysis sheets showing program satisfaction trends, learning outcomes, and quarterly comparisons. Use sophisticated formatting with professional color schemes, frozen headers, and clear data hierarchies. Include summary metrics and trend indicators.
2. A PowerPoint presentation (8-10 slides) that tells our impact story visually. Show satisfaction rankings, participation trends, knowledge gains by program, and key insights. Use premium design with charts that are immediately readable.

The board cares most about program satisfaction, completion rates, and demonstrable learning outcomes. They want to see which programs perform best and where we're improving quarter over quarter. Make the visualizations clear enough for quick comprehension but detailed enough to support strategic decisions.

Design these with consulting-firm quality and use colors that feel professional but warm (we're a health nonprofit, not a corporate consultancy).
```

## Inputs

- Excel/XLSX or CSV data file with quarterly program metrics
- Google Drive integration (recommended for accessing master files)
- Extended Thinking feature enabled
- Code execution and file creation enabled in settings
- Gmail/Slack connectors, historical reports or templates (optional)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Gmail
- Google Drive
- Slack
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

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Visualize program data](https://claude.com/resources/use-cases/visualize-program-data) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
