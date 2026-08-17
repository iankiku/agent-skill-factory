---
name: pull-metrics-from-analytics-dashboards
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Pull metrics from analytics dashboards."
metadata:
  status: template — resolve every TODO before use
  category: Claude in Chrome
  recommended_model: Haiku 4.5
  features: ["Browser Use"]
  surface: "Claude in Chrome"
  source_url: https://claude.com/resources/use-cases/pull-metrics-from-analytics-dashboards
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Pull metrics from analytics dashboards — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude in Chrome can navigate your analytics dashboards, extract the numbers you need, and compile them into a summary. No exports, no tab-switching, no manual copying.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

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

## Inputs

- Logged into Amplitude in Chrome before starting
- Logged into Mixpanel in Chrome before starting
- Saved dashboards or reports by name (optional)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude in Chrome extension
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms, and ANY click that finalizes state on a third-party site (browser-use skill: show a review step first)

## Workflow

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Nothing is submitted/saved on a website without showing the user a review step first
- Site actions limited to the domains named in the workflow
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Page fails to load or selector drifts → retry once, then stop and report; never guess at form fields
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Pull metrics from analytics dashboards](https://claude.com/resources/use-cases/pull-metrics-from-analytics-dashboards) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
