---
name: build-a-battle-card-library
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Build a battle card library."
metadata:
  status: template — resolve every TODO before use
  category: Sales
  recommended_model: Sonnet 4.5
  features: ["Web Search", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/build-a-battle-card-library
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Build a battle card library — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn sales losses and competitive data into ready-to-use battlecards with winning talk tracks, objection handlers, and differentiation strategies your team can use during actual calls.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Pull our HubSpot closed-lost deals from the last 6 months where DataGuard, BackupPro, or SecureVault appear in the competitor field. Read the deal notes for each competitor and tell me what patterns you see for each one. Search the web for their websites, G2 reviews, and recent positioning to find additional information.

Then, build a React-based competitive intelligence dashboard with a list view showing all three competitors and detailed battlecards for each. Build it like a modern analytics dashboard - clean, flat, metric-dense, with that tech meets creative minimalism. Think calculator app but for competitive intelligence.
```

## Inputs

- HubSpot connector (CRM integration)
- Web Search enabled
- Optional: Extended Thinking feature
- Optional: website screenshot/sales materials upload
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

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- CRM writes are drafted for approval, never auto-committed
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Build a battle card library](https://claude.com/resources/use-cases/build-a-battle-card-library) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
