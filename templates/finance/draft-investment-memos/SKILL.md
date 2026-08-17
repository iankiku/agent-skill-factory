---
name: draft-investment-memos
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Draft investment memos."
metadata:
  status: template — resolve every TODO before use
  category: Finance
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking", "Web Search", "Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/draft-investment-memos
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Draft investment memos — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Generate investment memos from platform data, formatted to match your firm's structure and requirements.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm evaluating CloudBridge Technologies (ticker: CLDG) for a potential equity investment and need an initial memo for our IC meeting next week.

Pull the data I need: Using Daloopa, get CloudBridge's revenue, operating margins, and free cash flow for the last 12 quarters, plus their segment revenue breakdowns. Using Kensho, identify who CloudBridge lists as competitors in their SEC filings and pull revenue growth and margins for those competitors. Also get CloudBridge's key business relationships and major customers.

Analyze this: Calculate cloud platform segment growth versus overall company growth. Determine free cash flow conversion rate. Compare margins year-over-year. Benchmark CloudBridge against the competitors we identified. Flag customer concentration risks.

Create a professional investment memo in Word format: executive summary with recommendation, business overview with segment analysis, financial performance highlighting trends, competitive positioning, valuation assessment, and key risks. Use IC-ready formatting.
```

## Inputs

- Connectors to financial data platforms: Daloopa and S&P Global (Kensho referenced in prompt)
- Existing subscriptions/licenses with underlying providers
- Claude for Enterprise access
- Optional: Web Search enabled in chat settings
- Optional: Extended Thinking enabled
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

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

1. Describe the task: specify the company being evaluated, key metrics needed, and deliverable format required
2. Give Claude context: connect data platforms (Daloopa, S&P Global) via connectors; enable Web Search and Extended Thinking
3. What Claude creates: pulls data, performs calculations, and generates a professional Word document with full analysis
4. Follow up prompts: cite exact sources for each metric; show the DCF math step-by-step with a sensitivity table; convert the analysis into a 6-slide PowerPoint
5. Tricks, tips, and troubleshooting: clear instructions, downloading actual files, model selection, and accessing specialized capabilities

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

Derived from [Draft investment memos](https://claude.com/resources/use-cases/draft-investment-memos) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
