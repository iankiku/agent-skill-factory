---
name: process-batches-of-vendors-with-cowork
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Process batches of vendors with Cowork."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Sonnet 4.5
  features: ["Cowork"]
  surface: "Cowork (with Claude in Chrome)"
  source_url: https://claude.com/resources/use-cases/process-batches-of-vendors-with-cowork
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Process batches of vendors with Cowork — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Onboard several vendors in one session — with Cowork, Claude can read a folder of vendor files, adds each to your tracker, generates their contracts, and fills multiple intake forms in your browser.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need to onboard several vendors. Their documents spread across my desktop. For each new vendor: Create an NDAs and MSAs from the templates, Fill out an onboarding form, Afterwards, add all information to the vendor tracker spreadsheet. Organize all the new documents on my desktop.
```

## Inputs

- Claude Desktop with Cowork capability
- Claude in Chrome installed and configured
- Vendor tracker spreadsheet
- Contract templates
- Vendor details documents
- Authenticated procurement portal access
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

1. Describe the task and desired end state in a Cowork session
2. Provide Claude context by selecting a folder with vendor tracker, contract templates, and vendor details
3. Claude works through onboarding in stages: updating spreadsheet, completing portal forms, generating agreements
4. Continue conversation to refine or expand (generate additional documents, organize vendor files)

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

Derived from [Process batches of vendors with Cowork](https://claude.com/resources/use-cases/process-batches-of-vendors-with-cowork) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
