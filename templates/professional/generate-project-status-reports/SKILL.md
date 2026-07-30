---
name: generate-project-status-reports
description: "Pull status updates from your emails, Slack channels, meeting notes, and project tools to create a tracker that shows who's working on what, what's blocked, and where things stand—all in one place. Use for tasks like “Generate project status reports” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/generate-project-status-reports
  source_title: Generate project status reports
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Generate project status reports — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Pull status updates from your emails, Slack channels, meeting notes, and project tools to create a tracker that shows who's working on what, what's blocked, and where things stand—all in one place.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- Connectors: Google Drive, Gmail, Google Calendar, Slack
- Optional: Extended Thinking (for better Word/Excel/PowerPoint results)
- Excel file creation
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Gmail
- Google Calendar
- Google Drive
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

1. Describe the task
2. Give Claude context
3. What Claude creates
4. Follow up prompts

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

Derived from [Generate project status reports](https://claude.com/resources/use-cases/generate-project-status-reports) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
