---
name: update-your-financial-model-after-earnings
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Update your financial model after earnings."
metadata:
  status: template — resolve every TODO before use
  category: Finance
  recommended_model: Opus 4.6
  features: ["Connectors", "Skills"]
  surface: "Cowork + Claude for Excel + Claude for PowerPoint"
  source_url: https://claude.com/resources/use-cases/update-your-financial-model-after-earnings
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Update your financial model after earnings — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Cowork pulls the release and transcript from S&P and checks them against your financial model. You take the flags into Claude for Excel to edit the cells, then open the deck in Claude for PowerPoint to build the page.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
ACME just jumped 8% after hours — what's driving this? I need to update my model and build a page for tomorrow's PM meeting.
```

## Inputs

- Portfolio folder with financial model attached
- S&P Global connector enabled
- Claude for Excel add-in installed
- Claude for PowerPoint add-in installed
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude for Excel add-in
- S&P Global
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Pull the earnings release and call transcript from S&P
2. Read your model in the folder and flag forecast discrepancies
3. Identify unsupported assumptions from the transcript
4. Provide a brief with cell references and recommended changes

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- All figures reconcile to source statements/workbooks; totals recomputed programmatically, not by eye
- Flag (never silently correct) discrepancies between model and source data
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Update your financial model after earnings](https://claude.com/resources/use-cases/update-your-financial-model-after-earnings) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
