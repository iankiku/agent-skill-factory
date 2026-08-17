---
name: prep-scattered-documents-for-a-compliance-audit
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Prep scattered documents for a compliance audit."
metadata:
  status: template — resolve every TODO before use
  category: Legal
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/prep-scattered-documents-for-a-compliance-audit
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Prep scattered documents for a compliance audit — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn a folder of scattered policy documents, contracts, and records into an organized, clearly named collection ready for regulatory review.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I have 100+ documents for our upcoming SOC 2 audit in this folder. Right now they're scattered with names like "policy_v2_final.docx" and "scan0042.pdf". I need to organize them before the auditors arrive:

- Rename files with clear titles showing document type, effective date, and which control area they cover
- Group by control category (Access Control, Change Management, Incident Response, etc.)
- Flag any control areas where we seem to have gaps in documentation

Our audit scope covers security, availability, and confidentiality. The audit period is January through December 2024.
```

## Inputs

- Claude Desktop
- Cowork feature
- Audit documents folder
- Control framework or audit checklist (optional)
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
2. Select "Work in a folder" and choose the folder containing audit documents
3. Include audit scope or control framework so Cowork categorizes documents
4. Claude reviews all documents, produces rename mapping organized by control area, identifies coverage, and flags gaps

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

- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Prep scattered documents for a compliance audit](https://claude.com/resources/use-cases/prep-scattered-documents-for-a-compliance-audit) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
