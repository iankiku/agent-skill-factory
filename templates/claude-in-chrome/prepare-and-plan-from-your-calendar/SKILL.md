---
name: prepare-and-plan-from-your-calendar
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Prepare and plan from your calendar."
metadata:
  status: template — resolve every TODO before use
  category: Claude in Chrome
  recommended_model: Haiku 4.5
  features: ["Browser Use"]
  surface: "Claude in Chrome"
  source_url: https://claude.com/resources/use-cases/prepare-and-plan-from-your-calendar
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Prepare and plan from your calendar — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude in Chrome reads your calendar, pulls context from email threads, flags which meetings need prep, and books rooms for the ones missing them.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Look at my calendar and help me get ready for tomorrow. For each meeting: Tell me if it's internal or external (check the attendee domains). Find any recent email threads with those attendees about this topic. Flag if the meeting is missing a room (for in-person) or a video link (for remote). If it is, assign one to the meeting. For external meetings, note anything I should review beforehand, like relevant docs attached to the meeting or related emails. Give me a quick prep summary for the day, finding what needs my attention before I show up.
```

## Inputs

- Google Calendar open showing tomorrow's date, logged in
- Gmail open in another tab, logged in
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude in Chrome extension
- Gmail
- Google Calendar
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms, and ANY click that finalizes state on a third-party site (browser-use skill: show a review step first)

## Workflow

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

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

Derived from [Prepare and plan from your calendar](https://claude.com/resources/use-cases/prepare-and-plan-from-your-calendar) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
