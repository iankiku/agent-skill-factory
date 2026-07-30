---
name: plan-your-career-path
description: "Map the jobs you want to a career plan—skill gaps, timelines, people to contact, and specific next steps. Use for tasks like “Plan your career path” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Education
  recommended_model: Sonnet 4.5
  features: ["Connectors", "Research"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/Plan-your-career-path
  source_title: Plan your career path
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Plan your career path — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Map the jobs you want to a career plan—skill gaps, timelines, people to contact, and specific next steps.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- Google Drive integration (to access resume)
- Optional: Extended Thinking and Web Search features enabled
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Google Drive
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

1. Describe the task
2. Give Claude context
3. What Claude creates
4. Follow up prompts
5. Tricks, tips, and troubleshooting

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
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

Derived from [Plan your career path](https://claude.com/resources/use-cases/Plan-your-career-path) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
