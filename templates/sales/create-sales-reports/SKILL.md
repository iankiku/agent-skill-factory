---
name: create-sales-reports
description: "Pull metrics from your CRM, analyze trends, and generate polished reports with data visualizations and strategic insights—all without manual data formatting. Use for tasks like “Create sales reports” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Sales
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-sales-reports
  source_title: Create sales reports
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create sales reports — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Pull metrics from your CRM, analyze trends, and generate polished reports with data visualizations and strategic insights—all without manual data formatting.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- HubSpot connector (enabled in Settings > Capabilities)
- Optional: Extended Thinking feature enabled
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- HubSpot
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

1. Describe the task (provide report requirements and formatting specifications)
2. Give Claude context (enable HubSpot connector; optionally enable Extended Thinking)
3. What Claude creates (generates analyzed report with executive summary and visualizations)
4. Follow up prompts (quiz on findings, add market benchmarks, deep-dive analysis)
5. Tips and troubleshooting (request professional formatting, leverage live connectors, expand across tools)

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- CRM writes are drafted for approval, never auto-committed
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
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

Derived from [Create sales reports](https://claude.com/resources/use-cases/create-sales-reports) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
