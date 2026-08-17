---
title: Package your brand guidelines in a skill
slug: package-your-brand-guidelines-in-a-skill
category: Professional
recommended_model: Sonnet 4.5
features: ["Skills"]
surface: "Claude.ai chat"
source_url: https://claude.com/resources/use-cases/package-your-brand-guidelines-in-a-skill
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Package your brand guidelines in a skill

Package your brand guidelines into a skill to create presentations, spreadsheets, or documents that automatically match your preferred style.

## Example prompt (verbatim, © Anthropic PBC)

```text
I want to create a skill that applies our company's brand styling to any presentation, document, or spreadsheet I create in Claude. Here's what I need to encode:

Color Palette:
Dark: #141413 (primary text, dark backgrounds)
Light: #faf9f5 (light backgrounds, text on dark)
Mid Gray: #b0aea5 (secondary elements)
Light Gray: #e8e6dc (subtle backgrounds)
Orange: #d97757 (primary accent for important elements)
Blue: #6a9bcc (secondary accent)
Green: #788c5d (tertiary accent)

Typography:
Headings (24pt and larger): Poppins font, bold weight
Body text: Lora font, regular weight
Fallbacks: Arial for headings if Poppins unavailable, Georgia for body if Lora unavailable

Application Rules:
- Apply Poppins to all slide titles and document headings
- Apply Lora to body text and paragraphs
- Use accent colors (orange, blue, green) for shapes, charts, and visual elements
- Cycle through accent colors to maintain visual interest
- Use dark color for primary text on light backgrounds
- Use light color for text on dark backgrounds

Create a complete skill with proper structure that I can use whenever I need brand-consistent presentations. Include the SKILL.md file with clear instructions for when to use it and how it applies the styling.
```

## Prerequisites (from source page)

- Skills feature enabled
- File creation enabled
- Google Drive integration (optional)
- Extended Thinking (optional)

## Attribution

Reproduced from [Package your brand guidelines in a skill](https://claude.com/resources/use-cases/package-your-brand-guidelines-in-a-skill) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
