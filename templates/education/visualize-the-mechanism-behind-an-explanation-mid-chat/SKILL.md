---
name: visualize-the-mechanism-behind-an-explanation-mid-chat
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Visualize the mechanism behind an explanation mid-chat."
metadata:
  status: template — resolve every TODO before use
  category: Education
  recommended_model: Sonnet 4.6
  features: ["Custom visuals"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/visualize-the-mechanism-behind-an-explanation-mid-chat
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Visualize the mechanism behind an explanation mid-chat — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude builds an interactive visual inline as you talk through the problem — shaped to the specific question you're asking, with controls you manipulate and buttons that drill deeper. Useful when a concept has moving parts text can't show.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm learning orbital mechanics and I understand that the planet speeds up when it's close to the sun and slows down when it's far. But I don't understand *why* that trade-off exists. Why can't it just go fast the whole time? Help me understand with a well crafted, interactive, dynamic visualization.
```

## Inputs

- No files required to upload
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

1. Describe the task — Claude builds a visual as part of its answer (diagram, chart, interactive element)
2. Give Claude context — state what you already know; name what isn't clicking
3. Claude creates — builds linked views with interactive controls (sliders)
4. Follow up prompts — click buttons in the visual for deeper exploration; ask Claude to redraw with changes; request a quiz format

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

Derived from [Visualize the mechanism behind an explanation mid-chat](https://claude.com/resources/use-cases/visualize-the-mechanism-behind-an-explanation-mid-chat) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
