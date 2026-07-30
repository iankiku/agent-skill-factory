---
name: quickly-prep-for-your-week
description: "Prepare and prioritize for your upcoming week through connecting your calendar and mail platforms. Use for tasks like “Quickly prep for your week” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/quickly-prep-for-your-week
  source_title: Quickly prep for your week
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Quickly prep for your week — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Prepare and prioritize for your upcoming week through connecting your calendar and mail platforms.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Help me plan my upcoming week: October 27-31.

Using my M365 connector look at my Outlook calendar and find all meetings that need prep, or where I'm making decisions. Show me where I'm overbooked, where I have real focus time, and any scheduling problems I need to fix now.

From my Outlook inbox and summarize any weekend emails I need to handle, any threads from last week that become urgent this week if ignored, and anyone blocked waiting for my response.

Create an overview document of my must-dos, daily structure, preparation I still need to do, blocks of time I need for deep work, and email triage of high-priority vs can-wait.
```

## Required context and inputs

- Microsoft 365 connector (Outlook calendar and inbox access)
- Extended Thinking feature
- Connectors feature
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Microsoft 365
- Outlook
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

1. Describe the task (user provides dates, scope, and output format)
2. Give Claude context (enable Microsoft 365 connector in Settings > Connectors)
3. What Claude creates (generates calendar analysis and email triage)
4. Follow up prompts (draft responses, create prep materials, adjust output)

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

Derived from [Quickly prep for your week](https://claude.com/resources/use-cases/quickly-prep-for-your-week) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
