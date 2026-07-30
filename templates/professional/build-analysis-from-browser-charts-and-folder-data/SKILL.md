---
name: build-analysis-from-browser-charts-and-folder-data
description: "Pull your quarterly revenue from scattered board decks, then grab GDP and inflation data from FRED. Cowork creates a comparison chart showing how your growth stacks up against the macro environment. Use for tasks like “Build analysis from browser charts and folder data” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork (with Claude in Chrome)"
  source_url: https://claude.com/resources/use-cases/build-analysis-from-browser-charts-and-folder-data
  source_title: Build analysis from browser charts and folder data
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Build analysis from browser charts and folder data — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Pull your quarterly revenue from scattered board decks, then grab GDP and inflation data from FRED. Cowork creates a comparison chart showing how your growth stacks up against the macro environment.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm preparing for our board meeting and need to show how our growth compares to the broader economy. Pull our revenue figures Q1-Q4 2025 board decks. Using Claude in Chrome to open FRED in my browser and grab GDP growth and inflation for the same quarters. Create a chart comparing our revenue growth to these economic indicators. Save the chart and a summary to my desktop folder.
```

## Required context and inputs

- Claude Desktop
- Cowork feature
- Claude in Chrome extension
- PowerPoint board decks in a folder
- Access to FRED website
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Claude in Chrome extension
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
2. Select "Work in a folder" and choose folder containing PowerPoint files
3. Install Claude in Chrome and add it as a connector to pull live data from FRED
4. Claude extracts revenue data and pulls economic indicators, producing comparison charts and analysis
5. Files save directly to your working folder

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

Derived from [Build analysis from browser charts and folder data](https://claude.com/resources/use-cases/build-analysis-from-browser-charts-and-folder-data) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
