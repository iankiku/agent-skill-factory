# Contributing

Thanks for helping. This is a content repo — one Python script, no dependencies
beyond the standard library, no build system, no tests. Most contributions are a
few edits and one command.

## The one rule that trips everyone up

**Four things are generated. Editing them by hand loses your work on the next build.**

| Generated (don't hand-edit) | Hand-written (edit freely) |
|---|---|
| `catalog/` | `data/raw/` and `data/manifest.json` |
| `templates/` | `skills/build-skill/` |
| `INDEX.md` | `docs/`, `CONTRIBUTING.md`, `ATTRIBUTION.md` |
| The README block between the `<!-- BEGIN GENERATED: field prompts -->` markers | The rest of `README.md` |

To change anything on the left, edit `scripts/generate.py` (structure, defaults,
wording) or `data/raw/*.json` (use-case content), then run:

```bash
python3 scripts/generate.py
```

It's idempotent — running it twice produces the same bytes. Commit the regenerated
output along with your source change.

## Common contributions

### Fix a typo or improve wording in a template

The templates are generated, so fix it in `scripts/generate.py` — usually in
`TEMPLATE_DOC`, `validation_defaults()`, or `failure_defaults()` — then regenerate.
A fix there improves all 94 at once.

### Add or refresh a use case

1. Add or update the JSON in `data/raw/<slug>.json`. Required fields: `slug`,
   `title`, `category`, `model`, `features`, `surface`, `description`, `prompt`,
   `steps`, `prerequisites`, `source_url`, `retrieved_at`, `extraction_status`.
2. Set `retrieved_at` to the date you actually read the source page, and
   `extraction_status` to `ok` — or `partial` if the page had no boxed example
   prompt and you used the task text from its steps instead.
3. Update `count` and the `use_cases` list in `data/manifest.json`.
4. Run `python3 scripts/generate.py`.
5. If the total changed, update the count wherever it's stated in prose —
   `README.md`, `ATTRIBUTION.md`, and `skills/build-skill/`.

New category? Add it to `CATEGORY_ORDER` and `CATEGORY_BLURB` in `generate.py`, and
mark it in `CATEGORY_KIND` if it's a delivery surface rather than an industry.
Without that it still builds, but it sorts to the end with no description.

### Improve the `build-skill` skill

`skills/build-skill/SKILL.md` and its `references/` are hand-written. Two things
travel with them:

- `docs/delegation-policy.md` is canonical and is inlined verbatim into
  `skills/build-skill/references/delegation-policy.md`. Change one, change both.
- `skills/build-skill/build-skill.gist.md` is the single-file copy-paste bundle with
  every reference inlined. If you change the skill or its references, that bundle is
  stale until you re-inline it. It and `build-skill.gist-README.md` mirror the two
  files in the [public gist](https://gist.github.com/iankiku/0366d5701cf8268ee05c24cd30fa366b).

## Non-negotiables

- **Never reword Anthropic's content.** Use-case titles, descriptions, seed prompts,
  steps, and prerequisites are reproduced verbatim and marked © Anthropic PBC. Don't
  paraphrase them, don't "fix" their grammar, and don't drop the source URL,
  retrieval date, or attribution from any frontmatter. See
  [ATTRIBUTION.md](ATTRIBUTION.md) for what's theirs and what's MIT.
- **Never commit a secret.** Skills and templates name connectors and environment
  variables — never values. No API keys, tokens, passwords, or connection strings in
  any file, including examples. `.gitignore` is a backstop, not the control.
- **No recommended-model names in browse surfaces.** Model recommendations age out
  fast and make the repo look stale. `data/raw/` and the catalog frontmatter keep the
  value as provenance — what the source page said on the retrieval date — but the
  README and `INDEX.md` don't display it.
- **Keep prompt lines short.** Prose lines in the generated prompt blocks stay under
  ~74 characters so GitHub doesn't scroll them sideways and hide the placeholders.

## README structure

If you're touching the README, keep the four conventions borrowed from
[Best-README-Template](https://github.com/othneildrew/Best-README-Template): the
`readme-top` anchor at the top, the collapsible Table of Contents, a
`back to top ↑` link closing every `##` section, and reference-style badge
definitions at the bottom.

There are no tabs, and there can't be — GitHub strips `<style>` and `<script>` from
rendered markdown. The pill strip plus anchored `<details>` accordions is the closest
thing that works for every reader. Extend those rather than reaching for a widget.

## Pull requests

`main` is protected: no direct pushes, everything lands through a pull request.

1. Branch off `main`.
2. Make your change, run `python3 scripts/generate.py`, and commit the regenerated
   files with it.
3. Open a PR that says **why** in a sentence or two, not just what.
4. Squash-merge once it's green.

Before you push, a 30-second self-check:

- [ ] `python3 scripts/generate.py` runs clean and a second run changes nothing
- [ ] No hand-edits left in `catalog/`, `templates/`, `INDEX.md`, or the generated README block
- [ ] Anthropic content still verbatim, with source URL and retrieval date intact
- [ ] No secrets, and no machine-specific absolute paths
- [ ] Any link you added actually resolves

## Reporting something instead

Not everything needs a PR. Open an issue for a use case that's gone stale on
Anthropic's side, a template whose defaults are wrong for its domain, or a `build-skill`
run that went sideways — a transcript of what it asked and what it produced is the
most useful thing you can attach.
