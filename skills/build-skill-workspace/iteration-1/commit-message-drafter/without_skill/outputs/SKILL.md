---
name: commit-message-drafter
description: Reviews the currently staged git diff and drafts a commit message in conventional "type(scope): summary" format — imperative mood, subject under 72 chars, body explains WHY not what. Use when the user says "draft my commit message", "write a commit message", "/commit-message", or is about to run `git commit` and wants a message proposed from staged changes to sanity-check, not write from scratch. Never runs `git commit` itself — output is a draft for the human to review and use.
---

# Commit Message Drafter

Drafts a commit message from the **currently staged** diff, in this format:

```
type(scope): summary in imperative mood, <=72 chars

Body explains WHY the change was made — motivation, problem, tradeoff —
not a restatement of what the diff shows line by line. Wrap at ~72 chars.
Reference an issue/ticket if one applies.
```

The output is a **draft to sanity-check**, not a final commit. Never run
`git commit` on the user's behalf — stop after presenting the message.

## When to use this

Trigger on: "draft a commit message", "write my commit message", "what
should the commit message be", "/commit-message", or any moment right
before the user is about to commit staged work and wants a message
proposed instead of writing one from scratch.

## Step 1 — Gather the staged diff

Run the bundled script, which does the read-only git inspection in one
shot so you don't have to issue five separate commands:

```bash
bash scripts/gather-staged-diff.sh
```

This prints, in order:
1. Whether there are staged changes at all (fails loudly if not — see
   Edge cases below).
2. `git diff --staged --stat` — file-level summary.
3. Up to 20 recent subject lines from `git log`, so you can match this
   **repo's own** existing convention rather than assuming generic
   Conventional Commits.
4. The full `git diff --staged`, capped at ~4000 lines with a note if
   truncated (for huge diffs, rely on the stat summary + a sampled
   subset of hunks rather than reading the entire truncated tail).

If the script isn't available in this environment (e.g. you're operating
directly in a shell without file access to this skill's `scripts/`
directory), run the equivalent commands by hand:

```bash
git rev-parse --is-inside-work-tree            # confirm we're in a repo
git diff --staged --stat
git log --oneline -20
git diff --staged
```

## Step 2 — Determine the repo's actual convention

Don't assume every repo uses bare Conventional Commits. Before drafting:

- Scan the recent `git log` subjects captured in Step 1 for a pattern —
  do they use `type(scope):`? Just `type:`? All lowercase? A ticket
  prefix like `NMOSA-123:`? Match what's already there.
- If a `CONTRIBUTING.md`, `CONVENTIONS.md`, or `.github/` template
  documents a commit format, that wins over inferred history.
- If there's no established convention (first commit, or history is
  inconsistent), default to the standard the user asked for:
  `type(scope): summary`, imperative, <=72 chars subject, body explains
  why.

Standard `type` values if inferring: `feat`, `fix`, `docs`, `refactor`,
`perf`, `test`, `build`, `ci`, `chore`, `revert`, `style`. Pick the one
type that best matches the *dominant* intent of the diff — don't invent
a new type just because one file is a test.

## Step 3 — Infer scope

Derive `scope` from the changed paths in the diff stat, not from
guessing:

- Single package/service/module touched → use its directory or package
  name (e.g. `auth`, `api`, `cli`, `ingest`).
- Changes span multiple unrelated top-level areas → say so explicitly
  and either pick the dominant one or omit scope (`type: summary`) —
  don't fabricate a scope that doesn't correspond to a real path.
- Monorepo with named packages (check `package.json`/`pyproject.toml`/
  workspace config) → prefer the package name over the raw directory
  path.

## Step 4 — Draft the message

- **Subject**: `type(scope): summary`, imperative mood ("add", "fix",
  "remove" — not "added", "adds", "adding"), no trailing period, target
  50 chars and hard-cap 72.
- **Body**: one blank line after the subject, then prose (or short
  bullets) that explains the *reasoning* — what problem this solves,
  why this approach over an alternative, what triggered the change (bug
  report, perf regression, review feedback) — inferred from the diff's
  intent, comments, and any docstrings/tests added. Do NOT just narrate
  "changed X to Y" for every hunk; that's restating the diff, which is
  exactly what the user said they don't want.
- If the diff is a small, self-evidently mechanical change (typo fix,
  formatting, version bump), a body may be unnecessary — say so rather
  than padding one out.
- If staged changes look like **multiple unrelated concerns** bundled
  together, flag this before drafting: recommend splitting into
  separate commits, and either draft a message for the dominant concern
  or offer one draft per concern — don't silently paper over an
  unrelated bundle with a vague message.

## Step 5 — Present the draft

Output the message in a fenced code block, ready to paste into
`git commit -F -` or an editor. After the block, briefly flag:
- Any assumptions made (inferred type/scope, uncertainty about intent).
- Whether unrelated changes were detected and should be split.
- Any BREAKING CHANGE the diff appears to introduce (public API/schema/
  config removed or changed incompatibly) — surface it as a footer
  candidate (`BREAKING CHANGE: ...`) rather than deciding for the user.

Then stop. Do not run `git commit`, `git commit --amend`, or stage/
unstage anything — this skill only drafts.

## Edge cases

- **Nothing staged**: if `git diff --staged` is empty but there are
  unstaged changes, tell the user what's unstaged and ask them to
  `git add` first — do not draft from unstaged changes and do not stage
  anything yourself.
- **Nothing staged and nothing unstaged**: say there's nothing to
  commit; stop.
- **Not a git repo**: say so; stop.
- **Merge/rebase in progress**: note it (`git status` will show it) —
  a commit message here may need to follow the merge/rebase's own
  conventions (e.g. `Merge branch 'x'`), not the standard format.
- **Huge diff** (script reports truncation): draft from the stat
  summary plus the recent-log convention check; be explicit that the
  body is based on a partial read of the diff and the user should
  double check the "why" reasoning against their own knowledge of the
  change.
