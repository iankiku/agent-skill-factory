---
name: build-financial-models
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Build financial models."
metadata:
  status: template — resolve every TODO before use
  category: Finance
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking", "Web Search", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/build-financial-models
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Build financial models — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Create investment analyses with complete financial models, scenario planning, and risk evaluation.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm evaluating MediTech Solutions (healthcare SaaS) and need a complete investment analysis.

Deal structure: $75M growth equity stake at 3.6x ARR entry, exit at 7.0x in year 5. Current metrics are $50M ARR growing 35% with 18% EBITDA margin.

Get the company financials from Daloopa - search for MediTech Solutions and pull their historical revenue, EBITDA margins, customer metrics, and growth rates.

Pull healthcare SaaS comparables from S&P Global - find public companies in the sector and get their current trading multiples, growth rates, and margin profiles. I need this to validate our 7.0x exit assumption.

Search the web for healthcare SaaS customer concentration benchmarks - the company mentioned their top 3 customers represent about 40% of revenue and I need to know if that's typical or concerning for this sector. Also look up recent healthcare SaaS growth trends to stress-test the 35% growth assumption.

Retrieve our IC template from Box - search the "IC Templates" folder and use the private equity model format as the structure.

Key questions to address: How do returns look if growth slows to 25% or 20%? What does the customer concentration risk mean for our downside scenario? How does our 7.0x exit assumption compare to where public healthcare SaaS companies are trading today?

Create an Excel model with scenarios (base, upside, downside), sensitivity analysis on growth and exit multiple, risk assessment focusing on customer concentration, and a comps table showing where public companies trade. Use sophisticated private equity formatting with premium visual quality, an intentional color scheme, working formulas, frozen panes, and conditional formatting.
```

## Inputs

- Connectors: Daloopa, S&P Global, Box
- Features: Extended Thinking, Web Search
- Excel for downloading and editing models
- Optional: Claude for Excel (beta)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Box
- Claude for Excel add-in
- Daloopa
- S&P Global
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task: specify investment opportunity details and partner requirements
2. Give Claude context: connect data platforms (Daloopa, S&P Global, Box); enable Extended Thinking and Web Search
3. What Claude creates: multi-sheet model with Executive Summary, Financial Model, Scenario Analysis, Risk Assessment, and Comps & Valuation
4. Follow up prompts: create IC memo, validate growth assumptions, research exit multiples
5. Tricks, tips, and troubleshooting: keep comps fresh, work in Excel with Claude, unlock further capabilities

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- All figures reconcile to source statements/workbooks; totals recomputed programmatically, not by eye
- Flag (never silently correct) discrepancies between model and source data
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Build financial models](https://claude.com/resources/use-cases/build-financial-models) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
