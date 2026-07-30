---
title: Draft a credit memo from spreads and statements with Claude for Excel
slug: draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel
category: Finance
recommended_model: Sonnet 4.6
features: ["Connectors"]
surface: "Cowork + Claude for Excel + Claude for Word"
source_url: https://claude.com/resources/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Draft a credit memo from spreads and statements with Claude for Excel

Cowork pulls the borrower's filings and spreads through the S&P Capital IQ connector and reads the underwriting workbook from your deal folder. You take the ratios and exceptions into Claude for Excel to update the model, then bring the writeup into Claude for Word for the credit memo.

## Example prompt (verbatim, © Anthropic PBC)

```text
Acme Manufacturing — $25M revolver renewal, committee Thursday. Walk me through the credit before I touch the spread.
```

## How it works (from source page)

1. Pull three years of financials and peer spreads from S&P Capital IQ
2. Read the underwriting workbook in the deal folder and flag where ratios trip policy
3. Tell which assumptions in the model don't match what's in the statements
4. Provide a brief to take into Excel with cell references, what to change, and why

## Prerequisites (from source page)

- S&P Capital IQ connector enabled
- Deal folder with underwriting workbook attached
- Credit memo template
- Claude for Excel add-in installed
- Claude for Word add-in installed

## Attribution

Reproduced from [Draft a credit memo from spreads and statements with Claude for Excel](https://claude.com/resources/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
