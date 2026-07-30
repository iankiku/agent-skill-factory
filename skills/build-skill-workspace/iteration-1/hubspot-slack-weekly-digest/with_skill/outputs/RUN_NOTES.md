# Run notes — hubspot-slack-weekly-digest

Built by following `build-skill`'s five phases exactly, in a **non-interactive
evaluation run**: there was no live human to answer clarifying questions, so
every question that the skill's own process calls for was answered in-character
as the requesting user (a sales manager who owns the Monday #sales-leadership
post for their VP), and is flagged below wherever that happened. This is
explicit per the task's instructions — nothing here should be read as the
real user's actual preference, only the most reasonable default consistent
with what they said.

## Catalog template selection (Phase 2)

Read `references/template-index.md` and grepped for hubspot/slack/sales/deal/
crm/digest/pipeline hits. Candidates considered:

- `templates/sales/create-sales-reports/SKILL.md` — Sales category, HubSpot
  connector, "pull metrics from CRM, generate a report" artifact. **Selected
  as primary** — closest match on domain (sales/CRM) and connector (HubSpot).
- `templates/professional/build-a-daily-briefing-across-your-tools/SKILL.md`
  — Slack + cross-tool read, briefing artifact. **Selected as secondary** —
  borrowed for the Slack-channel-read → reconcile → channel-post mechanics,
  which `create-sales-reports` doesn't cover (it targets a single-connector
  report, not a cross-source reconciliation delivered to a channel).
- `templates/professional/generate-project-status-reports/SKILL.md` — read
  and rejected: closer on "multi-source reconciliation" shape but its domain
  (project/task tracker, Excel deliverable) and connector set (Gmail/Calendar/
  Drive/Slack) don't match a sales/HubSpot digest; would have meant discarding
  more of the template than reusing.
- Also cross-referenced the skill's own bundled worked example,
  `examples/example-1-weekly-pipeline-digest.md` — not a catalog template,
  but structurally the nearest analog (connector-heavy, Monday-morning, sales,
  digest to Slack). Its America/Chicago week-window convention and
  empty-success-trap failure mode were reused directly since no other
  precedent existed to contradict them.

This task's artifact (a closed-won reconciliation posted to a leadership
channel) is different enough from both catalog templates on its own — CRM
report vs. cross-tool briefing — that the draft borrows structure from both
rather than forcing a single one, per Phase 2's instruction not to force a
bad fit.

## Assumptions made (and why), answering Phase 1/3 questions myself

Per the task's instructions, I answered the interview in-character rather than
stalling. Using the skill's own "I don't know" protocol framing (would have
been 2–4 concrete options, then a labeled default after three attempts), here
is what I decided and why — these are also recorded as `ASSUMED:` lines inside
`SKILL.md`'s Assumptions section, per Phase 5 step 1:

1. **Week window** — Mon 00:00–Sun 23:59, America/Chicago. No timezone was
   stated; picked the only available precedent (the bundled example) rather
   than inventing a new one. Mon–Sun (not Mon–Fri) because HubSpot close dates
   aren't restricted to business days — a Mon–Fri cut would recreate the
   "missed a deal" bug for any weekend auto-close.
2. **"Closed-won" pipeline scope** — ALL HubSpot pipelines, not just the
   default one. Chosen because scoping to one pipeline is exactly the kind of
   silent under-count that causes the "forgot a deal" complaint that started
   this request. Flagged as a Setup step to confirm on first real run, since
   getting this wrong is the highest-cost mistake this skill could make.
3. **How to find RevOps' numbers in #sales-metrics** — by content/keyword
   search in the last 7 days of the channel, not a fixed time or exact
   phrasing, since the user described RevOps "posting" without specifying a
   schedule or format.
4. **Delivery mechanics** — single channel post to #sales-leadership, no VP
   @mention. The user said "write up a short summary post," which reads as a
   channel post the VP will see in the normal course of reading that channel,
   not a targeted ping.
5. **Digest fields per deal** — name, amount, close date, owner. This is the
   minimum needed to answer "did we miss a deal," and mirrors what a person
   would manually copy from HubSpot; no segmentation (e.g., by deal size or
   segment) was requested, so none was added — avoiding scope creep beyond
   what replaces the current 45-minute manual process.

None of these needed a third retry to reach a default — each had a single
clearly-most-reasonable reading given the task description, so no decision
was left fully open; all five are still labeled `ASSUMED:` in the skill so the
first live run can correct any of them in one pass, per the checklist.

## Phase-by-phase adherence

- **Phase 1 (pin the outcome):** all four slots filled — trigger (Monday
  morning, on request or optional schedule), artifact (one #sales-leadership
  message), inputs (HubSpot closed-won deals + #sales-metrics RevOps figures),
  bar (zero missed deals + explicit, non-silent reconciliation). Scope edges
  defined: no forecasting/pipeline skill, no HubSpot writes, no DMs, no comp
  math.
- **Phase 2 (template selection):** done as above — primary + secondary
  template, reasoning stated, one rejected candidate noted with why.
- **Phase 3 (machinery):** every sub-item specified — required context,
  inputs w/ missing-data behavior, tools/connectors/auth (names only, zero
  credential values), permissions (read/write/never-without-approval),
  6-step workflow (gather → gather → reconcile → compose → validate →
  deliver), 5 decision points each with a deciding rule (no "use judgment"
  forks), validation with two mechanical checks (row-count match, recomputed
  sum match) plus a traceability check, and failure modes for every
  dependency (HubSpot query/connector, Slack read, Slack write, validation
  itself) each with a retry policy, degraded path, and stop condition.
- **Phase 4 (delegation):** table with all four steps assessed; two delegated
  (HubSpot fetch, RevOps-figure extraction — both self-contained,
  independent, parallelizable) each with the full context/output/validation/
  fallback contract; reconciliation and composition/posting kept on the
  primary per policy (judgment-heavy and sensitive-action respectively).
- **Phase 5 (draft/validate/refine):** drafted the full SKILL.md, then
  self-checked it line-by-line against `references/validation-checklist.md`
  (triggering, outcome/inputs, tools/auth, safety/permissions, workflow
  quality, delegation, attribution/hygiene — every box addressed; added an
  explicit `## Attribution` section to satisfy the catalog-derivation check).
  Ran one dry-run trace (below) and found no gaps requiring a redraft, so no
  further refinement round was needed. Because this is a non-interactive run,
  the "present to user, ask for corrections" step of Phase 5.4 was simulated
  by the self-check above rather than skipped — there is no live round to
  report back from.

## Dry-run trace (Phase 5.3)

Scenario: skill runs Monday 2026-08-03, digesting the week of
2026-07-27–2026-08-02 (America/Chicago).

1. HubSpot fetch (delegated) returns 9 closed-won deals across 2 pipelines,
   schema-valid; one deal (`Acme Renewal`) has no `owner` field populated.
   Primary checks array length (9) against HubSpot's own reported total (9)
   → pass.
2. RevOps-figure extraction (delegated, parallel) scans #sales-metrics,
   finds RevOps' Monday 7:15am message: "Closed-won last week: 8 deals,
   $142,300." Returns `{count: 8, revenue: 142300, source_message_ts: ...}`.
   Primary spot-checks the figure against the quoted message text → pass.
3. Reconciliation (primary): HubSpot = 9 deals / $151,800 vs. RevOps = 8
   deals / $142,300 → `mismatch`, delta = 1 deal / $9,500. Not resolved
   automatically — flagged for the post.
4. Composition (primary): 9 deal rows (Acme Renewal shown with "no owner on
   file," not dropped), a totals line ($151,800 / 9 deals), and a
   reconciliation line stating both figures and the delta.
5. Validation: row count 9 == HubSpot query count 9 ✓. Recomputed sum of the
   9 listed amounts = $151,800, matches HubSpot's own aggregate ✓.
   Traceability: reconciliation line cites the RevOps message timestamp ✓.
   All checks pass.
6. Delivery: one message posted to #sales-leadership containing the 9-deal
   list, totals, and the explicit mismatch line. Trace ends — no HubSpot
   writes, no DMs, no second post.

This trace surfaced no gap that required revising the draft (the missing-
owner and mismatch paths both exercised cleanly against the decision points
already written), so Phase 5 completed after one pass.

## Install note

Drop this folder's `SKILL.md` into `.claude/skills/hubspot-slack-weekly-digest/`
for Claude Code, or upload `SKILL.md` directly as a custom skill in claude.ai /
Cowork. Before first use, complete the five Setup steps in `SKILL.md`
(enable HubSpot + Slack connectors with the stated read/write scopes, confirm
pipeline scope, optionally schedule the Monday run, and review the Assumptions
section with the actual user).
