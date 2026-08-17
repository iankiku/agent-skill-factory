---
name: thoughtful-gift-giving-with-claude
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Thoughtful gift giving with Claude."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Opus 4.5
  features: ["Web Search", "Connectors", "Extended Thinking"]
  surface: "Claude.ai chat (Claude for Desktop mentioned for connector access)"
  source_url: https://claude.com/resources/use-cases/thoughtful-gift-giving-with-claude
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Thoughtful gift giving with Claude — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn last-minute gift panic into thoughtful, personalized presents. Claude can suggest items, search your notes for forgotten hints, find specific products you can buy locally, and help you coordinate the actual shopping.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I always forget stocking stuffers until the last minute and end up panic-buying junk. This year I want to fill stockings with small things people will actually use or enjoy. Help me think through good stocking stuffer ideas for my family that I can find locally this week:

- Wife (38) — really into skincare lately, drinks a lot of tea, always cold
- Son (12) — obsessed with basketball, just started getting into music
- Daughter (9) — loves art projects, reads constantly, very into her pet hamster
- Dad (67) — impossible to buy for, likes golf and grilling, diabetic so no candy
- Mom (65) — does crossword puzzles every morning, into bird watching, practical about gifts

Can you put this together in a shopping list I can reference?
```

## Inputs

- Web Search (optional)
- iOS Connectors (Notes, iMessages)
- Extended Thinking
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

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Thoughtful gift giving with Claude](https://claude.com/resources/use-cases/thoughtful-gift-giving-with-claude) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
