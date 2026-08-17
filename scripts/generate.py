#!/usr/bin/env python3
"""Generate the use-case catalog and per-use-case skill templates from data/raw/*.json.

Idempotent: re-run after refreshing data/raw to regenerate catalog/ and templates/.
Source content is © Anthropic PBC (claude.com/resources/use-cases); this script and
the scaffolding it emits are original to this repository.
"""
import json, re, glob, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
CATALOG = os.path.join(ROOT, "catalog")
TEMPLATES = os.path.join(ROOT, "templates")

def cat_slug(cat: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")

def skill_name(slug: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")

def yml(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)

def load_all():
    items = []
    for f in sorted(glob.glob(os.path.join(RAW, "*.json"))):
        with open(f) as fh:
            items.append(json.load(fh))
    return items

# ---------- tool / auth derivation heuristics ----------
CONNECTOR_HINTS = {
    "salesforce": "Salesforce", "google calendar": "Google Calendar", "gmail": "Gmail",
    "google drive": "Google Drive", "slack": "Slack", "notion": "Notion", "jira": "Jira",
    "confluence": "Confluence", "hubspot": "HubSpot", "capital iq": "S&P Capital IQ",
    "s&p global": "S&P Global", "intercom": "Intercom", "asana": "Asana",
    "linear": "Linear", "github": "GitHub", "benchling": "Benchling",
    "pubmed": "PubMed", "microsoft 365": "Microsoft 365", "netlify": "Netlify",
    "canva": "Canva", "box": "Box", "daloopa": "Daloopa", "outlook": "Outlook",
    "claude for excel": "Claude for Excel add-in", "excel add-in": "Claude for Excel add-in",
    "claude for word": "Claude for Word add-in", "word add-in": "Claude for Word add-in",
    "apple notes": "Apple Notes", "chrome": "Claude in Chrome extension",
}

def derive_connectors(uc):
    found = set()
    hay = " ".join([uc.get("description", ""), uc.get("prompt", ""),
                    " ".join(uc.get("prerequisites", [])), uc.get("surface", "")]).lower()
    for k, v in CONNECTOR_HINTS.items():
        if re.search(r"(?<![a-z0-9])" + re.escape(k) + r"(?![a-z0-9])", hay):
            found.add(v)
    return sorted(found)

# Anthropic's pages are laid out under fixed section headings. The extractor captured
# those headings as `steps` for 51 of 94 use cases. A BARE heading is not a workflow
# step; the same heading WITH detail appended ("Describe the task (attach page…)") is.
# Match exactly, so annotated variants survive.
PAGE_HEADINGS = {
    "describe the task", "give claude context", "what claude creates",
    "follow up prompts", "follow up with refinement prompts",
    "tricks, tips, and troubleshooting",
}

def real_steps(uc):
    return [s for s in (uc.get("steps") or []) if s.strip().lower() not in PAGE_HEADINGS]

def validation_defaults(uc):
    cat = uc["category"]
    base = ["Every factual claim traces to a provided input, connector record, or cited source"]
    extra = {
        "Finance": ["All figures reconcile to source statements/workbooks; totals recomputed programmatically, not by eye",
                    "Flag (never silently correct) discrepancies between model and source data"],
        "Legal": ["No changed defined terms or citations without an explicit redline entry",
                  "Reviewed-by-human gate before anything leaves the building"],
        "Life Sciences": ["Methods/statistics restated only from the source material; no invented p-values",
                          "Units and sample sizes double-checked against source tables"],
        "Claude in Chrome": ["Nothing is submitted/saved on a website without showing the user a review step first",
                             "Site actions limited to the domains named in the workflow"],
        "Sales": ["CRM writes are drafted for approval, never auto-committed"],
        "Nonprofits": ["Donor/beneficiary PII is excluded from outputs unless explicitly requested"],
        "HR": ["No inferences about protected attributes; tone reviewed for policy compliance"],
    }
    return base + extra.get(cat, [])

def failure_defaults(uc):
    out = []
    feats = set(uc.get("features", []))
    if "Connectors" in feats or derive_connectors(uc):
        out.append("Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files")
    if "Web Search" in feats or "Research" in feats:
        out.append("Search returns thin/conflicting results → present both readings with sources instead of picking one silently")
    if "Browser Use" in feats:
        out.append("Page fails to load or selector drifts → retry once, then stop and report; never guess at form fields")
    if uc.get("surface", "").lower().find("cowork") >= 0:
        out.append("Expected files missing from the connected folder → list what was found, ask before proceeding on partial inputs")
    out.append("Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed")
    out.append("Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)")
    return out

# ---------- emitters ----------
CATALOG_DOC = """---
title: {title}
slug: {slug}
category: {category}
recommended_model: {model}
features: {features}
surface: {surface}
source_url: {source_url}
retrieved_at: {retrieved}
attribution: "© Anthropic PBC — published at claude.com/resources/use-cases"
extraction_status: {status}
---

# {title}

{description}

## Example prompt (verbatim, © Anthropic PBC)

```text
{prompt}
```
{steps_block}{prereq_block}
## Attribution

Reproduced from [{title}]({source_url}) (retrieved {retrieved}). Title, description,
prompt, and workflow content are © Anthropic PBC and remain subject to
[Anthropic's terms](https://www.anthropic.com/legal/consumer-terms). Reproduced here
for reference and skill-scaffolding with attribution; not an official Anthropic project.
"""

def emit_catalog(uc):
    steps_block = ""
    steps = real_steps(uc)
    if steps:
        steps_block = "\n## How it works (from source page)\n\n" + \
            "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps)) + "\n"
    prereq_block = ""
    if uc.get("prerequisites"):
        prereq_block = "\n## Prerequisites (from source page)\n\n" + \
            "\n".join(f"- {p}" for p in uc["prerequisites"]) + "\n"
    d = os.path.join(CATALOG, cat_slug(uc["category"]))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, uc["slug"].lower() + ".md"), "w") as f:
        f.write(CATALOG_DOC.format(
            title=uc["title"], slug=uc["slug"], category=uc["category"],
            model=uc["model"], features=json.dumps(uc.get("features", [])),
            surface=yml(uc.get("surface", "Claude.ai chat")),
            source_url=uc["source_url"], retrieved=uc["retrieved_at"],
            status=uc.get("extraction_status", "ok"),
            description=uc.get("description", ""), prompt=uc["prompt"],
            steps_block=steps_block, prereq_block=prereq_block))

TEMPLATE_DOC = """---
name: {name}
description: {trigger}
metadata:
  status: template — resolve every TODO before use
  category: {category}
  recommended_model: {model}
  features: {features}
  surface: {surface}
  source_url: {source_url}
  retrieved_at: {retrieved}
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# {title} — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

{description}

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
{prompt}
```

## Inputs

{prereqs}
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

{connectors}
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms{chrome_note}

## Workflow

{workflow}

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

{validation}
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

{failures}

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [{title}]({source_url}) (retrieved {retrieved}). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
"""

def emit_template(uc):
    name = skill_name(uc["slug"])
    # The source description is marketing prose about capability. A skill description
    # must say WHEN to fire, so leave it as an explicit TODO rather than shipping
    # trigger text that over-fires (validation-checklist enforces this).
    trigger = (f"TODO — write for triggering: when should this fire, in the user's own "
               f"words, plus one near-miss it must NOT handle. Seed use case: "
               f"{uc['title'].rstrip('.')}.")
    prereqs = "\n".join(f"- {p}" for p in uc.get("prerequisites", [])) or "- (source page listed no prerequisites)"
    conns = derive_connectors(uc)
    connectors = "\n".join(f"- {c}" for c in conns) or "- No connectors detected on the source page; base Claude capabilities only"
    steps = real_steps(uc)
    if steps:
        workflow = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))
        workflow += "\n\nTODO: rewrite as imperative steps for the executing agent."
    else:
        workflow = "TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver."
    validation = "\n".join(f"- {v}" for v in validation_defaults(uc))
    failures = "\n".join(f"- {v}" for v in failure_defaults(uc))
    chrome_note = ""
    if "Browser Use" in uc.get("features", []):
        chrome_note = ", and ANY click that finalizes state on a third-party site (browser-use skill: show a review step first)"
    d = os.path.join(TEMPLATES, cat_slug(uc["category"]), name)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "SKILL.md"), "w") as f:
        f.write(TEMPLATE_DOC.format(
            name=name, trigger=yml(trigger), category=uc["category"], model=uc["model"],
            features=json.dumps(uc.get("features", [])), surface=yml(uc.get("surface", "Claude.ai chat")),
            source_url=uc["source_url"], title=uc["title"], retrieved=uc["retrieved_at"],
            description=uc.get("description", ""), prompt=uc["prompt"], prereqs=prereqs,
            connectors=connectors, workflow=workflow, validation=validation,
            failures=failures, chrome_note=chrome_note))

def emit_indexes(items):
    by_cat = {}
    for uc in items:
        by_cat.setdefault(uc["category"], []).append(uc)
    lines = ["# Use-case catalog index",
             "",
             f"{len(items)} use cases reproduced with attribution from "
             "[claude.com/resources/use-cases](https://claude.com/resources/use-cases) "
             f"(retrieved {items[0]['retrieved_at']}). All titles, descriptions, and prompts © Anthropic PBC.",
             ""]
    for cat in sorted(by_cat):
        lines.append(f"## {cat} ({len(by_cat[cat])})")
        lines.append("")
        lines.append("| Use case | Features | Catalog | Skill template |")
        lines.append("|---|---|---|---|")
        for uc in sorted(by_cat[cat], key=lambda u: u["title"].lower()):
            cs, name = cat_slug(cat), skill_name(uc["slug"])
            lines.append(
                f"| [{uc['title']}]({uc['source_url']}) | "
                f"{', '.join(uc.get('features', [])) or '—'} | "
                f"[doc](catalog/{cs}/{uc['slug'].lower()}.md) | "
                f"[template](templates/{cs}/{name}/SKILL.md) |")
        lines.append("")
    with open(os.path.join(ROOT, "INDEX.md"), "w") as f:
        f.write("\n".join(lines))

# ---------- README field-prompt section ----------
# The README is hand-written EXCEPT the block between these markers, which is
# regenerated from data/raw/ so the 94 copy-paste prompts can never drift from the
# catalog. Edit the emitter below, not the README body between the markers.
README_BEGIN = "<!-- BEGIN GENERATED: field prompts (scripts/generate.py) -->"
README_END = "<!-- END GENERATED: field prompts -->"
REPO_BLOB = "https://github.com/iankiku/agent-skill-factory/blob/main"

# Fields first (what someone picks by industry), then the two delivery surfaces.
CATEGORY_ORDER = ["Marketing", "Sales", "Finance", "Legal", "HR", "Professional",
                  "Education", "Research", "Life Sciences", "Nonprofits", "Personal",
                  "Claude in Chrome", "Cowork"]
CATEGORY_KIND = {"Claude in Chrome": "surface", "Cowork": "surface"}
CATEGORY_BLURB = {
    "Marketing": "Campaign analysis, personas, and cross-platform content.",
    "Sales": "Deal prep, proposals, battle cards, and pipeline reporting.",
    "Finance": "Models, memos, reconciliation, and spreadsheet forensics.",
    "Legal": "Redlining, discovery timelines, and compliance prep.",
    "HR": "Onboarding and people-ops documents.",
    "Professional": "Cross-functional work: reporting, decks, brand, process.",
    "Education": "Course materials, syllabi, lit reviews, and practice loops.",
    "Research": "Literature reviews, feedback synthesis, and stats verification.",
    "Life Sciences": "Genomic and preclinical study analysis.",
    "Nonprofits": "Grants, donors, volunteers, programs, and impact reporting.",
    "Personal": "Everyday builds — apps, guides, plans, and personal systems.",
    "Claude in Chrome": "Workflows that act in the browser, on live pages.",
    "Cowork": "Long-running work on real folders and computers, kicked off remotely.",
}

def one_line(text: str, limit: int = 150) -> str:
    t = " ".join((text or "").split())
    if len(t) <= limit:
        return t
    cut = t[:limit]
    stop = max(cut.rfind(". "), cut.rfind("; "))
    if stop > limit * 0.5:
        return cut[:stop + 1]
    return cut.rsplit(" ", 1)[0].rstrip(",.;:") + "…"

def prompt_block(uc) -> str:
    """Keep every prose line under ~74 chars — GitHub code blocks scroll sideways
    past that, which hides the placeholders the reader is supposed to edit. The
    template URL is the one unavoidable long line."""
    cs, name = cat_slug(uc["category"]), skill_name(uc["slug"])
    return "\n".join([
        "```text",
        "Build me a Claude skill for [MY INDUSTRY].",
        "",
        f'Model it on the Anthropic use case "{uc["title"]}":',
        f"{REPO_BLOB}/templates/{cs}/{name}/SKILL.md",
        "",
        "Industry:   [MY INDUSTRY]",
        "Role:       [MY ROLE]",
        "Tools:      [MY TOOLS]",
        "Runs when:  [TRIGGER]",
        "",
        "Interview me on anything missing, resolve every TODO, and hand me",
        "a finished SKILL.md I can install and run unattended.",
        "```",
    ])

# GitHub strips CSS/JS from READMEs, so real tabs are impossible. The closest thing
# that actually renders everywhere: a shields.io pill strip that jumps to anchored
# accordions. Fields and surfaces get different colors so the strip reads as two
# groups at a glance. Keep the palette to these three values.
ACCENT = "D97757"   # fields
SURFACE = "6E7781"  # delivery surfaces (Chrome, Cowork)
INK = "1A1A1A"      # label side of every badge

def badge_text(s: str) -> str:
    """shields.io escaping: '-' -> '--', '_' -> '__', then URL-encode."""
    from urllib.parse import quote
    return quote(s.replace("-", "--").replace("_", "__"), safe="")

def field_anchor(cat: str) -> str:
    return "field-" + cat_slug(cat)

def pill_strip(by_cat, order) -> str:
    pills = []
    for cat in order:
        if cat not in by_cat:
            continue
        color = SURFACE if CATEGORY_KIND.get(cat) == "surface" else ACCENT
        pills.append(
            f"[![{cat}](https://img.shields.io/badge/{badge_text(cat)}-{len(by_cat[cat])}-{color}"
            f"?style=flat-square&labelColor={INK})](#{field_anchor(cat)})")
    return " ".join(pills)

def category_block(uc_cat: str, ucs) -> str:
    kind = CATEGORY_KIND.get(uc_cat, "field")
    tag = " · <em>surface, not an industry</em>" if kind == "surface" else ""
    out = [f'<a id="{field_anchor(uc_cat)}"></a>',
           "<details>",
           f"<summary><strong>{uc_cat}</strong> — {CATEGORY_BLURB.get(uc_cat, '')} "
           f"<code>{len(ucs)}</code>{tag}</summary>",
           "", "<br>", ""]
    for uc in sorted(ucs, key=lambda u: u["title"].lower()):
        cs, name = cat_slug(uc["category"]), skill_name(uc["slug"])
        out += [f"#### {uc['title']}",
                "",
                f"{one_line(uc.get('description', ''))}  ",
                f"[Source]({uc['source_url']}) · "
                f"[Catalog doc](catalog/{cs}/{uc['slug'].lower()}.md) · "
                f"[Template](templates/{cs}/{name}/SKILL.md)",
                "",
                prompt_block(uc),
                ""]
    out += ["</details>", ""]
    return "\n".join(out)

def emit_readme(items):
    readme = os.path.join(ROOT, "README.md")
    with open(readme) as f:
        body = f.read()
    if README_BEGIN not in body or README_END not in body:
        raise SystemExit(f"README.md is missing the generated-section markers:\n  {README_BEGIN}\n  {README_END}")
    by_cat = {}
    for uc in items:
        by_cat.setdefault(uc["category"], []).append(uc)
    unknown = [c for c in by_cat if c not in CATEGORY_ORDER]
    order = CATEGORY_ORDER + sorted(unknown)
    lines = ["",
             '<div align="center">', "", pill_strip(by_cat, order), "", "</div>", "",
             f"*{len(items)} use cases across {len(by_cat)} fields. Expand a field, hit the copy "
             "button on the prompt, swap the bracketed placeholders, paste into Claude.*", ""]
    for cat in order:
        if cat in by_cat:
            lines.append(category_block(cat, by_cat[cat]))
    generated = "\n".join(lines)
    start = body.index(README_BEGIN) + len(README_BEGIN)
    end = body.index(README_END)
    with open(readme, "w") as f:
        f.write(body[:start] + "\n" + generated + body[end:])


# ---------- gist bundle ----------
# The public gist's skill file is the SKILL.md plus its reference files inlined, so a
# reader can install by copying ONE file. Generating it means editing SKILL.md or a
# reference can never leave the bundle silently stale.
SKILLDIR = os.path.join(ROOT, "skills", "build-skill")
GIST_CALLOUT = '> **This is the single-file, standalone bundle of build-skill** — everything it\n> needs (the skill itself plus its four reference files) is inlined below so you\n> can install it by copying this ONE file, no `git clone` or GitHub account\n> required. See "Install" at the very bottom for the two ways to use it.\n>\n> Wherever the instructions below say "read `references/<file>.md`", the content\n> is already inlined in the "Bundled reference files" section further down this\n> same document — there is nothing extra to fetch.\n\n'
GIST_TEMPLATE_INDEX_NOTE = "### `references/template-index.md`\n\nOne line per template: `path | category | artifact/outcome | inputs & connectors | features`.\nSelect by artifact type first, then input sources, then category. Paths are relative to the repo root.\n\n**Categories covered:** Claude in Chrome, Cowork, Education, Finance, HR, Legal, Life\nSciences, Marketing, Nonprofits, Personal, Professional, Research, Sales — 94\ntemplates total. The full capability-tagged index (all 94 one-line entries) lives at\n`skills/build-skill/references/template-index.md` in the\n[full repo](https://github.com/iankiku/agent-skill-factory) — it's ~140 lines and\nwas left out of this bundle to keep the copy-paste file short. If you're using this\nstandalone bundle without the full index, treat Phase 2 as: ask the user for the\nclosest match to one of the 13 categories above, or fall back to the blank template\nbelow — never stall the draft over a missing index.\n\n"
GIST_WHAT_GOOD = '## What good looks like\n\nThe full repo ships two end-to-end example transcripts (a connector-heavy business\nskill and a file-processing skill) under `examples/` — not inlined here to keep this\nbundle short; see the "Install" section below for where to find them if you want the\ncomplete repo.\n\n'
GIST_INSTALL = '## Install\n\nCopy this whole file and save it as `SKILL.md` inside a folder named `build-skill`:\n\n- **Claude Code / Claude CLI:** `~/.claude/skills/build-skill/SKILL.md` (all projects),\n  or `.claude/skills/build-skill/SKILL.md` inside one project.\n- **Claude.ai / Claude Desktop:** Settings → Capabilities → Skills → upload this file\n  (or a `.zip` containing it as `SKILL.md`).\n- **Cowork:** same as Claude Desktop — upload via the Skills settings panel.\n\nWith Node.js, `npx skills add iankiku/agent-skill-factory --skill build-skill` installs\nthe full repo version instead (complete 94-entry template index, two worked examples).\n\nStep-by-step install and the first prompt to run: **`0-README.md`** in the\n[public gist](https://gist.github.com/iankiku/0366d5701cf8268ee05c24cd30fa366b).\nThe other 93 use cases, their templates, and a copy-paste prompt for each:\n**https://github.com/iankiku/agent-skill-factory**\n'

def emit_gist_bundle():
    src = open(os.path.join(SKILLDIR, "SKILL.md")).read()
    fm_end = src.index("---", 3) + 3
    frontmatter, body = src[:fm_end], src[fm_end:].lstrip("\n")
    # body starts "# build-skill\n\n<intro>"; splice the callout in after the H1
    h1, rest = body.split("\n", 1)
    # the bundle carries no examples/ dir, and only a note in place of the full index
    i = rest.index("## What good looks like")
    rest = rest[:i] + GIST_WHAT_GOOD + "\n"

    def ref(name):
        """Verbatim, except heading levels shift down so the bundle keeps one H1."""
        text = open(os.path.join(SKILLDIR, "references", name)).read().rstrip("\n")
        return re.sub(r"^(#{1,3}) ", r"#\1 ", text, flags=re.M)

    out = [frontmatter, "", h1, "", GIST_CALLOUT.rstrip("\n"), "", rest.rstrip("\n"), "",
           "---", "", "## Bundled reference files", "",
           "These are inlined verbatim so this single file is fully self-contained. In the full",
           "repo they live at `skills/build-skill/references/<name>.md`.", "",
           GIST_TEMPLATE_INDEX_NOTE.rstrip("\n"), "",
           "### `references/blank-skill-template.md`", "", ref("blank-skill-template.md"), "",
           "### `references/delegation-policy.md`", "", ref("delegation-policy.md"), "",
           "### `references/validation-checklist.md`", "", ref("validation-checklist.md"), "",
           "---", "", GIST_INSTALL.rstrip("\n"), ""]
    open(os.path.join(SKILLDIR, "build-skill.gist.md"), "w").write("\n".join(out))

def check_policy_sync():
    a = open(os.path.join(ROOT, "docs", "delegation-policy.md")).read()
    b = open(os.path.join(SKILLDIR, "references", "delegation-policy.md")).read()
    if a.strip() != b.strip():
        raise SystemExit("docs/delegation-policy.md and build-skill's copy have diverged")

def main():
    for d in (CATALOG, TEMPLATES):
        if os.path.isdir(d):
            shutil.rmtree(d)
    items = load_all()
    for uc in items:
        emit_catalog(uc)
        emit_template(uc)
    emit_indexes(items)
    emit_readme(items)
    check_policy_sync()
    emit_gist_bundle()
    print(f"Generated {len(items)} catalog docs, {len(items)} skill templates, "
          f"INDEX.md, the README field-prompt section, and the gist bundle")

if __name__ == "__main__":
    sys.exit(main())
