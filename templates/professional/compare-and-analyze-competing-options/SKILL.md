---
name: compare-and-analyze-competing-options
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Compare and analyze competing options."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/compare-and-analyze-competing-options
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Compare and analyze competing options — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Upload vendor proposals in any format and get a normalized comparison spreadsheet that extracts pricing structures, contract terms, and feature differences

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm evaluating three payroll providers and need to decide by Friday. I've uploaded proposals from PayFlow Pro, TeamSync HR, and WorkForce Central.

Extract and compare base monthly costs and fees, onboarding timelines, contract lengths and terms, key feature differences, and support options. Create a comparison spreadsheet that shows everything side-by-side. Make it easy to scan—I need to present this to our CFO and we need to make a decision fast. Flag anything important I should know: hidden fees, concerning contract terms, major feature gaps.

This spreadsheet should be extremely well-designed. Think: professional not playful, expert-grade execution, and surgical precision and craft.
```

## Inputs

- Vendor proposal documents (multiple formats supported)
- Extended Thinking feature (optional, recommended for complex proposals)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- No connectors detected on the source page; base Claude capabilities only
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Give Claude context (upload vendor proposals)
2. What Claude creates (analysis and spreadsheet)
3. Follow up prompts (draft decision memo, create vendor call questions, calculate costs)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Compare and analyze competing options](https://claude.com/resources/use-cases/compare-and-analyze-competing-options) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
