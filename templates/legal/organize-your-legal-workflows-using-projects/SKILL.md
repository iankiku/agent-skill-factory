---
name: organize-your-legal-workflows-using-projects
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Organize your legal workflows using Projects."
metadata:
  status: template — resolve every TODO before use
  category: Legal
  recommended_model: Opus 4.5
  features: ["Projects"]
  surface: "Claude.ai chat (Claude Projects)"
  source_url: https://claude.com/resources/use-cases/organize-your-legal-workflows-using-projects
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Organize your legal workflows using Projects — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Stop explaining your review standards for every contract. Claude Projects let you upload your playbooks once and reference them automatically across hundreds of reviews.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm setting up a Project for NDA reviews at our firm. We handle about 30 NDAs a week and I want Claude to reference our standard terms, flag deviations, and maintain consistency in our review comments.

I've uploaded our NDA playbook, our standard mutual NDA template, and our list of unacceptable terms. Analyze these documents and create an NDA Review Standards Guide that captures our voice, tone, and structure we use throughout our writing. Make this a professional reference document I can upload to the Project knowledge, so Claude can reference it during every review.

Then help me craft optimized project instructions I can paste into the custom instructions field—instructions that tell Claude to reference the standards guide and apply our approach.
```

## Inputs

- Upload core reference materials (review playbook, standard template, prohibited terms list)
- Google Drive, Microsoft 365, Notion, or Box connectors (optional)
- Extended Thinking for complex analysis (optional)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Box
- Google Drive
- Microsoft 365
- Notion
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

Derived from [Organize your legal workflows using Projects](https://claude.com/resources/use-cases/organize-your-legal-workflows-using-projects) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
