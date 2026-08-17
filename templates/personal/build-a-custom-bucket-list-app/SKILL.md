---
name: build-a-custom-bucket-list-app
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Build a custom bucket list."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Opus 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/build-a-custom-bucket-list-app
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Build a custom bucket list — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn any tracker, organizer, or goal system you've imagined into a working interactive tool. Describe what you want and watch Claude build it.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I want to create an interactive 'bucket list builder' that feels like browsing a beautiful, high-end boutique, but for life experiences instead of products.

The concept: Transform 'I should make a future goals list' into something more joyful. Instead of just a normal list, I want an experience.

Design: This needs to look like a world-class iOS app. Clean, intentional graphic design. Every detail (typography, spacing, hierarchy) should feel curated and thought-through. The end result should be stunning.

Include: Experiences by category; saving certain experiences to 'My List'; toggles between browsing and viewing saved items, satisfying interactions when selecting items. Populate it with beautiful life experiences to browse. Then, add in some additional fun surprises!
```

## Inputs

- Extended Thinking feature recommended
- No file uploads required
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

Derived from [Build a custom bucket list](https://claude.com/resources/use-cases/build-a-custom-bucket-list-app) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
