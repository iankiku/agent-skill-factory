---
name: create-a-daily-travel-itinerary
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create a daily travel itinerary."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Web Search", "Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-a-daily-travel-itinerary
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create a daily travel itinerary — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Create a customized travel itinerary with intelligent guidance, adapting to your preferences and desired activities.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Create a 5-day trip itinerary for my visit to Lisbon in early June.

I want authentic neighborhood restaurants where locals eat, Manueline and Pombaline architecture at the actual monuments, genuine fado experiences, to walk 8-10 miles daily instead of using transit, and to visit only truly exceptional museums like Gulbenkian while skipping generic collections.

Research current recommendations and build a realistic 5-day itinerary with actual walking times, meal schedules, and weather considerations.

Create a Word document designed for mobile use: day-by-day timing, addresses, alternatives when places are full, daily budget estimates, and neighborhood context. Include small thumbnail photos (160x120px) at key locations paired with clickable links to real photo galleries so I can preview places visually and browse full image sets.

Design this document like something a top-tier travel agency produces Think high-end travel magazine meets bespoke concierge service, not generic travel guide. Use a sophisticated color system, elegant typography, and organized text that feels expensive. Make every design choice serve both aesthetics and utility.
```

## Inputs

- Web Search (enable for current travel information)
- Extended Thinking (for detailed itinerary organization)
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

- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Create a daily travel itinerary](https://claude.com/resources/use-cases/create-a-daily-travel-itinerary) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
