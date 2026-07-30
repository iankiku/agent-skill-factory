---
name: write-an-impact-report
description: "Turn raw program data and participant outcomes into compelling narratives with data visualizations, stakeholder-specific insights, and authentic success stories that demonstrate real impact. Use for tasks like “Write an impact report” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: []
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/write-an-impact-report
  source_title: Write an impact report
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Write an impact report — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Turn raw program data and participant outcomes into compelling narratives with data visualizations, stakeholder-specific insights, and authentic success stories that demonstrate real impact.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- Spreadsheets/databases with program metrics: participant enrollment, demographics, attendance, assessment scores, volunteer hours, financial data, and qualitative feedback
- Three sample XLSX files referenced on the page
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
2. Give Claude context (upload raw program data)
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

Derived from [Write an impact report](https://claude.com/resources/use-cases/write-an-impact-report) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
