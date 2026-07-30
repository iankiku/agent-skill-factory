---
name: create-digital-recipe-cards
description: "Turn handwritten family recipes into digitally formatted recipes to save and share. Use for tasks like “Create digital recipe cards” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-digital-recipe-cards
  source_title: Create digital recipe cards
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create digital recipe cards — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Turn handwritten family recipes into digitally formatted recipes to save and share.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Read this recipe and turn it into something I can share with family. Decode the handwriting, convert vague measurements into precise amounts, and write clear steps. Create an interactive recipe artifact (for digital sharing). Include:
- A serving size adjuster that dynamically scales ingredient amounts
- A small, elegantly integrated "Explore the Tradition" box with buttons that fetch cultural facts when clicked
- The original handwritten recipe displayed at the end in a museum-quality frame.
```

## Required context and inputs

- Upload recipe image (JPEG or other supported format)
- Extended Thinking (optional, for higher-quality output)
- Optional: Web Search or Research features for learning more about recipes
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Box
- TODO: confirm which connectors are enabled in the runtime that will execute this skill
- Authentication: connectors authenticate via their own OAuth flows — this skill must
  NEVER ask for, store, or echo credentials, tokens, or API keys. If auth is missing,
  stop and tell the user which connector to enable.

## Permissions and sensitive actions

- Reads: TODO (folders, channels, records this skill may read)
- Writes: TODO (what it may create/modify, and where)
- Held back for the primary agent / human: sending external communications, financial
  transactions, deleting or overwriting originals, submitting web forms

## Workflow

1. Describe the task (analyze images, extract text, create digital cards)
2. Give Claude context (upload recipe photo/file via file browser or drag-and-drop)
3. What Claude creates (delivers interactive recipe artifact with serving adjuster and insights)
4. Follow up prompts (request culinary deep-dives, create shopping lists, build recipe collections)
5. Tricks, tips, and troubleshooting (enable Web Search/Research, elevate visual quality, batch format multiple recipes, vary output formats)

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Apply the repo's delegation policy (`docs/delegation-policy.md` — bundle or restate
it if you install this skill outside the repo). Defaults for this template:

- Run single-agent unless a step fans out over independent items (files, records,
  vendors, channels). Only independent work parallelizes.
- Each delegated task must ship with: the minimal context slice it needs, an explicit
  output contract, a validation check the primary agent runs on the result, and a
  fallback if it returns empty or fails.
- Final review, synthesis, and every sensitive action listed above stay with the
  primary agent.
- TODO: name the concrete subtasks (if any) that qualify for delegation here.

## Attribution

Derived from [Create digital recipe cards](https://claude.com/resources/use-cases/create-digital-recipe-cards) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
