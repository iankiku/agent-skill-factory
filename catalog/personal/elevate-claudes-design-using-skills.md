---
title: Elevate Claude's design using skills
slug: elevate-claudes-design-using-skills
category: Personal
recommended_model: Sonnet 4.5
features: ["Skills"]
surface: "Claude.ai chat"
source_url: https://claude.com/resources/use-cases/elevate-claudes-design-using-skills
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Elevate Claude's design using skills

Design a skill that automatically activates design principles into Claude's outputs.

## Example prompt (verbatim, © Anthropic PBC)

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

## How it works (from source page)

1. Enable code execution and file creation in Settings > Capabilities > Skills
2. Add the design-elevation folder to your skills directory
3. Claude will automatically consult reference files for visual outputs
4. Receive elevated outputs without repeating design requirements

## Prerequisites (from source page)

- Code execution and file creation enabled in Claude Settings > Capabilities > Skills
- Extended Thinking feature (optional)

## Attribution

Reproduced from [Elevate Claude's design using skills](https://claude.com/resources/use-cases/elevate-claudes-design-using-skills) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
