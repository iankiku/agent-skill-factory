---
title: Pull metrics from analytics dashboards
slug: pull-metrics-from-analytics-dashboards
category: Claude in Chrome
recommended_model: Haiku 4.5
features: ["Browser Use"]
surface: "Claude in Chrome"
source_url: https://claude.com/resources/use-cases/pull-metrics-from-analytics-dashboards
retrieved_at: 2026-07-26
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: ok
---

# Pull metrics from analytics dashboards

Claude in Chrome can navigate your analytics dashboards, extract the numbers you need, and compile them into a summary. No exports, no tab-switching, no manual copying.

## Example prompt (verbatim, © Anthropic PBC)

```text
Pull my weekly metrics from both my Amplitude and Mixpanel open tabs.

From Amplitude:
- Weekly active users (WAU) — past 4 weeks
- New user signups — this week vs. last week
- Retention (Day 1, Day 7, Day 30) — for the cohort from 30 days ago

From Mixpanel:
- Feature adoption rate for new dashboard (% of WAU who used it)
- Conversion rate through onboarding flow
- Top 5 events by volume this week

Output: Format as a summary I can paste into our weekly product update.
```

## Prerequisites (from source page)

- Logged into Amplitude in Chrome before starting
- Logged into Mixpanel in Chrome before starting
- Saved dashboards or reports by name (optional)

## Attribution

Reproduced from [Pull metrics from analytics dashboards](https://claude.com/resources/use-cases/pull-metrics-from-analytics-dashboards) (retrieved 2026-07-26). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
