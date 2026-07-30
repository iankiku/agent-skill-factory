---
name: create-health-and-exercise-notes
description: "Research specific exercises and save organized notes directly to your Notes app. Use for tasks like “Create health and exercise notes” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Web Search", "Connectors"]
  surface: "Claude for desktop"
  source_url: https://claude.com/resources/use-cases/create-health-and-exercise-notes
  source_title: Create health and exercise notes
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create health and exercise notes — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Research specific exercises and save organized notes directly to your Notes app.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I've been dealing with knee pain, and my doctor recommended I strengthen the muscles around it. I'd like to research appropriate exercises and create a routine I can do on my own.

Save this to my Notes app as "Knee Strengthening Routine" so I can pull it up on my phone while I'm exercising. I want to show it to my physical therapist next week to make sure I'm on the right track.

Format for Apple Notes on my phone. Use HTML <br> tags in order to create natural line breaks. Use abbreviations and keep it scannable - clear headers, quick reference info only, cut verbose explanations. Optimize for mobile, not desktop.
```

## Required context and inputs

- Claude for desktop app
- Notes connector enabled in Settings > Connectors
- Web Search feature enabled
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Apple Notes
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

1. Describe the task (provide health goals and constraints)
2. Give Claude context (enable Notes connector and Web Search)
3. Receive structured output saved to Notes app
4. Explore follow-up options (progress tracking, anatomical explanations, routine progression)

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

Derived from [Create health and exercise notes](https://claude.com/resources/use-cases/create-health-and-exercise-notes) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
