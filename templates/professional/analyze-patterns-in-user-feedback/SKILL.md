---
name: analyze-patterns-in-user-feedback
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Analyze patterns in user feedback."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/analyze-patterns-in-user-feedback
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Analyze patterns in user feedback — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Find recurring themes and pain points across user feedback to separate meaningful patterns from noise.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Pull all Intercom conversations from the past 90 days. I'm also uploading our Q2 NPS survey responses (CSV) and notes from six user interviews we did last month (PDFs).

Read everything and tell me what patterns you're seeing:

- What issues keep showing up across different feedback sources?
- When people ask for different things, are they actually pointing to the same underlying need?
- Which complaints seem most urgent based on how users describe them?
- What's worth prioritizing vs what's noise?

Create a data workbook (Excel) organizing all the feedback by theme with filters so I can dig into specific issues. Include the source for each piece of feedback (Intercom, NPS, or interview) and use professional formatting with frozen headers
```

## Inputs

- Intercom connector enabled (Settings > Connectors)
- Upload supplementary feedback files (NPS responses CSV, interview transcripts PDFs)
- Optional: Extended Thinking for deeper pattern recognition
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Intercom
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
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Analyze patterns in user feedback](https://claude.com/resources/use-cases/analyze-patterns-in-user-feedback) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
