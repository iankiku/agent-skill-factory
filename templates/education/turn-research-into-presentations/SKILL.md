---
name: turn-research-into-presentations
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Turn research into presentations."
metadata:
  status: template — resolve every TODO before use
  category: Education
  recommended_model: Sonnet 4.5
  features: ["Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/turn-research-into-presentations
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Turn research into presentations — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Learn how to turn research into presentations that stick. Claude helps translate findings into slide outlines and speaker notes.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm uploading our group paper on sleep quality and academic performance. We have 12 minutes to present to a mixed audience of professors and students, with 4 presenters sharing the time. Analyze this research to:

- Extract the 3-4 most compelling findings that will resonate with our audience
- Create a logical narrative flow that builds from problem to insights to implications
- Design visual slides that simplify complex data without losing accuracy

Then create:

A Canva slide deck outline with clean visuals, data charts, and transitions—we'll open this in Canva to refine and add our own style

Speaker notes document with minimalist design, box structures, muted color palette, and clean sans-serif hierarchy. Add elements like a split workspace/reference column layout and use a functional modernist aesthetic so this document is easy to use while preparing.
```

## Inputs

- Research paper (PDF upload)
- Data files (if separate)
- Canva connector
- Google Drive integration (optional)
- Extended Thinking feature (optional)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Box
- Canva
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
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Turn research into presentations](https://claude.com/resources/use-cases/turn-research-into-presentations) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
