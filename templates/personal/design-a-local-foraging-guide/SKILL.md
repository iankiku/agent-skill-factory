---
name: design-a-local-foraging-guide
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Design a local foraging guide."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Opus 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat (Artifacts)"
  source_url: https://claude.com/resources/use-cases/design-a-local-foraging-guide
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Design a local foraging guide — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Build artifacts where the map is the menu. Select your state on an interactive map browse by category and export a printable reference.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I want to build a foraging guide for someone new to wild edibles and unsure where to start.

What it should do:

- Let users click their state on an interactive US map to see regional foraging data (fetch map data from the us-atlas TopoJSON CDN at https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json and render with D3's geoAlbersUsa projection)
- Browse edible plants by category and show a 12-month season bar for each species so users see harvest windows at a glance
- Let users tap any plant to expand details, then let users add plants to a personal foraging list and export a printable field guide with their selected species and safety reminders

Design: Quiet and organic. Warm cream, muted sage, soft olive. Think field journal meets editorial magazine—sophisticated but approachable. Smooth transitions, rounded corners, good type hierarchy.
```

## Inputs

- Enable Artifacts in settings
- Extended Thinking for complex apps (optional)
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

Derived from [Design a local foraging guide](https://claude.com/resources/use-cases/design-a-local-foraging-guide) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
