---
name: create-health-and-exercise-notes
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create health and exercise notes."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Web Search", "Connectors"]
  surface: "Claude for desktop"
  source_url: https://claude.com/resources/use-cases/create-health-and-exercise-notes
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create health and exercise notes — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Research specific exercises and save organized notes directly to your Notes app.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I've been dealing with knee pain, and my doctor recommended I strengthen the muscles around it. I'd like to research appropriate exercises and create a routine I can do on my own.

Save this to my Notes app as "Knee Strengthening Routine" so I can pull it up on my phone while I'm exercising. I want to show it to my physical therapist next week to make sure I'm on the right track.

Format for Apple Notes on my phone. Use HTML <br> tags in order to create natural line breaks. Use abbreviations and keep it scannable - clear headers, quick reference info only, cut verbose explanations. Optimize for mobile, not desktop.
```

## Inputs

- Claude for desktop app
- Notes connector enabled in Settings > Connectors
- Web Search feature enabled
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Apple Notes
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (provide health goals and constraints)
2. Give Claude context (enable Notes connector and Web Search)
3. Receive structured output saved to Notes app
4. Explore follow-up options (progress tracking, anatomical explanations, routine progression)

TODO: rewrite as imperative steps for the executing agent.

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

Derived from [Create health and exercise notes](https://claude.com/resources/use-cases/create-health-and-exercise-notes) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
