# Delegation policy

Every skill generated in this repository embeds a delegation decision: when does the
primary agent do the work itself, and when does it hand a task to a capability-matched
model or sub-agent? This document is the single source of truth; generated skills
reference it and specialize its defaults.

## The decision, in order

1. **Does the step require trust the sub-agent can't carry?** Sensitive actions —
   sending external communications, writing to systems of record, financial
   transactions, deleting/overwriting originals, submitting web forms, anything
   irreversible — are NEVER delegated. The primary agent performs them, after final
   review, with human approval where the skill demands it.
2. **Is the step the synthesis?** Final review, cross-checking sub-results against
   each other, and assembling the deliverable stay with the primary agent. A sub-agent
   never grades its own work into the final artifact.
3. **Is the step self-contained?** Delegate only when the task can be specified with a
   closed context slice (the sub-agent needs nothing it wasn't handed) and a closed
   output contract (the primary can validate the result without re-doing the work).
   If specifying the task takes longer than doing it, don't delegate.
4. **Does capability match cost?** Route mechanical, high-volume steps (per-file
   extraction, per-record formatting, bulk classification) to a smaller/faster model;
   route judgment-heavy steps (ambiguous classification, adversarial verification,
   domain reasoning) to the strongest available model. Default: inherit the primary's
   model when unsure.

## The contract every delegated task must define

A skill that delegates MUST specify, per delegated task — no exceptions:

| Field | Meaning |
|---|---|
| **Context** | The minimal input slice the sub-agent receives (files, records, instructions). Nothing implicit. |
| **Output** | The exact deliverable and format (schema, file path, or structured summary). |
| **Validation** | The check the PRIMARY agent runs on the returned result before using it (schema-valid? count matches? spot-check passes?). |
| **Fallback** | What happens when the task fails or returns empty: retry once, degrade to primary doing it inline, or surface to the user. |

## Parallelization

- Parallelize **only independent work**: tasks that share no mutable state and whose
  outputs don't feed each other. Per-item fan-out (one task per file/vendor/channel)
  is the canonical safe case.
- Anything sequential by nature — a step consuming the previous step's output —
  runs in order, no barrier games.
- After a parallel fan-out, the primary agent merges, dedupes, and validates the
  results before anything downstream uses them.

## What stays with the primary agent — always

- Final review of the assembled deliverable against the skill's validation criteria
- All sensitive actions (list above), each behind explicit user approval when the
  skill touches external systems
- Secrets and credentials: sub-agents never receive tokens, keys, or passwords;
  connectors authenticate at the platform layer, and skills never proxy credentials
- The decision to stop: when validation fails twice, the primary halts and reports
  rather than delegating a third attempt
