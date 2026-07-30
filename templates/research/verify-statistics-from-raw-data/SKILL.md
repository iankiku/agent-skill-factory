---
name: verify-statistics-from-raw-data
description: "Learn to evaluate published statistics by checking them against raw data. Use for tasks like “Verify statistics from raw data” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Research
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/verify-statistics-from-raw-data
  source_title: Verify statistics from raw data
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Verify statistics from raw data — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Learn to evaluate published statistics by checking them against raw data.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm reading this paper that's central to my literature review, and I want to understand it more deeply before citing it extensively. I've got the published manuscript and their supplementary data files.

Can you help me verify their statistical claims? Go through the paper systematically and pull out every p-value, mean, standard error, sample size, and test result they report. Then run each analysis yourself using their actual data.

For each statistical claim, show me three things: what the paper states, what you calculated from their data, and whether these match. Flag any problems you notice - things like using wrong tests for the data type, sample sizes that don't add up, or p-values that seem mathematically questionable.

Then build me a detailed Excel workbook where I can see your complete verification. Create separate sheets for each analysis showing your calculations step by step, plus a summary sheet highlighting any issues I should understand before relying on this work.

Make the spreadsheet well-designed and easy to navigate - professional formatting, frozen headers, filtered columns, and clear notes explaining what you found.
```

## Required context and inputs

- Manuscript (PDF file)
- Data files (XLSX format)
- Optional: Extended Thinking (recommended for thorough verification)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- No connectors detected on the source page; base Claude capabilities only
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

1. Describe the task: provide manuscript and data context
2. Give Claude context: upload manuscript and data files
3. What Claude creates: comprehensive audit workbook with statistical verification
4. Follow up prompts: optional refinements and deeper analysis
5. Tricks, tips, and troubleshooting

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

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

Derived from [Verify statistics from raw data](https://claude.com/resources/use-cases/verify-statistics-from-raw-data) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
