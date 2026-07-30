---
name: create-a-sales-proposal-presentation
description: "Create a polished client proposal deck with professional layouts data visualizations and cohesive design—then refine through feedback until it matches your standards. Use for tasks like “Create a sales proposal presentation” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Sales
  recommended_model: Opus 4.5
  features: ["Extended Thinking", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-a-sales-proposal-presentation
  source_title: Create a sales proposal presentation
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create a sales proposal presentation — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Create a polished client proposal deck with professional layouts data visualizations and cohesive design—then refine through feedback until it matches your standards.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm putting together a proposal deck for Midwest Regional Health, a healthcare network we've been in conversations with about our patient engagement platform.

Search my Google Drive for documents with "Midwest Regional" in the title—there should be discovery call notes, their RFP, and a competitive analysis we did.

Pull the relevant information to build out these slides: Make sure to include executive summary, their challenges, our solution and how it addresses their specific situation, implementation approach, pricing, case study (find a similar healthcare client we can reference), timeline and next steps.

Design direction: Clean and professional, but not sterile. I want something modern and approachable while still appropriate for hospital executives. Use premium typography (not default fonts) and our brand colors from the logo I'm uploading. Make sure text is conservatively sized so nothing gets cut off, and verify that no elements overlap.
```

## Required context and inputs

- Google Drive integration enabled
- Company logo upload
- Extended Thinking feature enabled (optional but recommended)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Google Drive
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
5. Tricks, tips, and troubleshooting

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

Derived from [Create a sales proposal presentation](https://claude.com/resources/use-cases/create-a-sales-proposal-presentation) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
