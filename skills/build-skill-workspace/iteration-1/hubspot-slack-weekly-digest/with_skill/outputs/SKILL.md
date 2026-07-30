---
name: hubspot-slack-weekly-digest
description: >-
  Compose and post a Monday-morning closed-won deals summary to #sales-leadership,
  built from last week's HubSpot closed-won deals reconciled against the sales
  numbers RevOps posts in #sales-metrics. Use when the user asks for their weekly
  deal digest / Monday sales summary, or says things like "run my Monday digest",
  "post last week's closed-won deals", or "reconcile HubSpot against RevOps'
  numbers". Do NOT use for open-pipeline/forecast digests (see the separate
  weekly-pipeline-digest skill), for commission or comp calculations, or for
  editing/creating anything in HubSpot.
---

# HubSpot × Slack weekly deal digest

## Outcome

Every Monday morning (on request, or an optional scheduled run before the 9am
standup), produce ONE message posted to **#sales-leadership** summarizing last
week's HubSpot closed-won deals, reconciled against the weekly numbers RevOps
posts in **#sales-metrics**, such that every closed-won deal for the window
appears exactly once and any mismatch between HubSpot's count/total and RevOps'
posted figures is called out explicitly rather than silently dropped, averaged,
or hidden.

The bar this replaces: 45 minutes of manual copy-pasting that regularly missed
a deal or two. "Good" = zero missed deals, a mechanical reconciliation, not a
prettier report.

**Scope edges — this skill does NOT:**
- Cover open/in-progress pipeline, forecasting, or quota attainment (that's a
  different outcome — build a separate `weekly-pipeline-digest` skill for it).
- Write, edit, or create anything in HubSpot.
- Edit, delete, or react to RevOps' Slack message — it only reads it.
- DM the VP or any individual rep — it posts once, to the channel, and stops.
- Compute commission, comp, or payout numbers from the deal data.

## Assumptions

Decisions below were made under the "I don't know" protocol during a
non-interactive build (no live user available to answer follow-ups). Each is
labeled so the first real run can correct it in one pass — see Setup step 5.

- `ASSUMED: week window = prior Monday 00:00 through Sunday 23:59, America/Chicago`
  — chosen because it is the standard Monday-morning sales-week cut and matches
  the only other precedent available (the bundled weekly-pipeline-digest
  example); HubSpot deal close dates aren't restricted to business days, so a
  Mon–Fri window would silently under-count weekend auto-closes.
- `ASSUMED: "closed-won" = deals in ALL HubSpot pipelines whose stage maps to
  the pipeline's closed-won stage`, not just the default pipeline — chosen
  because under-scoping to one pipeline recreates the exact "forgot a deal"
  failure this skill exists to fix. If the org uses one pipeline, this is a
  no-op; if it uses several, confirm at Setup step 3.
- `ASSUMED: RevOps' post is located by content (a message in #sales-metrics
  in the same week window containing weekly deal-count/revenue figures),
  not by a fixed time or exact phrasing` — RevOps' posting time/format wasn't
  specified, and a keyword/time-window search is more robust than assuming a
  fixed schedule.
- `ASSUMED: the post is a single channel message, no @mention of the VP by
  name` — the VP reads #sales-leadership directly; add an @mention in Setup
  if the VP wants to be tagged.
- `ASSUMED: deal fields shown = deal name, amount, close date, owner` — this
  is the minimum needed to answer "did we miss one" and matches what a person
  copy-pastes manually today; no segmentation (Enterprise/Mid-Market/SMB) was
  requested, so none is added.

## Required context

- HubSpot stage vocabulary: "closed-won" = the terminal won stage in whichever
  pipeline(s) the org uses (see Assumptions — confirm pipeline scope once).
- Week = Monday–Sunday, America/Chicago (see Assumptions).
- RevOps posts weekly numbers in #sales-metrics; format is prose/plain numbers,
  not a fixed template — the skill must extract figures from natural text, not
  expect a parseable schema.
- Destination: #sales-leadership. Source-of-truth-for-numbers channel:
  #sales-metrics (read-only).

## Inputs

- HubSpot connector: deals with stage = closed-won and close date inside last
  week's window (all pipelines per Assumptions). Empty result → do not report
  "no closed-won deals" without first sanity-checking the window and pipeline
  scope (see Failure modes).
- Slack #sales-metrics: messages from the last 7 days, filtered to RevOps'
  weekly-numbers post. Not found → proceed in degraded mode (see Failure modes),
  never block the whole digest on it — the VP still needs an update before 9am.
- No files/folders; connector-only.

## Tools, connectors, APIs & authentication

- **HubSpot** — connector OAuth, read-only. Used to query closed-won deals.
- **Slack** — connector OAuth. Read access to #sales-metrics; write access
  (one message) to #sales-leadership.
- If either connector is unauthenticated or disabled, STOP and tell the user
  exactly which connector to enable — never ask for or accept a pasted API
  key/token as a substitute, and never fabricate figures to work around it.

## Permissions

- **Reads:** HubSpot closed-won deals (last 7 days, all pipelines); Slack
  #sales-metrics messages (last 7 days).
- **Writes:** exactly one message to #sales-leadership.
- **Never without explicit human approval:** writing/editing HubSpot records;
  posting to any channel other than #sales-leadership; DMing the VP or any
  rep; editing or deleting RevOps' message; re-posting if the first post
  already succeeded (no duplicate posts on retry).

## Workflow

1. **Gather deals** — query HubSpot for closed-won deals with close date in
   last week's window (all pipelines). Output: a deal list (id, name, amount,
   close date, owner), each field present-or-explicitly-missing.
2. **Gather RevOps figures** — read #sales-metrics for the last 7 days;
   extract RevOps' stated weekly deal count and/or revenue total, if present.
   Output: `{count, revenue}` or `not_found`.
   *(Steps 1 and 2 are independent — different connectors, no shared state —
   and run in parallel; see Delegation.)*
3. **Reconcile** — compare HubSpot's deduped count/total against RevOps'
   figures (if found). Output: `match` / `mismatch(details)` / `revops_missing`.
4. **Compose the digest** — deal-by-deal list (name, amount, close date, owner
   — "none on file" for any missing field, never a dropped row), a totals line,
   and the reconciliation line from step 3.
5. **Validate** — run the mechanical checks below on the composed digest
   before it goes anywhere.
6. **Deliver** — post the digest as one message to #sales-leadership.

## Decision points

- **HubSpot count/total ≠ RevOps count/total** → state both numbers and the
  delta explicitly in the post ("HubSpot: 9 deals / $151.8K — RevOps: 8 deals
  / $142.3K — mismatch, needs reconciliation"). Never average them, never
  silently prefer one source, never edit either system to make them agree.
- **RevOps hasn't posted numbers yet when the skill runs** → post the
  HubSpot-only digest with a banner: "RevOps weekly numbers not yet posted —
  reconcile manually when available." Do not delay the post past what the
  user needs before standup.
- **A closed-won deal is missing amount or owner** → include the deal with
  "no amount on file" / "no owner on file"; never drop a row for missing
  data — dropping rows is the exact failure this skill replaces.
- **Multiple HubSpot pipelines** → include closed-won deals from ALL
  pipelines by default (see Assumptions); if the user has confirmed a
  narrower scope at Setup, use that instead.
- **A deal's amount is $0 or negative** (e.g., a comped/free deal) → include
  it, flagged as "$0 — verify," rather than silently excluding it from the
  count (silent exclusion is how deals get "forgotten").

## Validation

- **Mechanical:** digest row count == deduped count of closed-won deals
  returned by the HubSpot query for the window. This is the primary check —
  it directly targets "I always forget a deal or two."
- **Mechanical:** sum of listed deal amounts, recomputed from the digest rows,
  equals the HubSpot query's own aggregate for the window (catches transcription
  errors during composition, not just missing rows).
- **Traceability:** every number in the reconciliation line traces to either
  the HubSpot query result or a quoted/paraphrased figure from a specific
  RevOps Slack message — no invented or interpolated numbers.
- Any check failing twice → stop; do not post; report exactly what failed
  (see Failure modes).

## Failure modes & fallbacks

- **HubSpot query returns zero deals** → before reporting "no closed-won
  deals last week," re-check the date window and pipeline scope (empty-success
  trap — an empty result is far more likely a bad filter than a genuinely
  dealless week). If still empty after the check, report it explicitly as
  zero, not as an error.
- **HubSpot connector unauthenticated/unreachable** → stop, name the
  connector, do not proceed with stale or fabricated data. Retry once; if
  still failing, surface to the user.
- **#sales-metrics unreadable, or no RevOps weekly-numbers message found** →
  degrade: post the HubSpot-only digest with the "not yet posted / reconcile
  manually" banner. Do not block the whole run — the time-critical bar (ready
  before 9am) outweighs waiting on RevOps.
- **Slack post to #sales-leadership fails** → do not silently drop the work;
  output the fully composed digest text in-conversation along with the error,
  so the user can hand-paste it before standup.
- **Validation fails twice** (row count or sum mismatch after recompute) →
  stop, report exactly which check failed and by how much, and do not post an
  unvalidated digest.

## Delegation

Per `references/delegation-policy.md` (restated here so this skill is
self-contained):

| Step | Decision | Contract |
|---|---|---|
| Fetch + normalize HubSpot closed-won deals | **Delegate** (smaller model, single task) | Context: pipeline id(s), stage id(s), date window. Output: JSON array `{id, name, amount, close_date, owner}` for every matching deal, missing fields explicit as `null`. Validation: primary checks array length against the HubSpot API's own reported total for the query. Fallback: retry once; on repeat failure, primary runs the query directly. |
| Extract RevOps' weekly figures from #sales-metrics | **Delegate** (smaller model, single task, runs in parallel with the HubSpot fetch — independent connector, no shared state) | Context: the last 7 days of #sales-metrics messages. Output: `{count: int\|null, revenue: number\|null, source_message_ts: string\|null}` or `{found: false}`. Validation: primary spot-checks the extracted figures against the quoted source message before using them. Fallback: if extraction is ambiguous or no candidate message exists, return `{found: false}` — never guess a number. |
| Reconcile HubSpot vs. RevOps figures | **Primary** | Judgment call on what counts as a "mismatch" worth flagging (e.g., rounding vs. a real gap); errors here reach the VP directly, so this stays with the primary agent. |
| Compose digest + post to #sales-leadership | **Primary, always** | Synthesis of the deliverable and the only write/send action in the whole skill — never delegated, per policy. |

Parallelization: only steps 1 and 2 (HubSpot fetch, RevOps extraction) — they
touch different connectors and neither depends on the other's output. The
primary merges both results and runs reconciliation + validation before
composing anything.

## Setup

1. Enable the **HubSpot** connector (read access to deals).
2. Enable the **Slack** connector with read access to **#sales-metrics** and
   post access to **#sales-leadership**.
3. Confirm HubSpot pipeline scope: if the org uses more than one pipeline,
   confirm whether ALL should count toward "closed-won" (current default) or
   only a named subset.
4. Optional: schedule "run hubspot-slack-weekly-digest" for Monday mornings
   (e.g., 7:30 America/Chicago) ahead of the 9am standup, instead of running
   it on request each week.
5. First live run: review the Assumptions section above with the user and
   correct any `ASSUMED:` line that doesn't match reality (especially the
   week-window timezone and whether the VP wants an @mention).

## Attribution

Structure and validation defaults adapted from two catalog templates in this
repository's `templates/` tree: primary —
[Create sales reports](https://claude.com/resources/use-cases/create-sales-reports)
(`templates/sales/create-sales-reports/SKILL.md`, Sales category, HubSpot
connector); secondary, for the Slack read/reconcile/post mechanics —
[Build a daily briefing across your tools](https://claude.com/resources/use-cases/build-a-daily-briefing-across-your-tools)
(`templates/professional/build-a-daily-briefing-across-your-tools/SKILL.md`).
Seed prompts and workflow content on those source pages are © Anthropic PBC;
all domain-specific content in this file (outcome, assumptions, decision
points, validation, delegation contracts) is original to this build.
