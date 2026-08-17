---
name: grant-proposal-assembly-line
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Grant proposal assembly line."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/grant-proposal-assembly-line
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Grant proposal assembly line — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Build a modular content library from your successful proposals and organizational materials then produce foundation-ready submissions in a fraction of the usual time.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need to build a grant proposal assembly line system to handle our 20+ annual grant applications more efficiently. We apply to foundations, government agencies, and corporate funders for youth programs, workforce development, and education initiatives. Start by creating a modular content library from the materials I'm providing: 3 recent successful proposals, our annual report, program one-pagers, and outcome data spreadsheets.

Step 1: Build the Content Library

Organize reusable modules including:

- Program descriptions (3 versions: brief/standard/detailed for each program)
- Need statements with current statistics and community data
- Organizational capacity sections (history, leadership, fiscal health)
- Evaluation methodologies and past outcome results
- Standard attachments (board list, audit, IRS letter)

Save everything to Google Drive in a "Grant Content Library" folder with clear naming conventions.

Step 2: Create First Proposal

Now generate a proposal for the Morrison Foundation Youth Innovation Grant ($75,000) using the library. The RFP requires:

- Executive summary (1 page)
- Problem statement linking to community needs (2 pages)
- Proposed program and innovation approach (3 pages)
- Budget with detailed narrative (2 pages)
- Logic model showing theory of change
- Evaluation plan with specific metrics

Pull relevant modules from the library, customize language to emphasize "innovation" and "youth voice" (their key priorities), and create new content where needed.

Step 3: Set Up the Assembly System

Create templates and tracking tools:

- Master tracking spreadsheet for all grants (deadlines, requirements, amounts, status)
- Funder research template to capture priorities before writing
- Module selection guide showing which content blocks work for different funder types
- Budget template that auto-calculates indirect costs and matches funder categories
- Email templates for submitting proposals and following up

Make this a true assembly line where I can produce proposals 60% faster by mixing and matching proven content.
```

## Inputs

- Google Drive integration
- Gmail integration
- Past successful proposals
- Program descriptions
- Organizational background documents
- Outcome data / impact reports
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Gmail
- Google Drive
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Step 1: Build the Content Library
2. Step 2: Create First Proposal
3. Step 3: Set Up the Assembly System

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

Derived from [Grant proposal assembly line](https://claude.com/resources/use-cases/grant-proposal-assembly-line) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
