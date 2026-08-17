---
name: audit-a-folder-of-visual-assets-against-your-guidelines
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Audit a folder of visual assets against your guidelines."
metadata:
  status: template — resolve every TODO before use
  category: Cowork
  recommended_model: Opus 4.7
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Audit a folder of visual assets against your guidelines — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

In Claude Cowork, Claude Opus 4.7 can read a large folder of image exports at full resolution to spot off-brand colors, outdated logos, and missing legal copy.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Audit every PNG and JPG in this folder against brand-meridian-2025-q2.pdf and legal-required-copy.txt. Flag: the old 2024 logo, off-brand hex codes (#0052B3 instead of #004B9F, #D4AF37 instead of #C9A961), missing or undersized legal copy. Group by violation type. For each one give me filename, issue, guideline value, asset value, and confidence. End with how many assets passed all checks.
```

## Inputs

- Claude Cowork project pointed at folder containing brand guidelines PDF, legal sheet, and PNG/JPEG assets
- Opus 4.7 model selected
- Optional: Asana, Linear, or Slack connectors
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Asana
- Linear
- Slack
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (specify rules and grouping)
2. Give Claude context (point Cowork project at folder with guidelines, PDFs, legal sheets, and asset exports)
3. Claude creates the audit (reads guides and checks all assets against them)
4. Follow-up prompts (check live pages, file tasks, schedule audits)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
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

Derived from [Audit a folder of visual assets against your guidelines](https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
