---
name: create-a-sales-proposal-presentation
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create a sales proposal presentation."
metadata:
  status: template — resolve every TODO before use
  category: Sales
  recommended_model: Opus 4.5
  features: ["Extended Thinking", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-a-sales-proposal-presentation
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create a sales proposal presentation — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Create a polished client proposal deck with professional layouts data visualizations and cohesive design—then refine through feedback until it matches your standards.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm putting together a proposal deck for Midwest Regional Health, a healthcare network we've been in conversations with about our patient engagement platform.

Search my Google Drive for documents with "Midwest Regional" in the title—there should be discovery call notes, their RFP, and a competitive analysis we did.

Pull the relevant information to build out these slides: Make sure to include executive summary, their challenges, our solution and how it addresses their specific situation, implementation approach, pricing, case study (find a similar healthcare client we can reference), timeline and next steps.

Design direction: Clean and professional, but not sterile. I want something modern and approachable while still appropriate for hospital executives. Use premium typography (not default fonts) and our brand colors from the logo I'm uploading. Make sure text is conservatively sized so nothing gets cut off, and verify that no elements overlap.
```

## Inputs

- Google Drive integration enabled
- Company logo upload
- Extended Thinking feature enabled (optional but recommended)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

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
- CRM writes are drafted for approval, never auto-committed
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Create a sales proposal presentation](https://claude.com/resources/use-cases/create-a-sales-proposal-presentation) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
