---
name: practice-case-interviews-with-feedback
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Practice case interviews with feedback."
metadata:
  status: template — resolve every TODO before use
  category: Education
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/practice-case-interviews-with-feedback
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Practice case interviews with feedback — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Work through consulting cases with structured frameworks, guidance, and intelligent feedback

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm practicing for consulting interviews. Set up this practice scenario for me—using case I've uploaded, extract the data into an spreadsheet model with formulas and frameworks. Then, tell me what questions I should focus on.

After I finish my analysis and write my recommendation, I'll share it for feedback. Review it like a senior partner would: check my numbers, evaluate my logic, and tell me specifically what needs improvement.
```

## Inputs

- Upload practice case study files (PDF)
- Optional: Extended Thinking feature for detailed feedback
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

1. Give Claude context (upload practice study files)
2. What Claude creates (financial analysis model and practice guide)
3. Follow up prompts (compare approaches, dive deeper into frameworks, request reviews)

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

Derived from [Practice case interviews with feedback](https://claude.com/resources/use-cases/practice-case-interviews-with-feedback) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
