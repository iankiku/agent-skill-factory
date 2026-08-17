---
name: see-budget-futures-side-by-side
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: See budget futures side by side, in chat with Claude."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.6
  features: ["Custom visuals"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/see-budget-futures-side-by-side
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# See budget futures side by side, in chat with Claude — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Type your budget split and the thing that might change, and Claude draws three scenarios next to each other with a toggle between dollars and percentages.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
We might lose our $400K federal grant next year. Current budget is about $2.1M: Roughly 60% programs, 25% ops, 15% fundraising. Show me three scenarios side by side: We lose the grant, we stay flat, it grows a bit. I want to flip between dollars and percentages, and if I click a scenario give me the one-line version of what it actually means.
```

## Inputs

- No file uploads required; works with manually entered numbers
- Optional: Google Drive connection for real budget spreadsheets
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Google Drive
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (provide budget and the variable that might change)
2. Give Claude context (type numbers directly; rough estimates acceptable)
3. Claude creates visual output (three stacked bar charts with toggle and scenario descriptions)
4. Follow up with refinements (constraint buttons, multi-year timelines, board-ready language)

TODO: rewrite as imperative steps for the executing agent.

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

Derived from [See budget futures side by side, in chat with Claude](https://claude.com/resources/use-cases/see-budget-futures-side-by-side) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
