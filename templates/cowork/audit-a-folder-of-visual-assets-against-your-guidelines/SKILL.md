---
name: audit-a-folder-of-visual-assets-against-your-guidelines
description: "In Claude Cowork, Claude Opus 4.7 can read a large folder of image exports at full resolution to spot off-brand colors, outdated logos, and missing legal copy. Use for tasks like “Audit a folder of visual assets against your guidelines” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Cowork
  recommended_model: Opus 4.7
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines
  source_title: Audit a folder of visual assets against your guidelines
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Audit a folder of visual assets against your guidelines — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

In Claude Cowork, Claude Opus 4.7 can read a large folder of image exports at full resolution to spot off-brand colors, outdated logos, and missing legal copy.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Audit every PNG and JPG in this folder against brand-meridian-2025-q2.pdf and legal-required-copy.txt. Flag: the old 2024 logo, off-brand hex codes (#0052B3 instead of #004B9F, #D4AF37 instead of #C9A961), missing or undersized legal copy. Group by violation type. For each one give me filename, issue, guideline value, asset value, and confidence. End with how many assets passed all checks.
```

## Required context and inputs

- Claude Cowork project pointed at folder containing brand guidelines PDF, legal sheet, and PNG/JPEG assets
- Opus 4.7 model selected
- Optional: Asana, Linear, or Slack connectors
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Asana
- Linear
- Slack
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

1. Describe the task (specify rules and grouping)
2. Give Claude context (point Cowork project at folder with guidelines, PDFs, legal sheets, and asset exports)
3. Claude creates the audit (reads guides and checks all assets against them)
4. Follow-up prompts (check live pages, file tasks, schedule audits)

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

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
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

Derived from [Audit a folder of visual assets against your guidelines](https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
