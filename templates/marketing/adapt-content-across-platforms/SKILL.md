---
name: adapt-content-across-platforms
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Adapt content across platforms."
metadata:
  status: template — resolve every TODO before use
  category: Marketing
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/adapt-content-across-platforms
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Adapt content across platforms — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Transform one piece of content into multiple formats adapted for different platforms and audiences.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Repurpose this blog post about AI-powered marketing analytics into multi-channel content:

- LinkedIn carousel
- Twitter thread
- Email nurture sequence (5 emails)
- Podcast talking points
- Infographic outline

All content should feel cohesive to my brand but fitting for the platform. To better understand our brand voice, review past work in my Google Drive's 'Social' folder.

Create a beautiful interactive artifact first so I can review everything in one place. Match the design style that I included in the attached screenshots. Also, provide individual files for each format.
```

## Inputs

- Google Drive integration (required for accessing source content and brand examples)
- Optional: Extended Thinking (for better results on complex multi-source tasks)
- Communication style guide document
- Source content document
- Design style screenshots
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

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

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

Derived from [Adapt content across platforms](https://claude.com/resources/use-cases/adapt-content-across-platforms) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
