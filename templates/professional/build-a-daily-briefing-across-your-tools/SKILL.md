---
name: build-a-daily-briefing-across-your-tools
description: "Generate a daily briefing that pulls from Slack, Notion, and your team dashboard to surface priorities and connections you'd miss scanning each platform separately. Use for tasks like “Build a daily briefing across your tools” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork (with Claude in Chrome)"
  source_url: https://claude.com/resources/use-cases/build-a-daily-briefing-across-your-tools
  source_title: Build a daily briefing across your tools
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Build a daily briefing across your tools — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Generate a daily briefing that pulls from Slack, Notion, and your team dashboard to surface priorities and connections you'd miss scanning each platform separately.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need my morning briefing. Pull from Slack and Notion, and visit my team dashboard: https://metrics.acme-corp.com/ops-team

Structure it as:

- Urgent items from the dashboard (anything red or trending down)
- Slack threads where I'm mentioned — read the full threads for context
- Threads I'm not in but should probably know about based on my current tasks
- Tasks due this week and anything blocking them

For urgent items, pull the deeper context: who's involved, what's been discussed, what's still unresolved.
```

## Required context and inputs

- Claude Desktop
- Cowork feature
- Connectors (Slack, Notion)
- Claude in Chrome
- Dashboard URL access
- Optionally calendar and email connectors
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Claude in Chrome extension
- Notion
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

1. Download Claude Desktop and start a Cowork session
2. Add connectors for Slack, Notion, and other desired tools
3. Install Claude in Chrome and add as a connector for dashboard access
4. Submit initial briefing prompt; Claude may ask clarifying questions
5. Review Claude's plan in the sidebar before execution
6. Follow up with refinement prompts as needed

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

Derived from [Build a daily briefing across your tools](https://claude.com/resources/use-cases/build-a-daily-briefing-across-your-tools) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
