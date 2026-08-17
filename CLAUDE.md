# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A catalog of the 94 use cases Anthropic publishes at claude.com/resources/use-cases, a skill template derived from each, and a primary `build-skill` skill (`skills/build-skill/`) that turns any narrow outcome into an executable Claude skill. It is a content/docs repo — one Python script, no dependencies beyond the stdlib, no tests, no build system.

## The one command

```bash
python3 scripts/generate.py
```

Regenerates `catalog/`, `templates/`, `INDEX.md`, and the README's 94 field prompts from `data/raw/*.json`. It **deletes and rewrites** `catalog/` and `templates/` on every run, and rewrites the README block between the `<!-- BEGIN GENERATED: field prompts ... -->` / `<!-- END GENERATED: field prompts -->` markers in place. It is idempotent; it exits non-zero if those README markers are missing.

## Generated vs. hand-written — the critical distinction

- **Build artifacts (never edit directly):** `catalog/`, `templates/`, `INDEX.md`, and the README section between the field-prompt markers. Any manual edit is lost on the next `generate.py` run. To change them, edit `scripts/generate.py` (scaffold structure, validation/failure defaults, connector heuristics, prompt wording in `prompt_block` / `category_block`, ordering in `CATEGORY_ORDER`, blurbs in `CATEGORY_BLURB`) or `data/raw/*.json` (use-case content), then regenerate.
- **Hand-written:** `skills/build-skill/` (SKILL.md, `references/`, `examples/`), `docs/`, `README.md` *outside* the markers, `ATTRIBUTION.md`, `data/raw/` + `data/manifest.json`.

## The public gist (two files, mirrored in this repo)

https://gist.github.com/iankiku/0366d5701cf8268ee05c24cd30fa366b holds exactly two files, displayed alphabetically:

| Gist file | Repo mirror | Role |
|---|---|---|
| `0-README.md` | `skills/build-skill/build-skill.gist-README.md` | Landing page: install per surface, first prompt, link back to the repo |
| `build-skill.gist.md` | `skills/build-skill/build-skill.gist.md` | The skill itself — self-contained, all four reference files inlined |

Edit the repo copy first, then push both with `gh gist edit <id> -f <gist-filename> <local-path>`. They must stay byte-identical (trailing newline aside). Changing `skills/build-skill/SKILL.md` or its `references/` means the bundle is stale — re-inline and re-push.

## README contract

The README is the front door and follows a deliberate ladder: banner → badges → nav pills → collapsible TOC → quick start → universal prompt → the 94 per-use-case prompts (generated) → install paths → repo map → design decisions. Each generated entry is one `####` heading, a one-line description, source/catalog/template links, and a single fenced `text` block so GitHub renders a one-click copy button. Placeholders are `[BRACKETED]` and uppercase. Adding a category to `data/raw/` without adding it to `CATEGORY_ORDER`/`CATEGORY_BLURB` still works (it sorts to the end, blurb blank) — but add it.

Structural conventions borrowed from [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template): `<a id="readme-top">` at line 1, a collapsible Table of Contents, a `back to top ↑` link closing every `##` section, and reference-style badge definitions in a block at the very bottom. Keep all four when editing.

**There are no tabs.** GitHub strips `<style>` and `<script>` from READMEs, so tab widgets cannot work — every "tabbed README" in the wild is badges plus anchors plus `<details>`, which is what this one is. Don't try to add real tabs; extend the pill strip or the accordions instead.

## Banner assets

`.github/assets/banner-{dark,light}.svg` are hand-maintained (not generated), embedded via `<picture>` with `prefers-color-scheme` so the header follows the viewer's theme. The right-hand grid is 94 squares — one per use case — so it must be regenerated if the count changes. Palette: `#D97757` accent, `#14130F`/`#FAF8F5` grounds. Verify a change by rendering it, e.g. `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --screenshot=/tmp/b.png --window-size=1220,320 file://$PWD/.github/assets/banner-dark.svg` — QuickLook (`qlmanage`) distorts the aspect ratio and is not a valid check.

`data/raw/` is the source of truth: one JSON per use case (slug, title, category, model, features, surface, description, verbatim prompt, steps, prerequisites, source_url, retrieved_at, extraction_status).

## Architecture of generate.py

For each raw JSON it emits a catalog doc (`catalog/<category-slug>/<slug>.md`) and a skill template (`templates/<category-slug>/<name>/SKILL.md`), then builds `INDEX.md`. Templates get per-category validation defaults (`validation_defaults`), feature-driven failure modes (`failure_defaults`), and connectors derived by keyword matching (`CONNECTOR_HINTS` / `derive_connectors`) — extend those tables rather than post-editing output.

## Invariants to preserve

- **Attribution split (see ATTRIBUTION.md):** use-case titles, descriptions, seed prompts, steps, and prerequisites are reproduced **verbatim** and marked © Anthropic PBC — never paraphrase, "fix", or reword them. Everything scaffolded around them is original to this repo under MIT. Every catalog doc and template carries source URL, retrieval date, and attribution in frontmatter; keep that intact.
- **No secrets, ever:** skills and templates reference connectors and env-var *names* only. Credential values never appear in any file. `.gitignore` blocks `.env`/key files as a backstop; checklist in `skills/build-skill/references/validation-checklist.md`.
- **Delegation policy sync:** `docs/delegation-policy.md` is canonical and is bundled verbatim into `skills/build-skill/references/` so the skill travels standalone. If you change one copy, change the other.
- **build-skill is self-contained:** it must work installed outside this repo — it reads `references/template-index.md` and falls back to `references/blank-skill-template.md` when `templates/` bodies aren't available. Don't add hard dependencies on repo-relative paths outside `skills/build-skill/`.

## Refresh workflow

When Anthropic updates the source pages: re-extract the JSONs into `data/raw/` (updating `retrieved_at` and `extraction_status` — `ok`, or `partial` when a page had no boxed example prompt), update `data/manifest.json`, then run `generate.py`. If use cases are added/removed, update the count (currently 94) in `README.md`, `ATTRIBUTION.md` references, and `skills/build-skill/` where mentioned.
