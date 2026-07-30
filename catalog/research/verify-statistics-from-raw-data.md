---
title: Verify statistics from raw data
slug: verify-statistics-from-raw-data
category: Research
recommended_model: Sonnet 4.5
features: ["Extended Thinking"]
surface: "Claude.ai chat"
source_url: https://claude.com/resources/use-cases/verify-statistics-from-raw-data
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Verify statistics from raw data

Learn to evaluate published statistics by checking them against raw data.

## Example prompt (verbatim, © Anthropic PBC)

```text
I'm reading this paper that's central to my literature review, and I want to understand it more deeply before citing it extensively. I've got the published manuscript and their supplementary data files.

Can you help me verify their statistical claims? Go through the paper systematically and pull out every p-value, mean, standard error, sample size, and test result they report. Then run each analysis yourself using their actual data.

For each statistical claim, show me three things: what the paper states, what you calculated from their data, and whether these match. Flag any problems you notice - things like using wrong tests for the data type, sample sizes that don't add up, or p-values that seem mathematically questionable.

Then build me a detailed Excel workbook where I can see your complete verification. Create separate sheets for each analysis showing your calculations step by step, plus a summary sheet highlighting any issues I should understand before relying on this work.

Make the spreadsheet well-designed and easy to navigate - professional formatting, frozen headers, filtered columns, and clear notes explaining what you found.
```

## How it works (from source page)

1. Describe the task: provide manuscript and data context
2. Give Claude context: upload manuscript and data files
3. What Claude creates: comprehensive audit workbook with statistical verification
4. Follow up prompts: optional refinements and deeper analysis
5. Tricks, tips, and troubleshooting

## Prerequisites (from source page)

- Manuscript (PDF file)
- Data files (XLSX format)
- Optional: Extended Thinking (recommended for thorough verification)

## Attribution

Reproduced from [Verify statistics from raw data](https://claude.com/resources/use-cases/verify-statistics-from-raw-data) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
