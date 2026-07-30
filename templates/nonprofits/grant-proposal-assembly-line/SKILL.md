---
name: grant-proposal-assembly-line
description: "Build a modular content library from your successful proposals and organizational materials then produce foundation-ready submissions in a fraction of the usual time. Use for tasks like “Grant proposal assembly line” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/grant-proposal-assembly-line
  source_title: Grant proposal assembly line
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Grant proposal assembly line — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Build a modular content library from your successful proposals and organizational materials then produce foundation-ready submissions in a fraction of the usual time.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- Google Drive integration
- Gmail integration
- Past successful proposals
- Program descriptions
- Organizational background documents
- Outcome data / impact reports
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Gmail
- Google Drive
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

1. Step 1: Build the Content Library
2. Step 2: Create First Proposal
3. Step 3: Set Up the Assembly System

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

Derived from [Grant proposal assembly line](https://claude.com/resources/use-cases/grant-proposal-assembly-line) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
