---
name: turn-text-threads-to-researched-notes
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Turn text threads to researched notes."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Connectors", "Web Search"]
  surface: "Claude for Desktop"
  source_url: https://claude.com/resources/use-cases/turn-text-threads-to-researched-notes
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Turn text threads to researched notes — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Search messages for information, research answers, and create organized notes directly in your Notes app.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I just got a text from Sarah asking me to bring dessert to Saturday's potluck—there will be about 15 people. Can you read my Messages to see the full context, then help me figure out what to make? I need something that's impressive but not too complicated, travels well, and can be made Friday night since Saturday morning I'll be busy. Research dessert options that fit those criteria, save recipe and shopping list to my Notes app—group the shopping list by store section so I'm not running back and forth, and include any technique tips that'll help me nail it. To ensure correct formatting in my notes, using HTML tags to create natural line breaks. Use abbreviations and concise language so the note isn't overly long.
```

## Inputs

- Download Claude for Desktop
- Enable Messages and Notes connectors (Desktop extensions)
- Enable Web Search
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

1. Follow-up prompts

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

Derived from [Turn text threads to researched notes](https://claude.com/resources/use-cases/turn-text-threads-to-researched-notes) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
