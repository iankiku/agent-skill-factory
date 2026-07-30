---
name: commit-message-drafter
description: Read the currently staged git diff and draft a commit message in
  type(scope): summary format (imperative mood, subject under 72 chars, body
  explains WHY not WHAT) so the user only has to sanity-check and edit it, not
  write it from scratch. Use when the user says "draft my commit message",
  "write a commit message for this", "what should I commit this as", or is
  about to run `git commit` and wants the message pre-written. Do NOT use to
  run `git add`, `git commit`, `git push`, or open a PR — this skill only
  drafts text and never changes repo state beyond an optional local
  COMMIT_EDITMSG prefill. Do NOT use for PR descriptions, changelogs, or
  release notes — those are different artifacts with different bars.
---

# commit-message-drafter

## Outcome
When the user has staged changes and asks for a commit message (or is about to
commit and wants one pre-written), produce a draft commit message — subject
line in `type(scope): summary` form (imperative mood, ≤72 chars) plus a body
that explains why the change was made, not what changed — from `git diff
--staged` and the repo's recent commit history, meeting the bar that the user
only needs to tweak wording, not compose a message from a blank state.

Scope edges — this skill does NOT:
- Stage, commit, amend, or push anything. It only produces text (and
  optionally pre-fills `.git/COMMIT_EDITMSG`, a working file, never a commit).
- Write PR descriptions, changelog entries, or release notes — different
  artifact, different bar; route those elsewhere.
- Silently paper over a diff that mixes unrelated concerns — it flags the mix
  instead of picking one and hiding the rest (see Decision points).
- Invent a Jira/Linear ticket reference in the footer unless one is already
  visible in the branch name or an existing convention in the repo's log.

## Assumptions
ASSUMED: the type vocabulary is Conventional Commits' standard set (`feat`,
`fix`, `refactor`, `docs`, `test`, `chore`, `style`, `perf`, `build`, `ci`) —
the user's own format string (`type(scope): summary`) is the de facto
Conventional Commits shape, and no narrower list was given. If a repo's
history shows a different/narrower set in use, that repo's actual usage wins
(see Required context).

ASSUMED: delivery is "print the draft in-conversation AND pre-fill
`.git/COMMIT_EDITMSG`" rather than only one of the two — this lets the user
run `git commit` with no `-m` and land straight in their editor on the
pre-written message to sanity-check, matching "I just have to sanity-check it,
not write it from scratch," while never invoking `git commit` itself. No
lower-risk option loses fidelity to the stated workflow, so this is not a
reversibility trade-off — both are non-destructive and cheap to offer together.

ASSUMED: body is required on every commit except genuinely trivial ones
(pure whitespace/formatting, a single typo fix, a version bump with no logic
change) — the user's own habit ("I always... write the commit message")
implies a body is the default, not the exception.

## Required context
- Format contract (given by the user, verbatim): `type(scope): summary`,
  imperative mood ("add", not "added"/"adds"), subject ≤72 chars, body
  explains WHY not WHAT.
- Type vocabulary: `feat | fix | refactor | docs | test | chore | style |
  perf | build | ci` (see `references/commit-format-cheatsheet.md` for the
  full definitions and imperative-mood word list this skill checks against).
  Before drafting, scan `git log --oneline -20` — if the repo's actual history
  uses a different or narrower set (e.g. only `feat`/`fix`/`chore`, or a
  project-specific type like `deploy`), match that instead of the default list.
- Scope convention: the shortest path segment common to every changed file
  (e.g. top-level dir, or package name from the nearest `package.json` /
  `pyproject.toml` / `go.mod` if the repo is a monorepo). If changed files
  share no common segment, omit the scope (`type: summary` is valid
  Conventional Commits) rather than inventing one.
- Also scan `git log --oneline -20 -- <touched paths>` for scope names already
  in use on these files — reuse the existing name (e.g. `api` vs `apiserver`)
  instead of introducing a synonym.

## Inputs
- Staged diff: `git diff --staged` (full patch) and `git diff --staged
  --stat` (file list + line counts). Required. If empty, this is a stop
  condition (see Failure modes) — never falls back to unstaged changes.
- Recent history: `git log --oneline -20` and, if useful, `git log --oneline
  -20 -- <paths>` scoped to the touched files. Used only for style
  calibration; absence (e.g. first commit in a fresh repo) is not an error.
- Branch name: `git rev-parse --abbrev-ref HEAD` — read only to detect an
  existing ticket ID pattern (e.g. `feature/OSAAI1-279-...`) already in the
  team's own convention; never invented if absent.
- Nothing is read from outside the repository. No files, connectors, or URLs.

## Tools, connectors, APIs & authentication
- Local `git` CLI, already configured by the user (identity + signing are
  irrelevant to drafting — this skill never runs a command that creates a
  commit object). No connector, no OAuth, no env var, no auth of any kind.
- Filesystem write access to `.git/COMMIT_EDITMSG` inside the current repo
  only, to offer the pre-fill. If that path isn't writable, degrade to
  in-conversation output only (see Failure modes) — never treat it as fatal.

## Permissions
Reads: staged diff, diff stat, commit log (bounded to last 20), current
branch name.
Writes: `.git/COMMIT_EDITMSG` only (a working file `git commit` reads and
discards — not part of history, not synced, not a commit).
Never without explicit human action: `git add`, `git commit`, `git commit
--amend`, `git push`, `git tag`, opening a PR, or touching any file outside
`.git/COMMIT_EDITMSG`. This skill never runs `git commit` itself, even with
the draft in hand — the user always presses the button.

## Workflow
1. **Gather.** Run `git diff --staged --stat` and `git diff --staged`. If
   stat is empty, stop (Failure modes). Run `git log --oneline -20` (repo-wide
   and, if the touched paths are a small subset, path-scoped) and `git
   rev-parse --abbrev-ref HEAD`.
2. **Classify.** Infer `type` from diff content (new function/route/file with
   no prior counterpart → `feat`; diff touches code guarded by an existing bug
   report or changes behavior to correct an error → `fix`; test-only files →
   `test`; docs/comments/README only → `docs`; build/CI config/lockfiles only
   → `build`/`ci`; behavior-preserving restructuring → `refactor`; anything
   else → `chore`). If the diff shows more than one unrelated concern (e.g. a
   bug fix plus an unrelated new feature), do not silently merge them — go to
   the multi-concern decision point.
3. **Infer scope.** Apply the Required-context scope rule; cross-check
   against scope names already seen in step 1's log output.
4. **Draft subject.** Compose `type(scope): summary` in imperative mood,
   count characters, trim to ≤72 without truncating mid-word.
5. **Draft body.** Write 1–4 sentences answering "why was this change made"
   (motivation, the problem it solves, a tradeoff taken) — never a restatement
   of the diff hunks or a file-by-file list. Wrap body lines at 72 chars.
6. **Validate** (below) before presenting anything. Fix in place if a
   mechanical check fails; if it fails twice on the same item, surface the
   gap to the user instead of guessing a third time.
7. **Deliver.** Print the draft in-conversation with a one-line rationale for
   the chosen type/scope, and offer to pre-fill `.git/COMMIT_EDITMSG` (ask
   once; a "yes" default is fine since it's non-destructive and the user
   still has to run `git commit` themselves).

## Decision points
- **Diff spans multiple unrelated concerns** (e.g. a fix in one module, a new
  feature in another, no shared motivation) → do not average them into one
  vague type. Draft against the larger/primary concern, and explicitly tell
  the user the diff looks mixed with a one-line suggestion to split into
  separate commits (`git add -p`). Never silently drop the smaller concern.
- **No common scope across changed files** → omit scope entirely
  (`type: summary`), never fabricate a top-level umbrella name like "misc" or
  "various".
- **Ambiguous type** (e.g. a change that is arguably both `refactor` and
  `fix`) → prefer `fix` if any behavior change is user-visible or corrects
  incorrect output; prefer `refactor` only when output is provably identical
  before/after. When still unclear, ask the user with the two candidates
  named, rather than silently picking one.
- **Trivial diff** (whitespace-only, single typo, version bump) → body may be
  a single short clause instead of full paragraph, but is never omitted
  entirely — "why" is still one sentence (e.g. "align with prettier config
  now enforced in CI").
- **Repo history uses a non-standard type/scope vocabulary** → the repo's
  own convention wins over the default list (Required context).

## Validation
- **Mechanical — subject length:** count characters in the subject line;
  must be ≤72. If over, trim the summary clause (not the type/scope prefix)
  and recount.
- **Mechanical — subject shape:** subject matches
  `^(feat|fix|refactor|docs|test|chore|style|perf|build|ci)(\([a-z0-9._/-]+\))?: [a-z].+[^.]$`
  (lowercase type, optional parenthesized scope, colon-space, lowercase start,
  no trailing period) — or the repo-specific vocabulary substituted in.
- **Mechanical — imperative mood spot check:** first word of the summary is
  not in the shipped disallowed-form list (`references/commit-format-cheatsheet.md`
  — e.g. no `-ed`/`-ing`/`-s` verb forms like "added", "adding", "fixes");
  flag and rewrite if it matches.
- **Mechanical — coverage:** every file listed in `git diff --staged --stat`
  is accounted for by the chosen scope, or explicitly named in the body if
  the diff is multi-concern. No changed file is silently unrepresented.
- **Content — body is not a diff echo:** body must not merely restate file
  names or hunk contents (heuristic check, not blocking on its own — if it
  looks like a restatement, rewrite toward motivation before presenting).
- If any mechanical check still fails after one rewrite pass, present the
  draft anyway with the specific unresolved check called out, rather than
  looping indefinitely.

## Failure modes & fallbacks
- **Nothing staged** (`git diff --staged` empty) → stop immediately; tell the
  user to `git add` the intended files first. Never fall back to drafting
  from unstaged changes or the last commit's diff.
- **Not inside a git repo / git not on PATH** → stop and report the exact
  error; no retry (this is not transient).
- **Diff is huge** (e.g. >1500 changed lines or mostly generated/binary
  files) → degrade: summarize per top-level directory with line counts
  instead of reading every hunk, still classify type/scope from the
  summary, and flag in the response that this was a coarse read so the user
  double-checks harder than usual.
- **Merge conflict markers present in the staged diff** → stop; do not
  draft — this is an unusual/unsafe repo state that needs the user's direct
  attention, not a commit message.
- **`git log` unreadable or repo has zero history (first commit)** → skip
  style calibration, use the default type/scope rules, note in the response
  that no history existed to calibrate against.
- **`.git/COMMIT_EDITMSG` not writable** → degrade to in-conversation output
  only; not fatal, just note it wasn't pre-filled.
- **Same mechanical validation check fails twice in a row** → stop looping;
  present the draft with the specific failure named, and let the user fix it
  by hand rather than guessing a third time.

## Delegation
Runs single-agent; no step meets the delegation bar. Reasoning against
`references/delegation-policy.md`: the whole task is reading ONE diff and
producing ONE coherent judgment (type, scope, and especially the "why"
narrative) — there is no independent per-item unit to fan out the way
per-file extraction or per-call summarization works in other skills, because
splitting the diff across sub-agents would produce a body that reads like a
stitched-together file list, which is exactly the failure mode this skill
exists to avoid ("body is not a diff echo"). Even on a large diff touching
many files, the type/scope/why decision is a single holistic judgment, not a
bulk mechanical extraction — so it stays with the primary agent per the
policy's ordering (synthesis and judgment-heavy work are not delegated).
Final review (Validation) and the only write action (COMMIT_EDITMSG prefill)
stay with the primary agent unconditionally either way.

## Setup
1. No connectors, API keys, or environment variables to provision — this
   skill only needs a local git repository with the CLI already on PATH.
2. Install location depends on scope of use:
   - Personal, cross-repo habit (matches how this was described — "before I
     commit anything I always...") → place under the user's personal/global
     skills directory so it's available in every repo (e.g. `~/.claude/skills/
     commit-message-drafter/`, or the equivalent personal skills path for
     the runtime in use).
   - If the `type(scope): summary` convention actually varies per repo/team,
     install per-repo instead (`.claude/skills/commit-message-drafter/`) and
     adjust the type vocabulary in `references/commit-format-cheatsheet.md`
     to that repo's actual set.
3. First run: confirm the type vocabulary and scope-naming rule above still
   match the team's format; edit `references/commit-format-cheatsheet.md` if
   not — everything else in this skill reads from that file rather than a
   hardcoded list.
