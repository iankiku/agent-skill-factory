---
name: verify-statistics-from-raw-data
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Verify statistics from raw data."
metadata:
  status: template — resolve every TODO before use
  category: Research
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/verify-statistics-from-raw-data
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Verify statistics from raw data — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Learn to evaluate published statistics by checking them against raw data.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm reading this paper that's central to my literature review, and I want to understand it more deeply before citing it extensively. I've got the published manuscript and their supplementary data files.

Can you help me verify their statistical claims? Go through the paper systematically and pull out every p-value, mean, standard error, sample size, and test result they report. Then run each analysis yourself using their actual data.

For each statistical claim, show me three things: what the paper states, what you calculated from their data, and whether these match. Flag any problems you notice - things like using wrong tests for the data type, sample sizes that don't add up, or p-values that seem mathematically questionable.

Then build me a detailed Excel workbook where I can see your complete verification. Create separate sheets for each analysis showing your calculations step by step, plus a summary sheet highlighting any issues I should understand before relying on this work.

Make the spreadsheet well-designed and easy to navigate - professional formatting, frozen headers, filtered columns, and clear notes explaining what you found.
```

## Inputs

- Manuscript (PDF file)
- Data files (XLSX format)
- Optional: Extended Thinking (recommended for thorough verification)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- No connectors detected on the source page; base Claude capabilities only
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task: provide manuscript and data context
2. Give Claude context: upload manuscript and data files
3. What Claude creates: comprehensive audit workbook with statistical verification
4. Follow up prompts: optional refinements and deeper analysis

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Verify statistics from raw data](https://claude.com/resources/use-cases/verify-statistics-from-raw-data) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
