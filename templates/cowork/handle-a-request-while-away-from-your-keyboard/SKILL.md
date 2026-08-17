---
name: handle-a-request-while-away-from-your-keyboard
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Handle a request while away from your keyboard."
metadata:
  status: template — resolve every TODO before use
  category: Cowork
  recommended_model: Sonnet 4.6
  features: ["Connectors", "Cowork"]
  surface: "Cowork (Dispatch) + Claude mobile app"
  source_url: https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Handle a request while away from your keyboard — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Use Dispatch in Claude Cowork to respond to requests from the Claude mobile app using everything on your computer.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Jamie just asked me on Slack for the latest Q2 budget spreadsheet. Find it in my Documents/Finance folder on my computer — the file with "Q2" and "budget" in the name. Post it to Jamie in the #proj-planning Slack channel. Add a note that the tab labeled "Revised" has the current numbers.
```

## Inputs

- Claude desktop app running with keep-awake toggle enabled
- Claude mobile app
- Local file access (Documents/Finance folder)
- Slack connector (required for posting)
- Gmail connector (optional, for email drafting)
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

1. Describe the task — explain what you need Claude to handle
2. Give Claude context — provide access to local files and necessary connectors
3. Claude creates the output — locates files, prepares messages, awaits approval
4. Follow up prompts — refine or expand the conversation
5. Continue on laptop — pick up the same conversation when returning to desktop

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

Derived from [Handle a request while away from your keyboard](https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
