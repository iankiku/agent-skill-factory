---
name: organize-files-by-whats-in-them
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Organize files across your desktop."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Opus 4.5
  features: ["Cowork"]
  surface: "Cowork"
  source_url: https://claude.com/resources/use-cases/organize-files-by-whats-in-them
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Organize files across your desktop — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Grant Cowork access to your cluttered desktop and walk away. It reads your files, figures out what they are, and sorts them into folders while you do something else.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Please help organize my desktop. Evaluate all of the scattered files and organize based on the contents inside of them.
```

## Inputs

- Claude Desktop app download
- Cowork feature access
- Desktop or folder access permissions
- Optional folder structure preferences and keep/archive/delete rules
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

1. Describe the task: Grant Claude desktop access; it evaluates scattered files and sorts them into clean folder structures
2. Give Claude context: Download Claude Desktop, start a Cowork session, grant desktop/folder access
3. What Claude creates: Scans desktop, categorizes files, creates folder structure with progress updates
4. Follow up prompts: Reorganize by custom logic, find lost files, create ongoing systems

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

Derived from [Organize files across your desktop](https://claude.com/resources/use-cases/organize-files-by-whats-in-them) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
