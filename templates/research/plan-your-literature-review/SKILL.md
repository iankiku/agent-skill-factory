---
name: plan-your-literature-review
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Plan your literature review."
metadata:
  status: template — resolve every TODO before use
  category: Research
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/plan-your-literature-review
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Plan your literature review — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

With Claude as your research assistant, find relevant research, prioritize what to read, and organize evidence as you work through papers.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm beginning a literature review on the gut-brain axis and its role in mood disorders, specifically depression and anxiety. I need to understand:

- Mechanisms linking gut microbiome changes to mood regulation
- Evidence for probiotic interventions in clinical trials
- The role of inflammation and neurotransmitter production

Search PubMed for the most relevant papers from the last 5 years and create a structured reading guide that helps me prioritize what to read first.

Organize everything into a beautifully designed Word document that serves as my research roadmap—something that feels like a premium research tool with clear visual hierarchy, color-coding by study type, and space for my notes as I work through the papers.
```

## Inputs

- PubMed connector (required)
- Optional: Extended Thinking enabled
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- PubMed
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Give Claude context (connect tools, enable features)
2. What Claude creates (output)
3. Follow up prompts (validation, contradiction investigation, gap searching)

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

Derived from [Plan your literature review](https://claude.com/resources/use-cases/plan-your-literature-review) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
