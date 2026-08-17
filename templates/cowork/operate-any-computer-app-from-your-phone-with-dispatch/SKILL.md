---
name: operate-any-computer-app-from-your-phone-with-dispatch
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Operate any computer app from your phone with Dispatch."
metadata:
  status: template — resolve every TODO before use
  category: Cowork
  recommended_model: Sonnet 4.6
  features: ["Connectors", "Cowork"]
  surface: "Cowork (Dispatch) + Claude mobile app"
  source_url: https://claude.com/resources/use-cases/operate-any-computer-app-from-your-phone-with-dispatch
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Operate any computer app from your phone with Dispatch — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

In Claude Cowork, Dispatch with computer use lets Claude control your computer's mouse and keyboard from the Claude mobile app to work in apps that have no other interface Claude could reach.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Open my accounting app and pull the outstanding invoices report for March. List every invoice over 60 days past due with the client name, invoice number, and amount. Send me the totals by client.
```

## Inputs

- Computer use toggle enabled in Dispatch settings
- Desktop accounting application open or pinned to taskbar/Dock
- Optional: Gmail or Slack connector for routing results
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Gmail
- Slack
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task — enable computer use in Dispatch settings; Claude asks for approval before controlling applications
2. Give Claude context — confirm the desktop application is open and computer use is enabled; no connectors required
3. What Claude creates — Claude opens the app, navigates to reports, runs the report, and delivers results
4. Follow up prompts — check web portals in Chrome, review reports at your desk, or email results to your team

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

Derived from [Operate any computer app from your phone with Dispatch](https://claude.com/resources/use-cases/operate-any-computer-app-from-your-phone-with-dispatch) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
