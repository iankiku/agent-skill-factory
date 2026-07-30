#!/usr/bin/env bash
# Wrapper for cron/launchd: loads .env from this directory and runs the
# digest with --post. Logs everything (stdout+stderr) to a timestamped file
# under logs/ so a silent Monday-morning failure is still discoverable.
#
# Manual/interactive use: just run `python3 weekly_digest.py` directly
# instead — you get a dry-run draft printed to your terminal.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

mkdir -p logs
LOG_FILE="logs/$(date +%Y-%m-%d).log"

python3 weekly_digest.py --post >>"$LOG_FILE" 2>&1
STATUS=$?

if [ "$STATUS" -eq 2 ]; then
  echo "weekly_digest.py posted the digest but flagged discrepancies — see $LOG_FILE" >&2
elif [ "$STATUS" -ne 0 ]; then
  echo "weekly_digest.py FAILED (exit $STATUS) — see $LOG_FILE" >&2
fi

exit "$STATUS"
