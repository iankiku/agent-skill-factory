# Run notes — commit-message-drafter

Non-interactive eval run: no real human was available to answer
`AskUserQuestion` prompts. Every place build-skill's process calls for asking
the user, I answered in-character as Ian Kiku (the persona in the task —
CTO/founder, direct communication style, git identity already configured per
his own CLAUDE.md) and flagged it below rather than stalling. `AskUserQuestion`
itself was never invoked; questions were resolved inline in this document and
the `## Assumptions` section of SKILL.md.

## Template selection (Phase 2)

Checked `references/template-index.md` for a match on artifact type (a
drafted commit message) or input source (a git staged diff / local repo).
This install of build-skill has no `templates/` directory on disk at all —
only the index — so per the skill's own fallback instruction ("if the
`templates/` bodies aren't readable in your environment, use the index
entry's summary plus the blank template") I worked from index summaries only.

The 94-template catalog's categories are: `claude-in-chrome`, `cowork`,
`education`, `finance`, `hr`, `legal`, `life-sciences`, `marketing`,
`nonprofits`, `personal`, `professional`, `research`, `sales`. There is no
engineering/developer/git category at all, and a keyword grep for
git/commit/diff/version-control/developer terms across the index returned
nothing on-domain (the only "commit" hit was `chart-your-data-before-you-commit`,
a data-analysis template unrelated in artifact or inputs). Nothing matches on
artifact (a git commit message) or on inputs (a staged diff read via the git
CLI) — confirmed by design, not by a shallow check.

**Fell back to `references/blank-skill-template.md`, explicitly, as build-skill
instructs when nothing matches on artifact OR inputs.** No catalog attribution
line is included in SKILL.md because none applies — this was not derived from
any Anthropic-published template.

## Phase 1 — Pinning the outcome (self-answered)

The task description already supplied most of the four slots directly:
- Trigger: user has staged changes and is about to commit / explicitly asks
  for a drafted message.
- Artifact: a commit message text (subject + body) in `type(scope): summary`
  form.
- Inputs: the staged diff.
- Bar: "just sanity-check it, not write it from scratch" — i.e. correct
  enough on type/scope/wording that edits are minor, not a rewrite.

Where the task was silent, I answered as Ian would, in one pass each (no
multi-round interrogation needed since these were low-ambiguity defaults, not
genuine "I don't know" cases):

- **Where does the draft land?** Chose both in-conversation text AND an
  optional `.git/COMMIT_EDITMSG` pre-fill, since the described workflow
  ("I just have to sanity-check it") is best served by landing directly in
  the editor `git commit` opens — while never having the skill run
  `git commit` itself. Recorded as `ASSUMED` in SKILL.md.
- **Body requirement.** Chose "always, except genuinely trivial diffs" —
  directly inferable from "I always... write the commit message by hand,"
  implying a body is the default, not opt-in. Recorded as `ASSUMED`.
- **Type vocabulary.** Chose standard Conventional Commits types
  (`feat/fix/refactor/docs/test/chore/style/perf/build/ci`) because
  `type(scope): summary` is literally that convention's shape and the user
  gave no narrower list. Made this overridable by a repo's actual git-log
  history rather than hardcoding it, since "our team's format" could still
  mean a repo-specific subset. Recorded as `ASSUMED`.
- **Scope inference rule.** No catalog/example precedent for this, so I
  derived a mechanical rule (shortest shared path segment across changed
  files, falling back to "omit scope" rather than inventing an umbrella
  scope) and shipped it as reusable Required-context in
  `references/commit-format-cheatsheet.md` rather than an unlabeled
  assumption, since it's a stated rule the skill applies consistently, not a
  one-off guess.

Scope edges (near-misses this skill refuses): never runs `git add/commit/
push`; never drafts PR descriptions/changelogs/release notes (different
artifact, different bar — a Team Nebula skill like `tmn-ship` already owns
PR-adjacent flow); never fabricates a scope or ticket reference that isn't
already evidenced in the repo's own history or branch name.

## Phase 3 — Machinery

Tools: local `git` CLI only (`diff --staged`, `diff --staged --stat`, `log
--oneline`, `rev-parse --abbrev-ref HEAD`), plus a filesystem write to
`.git/COMMIT_EDITMSG`. No connectors, no auth, no secrets — this is the
simplest possible tool surface, which is itself a fit check: a skill this
narrow shouldn't need more.

## Phase 4 — Delegation

Verdict: **single-agent**, argued explicitly in SKILL.md rather than left
implicit. Applied `delegation-policy.md`'s ordering: the task is dominated by
one holistic judgment (type + scope + why-narrative from ONE diff), not a
bulk/independent per-item job. Unlike the two bundled examples (per-call
transcript summaries, per-file invoice extraction — both naturally
independent units), splitting a single diff across sub-agents would produce
exactly the failure mode the skill's own validation guards against: a body
that reads like a stitched-together file list instead of one coherent "why."
I checked this wasn't just a size dodge — even on a diff touching many files,
the type/scope/why decision doesn't decompose into independent per-file
verdicts the way invoice fields do, so no step meets the delegation bar at any
scale.

## Phase 5 — Draft, validate, refine

Ran the full draft against `references/validation-checklist.md` line by line:
triggering (description + negative scope + kebab-case name), outcome/inputs
(all four outcome slots filled; every input has a missing/malformed path),
tools/auth (git CLI only, zero credential values, no orphaned tools),
safety/permissions (explicit never-list, nothing irreversible before
validation, no bypass instructions), workflow quality (7 steps, every fork has
a deciding rule, several mechanical checks, a named stop-and-report
condition), delegation (present, reasoned, correctly says no sub-agent
qualifies), and attribution/hygiene (no catalog attribution needed since
blank-template was used; three `ASSUMED:` lines; Setup section is
self-sufficient). No failing items found on this pass.

### Dry-run trace

Synthetic input: staged diff touches `src/auth/rate_limit.py` (new file, a
token-bucket limiter), `src/auth/login.py` (wires the limiter into the login
handler), and `tests/auth/test_rate_limit.py` (new tests). `git log --oneline
-20` shows prior commits like `fix(auth): reject expired refresh tokens` and
`feat(auth): add password-reset endpoint` — scope `auth` already in use.
Branch name: `fix/login-brute-force`.

1. **Gather:** stat shows 3 files, +142/-4 lines; log shows `auth` as the
   live scope name; branch name suggests a fix framing but isn't itself
   evidence of the type.
2. **Classify:** new rate-limiter + handler wiring = new capability, but
   branch name and the fact that login currently has no abuse protection
   reads as "correcting a security gap" more than "adding a feature nobody
   asked for." Per the ambiguous-type decision point (prefer `fix` when a
   real user-visible defect is being corrected): classified as `fix`, not
   `feat` — flagged in the one-line rationale shown to the user so they can
   overrule it.
3. **Scope:** all three files share `auth` as the shortest common segment,
   matching the log's existing usage → scope = `auth`.
4. **Subject draft:** `fix(auth): add rate limiting to login to stop brute
   force` — 57 characters (mechanical count) → under 72, passes shape regex,
   first word "add" passes the imperative-mood check.
5. **Body draft:** "Login had no throttling, so a scripted attacker could
   attempt unlimited password guesses against any account. Adds a
   token-bucket limiter (5 attempts / 60s per account) in front of the login
   handler; tests cover the boundary and reset-after-window cases." — this is
   why-focused (the risk being closed), not a restatement of the diff hunks.
6. **Validate:** subject length ✓, shape regex ✓, imperative-mood check ✓
   ("add" not "added"), coverage check ✓ (all 3 files fall under `auth`),
   body-is-not-a-diff-echo ✓ (no file names/line contents repeated verbatim).
   All pass on the first pass — no rewrite loop triggered.
7. **Deliver:** prints the draft plus the one-line rationale ("classified as
   `fix` rather than `feat` since it's closing an existing abuse gap, not
   adding a requested feature — say the word if you'd rather call it
   `feat`"), and offers to pre-fill `.git/COMMIT_EDITMSG`.

Trace exposed one gap during drafting: the first pass of the workflow didn't
say what happens when the *branch name* and the *diff content* disagree on
type (branch says "fix", diff alone could read as "feat"). Resolved by making
the ambiguous-type decision point explicit about preferring `fix` when a real
defect/gap is being closed, and always surfacing the alternate label rather
than silently picking one — this is now baked into SKILL.md's Decision points
and workflow step 7, not left to be improvised at run time.

One simulated refinement round (in place of a live user round, since none is
available): reviewed whether the "always ask before overwriting
COMMIT_EDITMSG" behavior was too chatty for a one-person workflow used
repeatedly — resolved by keeping the offer but defaulting it to "yes" since
the write is non-destructive and reversible (git ignores a stale
COMMIT_EDITMSG on the next real commit), consistent with the policy's
"prefer the reversible option" default. Re-ran the checklist after this
change; no new failures. Delivered after this single round, consistent with
Phase 5's "at most one clarifying round per revision, then re-run the
checklist" when no blocking feedback exists.

## Summary of deviations from a fully-interactive run

- No `AskUserQuestion` calls were made (none could be answered) — all
  decisions that would have been options-based questions were resolved
  inline and labeled either `ASSUMED:` (in SKILL.md) or as a self-answered
  choice (in this file), per the task's instruction to answer in-character
  rather than stall.
- Template selection had no ambiguity to resolve interactively — the
  catalog's category list made the "no match" call unambiguous rather than a
  judgment call requiring user input.
