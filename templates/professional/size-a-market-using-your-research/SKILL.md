---
name: size-a-market-using-your-research
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Size a market using your research."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/size-a-market-using-your-research
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Size a market using your research — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

With Cowork, ask Claude a market question and get back an analysis with professional deliverables.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need a market sizing analysis for the enterprise project management software space in North America.

Include TAM/SAM/SOM calculations with your methodology, key market drivers and growth projections, competitive landscape overview, and investment implications.

Output as:

- Executive PowerPoint (10-12 slides)
- Excel workbook with detailed calculations
- Markdown source document with all citations

Source all claims.
```

## Inputs

- Claude Desktop (download required)
- Cowork session/workspace access
- Optional: existing research, analyst reports, internal data files
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

1. Describe the task (provide market details and specify desired outputs)
2. Give Claude context (upload existing research or company data via folder/files)
3. What Claude creates (generates three coordinated deliverables)
4. Follow up prompts (drill into segments, build sensitivity models, generate competitor profiles)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Size a market using your research](https://claude.com/resources/use-cases/size-a-market-using-your-research) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
