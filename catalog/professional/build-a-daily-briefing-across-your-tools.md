---
title: Build a daily briefing across your tools
slug: build-a-daily-briefing-across-your-tools
category: Professional
recommended_model: Sonnet 4.5
features: ["Cowork"]
surface: "Cowork (with Claude in Chrome)"
source_url: https://claude.com/resources/use-cases/build-a-daily-briefing-across-your-tools
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Build a daily briefing across your tools

Generate a daily briefing that pulls from Slack, Notion, and your team dashboard to surface priorities and connections you'd miss scanning each platform separately.

## Example prompt (verbatim, © Anthropic PBC)

```text
I need my morning briefing. Pull from Slack and Notion, and visit my team dashboard: https://metrics.acme-corp.com/ops-team

Structure it as:

- Urgent items from the dashboard (anything red or trending down)
- Slack threads where I'm mentioned — read the full threads for context
- Threads I'm not in but should probably know about based on my current tasks
- Tasks due this week and anything blocking them

For urgent items, pull the deeper context: who's involved, what's been discussed, what's still unresolved.
```

## How it works (from source page)

1. Download Claude Desktop and start a Cowork session
2. Add connectors for Slack, Notion, and other desired tools
3. Install Claude in Chrome and add as a connector for dashboard access
4. Submit initial briefing prompt; Claude may ask clarifying questions
5. Review Claude's plan in the sidebar before execution
6. Follow up with refinement prompts as needed

## Prerequisites (from source page)

- Claude Desktop
- Cowork feature
- Connectors (Slack, Notion)
- Claude in Chrome
- Dashboard URL access
- Optionally calendar and email connectors

## Attribution

Reproduced from [Build a daily briefing across your tools](https://claude.com/resources/use-cases/build-a-daily-briefing-across-your-tools) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
