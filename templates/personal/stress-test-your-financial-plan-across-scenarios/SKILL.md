---
name: stress-test-your-financial-plan-across-scenarios
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Stress-test your financial plan across scenarios."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Opus 4.6
  features: ["Extended Thinking"]
  surface: "Claude.ai chat (primary), with Claude Desktop/Cowork for folder-based file access and Claude in Excel for follow-up work"
  source_url: https://claude.com/resources/use-cases/stress-test-your-financial-plan-across-scenarios
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Stress-test your financial plan across scenarios — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude Opus 4.6 tests a financial plan against a full range of possible outcomes, traces how each risk cascades through the rest, and builds a working model you can adjust yourself.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm 52, hoping to retire at 62. My partner and I have about $1.2M across a 401(k), Roth IRA, and taxable brokerage. I make $185K, he makes $95K, we spend about $8,500/month. Mortgage is paid off in 2031. Not sure if we should be doing Roth conversions now while we're in a lower bracket. I've uploaded our tax returns, investment statements, Social Security estimates, and budget. Where does this plan break and what are the highest-leverage moves?
```

## Inputs

- Tax returns
- Investment account statements
- Social Security benefit estimates
- Monthly expense breakdown
- Extended Thinking feature enabled (optional)
- Claude Desktop with Cowork for folder-based file access (optional)
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

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Stress-test your financial plan across scenarios](https://claude.com/resources/use-cases/stress-test-your-financial-plan-across-scenarios) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
