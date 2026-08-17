---
name: workflow-improvement-planner
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Workflow improvement planner."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/workflow-improvement-planner
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Workflow improvement planner — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn process pain points into structured improvement plans. Claude helps nonprofits define workflow challenges and design AI-powered solutions that save time and increase capacity.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need help defining a workflow improvement opportunity at my nonprofit. Can you create a detailed artifact that asks me questions to capture all the important context about a process we want to improve?

The artifact should help me think through:

- What the current workflow looks like
- Where the pain points and bottlenecks are
- What inputs and outputs are involved
- What success would look like
- Any constraints we're working within

Make this comprehensive enough that when I complete it, it provides me with a file that I can give back to Claude with all the information needed to design a practical solution. Include clear instructions at the end for how to use the completed template with Claude.

Format this as a well-designed artifact that's easy to fill out—with clear sections, fill-in-the-blank areas, and helpful prompts that make sure I don't miss important details.
```

## Inputs

- Extended Thinking (recommended)
- Optional file uploads (PDFs)
- Access to Claude
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

1. Describe the task - request a comprehensive planning template with questions
2. Give Claude context - upload relevant files (optional)
3. What Claude creates - generates multi-section assessment artifact
4. Follow up prompts - refine recommendations, create implementation materials, adjust for constraints

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Workflow improvement planner](https://claude.com/resources/use-cases/workflow-improvement-planner) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
