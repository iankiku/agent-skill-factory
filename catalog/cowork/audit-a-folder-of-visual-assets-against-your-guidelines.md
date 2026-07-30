---
title: Audit a folder of visual assets against your guidelines
slug: audit-a-folder-of-visual-assets-against-your-guidelines
category: Cowork
recommended_model: Opus 4.7
features: ["Cowork"]
surface: "Cowork"
source_url: https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Audit a folder of visual assets against your guidelines

In Claude Cowork, Claude Opus 4.7 can read a large folder of image exports at full resolution to spot off-brand colors, outdated logos, and missing legal copy.

## Example prompt (verbatim, © Anthropic PBC)

```text
Audit every PNG and JPG in this folder against brand-meridian-2025-q2.pdf and legal-required-copy.txt. Flag: the old 2024 logo, off-brand hex codes (#0052B3 instead of #004B9F, #D4AF37 instead of #C9A961), missing or undersized legal copy. Group by violation type. For each one give me filename, issue, guideline value, asset value, and confidence. End with how many assets passed all checks.
```

## How it works (from source page)

1. Describe the task (specify rules and grouping)
2. Give Claude context (point Cowork project at folder with guidelines, PDFs, legal sheets, and asset exports)
3. Claude creates the audit (reads guides and checks all assets against them)
4. Follow-up prompts (check live pages, file tasks, schedule audits)

## Prerequisites (from source page)

- Claude Cowork project pointed at folder containing brand guidelines PDF, legal sheet, and PNG/JPEG assets
- Opus 4.7 model selected
- Optional: Asana, Linear, or Slack connectors

## Attribution

Reproduced from [Audit a folder of visual assets against your guidelines](https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
