---
name: remote-control-your-computer-with-dispatch
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Remote control your computer with Dispatch."
metadata:
  status: template — resolve every TODO before use
  category: Cowork
  recommended_model: Sonnet 4.6
  features: ["Cowork", "Connectors"]
  surface: "Cowork (Dispatch) + Claude mobile app"
  source_url: https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Remote control your computer with Dispatch — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Use Dispatch in Claude Cowork to send instructions from your phone. Claude runs the task on your computer — reading files, pulling data, searching the web — and the result is waiting when you sit down.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need a competitive landscape summary for our Q2 planning meeting. Start with the spreadsheet at in my Sales folder - I think it's called competitor-tracker.xlsx — that has our current list of competitors and their pricing.
For each competitor listed there, search the web for any product launches, pricing changes, or funding announcements from the last 90 days.
Put together a report with one section per competitor: what they have changed since our last update, how their pricing compares to the figures in the spreadsheet, and anything we should flag for the planning meeting. Save the report as a Google Doc in my Strategy folder on Drive.
```

## Inputs

- Google Drive connector (save reports)
- Local file access (read spreadsheets)
- Claude desktop app running on computer
- Keep-awake toggle enabled in Dispatch settings
- Optional: Gmail and Google Calendar connectors
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Gmail
- Google Calendar
- Google Drive
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Give Claude context (connectors and required/optional integrations)
2. Claude creates the output
3. Follow up prompts to refine or expand results

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Remote control your computer with Dispatch](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
