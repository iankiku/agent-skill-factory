---
name: build-interactive-diagram-tools
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Build interactive diagram tools."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Opus 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/build-interactive-diagram-tools
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Build interactive diagram tools — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

From body systems to molecular structures, turn a detailed prompt into a working reference app with the depth and design you specify.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Build an interactive anatomy explorer using @ebi-gene-expression-group/anatomogram from npm. Use homo_sapiens.male.svg and homo_sapiens.brain.svg. Don't generate diagrams yourself—these SVGs contain accurate illustrations with UBERON ontology IDs already embedded. Embed the SVGs directly into the HTML—no fetch requests needed.

Critical: The SVGs style all elements with fill:none;stroke:none by default, making them invisible. After loading, apply default fills and strokes before any other styling. Also set cleanupIds: false when optimizing (the UBERON IDs are how you target elements) and remove the visibility:hidden attribute in JavaScript.

Design requirements: Restrained and sophisticated. No glows, no emojis, no neon. Warm colors over cold. Serif headings, sans-serif body, monospace for data. Think premium medical reference, not generic AI output.

Add tabbed information panels, physical-feeling sound feedback, and content rich enough to actually learn from. Build to flagship quality from the start—I'll iterate until this is exceptional.
```

## Inputs

- File creation enabled in settings
- Extended Thinking (optional, for complex apps)
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

1. Describe the task (what to learn, how to interact, data sources, aesthetic standards)
2. Give Claude context (enable file creation; optionally enable Extended Thinking)
3. Claude creates a fully functional React application

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Build interactive diagram tools](https://claude.com/resources/use-cases/build-interactive-diagram-tools) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
