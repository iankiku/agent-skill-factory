---
title: Draft investment memos
slug: draft-investment-memos
category: Finance
recommended_model: Sonnet 4.5
features: ["Extended Thinking", "Web Search", "Connectors"]
surface: "Claude.ai chat"
source_url: https://claude.com/resources/use-cases/draft-investment-memos
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Draft investment memos

Generate investment memos from platform data, formatted to match your firm's structure and requirements.

## Example prompt (verbatim, © Anthropic PBC)

```text
I'm evaluating CloudBridge Technologies (ticker: CLDG) for a potential equity investment and need an initial memo for our IC meeting next week.

Pull the data I need: Using Daloopa, get CloudBridge's revenue, operating margins, and free cash flow for the last 12 quarters, plus their segment revenue breakdowns. Using Kensho, identify who CloudBridge lists as competitors in their SEC filings and pull revenue growth and margins for those competitors. Also get CloudBridge's key business relationships and major customers.

Analyze this: Calculate cloud platform segment growth versus overall company growth. Determine free cash flow conversion rate. Compare margins year-over-year. Benchmark CloudBridge against the competitors we identified. Flag customer concentration risks.

Create a professional investment memo in Word format: executive summary with recommendation, business overview with segment analysis, financial performance highlighting trends, competitive positioning, valuation assessment, and key risks. Use IC-ready formatting.
```

## How it works (from source page)

1. Describe the task: specify the company being evaluated, key metrics needed, and deliverable format required
2. Give Claude context: connect data platforms (Daloopa, S&P Global) via connectors; enable Web Search and Extended Thinking
3. What Claude creates: pulls data, performs calculations, and generates a professional Word document with full analysis
4. Follow up prompts: cite exact sources for each metric; show the DCF math step-by-step with a sensitivity table; convert the analysis into a 6-slide PowerPoint
5. Tricks, tips, and troubleshooting: clear instructions, downloading actual files, model selection, and accessing specialized capabilities

## Prerequisites (from source page)

- Connectors to financial data platforms: Daloopa and S&P Global (Kensho referenced in prompt)
- Existing subscriptions/licenses with underlying providers
- Claude for Enterprise access
- Optional: Web Search enabled in chat settings
- Optional: Extended Thinking enabled

## Attribution

Reproduced from [Draft investment memos](https://claude.com/resources/use-cases/draft-investment-memos) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
