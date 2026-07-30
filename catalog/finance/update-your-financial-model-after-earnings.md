---
title: Update your financial model after earnings
slug: update-your-financial-model-after-earnings
category: Finance
recommended_model: Opus 4.6
features: ["Connectors", "Skills"]
surface: "Cowork + Claude for Excel + Claude for PowerPoint"
source_url: https://claude.com/resources/use-cases/update-your-financial-model-after-earnings
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Update your financial model after earnings

Cowork pulls the release and transcript from S&P and checks them against your financial model. You take the flags into Claude for Excel to edit the cells, then open the deck in Claude for PowerPoint to build the page.

## Example prompt (verbatim, © Anthropic PBC)

```text
ACME just jumped 8% after hours — what's driving this? I need to update my model and build a page for tomorrow's PM meeting.
```

## How it works (from source page)

1. Pull the earnings release and call transcript from S&P
2. Read your model in the folder and flag forecast discrepancies
3. Identify unsupported assumptions from the transcript
4. Provide a brief with cell references and recommended changes

## Prerequisites (from source page)

- Portfolio folder with financial model attached
- S&P Global connector enabled
- Claude for Excel add-in installed
- Claude for PowerPoint add-in installed

## Attribution

Reproduced from [Update your financial model after earnings](https://claude.com/resources/use-cases/update-your-financial-model-after-earnings) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
