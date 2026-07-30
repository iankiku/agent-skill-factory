---
name: create-a-daily-travel-itinerary
description: "Create a customized travel itinerary with intelligent guidance, adapting to your preferences and desired activities. Use for tasks like “Create a daily travel itinerary” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Web Search", "Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-a-daily-travel-itinerary
  source_title: Create a daily travel itinerary
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create a daily travel itinerary — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Create a customized travel itinerary with intelligent guidance, adapting to your preferences and desired activities.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Create a 5-day trip itinerary for my visit to Lisbon in early June.

I want authentic neighborhood restaurants where locals eat, Manueline and Pombaline architecture at the actual monuments, genuine fado experiences, to walk 8-10 miles daily instead of using transit, and to visit only truly exceptional museums like Gulbenkian while skipping generic collections.

Research current recommendations and build a realistic 5-day itinerary with actual walking times, meal schedules, and weather considerations.

Create a Word document designed for mobile use: day-by-day timing, addresses, alternatives when places are full, daily budget estimates, and neighborhood context. Include small thumbnail photos (160x120px) at key locations paired with clickable links to real photo galleries so I can preview places visually and browse full image sets.

Design this document like something a top-tier travel agency produces Think high-end travel magazine meets bespoke concierge service, not generic travel guide. Use a sophisticated color system, elegant typography, and organized text that feels expensive. Make every design choice serve both aesthetics and utility.
```

## Required context and inputs

- Web Search (enable for current travel information)
- Extended Thinking (for detailed itinerary organization)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- No connectors detected on the source page; base Claude capabilities only
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

Derived from [Create a daily travel itinerary](https://claude.com/resources/use-cases/create-a-daily-travel-itinerary) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
