---
name: see-what-your-campaign-goal-actually-requires
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: See what your campaign goal actually requires."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.6
  features: ["Custom visuals"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/see-what-your-campaign-goal-actually-requires
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# See what your campaign goal actually requires — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Type a campaign goal and Claude draws the gift pyramid inline, tiered from the lead gift down, with each tier showing how many gifts you need and how many qualified prospects that realistically takes.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
We're thinking about a $2M capital campaign. Show me what the gift pyramid needs to look like, meaning how many donors at each tier and how many qualified prospects I'd realistically need behind each one. Let me drag the goal and watch the shape change, and flag the tiers where I'm probably thin.
```

## Inputs

- No files required to start
- Optional: prospect list (XLSX) or wealth screening export for comparison against actual pipeline
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

1. Describe the task — input campaign goal number
2. Give Claude context — type numbers directly; optional prospect list upload
3. Claude creates interactive pyramid visualization with gift ranges and prospect requirements
4. Follow-up interactions (click tiers for details, redraw with constraints, create cultivation timelines)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [See what your campaign goal actually requires](https://claude.com/resources/use-cases/see-what-your-campaign-goal-actually-requires) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
