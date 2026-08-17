---
name: plan-your-career-path
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Plan your career path."
metadata:
  status: template — resolve every TODO before use
  category: Education
  recommended_model: Sonnet 4.5
  features: ["Connectors", "Research"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/Plan-your-career-path
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Plan your career path — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Map the jobs you want to a career plan—skill gaps, timelines, people to contact, and specific next steps.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm a sophomore at UC Berkeley targeting these roles:

- Associate Product Manager at a music streaming company - https://musicstreaming.com/careers/apm
- Product Designer at a design collaboration platform - https://designplatform.com/careers/designer
- UX Researcher at a travel platform - https://travelplatform.com/careers/researcher

After analyzing my resume against these roles, build:

Action Tracker (Google Doc): Forward-looking planner showing what to do next. Include skill gaps with projects to build, timeline with semester/year/grad milestones, networking targets, learning roadmap, and local resources. Tight spacing, scannable, built for weekly planning.

Skills Portfolio Log (Excel): Backward-looking evidence bank showing what I've done. Log completed projects with metrics, skills inventory with proof points, quantified achievements, learning completions, and STAR stories tagged by competency. Built for mining resume bullets and cover letters.
```

## Inputs

- Google Drive integration (to access resume)
- Optional: Extended Thinking and Web Search features enabled
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
- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Plan your career path](https://claude.com/resources/use-cases/Plan-your-career-path) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
