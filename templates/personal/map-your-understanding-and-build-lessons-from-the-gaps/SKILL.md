---
name: map-your-understanding-and-build-lessons-from-the-gaps
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Map your understanding and build lessons from the gaps."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Opus 4.6
  features: ["Extended Thinking"]
  surface: "Claude.ai chat (with optional Claude Desktop/Cowork and Claude in Excel for follow-up work)"
  source_url: https://claude.com/resources/use-cases/map-your-understanding-and-build-lessons-from-the-gaps
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Map your understanding and build lessons from the gaps — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude Opus 4.6 traces your confusion to its source. It maps what you already understand, finds the specific misconception underneath, and builds personalized learning experiences around it.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I keep running into 'Bayesian reasoning' in things I read—essays, podcasts, even conversations at work. People say 'update your priors' or 'you're ignoring the base rate' and I nod along, but I can't actually follow the logic when it gets specific. I understand basic probability fine. I can calculate odds, I know what a conditional probability is in the abstract. But when someone explains why a 99% accurate test doesn't mean a 99% chance you're sick, I lose the thread halfway through. Help me understand this. Then build me an interactive lesson, a workbook I can use to audit which signals in my hiring pipeline actually predict success, and a concept map connecting it to what I'll encounter next.
```

## Inputs

- Extended Thinking feature (optional but recommended)
- CSV or XLSX export of screening/pipeline data (optional, for personalized workbook)
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

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

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

Derived from [Map your understanding and build lessons from the gaps](https://claude.com/resources/use-cases/map-your-understanding-and-build-lessons-from-the-gaps) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
