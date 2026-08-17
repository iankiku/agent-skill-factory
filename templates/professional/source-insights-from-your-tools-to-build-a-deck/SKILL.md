---
name: source-insights-from-your-tools-to-build-a-deck
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Source insights from your tools to build a deck."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Opus 4.6
  features: ["Extended Thinking", "Browser Use"]
  surface: "Cowork (Claude Desktop), with optional Claude in Chrome and connectors"
  source_url: https://claude.com/resources/use-cases/source-insights-from-your-tools-to-build-a-deck
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Source insights from your tools to build a deck — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude Opus 4.6 chases leads across scattered sources, surfaces what no single source shows on its own, and builds a presentation around the through-line.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm prepping for board meeting Friday. Q3 was the quarter where everything happened at once: we shipped the platform consolidation, closed the Apex partnership, and lost two enterprise accounts.

Start with the Q3 project tracker in my local files — it has the key people, channels, and documents. Follow each person across their channels, emails, and documents they reference. When you find data, check it against other sources — the revenue numbers probably don't agree. Figure out which is current.

The board needs to understand whether the consolidation bet is paying off despite the churn. Create a PowerPoint deck (12–15 slides) with speaker notes, an Excel data appendix, and a two-page Word brief. Make an argument, not a summary.
```

## Inputs

- Cowork with local file access (supported formats required)
- Connected source: Slack, Gmail, or Google Suite
- Extended Thinking enabled
- Claude in Chrome (optional)
- Previous quarter's deck (optional)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude in Chrome extension
- Gmail
- Slack
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms, and ANY click that finalizes state on a third-party site (browser-use skill: show a review step first)

## Workflow

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Page fails to load or selector drifts → retry once, then stop and report; never guess at form fields
- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Source insights from your tools to build a deck](https://claude.com/resources/use-cases/source-insights-from-your-tools-to-build-a-deck) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
