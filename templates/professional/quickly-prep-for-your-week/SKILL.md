---
name: quickly-prep-for-your-week
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Quickly prep for your week."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/quickly-prep-for-your-week
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Quickly prep for your week — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Prepare and prioritize for your upcoming week through connecting your calendar and mail platforms.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Help me plan my upcoming week: October 27-31.

Using my M365 connector look at my Outlook calendar and find all meetings that need prep, or where I'm making decisions. Show me where I'm overbooked, where I have real focus time, and any scheduling problems I need to fix now.

From my Outlook inbox and summarize any weekend emails I need to handle, any threads from last week that become urgent this week if ignored, and anyone blocked waiting for my response.

Create an overview document of my must-dos, daily structure, preparation I still need to do, blocks of time I need for deep work, and email triage of high-priority vs can-wait.
```

## Inputs

- Microsoft 365 connector (Outlook calendar and inbox access)
- Extended Thinking feature
- Connectors feature
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Microsoft 365
- Outlook
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (user provides dates, scope, and output format)
2. Give Claude context (enable Microsoft 365 connector in Settings > Connectors)
3. What Claude creates (generates calendar analysis and email triage)
4. Follow up prompts (draft responses, create prep materials, adjust output)

TODO: rewrite as imperative steps for the executing agent.

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

Derived from [Quickly prep for your week](https://claude.com/resources/use-cases/quickly-prep-for-your-week) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
