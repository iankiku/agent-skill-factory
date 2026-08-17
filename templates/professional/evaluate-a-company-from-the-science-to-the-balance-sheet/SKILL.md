---
name: evaluate-a-company-from-the-science-to-the-balance-sheet
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Evaluate a company from the science to the balance sheet."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Opus 4.6
  features: ["Extended Thinking"]
  surface: "Claude.ai chat (primary), with optional Claude Desktop/Cowork, Claude for Chrome, and Claude in Excel"
  source_url: https://claude.com/resources/use-cases/evaluate-a-company-from-the-science-to-the-balance-sheet
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Evaluate a company from the science to the balance sheet — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude Opus 4.6 runs due diligence across SEC filings, clinical trial data, and patent documents at once, evaluating the science, modeling the financials, and catching where one contradicts the other.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm evaluating Meridian Therapeutics (~$4B mid-cap biotech) ahead of their Phase III readout. I've uploaded the 10-K, 10-Q, proxy, trial protocol, and patent filings. Evaluate the science and trial design. Build a risk-adjusted pipeline valuation. Flag anything in the filings that contradicts management's guidance or earnings narrative. Model the downside scenarios I should be stress-testing. Produce a research memo and a downloadable model. Tell me what I should be worried about that I haven't asked about.
```

## Inputs

- SEC filings (10-K, 10-Q, proxy statements)
- Clinical trial protocol documents
- Patent filings
- Claude Desktop with Cowork for folder-based file reading (optional)
- Claude for Chrome to access SEC filings and databases directly (optional)
- Extended Thinking feature, recommended for complex multi-document analysis (optional)
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
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (provide investment question and evaluation focus)
2. Give Claude context (upload complete filing set)
3. What Claude creates (research memo, financial model, scenario dashboard, timeline)
4. Follow up prompts (example prompts for deeper research, further analysis, and Excel export)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Evaluate a company from the science to the balance sheet](https://claude.com/resources/use-cases/evaluate-a-company-from-the-science-to-the-balance-sheet) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
