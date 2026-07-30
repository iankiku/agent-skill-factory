---
name: compare-and-analyze-competing-options
description: "Upload vendor proposals in any format and get a normalized comparison spreadsheet that extracts pricing structures, contract terms, and feature differences. Use for tasks like “Compare and analyze competing options” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/compare-and-analyze-competing-options
  source_title: Compare and analyze competing options
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Compare and analyze competing options — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Upload vendor proposals in any format and get a normalized comparison spreadsheet that extracts pricing structures, contract terms, and feature differences

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm evaluating three payroll providers and need to decide by Friday. I've uploaded proposals from PayFlow Pro, TeamSync HR, and WorkForce Central.

Extract and compare base monthly costs and fees, onboarding timelines, contract lengths and terms, key feature differences, and support options. Create a comparison spreadsheet that shows everything side-by-side. Make it easy to scan—I need to present this to our CFO and we need to make a decision fast. Flag anything important I should know: hidden fees, concerning contract terms, major feature gaps.

This spreadsheet should be extremely well-designed. Think: professional not playful, expert-grade execution, and surgical precision and craft.
```

## Required context and inputs

- Vendor proposal documents (multiple formats supported)
- Extended Thinking feature (optional, recommended for complex proposals)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- No connectors detected on the source page; base Claude capabilities only
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
2. Give Claude context (upload vendor proposals)
3. What Claude creates (analysis and spreadsheet)
4. Follow up prompts (draft decision memo, create vendor call questions, calculate costs)
5. Tricks, tips, and troubleshooting

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

Derived from [Compare and analyze competing options](https://claude.com/resources/use-cases/compare-and-analyze-competing-options) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
