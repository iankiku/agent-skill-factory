---
name: adapt-a-standard-textbook-page-to-every-reading-level
description: "Opus 4.7 reads a single source page in detail and returns a finished file for each audience that needs it. Use for tasks like “Adapt a standard textbook page to every reading level” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Cowork
  recommended_model: Opus 4.7
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level
  source_title: Adapt a standard textbook page to every reading level
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Adapt a standard textbook page to every reading level — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Opus 4.7 reads a single source page in detail and returns a finished file for each audience that needs it.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
From the textbook spread, build me: 1) One slide deck (8–10 slides) covering the core ideas, with the diagram redrawn simply on its own slide 2) Three versions of a one-page reading handout — Level A, B, C — same concepts, different vocabulary and sentence length 3) A short exit-ticket worksheet (3 questions) that checks the standard, same questions for everyone
```

## Required context and inputs

- Textbook page (photo, scan, or PDF)
- Learning standards/objectives document
- Class roster with reading-level groupings (optional)
- Claude Project with standards/rules (optional)
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

1. Describe the task (attach page, standards, rules for each version)
2. Give Claude context (upload photo/scan, standards/objectives, version rules)
3. Claude creates the materials (slide deck, handouts, exit ticket)
4. Follow up with refinement prompts

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

Derived from [Adapt a standard textbook page to every reading level](https://claude.com/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
