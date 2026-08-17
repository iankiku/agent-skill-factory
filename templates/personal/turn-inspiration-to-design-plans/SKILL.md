---
name: turn-inspiration-to-design-plans
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Turn inspiration into design plans."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Web Search"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/turn-inspiration-to-design-plans
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Turn inspiration into design plans — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn your saved design inspirations into a personalized cost-effective renovation plan with a balanced investment strategy.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm planning a kitchen reno and I've saved images of kitchens I love, but I'm overwhelmed by the choices. Figure out what style I'm going for and help me make smart purchase decisions about where to spend and where to invest.

Analyze my images and identify the style. Break down what defines it and how it differs from similar styles. Research materials across countertops, cabinets, flooring, backsplash, and hardware. Find 3-5 options per category at budget, mid-range, and premium levels with brands, pricing, quality ratings, and investment priorities.

Create a workbook with: Style guide—color palette with hex codes, signature materials, style distinctions, shopping strategy; Material database—all options with pricing, quality scores, investment priorities color-coded; Three packages with material selections and auto-calculating formulas; ROI sheet with financial projections, splurge-vs-save guidance color-coded, implementation timeline
```

## Inputs

- Design inspiration images (mood boards, screenshots, or photos)
- Web Search feature enabled
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

1. Give Claude context (upload inspiration images)
2. What Claude creates (delivers spreadsheet)
3. Follow-up prompts (conduct further research, adjust format, implement ideas)

TODO: rewrite as imperative steps for the executing agent.

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

Derived from [Turn inspiration into design plans](https://claude.com/resources/use-cases/turn-inspiration-to-design-plans) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
