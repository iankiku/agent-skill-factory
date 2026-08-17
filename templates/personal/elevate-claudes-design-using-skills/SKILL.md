---
name: elevate-claudes-design-using-skills
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Elevate Claude's design using skills."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Skills"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/elevate-claudes-design-using-skills
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Elevate Claude's design using skills — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Design a skill that automatically activates design principles into Claude's outputs.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

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

## Inputs

- Code execution and file creation enabled in Claude Settings > Capabilities > Skills
- Extended Thinking feature (optional)
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

1. Enable code execution and file creation in Settings > Capabilities > Skills
2. Add the design-elevation folder to your skills directory
3. Claude will automatically consult reference files for visual outputs
4. Receive elevated outputs without repeating design requirements

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

Derived from [Elevate Claude's design using skills](https://claude.com/resources/use-cases/elevate-claudes-design-using-skills) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
