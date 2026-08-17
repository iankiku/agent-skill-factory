---
name: create-sales-reports
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create sales reports."
metadata:
  status: template — resolve every TODO before use
  category: Sales
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-sales-reports
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create sales reports — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Pull metrics from your CRM, analyze trends, and generate polished reports with data visualizations and strategic insights—all without manual data formatting.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need a Q4 sales report for our exec team meeting next week. Pull October through December from HubSpot.

Show me:
- Total revenue vs Q3—how much did we grow, and was it from more deals or bigger deals?
- Break it down by segment: Enterprise, Mid-Market, and SMB. For each one, show revenue, number of deals, and win rate
- How long are sales cycles taking now compared to Q3?
- Current pipeline value and health
- Top 3 reps by revenue with their numbers
- What's actually working and what needs to change

Create this as a professional document with clean serif fonts, information dense with tight spacing, proper text hierarchy, and embedded charts PNGs that seamlessly integrate into the layout as opposed to looking pasted in. Use proper business style. Opt out of using your default styles.
```

## Inputs

- HubSpot connector (enabled in Settings > Capabilities)
- Optional: Extended Thinking feature enabled
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- HubSpot
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (provide report requirements and formatting specifications)
2. Give Claude context (enable HubSpot connector; optionally enable Extended Thinking)
3. What Claude creates (generates analyzed report with executive summary and visualizations)
4. Follow up prompts (quiz on findings, add market benchmarks, deep-dive analysis)
5. Tips and troubleshooting (request professional formatting, leverage live connectors, expand across tools)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- CRM writes are drafted for approval, never auto-committed
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Create sales reports](https://claude.com/resources/use-cases/create-sales-reports) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
