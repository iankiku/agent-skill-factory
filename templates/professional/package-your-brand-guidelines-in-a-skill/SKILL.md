---
name: package-your-brand-guidelines-in-a-skill
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Package your brand guidelines in a skill."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Skills"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/package-your-brand-guidelines-in-a-skill
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Package your brand guidelines in a skill — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Package your brand guidelines into a skill to create presentations, spreadsheets, or documents that automatically match your preferred style.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I want to create a skill that applies our company's brand styling to any presentation, document, or spreadsheet I create in Claude. Here's what I need to encode:

Color Palette:
Dark: #141413 (primary text, dark backgrounds)
Light: #faf9f5 (light backgrounds, text on dark)
Mid Gray: #b0aea5 (secondary elements)
Light Gray: #e8e6dc (subtle backgrounds)
Orange: #d97757 (primary accent for important elements)
Blue: #6a9bcc (secondary accent)
Green: #788c5d (tertiary accent)

Typography:
Headings (24pt and larger): Poppins font, bold weight
Body text: Lora font, regular weight
Fallbacks: Arial for headings if Poppins unavailable, Georgia for body if Lora unavailable

Application Rules:
- Apply Poppins to all slide titles and document headings
- Apply Lora to body text and paragraphs
- Use accent colors (orange, blue, green) for shapes, charts, and visual elements
- Cycle through accent colors to maintain visual interest
- Use dark color for primary text on light backgrounds
- Use light color for text on dark backgrounds

Create a complete skill with proper structure that I can use whenever I need brand-consistent presentations. Include the SKILL.md file with clear instructions for when to use it and how it applies the styling.
```

## Inputs

- Skills feature enabled
- File creation enabled
- Google Drive integration (optional)
- Extended Thinking (optional)
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
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Package your brand guidelines in a skill](https://claude.com/resources/use-cases/package-your-brand-guidelines-in-a-skill) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
