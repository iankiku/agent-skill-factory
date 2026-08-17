---
name: bring-your-whiteboard-lesson-to-life
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Bring your whiteboard lesson to life."
metadata:
  status: template — resolve every TODO before use
  category: Education
  recommended_model: Sonnet 4.6
  features: ["Custom visuals"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/bring-your-whiteboard-lesson-to-life
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Bring your whiteboard lesson to life — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Work through how to teach a concept with Claude sketching alongside. The visual streams in as part of the back-and-forth — a thinking tool for your prep first, and a teaching tool if you take it further.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm prepping to teach supply and demand equilibrium next week. Here's the sketch I've been using — students tend to follow the crossing but not *why* the price goes there. What's a better way to frame it? And is there a way to show them the pressure toward equilibrium, not just the intersection?
```

## Inputs

- A photo of your whiteboard, a slide, or a description of what you've been drawing
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

1. Describe the task (work out teaching approach and explain where students struggle)
2. Give Claude context (attach sketch, slide, or description; optionally note student sticking points)
3. Claude creates an interactive response with diagnosis, reframing, and visual
4. Follow up with refinements through additional prompts

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

Derived from [Bring your whiteboard lesson to life](https://claude.com/resources/use-cases/bring-your-whiteboard-lesson-to-life) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
