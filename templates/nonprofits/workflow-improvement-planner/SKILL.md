---
name: workflow-improvement-planner
description: "Turn process pain points into structured improvement plans. Claude helps nonprofits define workflow challenges and design AI-powered solutions that save time and increase capacity. Use for tasks like “Workflow improvement planner” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/workflow-improvement-planner
  source_title: Workflow improvement planner
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Workflow improvement planner — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Turn process pain points into structured improvement plans. Claude helps nonprofits define workflow challenges and design AI-powered solutions that save time and increase capacity.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- Extended Thinking (recommended)
- Optional file uploads (PDFs)
- Access to Claude
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

1. Describe the task - request a comprehensive planning template with questions
2. Give Claude context - upload relevant files (optional)
3. What Claude creates - generates multi-section assessment artifact
4. Follow up prompts - refine recommendations, create implementation materials, adjust for constraints

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
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

Derived from [Workflow improvement planner](https://claude.com/resources/use-cases/workflow-improvement-planner) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
