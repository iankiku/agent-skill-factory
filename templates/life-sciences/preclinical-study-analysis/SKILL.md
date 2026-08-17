---
name: preclinical-study-analysis
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Preclinical study analysis."
metadata:
  status: template — resolve every TODO before use
  category: Life Sciences
  recommended_model: Sonnet 4.5
  features: ["Connectors"]
  surface: "Claude for Desktop (via connectors)"
  source_url: https://claude.com/resources/use-cases/preclinical-study-analysis
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Preclinical study analysis — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Build study reports by connecting to research platforms and compiling data across experiments.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Summarize the study designs for ST042 and ST043 and how they're different, including a table indicating key differences. Link all my notebook entries and sources.
```

## Inputs

- Benchling connector (required)
- Claude for Desktop (required to pull data from Benchling workspace)
- Access to electronic lab notebooks, experimental protocols, and study data
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Benchling
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task: tell Claude what studies to compare and what to understand about them
2. Give Claude context: connect Claude to research data management systems like Benchling
3. What Claude creates: retrieves study data and synthesizes comprehensive summaries with key differences
4. Follow-up prompts: continue conversation to refine, expand, or explore further (example: 'generate a Study Report that I can include in my regulatory submission')

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Methods/statistics restated only from the source material; no invented p-values
- Units and sample sizes double-checked against source tables
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Preclinical study analysis](https://claude.com/resources/use-cases/preclinical-study-analysis) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
