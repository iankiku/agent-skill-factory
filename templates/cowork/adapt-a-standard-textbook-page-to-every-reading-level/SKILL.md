---
name: adapt-a-standard-textbook-page-to-every-reading-level
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Adapt a standard textbook page to every reading level."
metadata:
  status: template — resolve every TODO before use
  category: Cowork
  recommended_model: Opus 4.7
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Adapt a standard textbook page to every reading level — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Opus 4.7 reads a single source page in detail and returns a finished file for each audience that needs it.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
From the textbook spread, build me: 1) One slide deck (8–10 slides) covering the core ideas, with the diagram redrawn simply on its own slide 2) Three versions of a one-page reading handout — Level A, B, C — same concepts, different vocabulary and sentence length 3) A short exit-ticket worksheet (3 questions) that checks the standard, same questions for everyone
```

## Inputs

- Textbook page (photo, scan, or PDF)
- Learning standards/objectives document
- Class roster with reading-level groupings (optional)
- Claude Project with standards/rules (optional)
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

1. Describe the task (attach page, standards, rules for each version)
2. Give Claude context (upload photo/scan, standards/objectives, version rules)
3. Claude creates the materials (slide deck, handouts, exit ticket)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Adapt a standard textbook page to every reading level](https://claude.com/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
