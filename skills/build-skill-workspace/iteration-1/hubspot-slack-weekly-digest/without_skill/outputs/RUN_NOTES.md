# RUN_NOTES — HubSpot ↔ Slack weekly closed-won digest

## What this is

A single stdlib-only Python script (`weekly_digest.py`) that replaces the
45-minute Monday-morning manual routine: pull last week's closed-won deals
from HubSpot, cross-reference them against whatever RevOps posted in
`#sales-metrics`, and draft the summary for `#sales-leadership`.

It is delivered as a plain CLI script rather than a packaged "Skill" —
this iteration intentionally does not use the skill-authoring tooling.
If you later want it wrapped as an installable Claude Skill (a `SKILL.md`
with frontmatter, etc.), that's a thin wrapper around the same script.

## Why a script instead of "just ask Claude to do it live each Monday"

Two reasons:

1. **The whole point is to stop missing deals.** A script that always runs
   the exact same HubSpot query and the exact same channel-history pull is
   less likely to silently skip a deal than a fresh ad-hoc read each week.
2. **Determinism + auditability.** Every run writes a dated draft to
   `digest_drafts/` and (if run via `run_weekly_digest.sh`) a log to
   `logs/`, so if leadership asks "why did last week's number not match,"
   there's a paper trail.

The script is still meant to be run *by* you (or by Claude Code on your
behalf) each Monday, not a fully unattended black box — see "Safety
defaults" below.

## How it works

1. **Week math**: on a Monday, "last week" = the Monday–Sunday span that
   ended yesterday. `--week-start YYYY-MM-DD` overrides this for
   backfilling or testing.
2. **HubSpot**: `POST /crm/v3/objects/deals/search` filtered on
   `dealstage = closedwon` and `closedate` within the target week,
   paginated, with owner IDs resolved to names via `/crm/v3/owners`.
3. **Slack**: `conversations.history` on `#sales-metrics` for the same
   window, paginated. Top-level messages only (see limitations).
4. **Parsing RevOps's post**: RevOps's message is free text, not a
   structured feed, so this is a best-effort regex parser matching a
   handful of common shapes (`"Acme Corp - $12,500"`, `"Acme Corp: $12,500"`,
   a bulleted/numbered variant, and a `"Total: $X"` line). Anything
   containing a `$` that doesn't match is surfaced under **"could not
   auto-parse"** rather than silently dropped.
5. **Cross-reference**: each HubSpot deal is matched to a RevOps line by
   fuzzy name match first, then by amount match, within configurable
   tolerances (`DEAL_NAME_MATCH_THRESHOLD`, `DEAL_AMOUNT_MATCH_TOLERANCE`
   in `.env`). Every deal/line ends up in exactly one of four buckets:
   matched-clean, amount-mismatch, in-HubSpot-only, in-RevOps-only.
6. **Digest**: a Slack-formatted (`mrkdwn`) summary listing the total,
   every deal, and — front and center, not buried — every discrepancy
   found in step 5.

## Assumptions made (no RevOps/VP available to confirm — flag these before first real run)

- **"Last week" = calendar Monday–Sunday**, based on the `closedate`
  property. If your team's week is Mon–Fri, or deals are tracked by
  "stage entered" date instead of `closedate`, adjust `last_full_week()`
  and the HubSpot filter property.
- **HubSpot closed-won stage ID is the default `"closedwon"`.** Custom
  pipelines often rename this — set `HUBSPOT_CLOSED_WON_STAGE_ID` in
  `.env` to your actual internal stage ID (visible via the deal-stage API
  or by inspecting a closed-won deal's `dealstage` property).
- **RevOps posts one message with one line per deal** (or a small number
  of messages). If RevOps instead posts a table, a Google Sheet link, a
  screenshot, or replies-in-thread, the parser won't see it — thread
  replies are intentionally not fetched in v1 to keep the Slack read
  scope minimal; add a `conversations.replies` pass if needed.
- **Matching is name-first, amount-second**, with a 60% fuzzy-match
  threshold and 1% amount tolerance. These are guesses tuned for
  "reasonable defaults," not your actual data — the first couple of real
  runs will tell you whether they're too loose (false matches) or too
  tight (everything ends up in the mismatch/missing buckets). Adjust via
  `.env`.
- **Bias toward over-flagging, not under-flagging.** The parser and
  matcher would rather put something in front of you to double-check
  (a false "discrepancy") than silently reconcile something that
  shouldn't have matched. This is deliberate given the original problem
  ("I always forget a deal or two") — false positives cost you 10 seconds
  of reading, false negatives cost you the whole reason this exists.
- **Deal amount = HubSpot's `amount` property** in your default currency;
  multi-currency deals aren't normalized.
- **Posting is opt-in.** Default behavior only ever writes a local draft
  and prints it — it never touches Slack unless you pass `--post`. This
  is a deliberate safety default until you've watched it run correctly a
  few times against real data.

## Setup

```bash
cd outputs/
cp .env.example .env
# fill in HUBSPOT_ACCESS_TOKEN, SLACK_BOT_TOKEN, and both channel IDs
export $(grep -v '^#' .env | xargs)
python3 weekly_digest.py            # dry run — writes/prints a draft only
python3 weekly_digest.py --post     # actually posts to #sales-leadership
```

No `pip install` needed — the script only uses the Python standard
library (`urllib`, not `requests`).

### Try it right now with zero credentials

```bash
python3 weekly_digest.py --sample
```

Runs the full pipeline against bundled fixtures in `sample_data/` that
deliberately include a matched deal, an amount mismatch, a deal missing
from RevOps's post, a deal RevOps mentioned that isn't in HubSpot yet,
and one unparseable line — so you can see every branch of the digest
without touching real APIs. This was run during development; output
matched expectations for all five cases.

### Scheduling it for Monday mornings

`run_weekly_digest.sh` wraps the script for unattended use: loads `.env`,
runs with `--post`, and logs to `logs/YYYY-MM-DD.log`. Exit code `2` means
"posted, but discrepancies were found — check the log before standup";
exit code `1`+ means it failed outright.

**macOS (launchd)** — recommended over cron on macOS since it survives
sleep/wake better. Create
`~/Library/LaunchAgents/com.you.weekly-digest.plist` pointing `Program`
at the absolute path to `run_weekly_digest.sh`, with a `StartCalendarInterval`
of `{Weekday: 1, Hour: 7, Minute: 0}`, then
`launchctl load ~/Library/LaunchAgents/com.you.weekly-digest.plist`.

**cron** (simpler, works anywhere):
```
0 7 * * 1 /absolute/path/to/outputs/run_weekly_digest.sh
```

Either way: **watch the log for the first several Mondays.** The
parsing/matching heuristics need real RevOps message formats to validate
against — don't fully trust `--post` unattended until you've confirmed a
few weeks of correct output.

## Known limitations / good next steps

- Thread replies in `#sales-metrics` aren't read (only top-level messages).
- The RevOps free-text parser is a heuristic, not a real integration —
  if RevOps is open to it, the highest-leverage follow-up is asking them
  to post in one consistent format (or better, to a shared sheet/Notion
  table this script reads directly instead of regex-parsing chat).
  Once RevOps's actual message format is known, tighten `LINE_PATTERNS`
  in `weekly_digest.py` to it exactly rather than the generic guesses here.
- No retry/backoff beyond simple 429 handling; fine for weekly volumes.
- Deal ↔ Slack-mention matching has no persistence — if RevOps posts a
  correction later in the week in a *different* message, it's still
  picked up (message history is read for the whole week), but if they
  edit a message in place, Slack's `conversations.history` returns the
  edited text, which is what you want.
