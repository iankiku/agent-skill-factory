---
name: log-sales-calls-to-your-crm
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Log sales calls to your CRM."
metadata:
  status: template — resolve every TODO before use
  category: Claude in Chrome
  recommended_model: Haiku 4.5
  features: ["Browser Use"]
  surface: "Claude in Chrome"
  source_url: https://claude.com/resources/use-cases/log-sales-calls-to-your-crm
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Log sales calls to your CRM — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude in Chrome can read your calendar, match attendees to Salesforce contacts, and draft activity logs for each call. You add notes and approve before anything gets created.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Log my calls from today in Salesforce.

Steps:
1. Go to my Google Calendar and find today's external meetings (skip internal)
2. For each meeting, look up the attendees in Salesforce
3. Create an activity log for each call—I'll provide a quick summary of what was discussed
4. Format each log with next steps included

Do not submit. Show me everything for review before saving to Salesforce.
```

## Inputs

- Google Calendar login in Chrome
- Salesforce login in Chrome
- Accessible call notes in a doc, notepad, or bullet points (optional)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude in Chrome extension
- Google Calendar
- Salesforce
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms, and ANY click that finalizes state on a third-party site (browser-use skill: show a review step first)

## Workflow

1. Go to my Google Calendar and find today's external meetings (skip internal)
2. For each meeting, look up the attendees in Salesforce
3. Create an activity log for each call—I'll provide a quick summary of what was discussed
4. Format each log with next steps included

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Nothing is submitted/saved on a website without showing the user a review step first
- Site actions limited to the domains named in the workflow
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Page fails to load or selector drifts → retry once, then stop and report; never guess at form fields
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Log sales calls to your CRM](https://claude.com/resources/use-cases/log-sales-calls-to-your-crm) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
