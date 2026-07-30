---
name: prep-scattered-documents-for-a-compliance-audit
description: "Turn a folder of scattered policy documents, contracts, and records into an organized, clearly named collection ready for regulatory review. Use for tasks like “Prep scattered documents for a compliance audit” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Legal
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/prep-scattered-documents-for-a-compliance-audit
  source_title: Prep scattered documents for a compliance audit
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Prep scattered documents for a compliance audit — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Turn a folder of scattered policy documents, contracts, and records into an organized, clearly named collection ready for regulatory review.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I have 100+ documents for our upcoming SOC 2 audit in this folder. Right now they're scattered with names like "policy_v2_final.docx" and "scan0042.pdf". I need to organize them before the auditors arrive:

- Rename files with clear titles showing document type, effective date, and which control area they cover
- Group by control category (Access Control, Change Management, Incident Response, etc.)
- Flag any control areas where we seem to have gaps in documentation

Our audit scope covers security, availability, and confidentiality. The audit period is January through December 2024.
```

## Required context and inputs

- Claude Desktop
- Cowork feature
- Audit documents folder
- Control framework or audit checklist (optional)
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

1. Download Claude Desktop and start a Cowork session
2. Select "Work in a folder" and choose the folder containing audit documents
3. Include audit scope or control framework so Cowork categorizes documents
4. Claude reviews all documents, produces rename mapping organized by control area, identifies coverage, and flags gaps

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- No changed defined terms or citations without an explicit redline entry
- Reviewed-by-human gate before anything leaves the building
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

Derived from [Prep scattered documents for a compliance audit](https://claude.com/resources/use-cases/prep-scattered-documents-for-a-compliance-audit) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
