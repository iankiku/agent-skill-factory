---
name: analyze-fundraising-performance
description: "Analyze performance across email, events, direct mail, social media, and other channels to identify highest-return investments and optimize resource allocation for maximum fundraising impact. Use for tasks like “Analyze fundraising performance” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/analyze-fundraising-performance
  source_title: Analyze fundraising performance
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Analyze fundraising performance — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Analyze performance across email, events, direct mail, social media, and other channels to identify highest-return investments and optimize resource allocation for maximum fundraising impact.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I run development for a regional nonprofit with 25-30 annual fundraising events plus ongoing email, direct mail, social media, and corporate sponsorship programs. I need to analyze which channels drive the best ROI to inform next year's $500K+ budget decisions.

I'm uploading our fundraising data from the past two years, broken down by channel and quarter. The data includes revenue, costs, donor counts, and event-specific details for our major galas, community events, and smaller donor appreciation gatherings.

Here's what I need to understand:
1. Which channels deserve increased investment based on ROI?
2. Where can we reallocate inefficient spending?
3. Which event types generate the best returns?
4. What's our donor acquisition cost by channel?
5. Which high-performing channels are currently underfunded?

Deliverable: Comprehensive Excel workbook with consulting-firm quality—I'm presenting this to our board, so visual sophistication matters as much as analytical rigor.

Required sheets:
- Executive dashboard: KPIs, year-over-year comparisons, performance rankings
- Channel details: Quarterly breakdowns with formulas for all key metrics
- Strategic recommendations: Three-tier investment framework (grow/optimize/restructure)
- Event analysis: Individual event performance since events consume 40% of our budget

Design requirements: Make an extreme effort on visual quality—premium formatting, sophisticated color palette (not Excel defaults), consulting-grade typography, conditional formatting, data bars, color scales, frozen panes, and filters.
```

## Required context and inputs

- Extended Thinking enabled
- Exported CSV or Excel fundraising data (2 years recommended)
- Optional connectors: Microsoft 365, Benevity, or Blackbaud platforms
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Microsoft 365
- TODO: confirm which connectors are enabled in the runtime that will execute this skill
- Authentication: connectors authenticate via their own OAuth flows — this skill must
  NEVER ask for, store, or echo credentials, tokens, or API keys. If auth is missing,
  stop and tell the user which connector to enable.

## Permissions and sensitive actions

- Reads: TODO (folders, channels, records this skill may read)
- Writes: TODO (what it may create/modify, and where)
- Held back for the primary agent / human: sending external communications, financial
  transactions, deleting or overwriting originals, submitting web forms

## Workflow

1. Describe the task: provide fundraising channel data and specify desired analytical insights
2. Give Claude context: enable Extended Thinking and upload CSV/Excel files or connect data platforms
3. What Claude creates: multi-sheet Excel workbook with dashboards, detailed analysis, recommendations, and event performance tracking
4. Follow-up prompts: refine analysis through deeper event comparisons, executive briefings, or forecasting models

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
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

Derived from [Analyze fundraising performance](https://claude.com/resources/use-cases/analyze-fundraising-performance) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
