---
name: surface-themes-from-all-your-feedback-channels
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Surface themes from all your feedback channels."
metadata:
  status: template — resolve every TODO before use
  category: Research
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/surface-themes-from-all-your-feedback-channels
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Surface themes from all your feedback channels — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Synthesize feedback from call transcripts, Slack, CRM notes, and Linear issues to identify cross-platform patterns and generate prioritized product ideas.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need to understand what customers are really asking for by synthesizing feedback from multiple sources. Sources: Call transcripts: Scattered across my downloads folder, Slack in channels like #customer-feedback and #support-questions, Salesforce: Opportunity notes and lost deal reasons, Linear: Open feature requests and bug reports. Find the main themes and patterns across all sources — what keeps coming up? Give me counts by source, cross-platform patterns, and representative quotes. Then prioritize into product ideas based on frequency and business impact.
```

## Inputs

- Claude Desktop
- Call transcript folder access
- Connectors for Slack/CRM/Linear
- Optional theme taxonomy or customer segment definitions
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Linear
- Salesforce
- Slack
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (identifying customer needs via multi-source feedback synthesis)
2. Give Claude context (download Claude Desktop, select "Work in a folder," add connectors for Slack/CRM/Linear)
3. Claude creates synthesized analysis with themes, counts, cross-platform patterns, and prioritized product ideas
4. Follow up with refinement prompts (deep dives, roadmap proposals, customer tracking)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Surface themes from all your feedback channels](https://claude.com/resources/use-cases/surface-themes-from-all-your-feedback-channels) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
