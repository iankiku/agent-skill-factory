---
name: prepare-for-sales-deals
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Prepare for sales deals."
metadata:
  status: template — resolve every TODO before use
  category: Sales
  recommended_model: Sonnet 4.5
  features: ["Connectors", "Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/prepare-for-sales-deals
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Prepare for sales deals — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Pull relevant CRM data, like details on comparable opportunities, to prepare for upcoming sales conversations.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm working on a healthcare deal - mid-market, around 180 employees, about $60K. They're interested in our patient engagement platform but worried about integration into their current system and how long implementation takes.

Can you pull similar healthcare deals we've closed in the last year or two? I want to see what these typically look like - how long they take, what we usually close at and typical issues that come up. If there are reps who've done deals like this, I should probably talk to them.

Create an artifact I can scan before my next call to feel the most prepared. This artifact should follow top-tier design standards. Create a industry-leading MedTech company meets top creative agency aesthetic.
```

## Inputs

- HubSpot connector (required; enable in Settings > Capabilities)
- Optional: Extended Thinking (to improve analysis quality)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- HubSpot
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task: tell Claude about your deal and what insights you need from similar opportunities
2. Give Claude context: connect HubSpot connector (required); optionally enable Extended Thinking
3. What Claude creates: searches CRM for comparable deals, identifies patterns, creates prep artifact with key insights
4. Follow-up prompts: pull specific deal details, create talking points, or conduct competitor research

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- CRM writes are drafted for approval, never auto-committed
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Prepare for sales deals](https://claude.com/resources/use-cases/prepare-for-sales-deals) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
