---
name: prepare-for-sales-deals
description: "Pull relevant CRM data, like details on comparable opportunities, to prepare for upcoming sales conversations. Use for tasks like “Prepare for sales deals” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Sales
  recommended_model: Sonnet 4.5
  features: ["Connectors", "Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/prepare-for-sales-deals
  source_title: Prepare for sales deals
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Prepare for sales deals — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Pull relevant CRM data, like details on comparable opportunities, to prepare for upcoming sales conversations.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm working on a healthcare deal - mid-market, around 180 employees, about $60K. They're interested in our patient engagement platform but worried about integration into their current system and how long implementation takes.

Can you pull similar healthcare deals we've closed in the last year or two? I want to see what these typically look like - how long they take, what we usually close at and typical issues that come up. If there are reps who've done deals like this, I should probably talk to them.

Create an artifact I can scan before my next call to feel the most prepared. This artifact should follow top-tier design standards. Create a industry-leading MedTech company meets top creative agency aesthetic.
```

## Required context and inputs

- HubSpot connector (required; enable in Settings > Capabilities)
- Optional: Extended Thinking (to improve analysis quality)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- HubSpot
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

1. Describe the task: tell Claude about your deal and what insights you need from similar opportunities
2. Give Claude context: connect HubSpot connector (required); optionally enable Extended Thinking
3. What Claude creates: searches CRM for comparable deals, identifies patterns, creates prep artifact with key insights
4. Follow-up prompts: pull specific deal details, create talking points, or conduct competitor research

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- CRM writes are drafted for approval, never auto-committed
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

Derived from [Prepare for sales deals](https://claude.com/resources/use-cases/prepare-for-sales-deals) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
