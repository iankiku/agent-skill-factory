---
title: Build interactive diagram tools
slug: build-interactive-diagram-tools
category: Personal
recommended_model: Opus 4.5
features: ["Extended Thinking"]
surface: "Claude.ai chat"
source_url: https://claude.com/resources/use-cases/build-interactive-diagram-tools
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Build interactive diagram tools

From body systems to molecular structures, turn a detailed prompt into a working reference app with the depth and design you specify.

## Example prompt (verbatim, © Anthropic PBC)

```text
Build an interactive anatomy explorer using @ebi-gene-expression-group/anatomogram from npm. Use homo_sapiens.male.svg and homo_sapiens.brain.svg. Don't generate diagrams yourself—these SVGs contain accurate illustrations with UBERON ontology IDs already embedded. Embed the SVGs directly into the HTML—no fetch requests needed.

Critical: The SVGs style all elements with fill:none;stroke:none by default, making them invisible. After loading, apply default fills and strokes before any other styling. Also set cleanupIds: false when optimizing (the UBERON IDs are how you target elements) and remove the visibility:hidden attribute in JavaScript.

Design requirements: Restrained and sophisticated. No glows, no emojis, no neon. Warm colors over cold. Serif headings, sans-serif body, monospace for data. Think premium medical reference, not generic AI output.

Add tabbed information panels, physical-feeling sound feedback, and content rich enough to actually learn from. Build to flagship quality from the start—I'll iterate until this is exceptional.
```

## How it works (from source page)

1. Describe the task (what to learn, how to interact, data sources, aesthetic standards)
2. Give Claude context (enable file creation; optionally enable Extended Thinking)
3. Claude creates a fully functional React application
4. Follow up with refinement prompts

## Prerequisites (from source page)

- File creation enabled in settings
- Extended Thinking (optional, for complex apps)

## Attribution

Reproduced from [Build interactive diagram tools](https://claude.com/resources/use-cases/build-interactive-diagram-tools) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
