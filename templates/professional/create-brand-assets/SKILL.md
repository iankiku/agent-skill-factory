---
name: create-brand-assets
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create brand assets."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Web Search"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/Create-brand-assets
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create brand assets — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Generate professional business cards, flyers, and marketing materials that match your exact branding guidelines—ready to print or edit.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need two things for my coffee shop, Morning Ritual:

1. Business card (3.5" × 2") with:
- My contact info: 125 Hudson Street, New York, NY 10013, morningritualnyc.com
- QR code to my website (make this with rounded corners instead of blocky squares—more organic and unique)
- Print specs: 32pt cardstock, soft-touch coating, with bleeds and crop marks

2. Matching flyer (18" × 24") that I can:
- Edit in the future if needed
- Print professionally for our storefront

Match my branding guidelines document I've uploaded. Follow the typography, colors, and spacing exactly. The design should feel dawn-inspired with soft watercolor circles, paper grain, and organic dispersion with a premium, hand-crafted feel. Make sure no elements overlap or run off the page. Evaluate and grade your work to make sure all these standards are met. If there is room for improvement in your designs, iterate until you've reached success.
```

## Inputs

- Brand/style guidelines document (PDF upload)
- Extended Thinking feature (optional)
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

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Create brand assets](https://claude.com/resources/use-cases/Create-brand-assets) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
