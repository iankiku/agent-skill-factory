---
name: stress-test-your-financial-plan-across-scenarios
description: "Claude Opus 4.6 tests a financial plan against a full range of possible outcomes, traces how each risk cascades through the rest, and builds a working model you can adjust yourself. Use for tasks like “Stress-test your financial plan across scenarios” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Personal
  recommended_model: Opus 4.6
  features: ["Extended Thinking"]
  surface: "Claude.ai chat (primary), with Claude Desktop/Cowork for folder-based file access and Claude in Excel for follow-up work"
  source_url: https://claude.com/resources/use-cases/stress-test-your-financial-plan-across-scenarios
  source_title: Stress-test your financial plan across scenarios
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Stress-test your financial plan across scenarios — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Claude Opus 4.6 tests a financial plan against a full range of possible outcomes, traces how each risk cascades through the rest, and builds a working model you can adjust yourself.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm 52, hoping to retire at 62. My partner and I have about $1.2M across a 401(k), Roth IRA, and taxable brokerage. I make $185K, he makes $95K, we spend about $8,500/month. Mortgage is paid off in 2031. Not sure if we should be doing Roth conversions now while we're in a lower bracket. I've uploaded our tax returns, investment statements, Social Security estimates, and budget. Where does this plan break and what are the highest-leverage moves?
```

## Required context and inputs

- Tax returns
- Investment account statements
- Social Security benefit estimates
- Monthly expense breakdown
- Extended Thinking feature enabled (optional)
- Claude Desktop with Cowork for folder-based file access (optional)
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
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
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

Derived from [Stress-test your financial plan across scenarios](https://claude.com/resources/use-cases/stress-test-your-financial-plan-across-scenarios) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
