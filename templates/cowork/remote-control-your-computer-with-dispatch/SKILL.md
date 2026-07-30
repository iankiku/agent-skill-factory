---
name: remote-control-your-computer-with-dispatch
description: "Use Dispatch in Claude Cowork to send instructions from your phone. Claude runs the task on your computer — reading files, pulling data, searching the web — and the result is waiting when you sit down. Use for tasks like “Remote control your computer with Dispatch” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Cowork
  recommended_model: Sonnet 4.6
  features: ["Cowork", "Connectors"]
  surface: "Cowork (Dispatch) + Claude mobile app"
  source_url: https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch
  source_title: Remote control your computer with Dispatch
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Remote control your computer with Dispatch — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Use Dispatch in Claude Cowork to send instructions from your phone. Claude runs the task on your computer — reading files, pulling data, searching the web — and the result is waiting when you sit down.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need a competitive landscape summary for our Q2 planning meeting. Start with the spreadsheet at in my Sales folder - I think it's called competitor-tracker.xlsx — that has our current list of competitors and their pricing.
For each competitor listed there, search the web for any product launches, pricing changes, or funding announcements from the last 90 days.
Put together a report with one section per competitor: what they have changed since our last update, how their pricing compares to the figures in the spreadsheet, and anything we should flag for the planning meeting. Save the report as a Google Doc in my Strategy folder on Drive.
```

## Required context and inputs

- Google Drive connector (save reports)
- Local file access (read spreadsheets)
- Claude desktop app running on computer
- Keep-awake toggle enabled in Dispatch settings
- Optional: Gmail and Google Calendar connectors
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Gmail
- Google Calendar
- Google Drive
- TODO: confirm which connectors are enabled in the runtime that will execute this skill
- Authentication: connectors authenticate via their own OAuth flows — this skill must
  NEVER ask for, store, or echo credentials, tokens, or API keys. If auth is missing,
  stop and tell the user which connector to enable.

## Permissions and sensitive actions

- Reads: TODO (folders, channels, records this skill may read)
- Writes: TODO (what it may create/modify, and where)
- Held back for the primary agent / human: sending external communications, financial
  transactions, deleting or overwriting originals, submitting web forms

## Workflow

1. Describe the task
2. Give Claude context (connectors and required/optional integrations)
3. Claude creates the output
4. Follow up prompts to refine or expand results

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Apply the repo's delegation policy (`docs/delegation-policy.md` — bundle or restate
it if you install this skill outside the repo). Defaults for this template:

- Run single-agent unless a step fans out over independent items (files, records,
  vendors, channels). Only independent work parallelizes.
- Each delegated task must ship with: the minimal context slice it needs, an explicit
  output contract, a validation check the primary agent runs on the result, and a
  fallback if it returns empty or fails.
- Final review, synthesis, and every sensitive action listed above stay with the
  primary agent.
- TODO: name the concrete subtasks (if any) that qualify for delegation here.

## Attribution

Derived from [Remote control your computer with Dispatch](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
