---
name: see-your-theory-of-change-in-chat-with-claude
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: See your theory of change in chat with Claude."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.6
  features: ["Custom visuals"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/see-your-theory-of-change-in-chat-with-claude
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# See your theory of change in chat with Claude — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Describe your program and Claude draws the causal chain inline, inputs through impact, with every arrow clickable to show the assumption behind it.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I run a youth mentoring program. We pair high schoolers with adult mentors for weekly meetings over a year, and the goal is higher graduation rates. Show me our theory of change, and I want to be able to click the arrows between boxes to see what assumption each one is riding on. Where are the weak links?
```

## Inputs

- No files required to upload
- Optional: formal logic model or grant narrative paragraph
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
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [See your theory of change in chat with Claude](https://claude.com/resources/use-cases/see-your-theory-of-change-in-chat-with-claude) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
