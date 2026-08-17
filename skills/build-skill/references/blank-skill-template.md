# Blank skill template

Use when no catalog template matches the outcome on artifact type OR input sources.
Required: Outcome, Inputs, Workflow, Validation, Permissions (what it must never do
without a human), Setup. Everything else is included only when it changes behavior —
delete it otherwise. A section reading "n/a" is worse than no section: it costs the
runtime tokens and teaches the model that empty structure is acceptable.

```markdown
---
name: <kebab-case-name>
description: <What it produces and WHEN to invoke it, in the user's vocabulary.
  Include negative scope: "Do NOT use for <near-miss>.">
---

# <Skill title>

## Outcome
When <trigger>, produce <artifact> from <inputs>, meeting <bar>.

## Assumptions
<Only if the interview left decisions open. Each line: "ASSUMED: <decision> — <why>".
Delete the section when empty.>

## Required context
<Domain facts the model can't infer: conventions, thresholds, house style, jargon.>

## Inputs
<Exact paths/folders/formats expected at run time; behavior when missing/malformed.>

## Tools, connectors, APIs & authentication
<Each tool + what it's for + how it authenticates (connector OAuth / env-var NAME /
pre-authenticated CLI). Never credential values. Missing auth = stop and instruct.>

## Permissions
Reads: <...>  Writes: <...>
Never without human approval: <external sends, system-of-record writes, deletions,
payments, form submissions — plus skill-specific items>.

## Workflow
1. <gather> → 2. <process> → ... → n-1. <validate> → n. <deliver>
<Each step names its inputs and outputs.>

## Decision points
<Each fork + the rule that decides it. Default: prefer reversible; surface ambiguity.>

## Output

Shortest form that carries the result. No preamble, no restating the request, no
summary of the work performed. Expand only on request.

## Validation
<Checks run on the skill's OWN output before delivery. At least one mechanical check.>

## Failure modes & fallbacks
<Per dependency: failure signature → retry policy → degraded path → when to stop
and report.>

## Delegation
<Per the delegation policy (bundled with build-skill as
references/delegation-policy.md; restate the relevant rules inline so the generated
skill is self-contained). Either the per-step plan with the four contract
fields (context, output, validation, fallback) for each delegated task, or:
"Runs single-agent; no step meets the delegation bar." Parallelize only independent
work. Final review and sensitive actions stay with the primary agent.>

## Setup
<Everything the user must provision before first run: connectors to enable, files
to place, folder access to grant, env vars to set (names only).>
```
