---
name: create-digital-recipe-cards
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create digital recipe cards."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-digital-recipe-cards
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create digital recipe cards — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn handwritten family recipes into digitally formatted recipes to save and share.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Read this recipe and turn it into something I can share with family. Decode the handwriting, convert vague measurements into precise amounts, and write clear steps. Create an interactive recipe artifact (for digital sharing). Include:
- A serving size adjuster that dynamically scales ingredient amounts
- A small, elegantly integrated "Explore the Tradition" box with buttons that fetch cultural facts when clicked
- The original handwritten recipe displayed at the end in a museum-quality frame.
```

## Inputs

- Upload recipe image (JPEG or other supported format)
- Extended Thinking (optional, for higher-quality output)
- Optional: Web Search or Research features for learning more about recipes
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Box
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (analyze images, extract text, create digital cards)
2. Give Claude context (upload recipe photo/file via file browser or drag-and-drop)
3. What Claude creates (delivers interactive recipe artifact with serving adjuster and insights)
4. Follow up prompts (request culinary deep-dives, create shopping lists, build recipe collections)
5. Tricks, tips, and troubleshooting (enable Web Search/Research, elevate visual quality, batch format multiple recipes, vary output formats)

TODO: rewrite as imperative steps for the executing agent.

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

Derived from [Create digital recipe cards](https://claude.com/resources/use-cases/create-digital-recipe-cards) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
