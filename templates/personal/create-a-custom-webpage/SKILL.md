---
name: create-a-custom-webpage
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create a custom webpage."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-a-custom-webpage
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create a custom webpage — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Build a portfolio site to showcase your work and learn how to deploy it live without writing a line of code.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Help me create a professional portfolio HTML page to showcase my professional career and accomplishments. I've uploaded my resume, project descriptions, and some design inspiration files. Use those to understand my background and aesthetic preferences.

For the design direction, I want something sophisticated and editorial—think high-end creative agency, not corporate template. Avoid generic layouts, AI-looking gradients, or too much symmetry. The sites I admire (in the uploads) have an organic, hand-crafted quality with unexpected details.

After you create it, walk me through publishing it live on the internet. Assume I've never deployed a website—I need exact steps that don't require any coding knowledge.
```

## Inputs

- Resume (PDF upload)
- Project descriptions (3-5 detailed examples)
- Design inspiration files
- Extended Thinking (optional)
- Netlify connector (for deployment)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Netlify
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

Derived from [Create a custom webpage](https://claude.com/resources/use-cases/create-a-custom-webpage) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
