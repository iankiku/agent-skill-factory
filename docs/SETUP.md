# Setup

## Install the build-skill skill

Three ways in, from least to most involved:

**No GitHub account, no terminal — copy-paste:** open the public gist
(https://gist.github.com/iankiku/0366d5701cf8268ee05c24cd30fa366b), click **Raw**,
select all, copy. That's [`skills/build-skill/build-skill.gist.md`](../skills/build-skill/build-skill.gist.md)
in this repo — a single self-contained file with the skill body and all four
reference files inlined. Paste it in as `SKILL.md`:
- **Claude.ai / Claude Desktop / Cowork:** Settings → Capabilities → Skills → upload
  (wrap as `build-skill.zip` containing `SKILL.md` if the upload flow requires a zip).
- **Claude Code:** save to `~/.claude/skills/build-skill/SKILL.md` (all projects) or
  `.claude/skills/build-skill/SKILL.md` (one project).

**Have Node.js — CLI install:**
```bash
npx skills add iankiku/agent-skill-factory --skill build-skill
```
Pulls the full version from this repo (complete 94-entry template index, both
worked examples) via the [`skills` CLI](https://skills.sh). Add `-g` for a global
install; `npx skills update build-skill` to refresh later.

**Have git — clone and copy/symlink by hand:** zip `skills/build-skill/` and upload
it for Claude.ai/Cowork, or copy/symlink the folder into your project's
`.claude/skills/` directory (or `~/.claude/skills/` for all projects) for Claude
Code. Invoke with `/build-skill` or by asking to "build a skill for …". The folder is
self-contained — `SKILL.md` plus `references/` and `examples/` travel with it.

Note: `build-skill` reads `references/template-index.md` and template files by
relative path. In the gist/copy-paste bundle those references are inlined directly
in the same file. In claude.ai the bundled `references/` are always available;
template bodies under `templates/` are only readable when the repo itself is present
(Claude Code checkout, or a Cowork session with this repo cloned/connected). Without
them, build-skill still works — it falls back to `references/blank-skill-template.md`.

## Use a catalog template directly

1. Find your workflow in [`../INDEX.md`](../INDEX.md).
2. Copy `templates/<category>/<name>/` somewhere you can edit it.
3. Resolve every `TODO` marker — the template tells you what each one needs.
4. Rename the skill (frontmatter `name`) so it won't collide, sharpen the
   `description` for triggering, and delete the `status:` line under `metadata:`.
5. Install as above. Run it once on a low-stakes input before trusting it.

## Prerequisites by feature

Templates inherit prerequisites from their source use case (listed per template):

- **Connectors** — enable the named connector(s) in Claude's settings; they
  authenticate via their own OAuth flows. Skills never handle credentials.
- **Browser Use** — requires the Claude in Chrome extension with site permissions
  granted for the domains the skill touches.
- **Cowork** — requires a Cowork session with the relevant folder connected.
- **Claude for Excel / Word** — requires the respective add-in installed.
- **Custom visuals / Extended Thinking / Web Search / Research** — toggle the
  feature in the conversation where the skill runs.

## Secrets policy

No skill in this repo asks for, stores, or echoes credentials. If a skill you
generate needs an API that has no connector, reference an environment variable by
NAME in the skill and set the value only in the runtime's env — never in the skill
file, never in this repo. `.gitignore` blocks `.env` files as a backstop.

## Regenerating the catalog

```bash
# refresh data/raw/*.json first (re-extract from claude.com), then:
python3 scripts/generate.py   # rebuilds catalog/, templates/, INDEX.md
```

Regeneration overwrites `catalog/` and `templates/` entirely — customize copies,
not the generated trees.

## Validating your first generated skill

Follow either end-to-end example as a reference run
([1](../skills/build-skill/examples/example-1-weekly-pipeline-digest.md),
[2](../skills/build-skill/examples/example-2-invoice-folder-triage.md)): the
dry-run trace pattern in Phase 5 — one realistic input walked through every step on
paper, validations shown firing — is the acceptance test for any skill before its
first unattended run.
