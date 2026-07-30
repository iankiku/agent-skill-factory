---
title: Generate project status reports
slug: generate-project-status-reports
category: Professional
recommended_model: Sonnet 4.5
features: ["Connectors"]
surface: "Claude.ai chat"
source_url: https://claude.com/resources/use-cases/generate-project-status-reports
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Generate project status reports

Pull status updates from your emails, Slack channels, meeting notes, and project tools to create a tracker that shows who's working on what, what's blocked, and where things stand—all in one place.

## Example prompt (verbatim, © Anthropic PBC)

```text
I need to consolidate project status from multiple sources into a task tracker.

Pull information from:

- Gmail (past 2 weeks, search "Project Hermes")
- Slack #hermes-sprint channel
- Google Drive "Project Hermes" folder
- Recent calendar meetings

For each task, I need to see:

- Who owns it and what they're working on
- Current status (not started, in progress, blocked, done)
- Any blockers and how long they've been stuck
- Notes from their updates about plans and challenges

Create an Excel tracker and include these features: visual status indicators, cell comments with context from sources (so I can hover and see the details), dropdown menus for status and priority (to make updates easy), and data bars showing progress visually.

The tracker should make it obvious at a glance where the problems are and who needs help.
```

## How it works (from source page)

1. Describe the task
2. Give Claude context
3. What Claude creates
4. Follow up prompts

## Prerequisites (from source page)

- Connectors: Google Drive, Gmail, Google Calendar, Slack
- Optional: Extended Thinking (for better Word/Excel/PowerPoint results)
- Excel file creation

## Attribution

Reproduced from [Generate project status reports](https://claude.com/resources/use-cases/generate-project-status-reports) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
