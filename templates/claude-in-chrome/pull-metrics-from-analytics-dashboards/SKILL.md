---
name: pull-metrics-from-analytics-dashboards
description: "Claude in Chrome can navigate your analytics dashboards, extract the numbers you need, and compile them into a summary. No exports, no tab-switching, no manual copying. Use for tasks like “Pull metrics from analytics dashboards” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Claude in Chrome
  recommended_model: Haiku 4.5
  features: ["Browser Use"]
  surface: "Claude in Chrome"
  source_url: https://claude.com/resources/use-cases/pull-metrics-from-analytics-dashboards
  source_title: Pull metrics from analytics dashboards
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Pull metrics from analytics dashboards — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Claude in Chrome can navigate your analytics dashboards, extract the numbers you need, and compile them into a summary. No exports, no tab-switching, no manual copying.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- Logged into Amplitude in Chrome before starting
- Logged into Mixpanel in Chrome before starting
- Saved dashboards or reports by name (optional)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Claude in Chrome extension
- TODO: confirm which connectors are enabled in the runtime that will execute this skill
- Authentication: connectors authenticate via their own OAuth flows — this skill must
  NEVER ask for, store, or echo credentials, tokens, or API keys. If auth is missing,
  stop and tell the user which connector to enable.

## Permissions and sensitive actions

- Reads: TODO (folders, channels, records this skill may read)
- Writes: TODO (what it may create/modify, and where)
- Held back for the primary agent / human: sending external communications, financial
  transactions, deleting or overwriting originals, submitting web forms, and ANY click that finalizes state on a third-party site (browser-use skill: show a review step first)

## Workflow

1. Describe the task
2. Give Claude context
3. What Claude creates
4. Follow up prompts
5. Tricks, tips, and troubleshooting

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- Nothing is submitted/saved on a website without showing the user a review step first
- Site actions limited to the domains named in the workflow
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Page fails to load or selector drifts → retry once, then stop and report; never guess at form fields
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Apply the repo's delegation policy (`docs/delegation-policy.md` — bundle or restate
it if you install this skill outside the repo). Defaults for this template:

- Run single-agent unless a step fans out over independent items (files, records,
  vendors, channels). Only independent work parallelizes.
- Each delegated task must ship with: the minimal context slice it needs, an explicit
  output contract, a validation check the primary agent runs on the result, and a
  fallback if it returns empty or fails.
- Final review, synthesis, and every sensitive action listed above stay with the
  primary agent.
- TODO: name the concrete subtasks (if any) that qualify for delegation here.

## Attribution

Derived from [Pull metrics from analytics dashboards](https://claude.com/resources/use-cases/pull-metrics-from-analytics-dashboards) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
