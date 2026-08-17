---
name: chart-your-data-before-you-commit
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Chart your data in conversation with Claude before you commit to a reading."
metadata:
  status: template — resolve every TODO before use
  category: Education
  recommended_model: Sonnet 4.6
  features: ["Custom visuals"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/chart-your-data-before-you-commit
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Chart your data in conversation with Claude before you commit to a reading — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Upload a CSV and Claude builds the correlation grid inline, flagging the patterns worth a second look. The flags are a starting point — you click into what's interesting and the conversation goes from there.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Show me what this data is telling me. I'm looking for the strongest relationships in here. Can you give me a correlation matrix and let me click into any pair to see the scatter? Flag anything that surprises you. Don't hold back on making this readable; I'm presenting this to a committee.
```

## Inputs

- CSV file upload
- Google Drive connector (optional, for Google Sheets access)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Google Drive
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task: Upload data and ask Claude to show relationships
2. Give Claude context: Upload the CSV file as required context
3. What Claude creates: Builds correlation grid with flagged patterns
4. Follow up prompts: Click into visuals for deeper analysis, ask Claude to write reports, quiz yourself on findings

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Chart your data in conversation with Claude before you commit to a reading](https://claude.com/resources/use-cases/chart-your-data-before-you-commit) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
