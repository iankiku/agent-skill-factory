---
name: plan-your-syllabus-see-which-weeks-are-locked
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Plan your syllabus."
metadata:
  status: template — resolve every TODO before use
  category: Education
  recommended_model: Sonnet 4.6
  features: ["Custom visuals"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/plan-your-syllabus-see-which-weeks-are-locked
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Plan your syllabus — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Attach your syllabus and Claude shows which weeks are locked by real prerequisites and which you're free to rearrange — right in chat as you work through the order.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm building a 15-week Intro to Macro syllabus and I keep second-guessing the order. Can you map out which topics actually depend on which — like, what do they need to get first before the later stuff makes sense? I want to see where I have flexibility and where the sequence is locked. If I click a topic, tell me if there's another common way to order it.
```

## Inputs

- Syllabus (PDF or document)
- Optional: Google Drive integration
- Optional: Projects for semester-to-semester refinement
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

1. Describe the task (identify topics with dependencies vs. flexible ordering)
2. Give Claude context (attach working syllabus; optionally specify textbook)
3. Claude creates visual output (dependency graph with locked/flexible tags)
4. Follow-up prompts (request reorderings; generate revised syllabus)
5. Tips and troubleshooting (phrasing matters; validate against course knowledge)

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

Derived from [Plan your syllabus](https://claude.com/resources/use-cases/plan-your-syllabus-see-which-weeks-are-locked) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
