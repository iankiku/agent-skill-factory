#!/usr/bin/env bash
# gather-staged-diff.sh
#
# Read-only helper for the commit-message-drafter skill. Collects
# everything an agent needs to draft a commit message from the CURRENTLY
# STAGED diff in one shot: whether anything is staged, a stat summary,
# recent commit-subject conventions (so the draft matches THIS repo's
# style, not a generic assumption), and the diff itself (capped, so a
# huge diff doesn't blow the context window).
#
# This script never mutates repo state: no `git add`, no `git commit`,
# no `git stash`. It only reads.
#
# Usage:
#   bash gather-staged-diff.sh [max_diff_lines]
#
# max_diff_lines defaults to 4000.

set -euo pipefail

MAX_DIFF_LINES="${1:-4000}"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: not inside a git repository." >&2
  exit 1
fi

echo "=== Repo state ==="
git status --short --branch || true
if [ -d "$(git rev-parse --git-dir)/rebase-merge" ] || [ -d "$(git rev-parse --git-dir)/rebase-apply" ]; then
  echo "NOTE: a rebase is in progress — commit message conventions may differ (see skill's edge cases)."
fi
if [ -f "$(git rev-parse --git-dir)/MERGE_HEAD" ]; then
  echo "NOTE: a merge is in progress — commit message conventions may differ (see skill's edge cases)."
fi
echo

STAGED_COUNT="$(git diff --staged --name-only | wc -l | tr -d ' ')"

if [ "$STAGED_COUNT" -eq 0 ]; then
  echo "=== Staged changes ==="
  echo "NONE. Nothing is staged."
  UNSTAGED_COUNT="$(git diff --name-only | wc -l | tr -d ' ')"
  UNTRACKED_COUNT="$(git ls-files --others --exclude-standard | wc -l | tr -d ' ')"
  if [ "$UNSTAGED_COUNT" -gt 0 ] || [ "$UNTRACKED_COUNT" -gt 0 ]; then
    echo "There ARE unstaged/untracked changes ($UNSTAGED_COUNT unstaged, $UNTRACKED_COUNT untracked)."
    echo "Do not draft from these and do not stage them automatically — ask the user to 'git add' first."
  else
    echo "Nothing unstaged either. Working tree is clean; there is nothing to commit."
  fi
  exit 0
fi

echo "=== Staged diff --stat ==="
git diff --staged --stat
echo

echo "=== Staged file list (for scope inference) ==="
git diff --staged --name-status
echo

echo "=== Recent commit subjects (match this repo's own convention) ==="
git log --oneline -20 2>/dev/null || echo "(no commit history yet — first commit)"
echo

echo "=== Full staged diff (capped at ${MAX_DIFF_LINES} lines) ==="
DIFF_LINE_COUNT="$(git diff --staged | wc -l | tr -d ' ')"
if [ "$DIFF_LINE_COUNT" -gt "$MAX_DIFF_LINES" ]; then
  git diff --staged | head -n "$MAX_DIFF_LINES"
  echo
  echo "... TRUNCATED: full staged diff is ${DIFF_LINE_COUNT} lines, showing first ${MAX_DIFF_LINES}."
  echo "Draft the body from the stat summary + this partial diff, and flag to the user that the"
  echo "'why' reasoning is based on a partial read for very large diffs."
else
  git diff --staged
fi
