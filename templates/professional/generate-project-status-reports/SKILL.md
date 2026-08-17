---
name: generate-project-status-reports
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Generate project status reports."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/generate-project-status-reports
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Generate project status reports — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Pull status updates from your emails, Slack channels, meeting notes, and project tools to create a tracker that shows who's working on what, what's blocked, and where things stand—all in one place.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need to consolidate project status from multiple sources into a task tracker.

Pull information from:

- Gmail (past 2 weeks, search "Project Hermes")
- Slack #hermes-sprint channel
- Google Drive "Project Hermes" folder
- Recent calendar meetings

For each task, I need to see:

- Who owns it and what they're working on
- Current status (not started, in progress, blocked, done)
- Any blockers and how long they've been stuck
- Notes from their updates about plans and challenges

Create an Excel tracker and include these features: visual status indicators, cell comments with context from sources (so I can hover and see the details), dropdown menus for status and priority (to make updates easy), and data bars showing progress visually.

The tracker should make it obvious at a glance where the problems are and who needs help.
```

## Inputs

- Connectors: Google Drive, Gmail, Google Calendar, Slack
- Optional: Extended Thinking (for better Word/Excel/PowerPoint results)
- Excel file creation
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Gmail
- Google Calendar
- Google Drive
- Slack
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

Derived from [Generate project status reports](https://claude.com/resources/use-cases/generate-project-status-reports) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
