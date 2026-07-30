---
name: handle-a-request-while-away-from-your-keyboard
description: "Use Dispatch in Claude Cowork to respond to requests from the Claude mobile app using everything on your computer. Use for tasks like “Handle a request while away from your keyboard” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Cowork
  recommended_model: Sonnet 4.6
  features: ["Connectors", "Cowork"]
  surface: "Cowork (Dispatch) + Claude mobile app"
  source_url: https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard
  source_title: Handle a request while away from your keyboard
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Handle a request while away from your keyboard — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Use Dispatch in Claude Cowork to respond to requests from the Claude mobile app using everything on your computer.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Jamie just asked me on Slack for the latest Q2 budget spreadsheet. Find it in my Documents/Finance folder on my computer — the file with "Q2" and "budget" in the name. Post it to Jamie in the #proj-planning Slack channel. Add a note that the tab labeled "Revised" has the current numbers.
```

## Required context and inputs

- Claude desktop app running with keep-awake toggle enabled
- Claude mobile app
- Local file access (Documents/Finance folder)
- Slack connector (required for posting)
- Gmail connector (optional, for email drafting)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Gmail
- Slack
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

1. Describe the task — explain what you need Claude to handle
2. Give Claude context — provide access to local files and necessary connectors
3. Claude creates the output — locates files, prepares messages, awaits approval
4. Follow up prompts — refine or expand the conversation
5. Continue on laptop — pick up the same conversation when returning to desktop

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

Derived from [Handle a request while away from your keyboard](https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
