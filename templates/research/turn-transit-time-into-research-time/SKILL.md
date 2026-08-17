---
name: turn-transit-time-into-research-time
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Turn transit time into research time."
metadata:
  status: template — resolve every TODO before use
  category: Research
  recommended_model: Opus 4.5
  features: ["Research", "Web Search", "Extended Thinking"]
  surface: "Claude mobile app and Claude.ai desktop (cross-device continuity)"
  source_url: https://claude.com/resources/use-cases/turn-transit-time-into-research-time
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Turn transit time into research time — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Capture rough thoughts by voice on mobile, then let Claude research your ideas and produce polished deliverables at your desk.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I just had a thought for the product meeting later. I want to look into what our competitors are doing with their onboarding flows. I feel like everybody's moving towards a simpler experience.

Can you pull in our Q1 planning doc because I need to remember where we landed on roadmap priorities. I think we might be overcomplicating our onboarding flow, and I want to make sure that if I make that case in the meeting, I have the data to back it up.

Can you please look through the doc, do some competitor research on their onboarding flows, find any good onboarding stats, and prep me for later? Thanks.
```

## Inputs

- Enable web search
- Enable Extended Thinking (optional)
- Upload Q1 planning document or reference documents on mobile
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

- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Turn transit time into research time](https://claude.com/resources/use-cases/turn-transit-time-into-research-time) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
