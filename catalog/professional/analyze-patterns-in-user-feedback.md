---
title: Analyze patterns in user feedback
slug: analyze-patterns-in-user-feedback
category: Professional
recommended_model: Sonnet 4.5
features: ["Connectors"]
surface: "Claude.ai chat"
source_url: https://claude.com/resources/use-cases/analyze-patterns-in-user-feedback
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Analyze patterns in user feedback

Find recurring themes and pain points across user feedback to separate meaningful patterns from noise.

## Example prompt (verbatim, © Anthropic PBC)

```text
Pull all Intercom conversations from the past 90 days. I'm also uploading our Q2 NPS survey responses (CSV) and notes from six user interviews we did last month (PDFs).

Read everything and tell me what patterns you're seeing:

- What issues keep showing up across different feedback sources?
- When people ask for different things, are they actually pointing to the same underlying need?
- Which complaints seem most urgent based on how users describe them?
- What's worth prioritizing vs what's noise?

Create a data workbook (Excel) organizing all the feedback by theme with filters so I can dig into specific issues. Include the source for each piece of feedback (Intercom, NPS, or interview) and use professional formatting with frozen headers
```

## Prerequisites (from source page)

- Intercom connector enabled (Settings > Connectors)
- Upload supplementary feedback files (NPS responses CSV, interview transcripts PDFs)
- Optional: Extended Thinking for deeper pattern recognition

## Attribution

Reproduced from [Analyze patterns in user feedback](https://claude.com/resources/use-cases/analyze-patterns-in-user-feedback) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
