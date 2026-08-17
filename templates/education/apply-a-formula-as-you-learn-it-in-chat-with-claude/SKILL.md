---
name: apply-a-formula-as-you-learn-it-in-chat-with-claude
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Apply a formula as you learn it."
metadata:
  status: template — resolve every TODO before use
  category: Education
  recommended_model: Sonnet 4.6
  features: ["Custom visuals"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/apply-a-formula-as-you-learn-it-in-chat-with-claude
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Apply a formula as you learn it — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude builds a blank scatter right in the conversation — you place the points, drag them, watch what happens to the fit.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm learning linear regression and I can do the formula but I don't get it. Can you give me something where I can mess with the data points myself and watch what happens to the line? I want to actually feel why one weird point can throw the whole thing off. Can you help me visualize?
```

## Inputs

- No files required
- Optional: problem sets or lecture slides for context
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Linear
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (express the gap between computing and understanding)
2. Give Claude context (optional lecture materials for connection to coursework)
3. Claude creates an interactive canvas for manipulation
4. Follow up with refinement prompts (request math explanations, overlay comparisons, or prediction tests)

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

Derived from [Apply a formula as you learn it](https://claude.com/resources/use-cases/apply-a-formula-as-you-learn-it-in-chat-with-claude) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
