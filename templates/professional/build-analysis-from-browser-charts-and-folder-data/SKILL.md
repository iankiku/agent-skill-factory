---
name: build-analysis-from-browser-charts-and-folder-data
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Build analysis from browser charts and folder data."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork (with Claude in Chrome)"
  source_url: https://claude.com/resources/use-cases/build-analysis-from-browser-charts-and-folder-data
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Build analysis from browser charts and folder data — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Pull your quarterly revenue from scattered board decks, then grab GDP and inflation data from FRED. Cowork creates a comparison chart showing how your growth stacks up against the macro environment.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm preparing for our board meeting and need to show how our growth compares to the broader economy. Pull our revenue figures Q1-Q4 2025 board decks. Using Claude in Chrome to open FRED in my browser and grab GDP growth and inflation for the same quarters. Create a chart comparing our revenue growth to these economic indicators. Save the chart and a summary to my desktop folder.
```

## Inputs

- Claude Desktop
- Cowork feature
- Claude in Chrome extension
- PowerPoint board decks in a folder
- Access to FRED website
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude in Chrome extension
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Download Claude Desktop and start a Cowork session
2. Select "Work in a folder" and choose folder containing PowerPoint files
3. Install Claude in Chrome and add it as a connector to pull live data from FRED
4. Claude extracts revenue data and pulls economic indicators, producing comparison charts and analysis
5. Files save directly to your working folder

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

Derived from [Build analysis from browser charts and folder data](https://claude.com/resources/use-cases/build-analysis-from-browser-charts-and-folder-data) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
