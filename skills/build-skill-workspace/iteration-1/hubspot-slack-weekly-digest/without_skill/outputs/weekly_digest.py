#!/usr/bin/env python3
"""
weekly_digest.py — Monday-morning closed-won sales digest.

Automates the manual workflow:
  1. Pull last week's closed-won deals out of HubSpot.
  2. Pull RevOps's posted numbers from the #sales-metrics Slack channel.
  3. Cross-reference the two (catch deals RevOps didn't mention, deals HubSpot
     doesn't have yet, and dollar-amount mismatches).
  4. Draft (or, with --post, actually send) a short summary to #sales-leadership.

Design goals:
  - Pure stdlib (urllib), so there is nothing to `pip install` to try it.
  - Safe by default: always writes a local draft; only touches Slack with --post.
  - --sample mode runs the entire pipeline against bundled fixture data so it can
    be exercised (and its output inspected) with zero credentials.
  - Discrepancies are surfaced explicitly and loudly — the whole point is to stop
    silently dropping a deal or two, so mismatches are never resolved silently.

Usage:
  # First real run, dry-run (writes a draft, does not post to Slack):
  python3 weekly_digest.py

  # Actually post the digest to #sales-leadership:
  python3 weekly_digest.py --post

  # Try it right now with no credentials at all:
  python3 weekly_digest.py --sample

  # Re-run for an arbitrary week (Monday date, inclusive) instead of "last week":
  python3 weekly_digest.py --week-start 2026-07-20

See RUN_NOTES.md in this directory for setup, assumptions, and scheduling.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

HERE = Path(__file__).resolve().parent

# --------------------------------------------------------------------------
# Configuration (env vars, with sane defaults). Copy .env.example to .env and
# `export $(grep -v '^#' .env | xargs)` before running, or set these in your
# shell/cron/launchd environment directly.
# --------------------------------------------------------------------------

HUBSPOT_ACCESS_TOKEN = os.environ.get("HUBSPOT_ACCESS_TOKEN", "")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")

SLACK_SALES_METRICS_CHANNEL_ID = os.environ.get("SLACK_SALES_METRICS_CHANNEL_ID", "")
SLACK_SALES_LEADERSHIP_CHANNEL_ID = os.environ.get("SLACK_SALES_LEADERSHIP_CHANNEL_ID", "")

HUBSPOT_PIPELINE_ID = os.environ.get("HUBSPOT_PIPELINE_ID", "")  # optional filter
HUBSPOT_CLOSED_WON_STAGE_ID = os.environ.get("HUBSPOT_CLOSED_WON_STAGE_ID", "closedwon")

# How close two dollar amounts must be (relative) to count as "the same deal".
AMOUNT_MATCH_TOLERANCE = float(os.environ.get("DEAL_AMOUNT_MATCH_TOLERANCE", "0.01"))  # 1%
# How similar two names must be (0-1, difflib ratio) to count as the same deal.
NAME_MATCH_THRESHOLD = float(os.environ.get("DEAL_NAME_MATCH_THRESHOLD", "0.6"))

HUBSPOT_API_BASE = "https://api.hubapi.com"
SLACK_API_BASE = "https://slack.com/api"

DRAFTS_DIR = HERE / "digest_drafts"


# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------

@dataclass
class Deal:
    id: str
    name: str
    amount: Optional[float]
    close_date: Optional[str]
    owner: str = "Unassigned"

    @property
    def amount_display(self) -> str:
        return f"${self.amount:,.2f}" if self.amount is not None else "amount unknown"


@dataclass
class RevOpsLine:
    raw_text: str
    label: str
    amount: Optional[float]


@dataclass
class MatchResult:
    matched: list = field(default_factory=list)       # list[(Deal, RevOpsLine)]
    amount_mismatch: list = field(default_factory=list)  # list[(Deal, RevOpsLine)]
    missing_from_revops: list = field(default_factory=list)  # list[Deal]
    missing_from_hubspot: list = field(default_factory=list)  # list[RevOpsLine]


# --------------------------------------------------------------------------
# HTTP helper (stdlib only — no `requests` dependency)
# --------------------------------------------------------------------------

def _http(method: str, url: str, headers: dict, body: Optional[dict] = None,
          retries: int = 3) -> dict:
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    for k, v in headers.items():
        req.add_header(k, v)
    if data is not None:
        req.add_header("Content-Type", "application/json")

    last_err = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            body_text = e.read().decode("utf-8", errors="replace")
            if e.code == 429 and attempt < retries - 1:
                wait = int(e.headers.get("Retry-After", "2"))
                time.sleep(wait)
                continue
            raise RuntimeError(f"HTTP {e.code} calling {url}: {body_text}") from e
        except urllib.error.URLError as e:
            last_err = e
            time.sleep(1 + attempt)
    raise RuntimeError(f"Failed calling {url}: {last_err}")


# --------------------------------------------------------------------------
# HubSpot: closed-won deals for the target week
# --------------------------------------------------------------------------

def fetch_hubspot_closed_won(week_start: date, week_end: date) -> list[Deal]:
    """Pull all deals in the closed-won stage with a closedate in
    [week_start, week_end] (inclusive), paginating through results."""
    if not HUBSPOT_ACCESS_TOKEN:
        raise RuntimeError(
            "HUBSPOT_ACCESS_TOKEN is not set. Create a HubSpot private app with "
            "crm.objects.deals.read and crm.objects.owners.read scopes, then set "
            "the token in your environment (see .env.example)."
        )

    start_ms = int(datetime.combine(week_start, datetime.min.time(), tzinfo=timezone.utc).timestamp() * 1000)
    end_ms = int(datetime.combine(week_end + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc).timestamp() * 1000) - 1

    filters = [
        {"propertyName": "dealstage", "operator": "EQ", "value": HUBSPOT_CLOSED_WON_STAGE_ID},
        {"propertyName": "closedate", "operator": "BETWEEN", "value": start_ms, "highValue": end_ms},
    ]
    if HUBSPOT_PIPELINE_ID:
        filters.append({"propertyName": "pipeline", "operator": "EQ", "value": HUBSPOT_PIPELINE_ID})

    headers = {"Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}"}
    owners_cache: dict[str, str] = {}
    deals: list[Deal] = []
    after = None

    while True:
        payload = {
            "filterGroups": [{"filters": filters}],
            "properties": ["dealname", "amount", "closedate", "dealstage", "hubspot_owner_id"],
            "limit": 100,
        }
        if after:
            payload["after"] = after

        resp = _http("POST", f"{HUBSPOT_API_BASE}/crm/v3/objects/deals/search", headers, payload)

        for r in resp.get("results", []):
            props = r.get("properties", {})
            owner_id = props.get("hubspot_owner_id")
            owner = _resolve_owner(owner_id, headers, owners_cache) if owner_id else "Unassigned"
            amount_raw = props.get("amount")
            deals.append(Deal(
                id=r["id"],
                name=props.get("dealname") or f"Deal {r['id']}",
                amount=float(amount_raw) if amount_raw not in (None, "") else None,
                close_date=props.get("closedate"),
                owner=owner,
            ))

        paging = resp.get("paging", {}).get("next", {}).get("after")
        if not paging:
            break
        after = paging

    return deals


def _resolve_owner(owner_id: str, headers: dict, cache: dict) -> str:
    if owner_id in cache:
        return cache[owner_id]
    try:
        resp = _http("GET", f"{HUBSPOT_API_BASE}/crm/v3/owners/{owner_id}", headers)
        name = f"{resp.get('firstName', '')} {resp.get('lastName', '')}".strip() or owner_id
    except RuntimeError:
        name = owner_id
    cache[owner_id] = name
    return name


# --------------------------------------------------------------------------
# Slack: RevOps's post(s) in #sales-metrics for the target week
# --------------------------------------------------------------------------

def fetch_slack_metrics_messages(week_start: date, week_end: date) -> list[str]:
    """Return raw text of every message posted in the metrics channel during
    the target week (oldest first)."""
    if not SLACK_BOT_TOKEN or not SLACK_SALES_METRICS_CHANNEL_ID:
        raise RuntimeError(
            "SLACK_BOT_TOKEN and SLACK_SALES_METRICS_CHANNEL_ID must both be set. "
            "The bot needs channels:history (or groups:history for a private "
            "channel) on #sales-metrics. See .env.example."
        )

    oldest = datetime.combine(week_start, datetime.min.time(), tzinfo=timezone.utc).timestamp()
    latest = datetime.combine(week_end + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc).timestamp()

    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
    texts: list[str] = []
    cursor = None

    while True:
        url = (f"{SLACK_API_BASE}/conversations.history"
               f"?channel={SLACK_SALES_METRICS_CHANNEL_ID}&oldest={oldest}&latest={latest}&limit=200")
        if cursor:
            url += f"&cursor={cursor}"
        resp = _http("GET", url, headers)
        if not resp.get("ok"):
            raise RuntimeError(f"Slack conversations.history failed: {resp.get('error')}")

        for msg in resp.get("messages", []):
            if msg.get("subtype"):  # skip joins/leaves/system messages
                continue
            texts.append(msg.get("text", ""))

        cursor = resp.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break

    return list(reversed(texts))  # oldest first


def post_slack_digest(channel_id: str, text: str) -> None:
    if not SLACK_BOT_TOKEN:
        raise RuntimeError("SLACK_BOT_TOKEN is not set — cannot post. Run without --post to just draft.")
    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
    resp = _http("POST", f"{SLACK_API_BASE}/chat.postMessage", headers,
                 {"channel": channel_id, "text": text, "unfurl_links": False})
    if not resp.get("ok"):
        raise RuntimeError(f"Slack chat.postMessage failed: {resp.get('error')}")


# --------------------------------------------------------------------------
# Parsing RevOps's free-text Slack post into line items
# --------------------------------------------------------------------------
#
# RevOps posts are free text, not a structured feed, so this is inherently a
# best-effort heuristic. It tries a few common shapes:
#   "Acme Corp - $12,500"
#   "Acme Corp: $12,500"
#   "- Acme Corp — $12,500 (closed 7/28)"
#   "1. Acme Corp   $12,500"
# and pulls out (label, amount) pairs. Anything that doesn't match any pattern
# is surfaced separately as "unparsed_lines" so nothing is silently dropped —
# tune LINE_PATTERNS below once you've seen a few real RevOps posts.

LINE_PATTERNS = [
    re.compile(r"^[\-\*•]?\s*\d*\.?\s*(?P<label>[^:\-—$]{2,80}?)\s*[:\-—]\s*\$?(?P<amount>[\d,]+(?:\.\d+)?)"),
    re.compile(r"^[\-\*•]?\s*\d*\.?\s*(?P<label>[^$]{2,80}?)\s+\$(?P<amount>[\d,]+(?:\.\d+)?)"),
]

TOTAL_PATTERN = re.compile(r"total[^$\d]{0,20}\$?(?P<amount>[\d,]+(?:\.\d+)?)", re.IGNORECASE)


def parse_revops_lines(messages: list[str]) -> tuple[list[RevOpsLine], Optional[float], list[str]]:
    lines: list[RevOpsLine] = []
    unparsed: list[str] = []
    reported_total: Optional[float] = None

    for msg in messages:
        for raw_line in msg.splitlines():
            line = raw_line.strip()
            if not line:
                continue

            total_match = TOTAL_PATTERN.search(line)
            if total_match and reported_total is None:
                reported_total = float(total_match.group("amount").replace(",", ""))
                continue

            matched = False
            for pattern in LINE_PATTERNS:
                m = pattern.match(line)
                if m:
                    label = m.group("label").strip(" -—*")
                    amount = float(m.group("amount").replace(",", ""))
                    if label:
                        lines.append(RevOpsLine(raw_text=line, label=label, amount=amount))
                        matched = True
                        break
            if not matched and "$" in line:
                unparsed.append(line)

    return lines, reported_total, unparsed


# --------------------------------------------------------------------------
# Cross-referencing
# --------------------------------------------------------------------------

def _names_match(a: str, b: str) -> bool:
    a_norm = re.sub(r"[^a-z0-9]+", " ", a.lower()).strip()
    b_norm = re.sub(r"[^a-z0-9]+", " ", b.lower()).strip()
    if not a_norm or not b_norm:
        return False
    if a_norm in b_norm or b_norm in a_norm:
        return True
    return difflib.SequenceMatcher(None, a_norm, b_norm).ratio() >= NAME_MATCH_THRESHOLD


def _amounts_match(a: Optional[float], b: Optional[float]) -> bool:
    if a is None or b is None:
        return False
    if a == 0 and b == 0:
        return True
    denom = max(abs(a), abs(b), 1e-9)
    return abs(a - b) / denom <= AMOUNT_MATCH_TOLERANCE


def cross_reference(deals: list[Deal], revops_lines: list[RevOpsLine]) -> MatchResult:
    result = MatchResult()
    unmatched_lines = list(revops_lines)

    for deal in deals:
        candidate = None
        # Prefer a name match; fall back to an amount-only match.
        for line in unmatched_lines:
            if _names_match(deal.name, line.label):
                candidate = line
                break
        if candidate is None:
            for line in unmatched_lines:
                if _amounts_match(deal.amount, line.amount):
                    candidate = line
                    break

        if candidate is None:
            result.missing_from_revops.append(deal)
            continue

        unmatched_lines.remove(candidate)
        if _amounts_match(deal.amount, candidate.amount):
            result.matched.append((deal, candidate))
        else:
            result.amount_mismatch.append((deal, candidate))

    result.missing_from_hubspot = unmatched_lines
    return result


# --------------------------------------------------------------------------
# Formatting the digest
# --------------------------------------------------------------------------

def format_digest(week_start: date, week_end: date, deals: list[Deal],
                   match: MatchResult, revops_total: Optional[float],
                   unparsed_lines: list[str]) -> str:
    hs_total = sum(d.amount for d in deals if d.amount is not None)
    hs_count = len(deals)
    lines = []

    lines.append(f"*Weekly Closed-Won Summary — {week_start:%b %d} to {week_end:%b %d}*")
    lines.append("")
    lines.append(f"*{hs_count} deals closed-won · {_money(hs_total)}* (per HubSpot)")
    if revops_total is not None:
        delta = hs_total - revops_total
        if abs(delta) < 0.01:
            lines.append(f"Matches RevOps's reported total of {_money(revops_total)}. ✅")
        else:
            sign = "+" if delta > 0 else "-"
            lines.append(
                f"⚠️ RevOps reported {_money(revops_total)} in #sales-metrics — "
                f"HubSpot total differs by {sign}{_money(abs(delta))}."
            )
    lines.append("")

    lines.append("*Deals:*")
    for deal in sorted(deals, key=lambda d: (d.amount or 0), reverse=True):
        lines.append(f"• {deal.name} — {deal.amount_display} ({deal.owner})")
    if not deals:
        lines.append("• _No closed-won deals found in HubSpot for this week._")
    lines.append("")

    if match.amount_mismatch:
        lines.append("*⚠️ Amount mismatches vs RevOps's post (verify before standup):*")
        for deal, revops_line in match.amount_mismatch:
            lines.append(
                f"• {deal.name}: HubSpot {deal.amount_display} vs RevOps "
                f"\"{revops_line.raw_text}\""
            )
        lines.append("")

    if match.missing_from_revops:
        lines.append("*⚠️ In HubSpot but not mentioned in RevOps's #sales-metrics post:*")
        for deal in match.missing_from_revops:
            lines.append(f"• {deal.name} — {deal.amount_display} ({deal.owner})")
        lines.append("")

    if match.missing_from_hubspot:
        lines.append("*⚠️ In RevOps's post but no matching closed-won deal found in HubSpot:*")
        for line in match.missing_from_hubspot:
            lines.append(f"• \"{line.raw_text}\" — check deal stage/close date in HubSpot")
        lines.append("")

    if unparsed_lines:
        lines.append("*Note: could not auto-parse (review manually):*")
        for line in unparsed_lines:
            lines.append(f"• \"{line}\"")
        lines.append("")

    if not (match.amount_mismatch or match.missing_from_revops or match.missing_from_hubspot or unparsed_lines):
        lines.append("_HubSpot and RevOps's #sales-metrics post are fully reconciled — no discrepancies._")

    return "\n".join(lines).strip() + "\n"


def _money(amount: float) -> str:
    return f"${amount:,.2f}"


# --------------------------------------------------------------------------
# Sample data (for --sample, zero-credential dry runs)
# --------------------------------------------------------------------------

def load_sample_deals() -> list[Deal]:
    data = json.loads((HERE / "sample_data" / "hubspot_deals_sample.json").read_text())
    return [Deal(id=d["id"], name=d["name"], amount=d["amount"],
                 close_date=d["close_date"], owner=d["owner"]) for d in data]


def load_sample_slack_messages() -> list[str]:
    data = json.loads((HERE / "sample_data" / "slack_sales_metrics_sample.json").read_text())
    return data["messages"]


# --------------------------------------------------------------------------
# Week math
# --------------------------------------------------------------------------

def last_full_week(today: Optional[date] = None) -> tuple[date, date]:
    """When run on a Monday, 'last week' = the Monday-Sunday span that ended
    yesterday."""
    today = today or date.today()
    this_monday = today - timedelta(days=today.weekday())
    last_monday = this_monday - timedelta(days=7)
    last_sunday = last_monday + timedelta(days=6)
    return last_monday, last_sunday


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--week-start", type=str, default=None,
                         help="Monday of the target week, YYYY-MM-DD (default: last full week).")
    parser.add_argument("--post", action="store_true",
                         help="Actually post the digest to #sales-leadership. Without this flag, "
                              "the digest is only written to digest_drafts/ and printed to stdout.")
    parser.add_argument("--sample", action="store_true",
                         help="Run against bundled fixture data instead of live HubSpot/Slack APIs. "
                              "Ignores --post (never sends anything real).")
    args = parser.parse_args()

    if args.week_start:
        week_start = datetime.strptime(args.week_start, "%Y-%m-%d").date()
        week_end = week_start + timedelta(days=6)
    else:
        week_start, week_end = last_full_week()

    print(f"Target week: {week_start} to {week_end}{'  [SAMPLE DATA]' if args.sample else ''}")

    if args.sample:
        deals = load_sample_deals()
        slack_messages = load_sample_slack_messages()
    else:
        deals = fetch_hubspot_closed_won(week_start, week_end)
        slack_messages = fetch_slack_metrics_messages(week_start, week_end)

    revops_lines, revops_total, unparsed = parse_revops_lines(slack_messages)
    match = cross_reference(deals, revops_lines)
    digest = format_digest(week_start, week_end, deals, match, revops_total, unparsed)

    DRAFTS_DIR.mkdir(exist_ok=True)
    draft_path = DRAFTS_DIR / f"{week_start:%Y-%m-%d}.md"
    draft_path.write_text(digest)

    print("\n" + "=" * 72)
    print(digest)
    print("=" * 72)
    print(f"\nDraft written to: {draft_path}")

    if args.post and not args.sample:
        if not SLACK_SALES_LEADERSHIP_CHANNEL_ID:
            print("SLACK_SALES_LEADERSHIP_CHANNEL_ID not set — cannot post. Draft saved only.", file=sys.stderr)
            return 1
        post_slack_digest(SLACK_SALES_LEADERSHIP_CHANNEL_ID, digest)
        print(f"Posted to Slack channel {SLACK_SALES_LEADERSHIP_CHANNEL_ID}.")
    elif args.post and args.sample:
        print("(--sample run: not posting to Slack even though --post was passed.)")
    else:
        print("Dry run — nothing was posted. Re-run with --post to send to #sales-leadership.")

    has_discrepancy = bool(match.amount_mismatch or match.missing_from_revops
                            or match.missing_from_hubspot or unparsed)
    return 2 if has_discrepancy else 0


if __name__ == "__main__":
    sys.exit(main())
