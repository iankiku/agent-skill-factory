# Commit format cheatsheet

Shipped with `commit-message-drafter`. This is the file to edit if a specific
repo's real convention differs from the default below — the skill reads its
type vocabulary and imperative-mood check from here, not from a hardcoded list
in SKILL.md.

## Default type vocabulary (Conventional Commits)

| Type       | Use for |
|------------|---------|
| `feat`     | a new capability or behavior that didn't exist before |
| `fix`      | correcting incorrect/broken behavior |
| `refactor` | restructuring code with no behavior change |
| `docs`     | documentation, comments, README only |
| `test`     | adding or changing tests only |
| `chore`    | maintenance that doesn't fit the above (deps, config, cleanup) |
| `style`    | formatting only (whitespace, semicolons) — no logic change |
| `perf`     | a change whose primary purpose is performance |
| `build`    | build system or external dependency changes |
| `ci`       | CI pipeline/config changes |

If a repo's `git log --oneline -20` shows a narrower or different set in
active use (common in small personal repos: just `feat`/`fix`/`chore`), match
that set instead of introducing new types the repo hasn't used.

## Imperative mood check

Subject's first word after `type(scope): ` should read like a command, as if
completing "If applied, this commit will ___."

- Correct: `add`, `fix`, `remove`, `rename`, `bump`, `guard`, `extract`, `wire`
- Wrong (flag and rewrite): `added`, `adds`, `adding`, `fixed`, `fixes`,
  `fixing`, `removed`, `removes`, `renamed`

Quick mechanical test: strip the first word's trailing `d`, `ed`, `s`, or
`ing` and see if what's left is still a real, different verb stem meaning the
same thing — if the word ends in one of those suffixes and reads as
past-tense or third-person, it's wrong.

## Scope naming

Scope = the shortest path segment shared by every changed file.

- All changes under `src/auth/**` → scope `auth`.
- Monorepo with `packages/api/**` and `packages/api/routes/**` → scope `api`.
- Changes split across `src/auth/**` and `src/billing/**` with no shared
  parent below the repo root → no common scope; omit it (`type: summary`).

Prefer whatever scope name the repo's own log already uses over introducing a
synonym (e.g. if history already has `fix(api): ...`, don't switch to
`fix(apiserver): ...` for the same directory).

## Subject line shape

```
type(scope): summary
```

- `type` lowercase, from the vocabulary above (or the repo's own set).
- `(scope)` optional; lowercase, may contain `.`, `-`, `_`, `/`.
- `summary`: imperative mood, lowercase first word, no trailing period,
  whole subject line ≤72 characters.

## Body

- Explains WHY the change was made — the problem, the motivation, or the
  tradeoff — never a restatement of WHAT changed (that's what the diff
  already shows).
- Wrap at 72 characters per line.
- Required on every commit except genuinely trivial ones (pure
  whitespace/formatting, a single typo, a version bump with no logic change),
  where a single short clause is enough — never omitted outright.
- If the diff mixes unrelated concerns, name the secondary concern explicitly
  in the body rather than silently dropping it from the message.
