---
name: track-discovery-timelines-and-analyze-patterns
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Track discovery timelines and analyze patterns."
metadata:
  status: template — resolve every TODO before use
  category: Legal
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/track-discovery-timelines-and-analyze-patterns
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Track discovery timelines and analyze patterns — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Build chronologies and identify document patterns across large discovery productions.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm representing a small software company in a contract dispute with a vendor. We hired them to build a custom inventory management system, but the project failed and we're in litigation. I've got about 40 discovery documents—contracts, change orders, email threads, project status reports, invoices, and technical documentation from the 12-month project timeline. Create a chronological timeline with document citations, analyze patterns around scope changes and deliverables, and identify our strongest evidence and key witnesses for depositions. Generate a professional legal memo with clear sections, proper citations to source documents, and formatting suitable for sharing with co-counsel. This needs to be a top of class legal document with exceptional formatting and structure. Opt for elevated, elegant typography, tight spacing, and muted color instead of using your default styling. Take your time developing an extremely high quality legal document that has coherent structure, and articulate legal expertise throughout.
```

## Inputs

- Gmail and Google Drive integrations enabled
- PDF, Word files, Excel spreadsheets, or email uploads
- Optional: Extended Thinking (recommended)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Gmail
- Google Drive
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- No changed defined terms or citations without an explicit redline entry
- Reviewed-by-human gate before anything leaves the building
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Track discovery timelines and analyze patterns](https://claude.com/resources/use-cases/track-discovery-timelines-and-analyze-patterns) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
