---
name: genomic-data-analysis
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Genomic data analysis."
metadata:
  status: template — resolve every TODO before use
  category: Life Sciences
  recommended_model: Sonnet 4.5
  features: ["Connectors", "Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/genomic-data-analysis
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Genomic data analysis — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

With Claude as your research partner, analyze gene expression data to identify patterns and form testable hypotheses about biological mechanisms, while Claude handles the computational heavy lifting of bioinformatics and literature synthesis.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
My colleagues recently published the attached single-cell dataset that describes gene expression differences between adult and pediatric liver samples with a focus on the immune system. I would like to explore these samples but focus on the parenchymal cells and differences between adult and pediatric liver. Can you help me first go through the differentially expressed genes and create a heatmap and then also identify pathways or sets of genes that are enriched in each sample?
```

## Inputs

- CSV or TSV files containing differential expression data
- Optional: PubMed connector for literature integration
- Optional: Extended Thinking enabled
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- PubMed
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task: share genomic data and specify what to explore; Claude analyzes differential expression patterns, creates visualizations, and searches scientific databases
2. Give Claude context: upload CSV/TSV files with differential expression results; optionally connect to research databases via connectors
3. What Claude creates: examines datasets, performs pathway enrichment analysis, creates visual representations, and identifies key biological processes

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Methods/statistics restated only from the source material; no invented p-values
- Units and sample sizes double-checked against source tables
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Genomic data analysis](https://claude.com/resources/use-cases/genomic-data-analysis) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
