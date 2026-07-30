# RUN_NOTES — commit-message-drafter (without_skill baseline)

## What this is

A self-contained Claude Code skill package (no skill-authoring tooling
used to build it — this is the "without_skill" baseline: a skill written
directly by hand/agent, not via `skill-creator`) that drafts a commit
message from the currently **staged** git diff, in the user's stated
format: `type(scope): summary`, imperative mood, subject <=72 chars,
body explains *why* not *what*.

## Files produced

- `SKILL.md` — the skill definition (YAML frontmatter with `name` +
  trigger `description`, plus the full procedure Claude follows: gather
  the diff, determine the repo's actual convention, infer type/scope,
  draft subject + body, present the draft, handle edge cases).
- `scripts/gather-staged-diff.sh` — a read-only bash helper that does
  all git inspection in one call (repo/merge/rebase state, staged
  stat, staged file list, last 20 commit subjects, capped full diff)
  instead of the agent issuing 4-5 separate `git` commands per run.
  Verified working, executable (`chmod +x`), tested against four
  scenarios in a scratch repo (staged changes present, only unstaged
  changes, clean tree, not-a-git-repo) — all four produced correct
  output/exit codes.

## Design decisions / assumptions made

1. **Repo-specific convention beats a hardcoded template.** The user
   said "our team's format," but didn't paste an exact spec beyond
   `type(scope): summary`, imperative, <72 chars, body-explains-why.
   Rather than hardcoding one fixed type list or scope-naming rule, the
   skill instructs Claude to check the repo's own recent `git log`
   subjects and any `CONTRIBUTING.md`/commit-template first, and use the
   standard Conventional-Commits-style types (`feat/fix/docs/refactor/
   perf/test/build/ci/chore/revert/style`) only as a fallback. This
   matches the workspace's own global instruction to "match the
   conventions already present in a repo" (from
   `~/moonshot/launchpad/CLAUDE.md` / `~/moonshot/CLAUDE.md`) and makes
   the skill reusable across the user's several isolated tenant repos
   (nmosa, pnm, tmn, etc.) rather than baking in one project's style.

2. **Never runs `git commit`.** The user explicitly said they want to
   "sanity-check" the draft, not have it committed for them. The skill
   is written to stop after presenting the draft in a code block —
   no auto-commit, no auto-stage, no auto-amend.

3. **Won't draft from unstaged changes or silently stage things.** If
   nothing is staged, the skill tells the user what's unstaged and asks
   them to `git add` — it does not run `git add` on their behalf, since
   staging is a deliberate choice the user makes about what belongs in
   this commit.

4. **Flags bundled/unrelated changes instead of papering over them.**
   If the staged diff spans clearly unrelated concerns, the instructions
   tell Claude to say so and suggest splitting rather than inventing one
   vague message that covers everything — this was an explicit design
   choice since a drafted message hiding an unrelated bundle would be
   worse than no message.

5. **Large-diff handling.** The helper script caps the full diff at
   4000 lines (configurable via an optional arg) and reports truncation
   explicitly; the skill instructs Claude to fall back to the stat
   summary plus a partial diff and flag to the user that the "why"
   reasoning may be incomplete for huge diffs, rather than silently
   guessing beyond what it actually read.

6. **BREAKING CHANGE detection is a suggestion, not a decision.** The
   skill surfaces a candidate `BREAKING CHANGE:` footer if the diff
   looks like it removes/changes a public API, schema, or config
   incompatibly, but leaves the decision to add it to the user (footer
   conventions vary by repo and the agent can't always be certain of
   downstream impact).

## What I did NOT do

- Did not invoke `skill-creator` or any other meta-skill/scaffold to
  produce this — built directly as the "without_skill" baseline per the
  task instructions.
- Did not wire this into any actual Claude Code skills directory
  (`~/.claude/skills/` or similar) or register it anywhere — the
  deliverable is the skill package itself at the requested output path.
- Did not add a `git commit` wrapper mode, interactive editor launch, or
  any mutating git behavior — kept strictly to draft-only per the user's
  stated intent ("just have to sanity-check it").

## Verification performed

Ran `scripts/gather-staged-diff.sh` against a disposable scratch git
repo (created and destroyed under the session scratchpad, not under any
tracked project) covering:
- Staged changes present (modified + new file) → correct stat, file
  list, recent-log, and diff output.
- Only unstaged changes present → correctly reports "NONE staged" and
  the unstaged count, without staging anything.
- Clean working tree → correctly reports nothing to commit.
- Run from outside any git repo → correctly errors with a clear message
  and non-zero exit.

No further verification is possible without a human's real staged diff
and their team's actual commit-message templates/CONTRIBUTING doc, since
this is a non-interactive evaluation and the skill's core value (judging
"why" from an arbitrary real diff) can only be fully exercised inside a
live coding session.
