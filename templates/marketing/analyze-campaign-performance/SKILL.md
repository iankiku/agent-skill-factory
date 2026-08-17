---
name: analyze-campaign-performance
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Analyze campaign performance."
metadata:
  status: template — resolve every TODO before use
  category: Marketing
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/analyze-campaign-performance
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Analyze campaign performance — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Analyze campaign performance data to identify your best and worst performing channels, then get specific budget reallocation recommendations for next quarter.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm running three campaigns targeting different customer segments. I have Q3 data showing impressions, clicks, conversions, and spend across social, search, and email.

Analyze performance and tell me:

- Which campaigns and channels are working
- Where to reallocate budget for Q4
- What patterns I'm missing across segments

Create a dashboard and analysis report. I need to know what to do differently next quarter.

Context: Our target ROI is 300%+. Enterprise customers have 3x higher LTV than SMB. Industry benchmark is 200-250% ROI. I can shift up to 30% of budget based on performance.
```

## Inputs

- Campaign performance data (XLSX files mentioned as example)
- Optional: Extended Thinking (for better results)
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

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Analyze campaign performance](https://claude.com/resources/use-cases/analyze-campaign-performance) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
