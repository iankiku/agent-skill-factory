---
name: debate-practice-with-feedback
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Debate practice with feedback."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/debate-practice-with-feedback
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Debate practice with feedback — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Test your ideas against opposing views through an interactive tool where you defend your position and get real-time pushback.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I have a debate coming up and need to prepare. I want to be able to state my topic and position, then get challenged with real counterarguments and evidence so I can test my responses.

Can you create an artifact where I can practice debating any topic against the strongest possible opponent? Make it genuinely tough - I need practice against the best case for the other side, not weak strawman arguments.

The artifact's design should be offwhite with grayscale foundation with desaturated watercolor punctuation and analog fidelity through blueprint grids and paper textures. Think editorial refinement meets architectural drawing with transparency modulation, atmospheric zoning, and layered warmth.
```

## Inputs

- AI-powered artifacts enabled (required)
- Extended Thinking (optional, for higher-quality output)
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

1. Describe the task — state debate topic and position; request interactive simulator with strong counterarguments and feedback
2. Give Claude context — enable AI-powered artifacts in Settings under Capabilities; optionally enable Extended Thinking
3. What Claude creates — interactive practice simulator analyzing opposing arguments and evaluating responses in real-time
4. Follow-up prompts — analyze weaknesses, create response cards, handle rhetorical tactics

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

Derived from [Debate practice with feedback](https://claude.com/resources/use-cases/debate-practice-with-feedback) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
