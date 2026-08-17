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

def validation_defaults(uc):
    cat = uc["category"]
    base = ["Output matches the outcome statement above (spot-check against the seed prompt's asks)",
            "Every factual claim is traceable to a provided input, connector record, or cited source"]
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
    if uc.get("steps"):
        steps_block = "\n## How it works (from source page)\n\n" + \
            "\n".join(f"{i+1}. {s}" for i, s in enumerate(uc["steps"])) + "\n"
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
  status: template — customize all TODO markers before use
  category: {category}
  recommended_model: {model}
  features: {features}
  surface: {surface}
  source_url: {source_url}
  source_title: {title}
  retrieved_at: {retrieved}
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# {title} — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

{description}

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
{prompt}
```

## Required context and inputs

{prereqs}
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

{connectors}
- TODO: confirm which connectors are enabled in the runtime that will execute this skill
- Authentication: connectors authenticate via their own OAuth flows — this skill must
  NEVER ask for, store, or echo credentials, tokens, or API keys. If auth is missing,
  stop and tell the user which connector to enable.

## Permissions and sensitive actions

- Reads: TODO (folders, channels, records this skill may read)
- Writes: TODO (what it may create/modify, and where)
- Held back for the primary agent / human: sending external communications, financial
  transactions, deleting or overwriting originals, submitting web forms{chrome_note}

## Workflow

{workflow}

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

{validation}
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

{failures}

## Delegation

Apply the repo's delegation policy (`docs/delegation-policy.md` — bundle or restate
it if you install this skill outside the repo). Defaults for this template:

- Run single-agent unless a step fans out over independent items (files, records,
  vendors, channels). Only independent work parallelizes.
- Each delegated task must ship with: the minimal context slice it needs, an explicit
  output contract, a validation check the primary agent runs on the result, and a
  fallback if it returns empty or fails.
- Final review, synthesis, and every sensitive action listed above stay with the
  primary agent.
- TODO: name the concrete subtasks (if any) that qualify for delegation here.

## Attribution

Derived from [{title}]({source_url}) (retrieved {retrieved}). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
"""

def emit_template(uc):
    name = skill_name(uc["slug"])
    trigger = (uc.get("description", "") or uc["title"]).strip().rstrip(".")
    trigger = f"{trigger}. Use for tasks like “{uc['title'].rstrip('.')}” and close variants. TEMPLATE — customize before installing."
    prereqs = "\n".join(f"- {p}" for p in uc.get("prerequisites", [])) or "- (source page listed no prerequisites)"
    conns = derive_connectors(uc)
    connectors = "\n".join(f"- {c}" for c in conns) or "- No connectors detected on the source page; base Claude capabilities only"
    if uc.get("steps"):
        workflow = "\n".join(f"{i+1}. {s}" for i, s in enumerate(uc["steps"]))
        workflow += "\n\nTODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps."
    else:
        workflow = "TODO: decompose the seed prompt into 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver."
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
        lines.append("| Use case | Model | Features | Catalog | Skill template |")
        lines.append("|---|---|---|---|---|")
        for uc in sorted(by_cat[cat], key=lambda u: u["title"].lower()):
            cs, name = cat_slug(cat), skill_name(uc["slug"])
            lines.append(
                f"| [{uc['title']}]({uc['source_url']}) | {uc['model']} | "
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
    return t[:limit].rsplit(" ", 1)[0].rstrip(",.;:") + "…"

def prompt_block(uc) -> str:
    cs, name = cat_slug(uc["category"]), skill_name(uc["slug"])
    return "\n".join([
        "```text",
        f'Build me a Claude skill for [MY INDUSTRY], modeled on the Anthropic use case "{uc["title"]}".',
        "",
        f"Start from this template: {REPO_BLOB}/templates/{cs}/{name}/SKILL.md",
        "",
        "My context — industry: [MY INDUSTRY] · role: [MY ROLE] · tools I use: [MY TOOLS] · when it runs: [TRIGGER]",
        "",
        "Use the build-skill workflow: interview me on anything missing, resolve every TODO,",
        "and hand me a finished SKILL.md I can install and run unattended.",
        "```",
    ])

def category_block(uc_cat: str, ucs) -> str:
    kind = CATEGORY_KIND.get(uc_cat, "field")
    label = f"{uc_cat} ({len(ucs)})" + (" — surface, not an industry" if kind == "surface" else "")
    out = [f"<details>", f"<summary><strong>{label}</strong> — {CATEGORY_BLURB.get(uc_cat, '')}</summary>", ""]
    for uc in sorted(ucs, key=lambda u: u["title"].lower()):
        cs, name = cat_slug(uc["category"]), skill_name(uc["slug"])
        out += [f"#### {uc['title']}",
                "",
                f"{one_line(uc.get('description', ''))}  ",
                f"[Source]({uc['source_url']}) · [Catalog doc](catalog/{cs}/{uc['slug'].lower()}.md) · "
                f"[Template](templates/{cs}/{name}/SKILL.md) · {uc['model']}",
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
    lines = ["", f"*{len(items)} use cases across {len(by_cat)} fields, regenerated from `data/raw/` — "
                 "each one expands to a copy-paste prompt. Click the copy icon on the code block, "
                 "swap the bracketed placeholders, paste into Claude.*", ""]
    for cat in order:
        if cat in by_cat:
            lines.append(category_block(cat, by_cat[cat]))
    generated = "\n".join(lines)
    start = body.index(README_BEGIN) + len(README_BEGIN)
    end = body.index(README_END)
    with open(readme, "w") as f:
        f.write(body[:start] + "\n" + generated + body[end:])

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
    print(f"Generated {len(items)} catalog docs, {len(items)} skill templates, "
          f"INDEX.md, and the README field-prompt section")

if __name__ == "__main__":
    sys.exit(main())
