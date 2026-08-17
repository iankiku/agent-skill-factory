---
name: validate-reserves-and-draft-filing-narrative-with-claude-for-excel
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Validate reserves and draft filing narrative with Claude for Excel."
metadata:
  status: template — resolve every TODO before use
  category: Finance
  recommended_model: Sonnet 4.6
  features: ["Connectors"]
  surface: "Cowork + Claude for Excel + Claude for Word"
  source_url: https://claude.com/resources/use-cases/validate-reserves-and-draft-filing-narrative-with-claude-for-excel
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Validate reserves and draft filing narrative with Claude for Excel — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Cowork reads your reserve workbook from the valuation folder and pulls prior filings and bulletins through the NAIC connector. You take the formula flags and reserve walk into Claude for Excel to clean the workbook, then bring the narrative into Claude for Word for the filing memo.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Q1 reserve review for Personal Auto BI — appointed actuary review next week, filing due in two. Walk me through the workbook before I lock the numbers.
```

## Inputs

- Valuation folder with reserve workbook attached
- NAIC connector enabled
- Claude for Excel add-in installed
- Claude for Word add-in installed
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude for Excel add-in
- Claude for Word add-in
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Read the reserve workbook in the valuation folder and validate the formulas
2. Pull the FY24 filing and any new bulletins from NAIC
3. Flag development factors and tail assumptions that look off vs. prior
4. Give a brief for Excel with sheet references, what's broken, and what's just a movement to explain

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

Derived from [Validate reserves and draft filing narrative with Claude for Excel](https://claude.com/resources/use-cases/validate-reserves-and-draft-filing-narrative-with-claude-for-excel) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
