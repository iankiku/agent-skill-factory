---
name: elevate-claudes-design-using-skills
description: "Design a skill that automatically activates design principles into Claude's outputs. Use for tasks like “Elevate Claude's design using skills” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Skills"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/elevate-claudes-design-using-skills
  source_title: Elevate Claude's design using skills
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Elevate Claude's design using skills — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Design a skill that automatically activates design principles into Claude's outputs.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I create a lot of visual outputs with Claude—presentations, dashboards, reports, HTML pages. They're functional but always feel generic, like first drafts rather than polished work. I want them to look like they've been through multiple rounds of professional design refinement.

I'd like to create a skill that automatically applies design thinking to any visual output I request. Something that makes Claude interrogate design choices, reference best practices, and push for excellence before delivering anything.

The skill should activate whenever I ask for presentations, spreadsheets, HTML artifacts, PDFs, or anything visual. Claude should:

- Start with a functional version, then elevate it
- Question every design choice (typography, color, layout, spacing)
- Draw from professional design references (Stripe, Linear, Apple, Bauhaus, Swiss design)
- Apply specific visual techniques rather than generic defaults
- Balance bold choices with tasteful restraint
- Ensure the final output looks hand-crafted, not template-based

I want the skill to have reference files that Claude consults:

- A design interrogation checklist (questions to ask before delivering)
- A technique catalog (specific visual moves organized by what they achieve)
- A reference library (design exemplars and principles to draw from)
- An elevation protocol (systematic process for refinement)
- A design philosophy (principles for balancing expertise with restraint)

The goal is that when I ask "create a sales dashboard" or "make a presentation deck," Claude automatically thinks like a design director who wouldn't accept generic output. The user sees only the polished result unless they specifically ask to see the design thinking process. Help me create this skill with all the necessary reference files.
```

## Required context and inputs

- Code execution and file creation enabled in Claude Settings > Capabilities > Skills
- Extended Thinking feature (optional)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Linear
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

1. Enable code execution and file creation in Settings > Capabilities > Skills
2. Add the design-elevation folder to your skills directory
3. Claude will automatically consult reference files for visual outputs
4. Receive elevated outputs without repeating design requirements

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

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
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

Derived from [Elevate Claude's design using skills](https://claude.com/resources/use-cases/elevate-claudes-design-using-skills) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
