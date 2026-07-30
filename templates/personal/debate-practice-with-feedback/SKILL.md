---
name: debate-practice-with-feedback
description: "Test your ideas against opposing views through an interactive tool where you defend your position and get real-time pushback. Use for tasks like “Debate practice with feedback” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/debate-practice-with-feedback
  source_title: Debate practice with feedback
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Debate practice with feedback — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Test your ideas against opposing views through an interactive tool where you defend your position and get real-time pushback.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I have a debate coming up and need to prepare. I want to be able to state my topic and position, then get challenged with real counterarguments and evidence so I can test my responses.

Can you create an artifact where I can practice debating any topic against the strongest possible opponent? Make it genuinely tough - I need practice against the best case for the other side, not weak strawman arguments.

The artifact's design should be offwhite with grayscale foundation with desaturated watercolor punctuation and analog fidelity through blueprint grids and paper textures. Think editorial refinement meets architectural drawing with transparency modulation, atmospheric zoning, and layered warmth.
```

## Required context and inputs

- AI-powered artifacts enabled (required)
- Extended Thinking (optional, for higher-quality output)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- No connectors detected on the source page; base Claude capabilities only
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

1. Describe the task — state debate topic and position; request interactive simulator with strong counterarguments and feedback
2. Give Claude context — enable AI-powered artifacts in Settings under Capabilities; optionally enable Extended Thinking
3. What Claude creates — interactive practice simulator analyzing opposing arguments and evaluating responses in real-time
4. Follow-up prompts — analyze weaknesses, create response cards, handle rhetorical tactics

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

Derived from [Debate practice with feedback](https://claude.com/resources/use-cases/debate-practice-with-feedback) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
