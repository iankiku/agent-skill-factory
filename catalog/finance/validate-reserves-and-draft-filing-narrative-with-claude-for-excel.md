---
title: Validate reserves and draft filing narrative with Claude for Excel
slug: validate-reserves-and-draft-filing-narrative-with-claude-for-excel
category: Finance
recommended_model: Sonnet 4.6
features: ["Connectors"]
surface: "Cowork + Claude for Excel + Claude for Word"
source_url: https://claude.com/resources/use-cases/validate-reserves-and-draft-filing-narrative-with-claude-for-excel
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Validate reserves and draft filing narrative with Claude for Excel

Cowork reads your reserve workbook from the valuation folder and pulls prior filings and bulletins through the NAIC connector. You take the formula flags and reserve walk into Claude for Excel to clean the workbook, then bring the narrative into Claude for Word for the filing memo.

## Example prompt (verbatim, © Anthropic PBC)

```text
Q1 reserve review for Personal Auto BI — appointed actuary review next week, filing due in two. Walk me through the workbook before I lock the numbers.
```

## How it works (from source page)

1. Read the reserve workbook in the valuation folder and validate the formulas
2. Pull the FY24 filing and any new bulletins from NAIC
3. Flag development factors and tail assumptions that look off vs. prior
4. Give a brief for Excel with sheet references, what's broken, and what's just a movement to explain

## Prerequisites (from source page)

- Valuation folder with reserve workbook attached
- NAIC connector enabled
- Claude for Excel add-in installed
- Claude for Word add-in installed

## Attribution

Reproduced from [Validate reserves and draft filing narrative with Claude for Excel](https://claude.com/resources/use-cases/validate-reserves-and-draft-filing-narrative-with-claude-for-excel) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
