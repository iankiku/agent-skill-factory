---
name: draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Draft a credit memo from spreads and statements with Claude for Excel."
metadata:
  status: template — resolve every TODO before use
  category: Finance
  recommended_model: Sonnet 4.6
  features: ["Connectors"]
  surface: "Cowork + Claude for Excel + Claude for Word"
  source_url: https://claude.com/resources/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Draft a credit memo from spreads and statements with Claude for Excel — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Cowork pulls the borrower's filings and spreads through the S&P Capital IQ connector and reads the underwriting workbook from your deal folder. You take the ratios and exceptions into Claude for Excel to update the model, then bring the writeup into Claude for Word for the credit memo.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Acme Manufacturing — $25M revolver renewal, committee Thursday. Walk me through the credit before I touch the spread.
```

## Inputs

- S&P Capital IQ connector enabled
- Deal folder with underwriting workbook attached
- Credit memo template
- Claude for Excel add-in installed
- Claude for Word add-in installed
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude for Excel add-in
- Claude for Word add-in
- S&P Capital IQ
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Pull three years of financials and peer spreads from S&P Capital IQ
2. Read the underwriting workbook in the deal folder and flag where ratios trip policy
3. Tell which assumptions in the model don't match what's in the statements
4. Provide a brief to take into Excel with cell references, what to change, and why

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

Derived from [Draft a credit memo from spreads and statements with Claude for Excel](https://claude.com/resources/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
