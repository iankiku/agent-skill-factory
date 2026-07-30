---
title: Handle a request while away from your keyboard
slug: handle-a-request-while-away-from-your-keyboard
category: Cowork
recommended_model: Sonnet 4.6
features: ["Connectors", "Cowork"]
surface: "Cowork (Dispatch) + Claude mobile app"
source_url: https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Handle a request while away from your keyboard

Use Dispatch in Claude Cowork to respond to requests from the Claude mobile app using everything on your computer.

## Example prompt (verbatim, © Anthropic PBC)

```text
Jamie just asked me on Slack for the latest Q2 budget spreadsheet. Find it in my Documents/Finance folder on my computer — the file with "Q2" and "budget" in the name. Post it to Jamie in the #proj-planning Slack channel. Add a note that the tab labeled "Revised" has the current numbers.
```

## How it works (from source page)

1. Describe the task — explain what you need Claude to handle
2. Give Claude context — provide access to local files and necessary connectors
3. Claude creates the output — locates files, prepares messages, awaits approval
4. Follow up prompts — refine or expand the conversation
5. Continue on laptop — pick up the same conversation when returning to desktop

## Prerequisites (from source page)

- Claude desktop app running with keep-awake toggle enabled
- Claude mobile app
- Local file access (Documents/Finance folder)
- Slack connector (required for posting)
- Gmail connector (optional, for email drafting)

## Attribution

Reproduced from [Handle a request while away from your keyboard](https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
