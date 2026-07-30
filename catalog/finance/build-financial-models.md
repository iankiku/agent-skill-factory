---
title: Build financial models
slug: build-financial-models
category: Finance
recommended_model: Sonnet 4.5
features: ["Extended Thinking", "Web Search", "Connectors"]
surface: "Claude.ai chat"
source_url: https://claude.com/resources/use-cases/build-financial-models
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Build financial models

Create investment analyses with complete financial models, scenario planning, and risk evaluation.

## Example prompt (verbatim, © Anthropic PBC)

```text
I'm evaluating MediTech Solutions (healthcare SaaS) and need a complete investment analysis.

Deal structure: $75M growth equity stake at 3.6x ARR entry, exit at 7.0x in year 5. Current metrics are $50M ARR growing 35% with 18% EBITDA margin.

Get the company financials from Daloopa - search for MediTech Solutions and pull their historical revenue, EBITDA margins, customer metrics, and growth rates.

Pull healthcare SaaS comparables from S&P Global - find public companies in the sector and get their current trading multiples, growth rates, and margin profiles. I need this to validate our 7.0x exit assumption.

Search the web for healthcare SaaS customer concentration benchmarks - the company mentioned their top 3 customers represent about 40% of revenue and I need to know if that's typical or concerning for this sector. Also look up recent healthcare SaaS growth trends to stress-test the 35% growth assumption.

Retrieve our IC template from Box - search the "IC Templates" folder and use the private equity model format as the structure.

Key questions to address: How do returns look if growth slows to 25% or 20%? What does the customer concentration risk mean for our downside scenario? How does our 7.0x exit assumption compare to where public healthcare SaaS companies are trading today?

Create an Excel model with scenarios (base, upside, downside), sensitivity analysis on growth and exit multiple, risk assessment focusing on customer concentration, and a comps table showing where public companies trade. Use sophisticated private equity formatting with premium visual quality, an intentional color scheme, working formulas, frozen panes, and conditional formatting.
```

## How it works (from source page)

1. Describe the task: specify investment opportunity details and partner requirements
2. Give Claude context: connect data platforms (Daloopa, S&P Global, Box); enable Extended Thinking and Web Search
3. What Claude creates: multi-sheet model with Executive Summary, Financial Model, Scenario Analysis, Risk Assessment, and Comps & Valuation
4. Follow up prompts: create IC memo, validate growth assumptions, research exit multiples
5. Tricks, tips, and troubleshooting: keep comps fresh, work in Excel with Claude, unlock further capabilities

## Prerequisites (from source page)

- Connectors: Daloopa, S&P Global, Box
- Features: Extended Thinking, Web Search
- Excel for downloading and editing models
- Optional: Claude for Excel (beta)

## Attribution

Reproduced from [Build financial models](https://claude.com/resources/use-cases/build-financial-models) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
