---
name: reconcile-transactions-across-your-accounts
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Reconcile transactions across your accounts."
metadata:
  status: template — resolve every TODO before use
  category: Finance
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/reconcile-transactions-across-your-accounts
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Reconcile transactions across your accounts — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Hand Cowork your bank exports and ledger files. It matches transactions across sources, flags discrepancies, and outputs an annotated reconciliation report.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need to reconcile my January 2024 bank statement. I've uploaded my checking account statement export and my current chart of accounts. Can you analyze the transactions, match them to the right accounts, and flag anything that doesn't line up? If there are discrepancies, I'd love journal entries to fix them.
```

## Inputs

- Claude Desktop app
- Cowork feature
- Bank statement export file
- Chart of accounts file
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

1. Download Claude Desktop and start a Cowork session
2. Select "Work in a folder" to give Cowork access to financial files, or use the "+" button to add individual files
3. Claude analyzes both files, matches transactions to accounts, and surfaces discrepancies
4. Review matching results (percentages matched, items needing categorization, discrepancies identified)
5. Export journal entries as CSV or create reconciliation summaries as needed

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

- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Reconcile transactions across your accounts](https://claude.com/resources/use-cases/reconcile-transactions-across-your-accounts) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
