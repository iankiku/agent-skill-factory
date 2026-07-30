# End-to-end example 1: weekly pipeline digest (connector-heavy)

A condensed but complete transcript of a `build-skill` run, showing the interview,
the "I don't know" protocol producing a labeled assumption, template selection,
the delegation decision, a dry-run trace, and the final generated skill.

---

## Phase 1 — Pin the outcome

**Agent:** What should exist after a run that doesn't exist before it?

**User:** A digest of my sales pipeline I can skim Monday morning.

**Agent (AskUserQuestion):** Where should the digest land? — options: *Slack DM to
you (recommended)* / *Email draft* / *Markdown file in a folder*

**User:** Slack DM.

**Agent (AskUserQuestion):** What makes a digest GOOD vs. merely complete?

**User:** I don't know, honestly.

**Agent (retry 1, options):** Pick the closest bar: *A) Every open deal >$10k
appears with stage + next step* / *B) Only deals that CHANGED last week appear* /
*C) Top 5 deals by size, whatever their state*

**User:** Don't know. Maybe B? Not sure.

**Agent (retry 2, options):** B with a floor, then? *B1) Changed deals only, any
size* / *B2) Changed deals plus anything closing this month (recommended)*

**User:** No idea, you pick.

**Agent:** Three attempts reached — proceeding with B2 as a labeled assumption.

> Draft gains: `ASSUMED: digest bar = deals changed last week + anything closing in
> the current month — chosen because "changed + closing soon" is the standard
> Monday-review cut and avoids a size threshold the user hasn't defined.`

**Outcome sentence:** *When the user asks for their pipeline digest (or Monday 8am
scheduled run), produce a Slack DM digest from HubSpot deal data and last week's
call notes, covering deals changed last week plus deals closing this month, each
with stage, delta, and next step.*

Scope edge: does NOT handle forecasting or quota math — refuse and suggest a
separate skill.

## Phase 2 — Template selection

From `references/template-index.md`, closest on artifact (recurring cross-tool
briefing) and inputs (CRM connector): **`templates/professional/build-a-daily-briefing-across-your-tools/SKILL.md`**,
with the validation defaults borrowed from `templates/sales/prepare-for-sales-deals/SKILL.md`
(CRM writes drafted-not-committed). Told the user in one sentence; no objection.

## Phase 3 — Machinery (as captured in the draft)

- **Context:** "stage" vocabulary = HubSpot default pipeline; "next step" = the deal's
  open task with nearest due date; user's working week = Mon–Fri America/Chicago.
- **Inputs:** HubSpot deals (connector), Fireflies call summaries from the last 7 days
  (connector). No files.
- **Auth:** both via platform connectors — if either is unauthenticated, stop and name
  the connector; never ask for tokens.
- **Permissions:** read-only on both connectors; the ONLY write is the Slack DM to the
  user themself. Never messages anyone else, never writes to HubSpot.
- **Decision point:** deal appears in both "changed" and "closing this month" → list
  once, under "closing", tagged with the change.
- **Validation (mechanical):** count of deals in digest == count returned by the two
  queries after dedupe; every deal line contains all three fields (stage, delta, next
  step) — checked by pattern, not by eye.
- **Failure modes:** HubSpot query empty → verify pipeline ID before concluding "no
  changes" (empty-success trap); Fireflies down → send digest anyway with a "call
  notes unavailable" banner (degraded path); Slack send fails → deliver digest text
  in-conversation and say why.

## Phase 4 — Delegation plan

Two candidate fan-outs assessed against `references/delegation-policy.md`:

| Step | Decision | Why |
|---|---|---|
| Fetch + normalize HubSpot deals | **Delegate** (small model) | Mechanical, self-contained. Context: query params + field list. Output: JSON array with fixed schema. Validation: schema check + count vs. API total. Fallback: retry once, then primary fetches inline. |
| Summarize each call transcript | **Delegate** (small model, parallel per call) | Independent per item — no shared state. Context: one transcript + deal name. Output: ≤2-sentence summary + explicit next step or "none stated". Validation: primary spot-checks 2 random summaries against transcripts. Fallback: skip that call, note the gap in the digest. |
| Match calls → deals | **Primary** | Judgment call on fuzzy names; errors here corrupt everything downstream. |
| Compose + send digest | **Primary** | Synthesis and the only write action — never delegated. |

Parallelization: only the per-call summaries fan out. Merge and validation happen
before composition.

## Phase 5 — Dry-run trace (shown to user)

Input: week of 2026-07-20; HubSpot returns 14 changed deals, 3 closing in July
(1 overlap → 16 after dedupe); Fireflies returns 6 calls, 1 transcript empty.

1. Fetch task returns 16 deals, schema-valid, count matches → pass.
2. 6 summary tasks fan out; empty transcript hits fallback → 5 summaries + 1 gap note.
3. Primary matches 4 calls to deals; 1 unmatched call listed under "unattached calls".
4. Validation: 16 lines in digest == 16 deals ✓; field-pattern check flags one deal
   missing a next step → rendered as "next step: none on file" rather than dropped.
5. DM sent to user only. Trace ends.

User corrected one thing after seeing the trace: unattached calls should be top of
the digest, not bottom. One refinement round; checklist re-run; accepted.

---

## Final generated skill

```markdown
---
name: weekly-pipeline-digest
description: Compose and DM a Monday-morning sales pipeline digest from HubSpot and
  Fireflies. Use when the user asks for their pipeline digest or the Monday 8am
  scheduled run fires. Do NOT use for forecasting, quota math, or updating deals.
---

# Weekly pipeline digest

## Outcome
When invoked (on request or Monday 8:00 America/Chicago), produce a Slack DM to the
user digesting HubSpot deals changed in the last 7 days plus deals closing this
month, each with stage, what changed, and next step, with last week's call summaries
attached to their deals.

## Assumptions
ASSUMED: digest bar = deals changed last week + anything closing in the current
month — standard Monday-review cut; user declined to set a size threshold.

## Required context
- Pipeline vocabulary = HubSpot default stages; "next step" = open task with nearest
  due date; week = Mon–Fri America/Chicago.

## Inputs
- HubSpot connector: deals modified in last 7 days; deals with close date in current
  month. Empty result → verify pipeline ID before reporting "no changes".
- Fireflies connector: meetings from last 7 days. Unavailable → proceed with banner.

## Tools, connectors & authentication
- HubSpot (connector OAuth, read-only) — deal queries.
- Fireflies (connector OAuth, read-only) — transcripts.
- Slack (connector OAuth) — one DM to the user. If any connector is unauthenticated,
  stop and name it. Never request or store credentials.

## Permissions
Reads: HubSpot deals/tasks, Fireflies meetings. Writes: one Slack DM to the user.
Never without approval: messaging anyone other than the user, any HubSpot write,
any channel post.

## Workflow
1. Query HubSpot (changed-7d; closing-this-month) → dedupe → deal list.
2. Fetch last week's Fireflies meetings → per-call summaries (delegated, parallel).
3. Match summaries to deals by company/contact name (primary; fuzzy matches flagged).
4. Compose digest: unattached calls first, then closing-this-month, then changed.
5. Validate (below), then DM the user.

## Decision points
- Deal in both buckets → list once under "closing", tagged with its change.
- Call matches no deal → "unattached calls" section at TOP of digest.
- Fuzzy name match < confident → include under unattached rather than guess.

## Validation
- Digest line count == deduped deal count (mechanical).
- Every deal line matches the `stage | delta | next step` pattern; missing next step
  renders as "none on file", never dropped (mechanical pattern check).
- Spot-check 2 random call summaries against transcripts before composing.

## Failure modes & fallbacks
- HubSpot empty → pipeline-ID sanity check, then report "no changes" explicitly.
- Fireflies down → send digest with "call notes unavailable" banner.
- Slack send fails → output digest in-conversation with the error.
- Any validation failure twice → stop, report what failed, send nothing.

## Delegation
Per the delegation policy this skill was built under (rules restated here so the
skill is self-contained): HubSpot fetch/normalize and per-call summaries are
delegated to a smaller model (contracts above — context, output, validation,
fallback each defined); per-call summaries are the only parallel fan-out
(independent items). Matching, composition, validation, and the Slack send stay
with the primary agent.

## Setup
1. Enable HubSpot, Fireflies, and Slack connectors.
2. Confirm HubSpot pipeline ID if not using the default pipeline.
3. Optional: schedule "run weekly-pipeline-digest" Mondays 8:00 America/Chicago.
```
