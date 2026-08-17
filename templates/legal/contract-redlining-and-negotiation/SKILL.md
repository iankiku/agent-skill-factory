---
name: contract-redlining-and-negotiation
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Contract redlining and negotiation."
metadata:
  status: template — resolve every TODO before use
  category: Legal
  recommended_model: Opus 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/contract-redlining-and-negotiation
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Contract redlining and negotiation — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Analyze agreements to spot terms affecting your work, with suggested redlines and negotiation points.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm reviewing a vendor services agreement for our marketing automation platform. We're a Series B startup with limited budget flexibility. Create a redlined version that protects us from getting locked into something we can't get out of, ensures we keep ownership of our data and any work we pay for, and gives us flexibility to adjust or leave if things don't work out. Create a new file that is an exact copy of the contract with track changes enabled. The redlines should show deletions (strikethrough red text) and insertions (underlined colored text). Use a script to create real comments or suggestions in the margins of the doc for each edit explaining the issue. Flag anything that could bite us later.
```

## Inputs

- Google Drive integration enabled
- Extended Thinking feature (recommended)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Google Drive
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task—provide business context and contract concerns
2. Give Claude context—share contract via Google Drive integration or paste link
3. What Claude creates—generates redlined contract with tracked changes and margin comments
4. Follow up prompts—refine negotiation strategy, create comparison tables

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- No changed defined terms or citations without an explicit redline entry
- Reviewed-by-human gate before anything leaves the building
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Contract redlining and negotiation](https://claude.com/resources/use-cases/contract-redlining-and-negotiation) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
