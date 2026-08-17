---
name: analyze-fundraising-performance
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Analyze fundraising performance."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/analyze-fundraising-performance
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Analyze fundraising performance — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Analyze performance across email, events, direct mail, social media, and other channels to identify highest-return investments and optimize resource allocation for maximum fundraising impact.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

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

## Inputs

- Extended Thinking enabled
- Exported CSV or Excel fundraising data (2 years recommended)
- Optional connectors: Microsoft 365, Benevity, or Blackbaud platforms
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Microsoft 365
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task: provide fundraising channel data and specify desired analytical insights
2. Give Claude context: enable Extended Thinking and upload CSV/Excel files or connect data platforms
3. What Claude creates: multi-sheet Excel workbook with dashboards, detailed analysis, recommendations, and event performance tracking
4. Follow-up prompts: refine analysis through deeper event comparisons, executive briefings, or forecasting models

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Analyze fundraising performance](https://claude.com/resources/use-cases/analyze-fundraising-performance) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
