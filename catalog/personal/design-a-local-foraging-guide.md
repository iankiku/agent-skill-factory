---
title: Design a local foraging guide
slug: design-a-local-foraging-guide
category: Personal
recommended_model: Opus 4.5
features: ["Extended Thinking"]
surface: "Claude.ai chat (Artifacts)"
source_url: https://claude.com/resources/use-cases/design-a-local-foraging-guide
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Design a local foraging guide

Build artifacts where the map is the menu. Select your state on an interactive map browse by category and export a printable reference.

## Example prompt (verbatim, © Anthropic PBC)

```text
I want to build a foraging guide for someone new to wild edibles and unsure where to start.

What it should do:

- Let users click their state on an interactive US map to see regional foraging data (fetch map data from the us-atlas TopoJSON CDN at https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json and render with D3's geoAlbersUsa projection)
- Browse edible plants by category and show a 12-month season bar for each species so users see harvest windows at a glance
- Let users tap any plant to expand details, then let users add plants to a personal foraging list and export a printable field guide with their selected species and safety reminders

Design: Quiet and organic. Warm cream, muted sage, soft olive. Think field journal meets editorial magazine—sophisticated but approachable. Smooth transitions, rounded corners, good type hierarchy.
```

## How it works (from source page)

1. Describe the task
2. Give Claude context
3. What Claude creates
4. Follow up prompts
5. Tricks, tips, and troubleshooting

## Prerequisites (from source page)

- Enable Artifacts in settings
- Extended Thinking for complex apps (optional)

## Attribution

Reproduced from [Design a local foraging guide](https://claude.com/resources/use-cases/design-a-local-foraging-guide) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
