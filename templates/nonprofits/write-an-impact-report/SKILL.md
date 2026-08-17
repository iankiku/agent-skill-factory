---
name: write-an-impact-report
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Write an impact report."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: []
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/write-an-impact-report
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Write an impact report — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn raw program data and participant outcomes into compelling narratives with data visualizations, stakeholder-specific insights, and authentic success stories that demonstrate real impact.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm the Program Director at Bright Futures Learning Center, a nonprofit providing after-school tutoring and enrichment programs for middle school students in underserved Seattle neighborhoods. I need to create our annual impact report that will go to our board, major donors, and foundation funders.

I'm uploading our program data: student enrollment and demographics, attendance records, academic assessment results (pre/post test scores), volunteer hours, and our financial summary. We served 347 students this year across three locations.

For the report, I need:

- An executive summary with our biggest wins and key metrics
- Compelling data visualizations that show academic growth, attendance trends, and program reach
- Narrative sections that tell the story of what we accomplished
- Student demographics and community impact data
- Financial overview showing how funds were used
- A forward-looking section on next year's goals

Make this board-ready and donor-worthy. Use sophisticated design that matches the quality of professional nonprofit reports—this goes to foundation program officers who see dozens of these. Include charts and visual elements that make the data immediately clear. The tone should be confident about our achievements while staying authentic and mission-focused.
```

## Inputs

- Spreadsheets/databases with program metrics: participant enrollment, demographics, attendance, assessment scores, volunteer hours, financial data, and qualitative feedback
- Three sample XLSX files referenced on the page
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

1. Give Claude context (upload raw program data)

TODO: rewrite as imperative steps for the executing agent.

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

Derived from [Write an impact report](https://claude.com/resources/use-cases/write-an-impact-report) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
