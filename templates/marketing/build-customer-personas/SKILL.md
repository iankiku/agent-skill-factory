---
name: build-customer-personas
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Build customer personas."
metadata:
  status: template — resolve every TODO before use
  category: Marketing
  recommended_model: Sonnet 4.5
  features: ["Connectors", "Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/build-customer-personas
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Build customer personas — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Create personas with demographics, goals, and pain points synthesized from your research data.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I've uploaded customer feedback from different sources—could be sales call notes, support conversations, survey responses, whatever we've collected. Figure out what types of customers we have based on their actual behavior and problems.

Create an interactive artifact where I can explore each persona and see their journey. Show their goals, what frustrates them, and include actual quotes from customers. Make the artifact professionally and elegantly designed, as it will be shared with others. Focus on creating analytical and helpful content. Take time to analyze thoroughly, outline carefully, and validate your work.
```

## Inputs

- Upload customer research files (sales call notes, interview transcripts, survey responses)
- Optional connectors: HubSpot, Intercom
- Extended Thinking feature enabled
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- HubSpot
- Intercom
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Follow up prompts (create written report, identify revenue opportunity, find quick wins)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Build customer personas](https://claude.com/resources/use-cases/build-customer-personas) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
