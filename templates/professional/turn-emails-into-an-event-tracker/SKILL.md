---
name: turn-emails-into-an-event-tracker
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Turn emails into an event tracker."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/turn-emails-into-an-event-tracker
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Turn emails into an event tracker — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Build an event tracker by extracting dates, locations, and logistics from email threads.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Search my Gmail for speaker confirmations and extract their name and company, what session topic they confirmed, time preference if mentioned, A/V needs, travel arrangements if they brought it up, whether they've sent their bio and headshot. We're locking in the agenda next week. Build me a tracker with formulas, color-coded cells, and clear sections. Make the spreadsheet look like a boutique design studio created a data visualization piece, not like someone filled out an Excel template. The typography and color should look editorial and refined with modern professionalism. Include professional spreadsheet elements like frozen headers, sortable columns, and working formulas.
```

## Inputs

- Gmail connector (enabled in Settings > Connectors)
- Extended Thinking (optional but recommended)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Gmail
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (search Gmail and extract speaker data)
2. Give Claude context (enable Gmail integration and Extended Thinking)
3. Claude creates structured spreadsheet with speaker directory, production overview, technical notes, and materials tracking
4. Follow up prompts available for calendar events, follow-up messages, and dynamic formulas

TODO: rewrite as imperative steps for the executing agent.

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

Derived from [Turn emails into an event tracker](https://claude.com/resources/use-cases/turn-emails-into-an-event-tracker) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
