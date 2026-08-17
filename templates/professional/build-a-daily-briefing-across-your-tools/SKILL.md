---
name: build-a-daily-briefing-across-your-tools
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Build a daily briefing across your tools."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork (with Claude in Chrome)"
  source_url: https://claude.com/resources/use-cases/build-a-daily-briefing-across-your-tools
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Build a daily briefing across your tools — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Generate a daily briefing that pulls from Slack, Notion, and your team dashboard to surface priorities and connections you'd miss scanning each platform separately.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

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

## Inputs

- Claude Desktop
- Cowork feature
- Connectors (Slack, Notion)
- Claude in Chrome
- Dashboard URL access
- Optionally calendar and email connectors
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude in Chrome extension
- Notion
- Slack
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Download Claude Desktop and start a Cowork session
2. Add connectors for Slack, Notion, and other desired tools
3. Install Claude in Chrome and add as a connector for dashboard access
4. Submit initial briefing prompt; Claude may ask clarifying questions
5. Review Claude's plan in the sidebar before execution
6. Follow up with refinement prompts as needed

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

Derived from [Build a daily briefing across your tools](https://claude.com/resources/use-cases/build-a-daily-briefing-across-your-tools) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
