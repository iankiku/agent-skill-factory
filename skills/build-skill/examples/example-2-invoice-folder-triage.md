# End-to-end example 2: invoice folder triage (file-processing)

Second complete `build-skill` run: no connectors, pure file work in Cowork, showing
a template match on artifact+inputs, a genuinely single-agent delegation verdict
overturned by scale, and a validation-first workflow. Interview condensed.

---

## Phase 1 — Pin the outcome

**User:** Every month I dump supplier invoices into a folder and hand-sort them
before bookkeeping. Make that a skill.

**Agent (AskUserQuestion):** What does "sorted" mean at the end? — *Renamed +
foldered by supplier/month (recommended)* / *A summary spreadsheet, files untouched* /
*Both*

**User:** Both.

**Agent:** Both is two artifacts but one pass — fine as one skill. What's in the
folder besides invoices?

**User:** Receipts, the odd statement, sometimes duplicates of the same invoice.

**Agent (AskUserQuestion):** Duplicate handling? — *Move to a `_duplicates/` folder
(recommended)* / *Delete* / *Keep in place, flag in the sheet*

**User:** I don't know.

**Agent (retry 1):** Deleting is irreversible, so: *A) `_duplicates/` folder* /
*B) keep + flag in sheet*?

**User:** Fine — A.

(Resolved on attempt 2 — no assumption needed. Note the recommended option led
with the reversible choice, per policy.)

**Outcome sentence:** *When the user points the skill at an invoice folder, rename
and file every invoice as `YYYY-MM_supplier_amount.pdf` under `sorted/<supplier>/`,
divert non-invoices and duplicates to labeled folders, and produce `index.xlsx`
listing every file with supplier, date, amount, and destination — zero files
unaccounted for.*

Scope edge: does NOT do bookkeeping categorization or tax coding — refuse and point
at the bookkeeper.

## Phase 2 — Template selection

Closest on artifact (organized folder + workbook) and inputs (local folder of
mixed documents): **`templates/personal/organize-files-by-whats-in-them/SKILL.md`**,
borrowing the reconciliation validation ("every source row accounted for") from
`templates/finance/reconcile-transactions-across-your-accounts/SKILL.md`. Announced;
accepted.

## Phase 3 — Machinery highlights

- **Context:** supplier canonical names list (user supplied 12; skill appends new
  ones it meets, flagged as `NEW`); amount = grand total incl. tax; date = invoice
  date, not received date.
- **Inputs:** one folder path per run. PDFs, images, occasional .docx. Unreadable
  file → `_unreadable/`, never skipped silently.
- **Auth/tools:** none — filesystem + spreadsheet generation only. No secrets in play.
- **Permissions:** reads the target folder; writes ONLY inside it (`sorted/`,
  `_duplicates/`, `_not_invoices/`, `_unreadable/`, `index.xlsx`). Originals are
  MOVED, never deleted; no writes outside the folder.
- **Decision points:** invoice vs. receipt (has payable amount + supplier + invoice
  number → invoice; ambiguous → `_review/`); duplicate = same supplier + number +
  amount (same supplier/amount but different number is NOT a duplicate).
- **Validation (mechanical):** `count(files before) == count(rows in index.xlsx)`
  — the zero-unaccounted invariant, recomputed by script; every sorted filename
  parses back into the naming pattern; spreadsheet totals per supplier recomputed
  from rows.
- **Failure modes:** OCR fails → `_unreadable/` + row with `status=unreadable`;
  supplier not in canonical list and no confident read → `_review/`; >20% of files
  landing in `_review/` → stop and report (extraction is probably broken) rather
  than plowing on.

## Phase 4 — Delegation plan

First verdict: single-agent — extraction is sequential-feeling and the folder is
"maybe 40 files". Overturned at the dry-run: 40 independent per-file extractions is
exactly the per-item fan-out the policy names as the canonical safe case.

| Step | Decision | Why |
|---|---|---|
| Per-file field extraction (supplier, date, amount, invoice #) | **Delegate** (small model, parallel) | Independent per file. Context: one file + canonical supplier list. Output: fixed JSON (`{file, kind, supplier, date, amount, invoice_no, confidence}`). Validation: primary schema-checks all rows and re-reads any file with confidence < 0.8. Fallback: retry once; then `_review/`. |
| Duplicate detection | **Primary** | Needs the WHOLE extraction table — cross-item comparison, not independent. |
| Moves/renames + index.xlsx | **Primary** | File mutations are the sensitive action here; batched after validation passes, so a bad run costs nothing. |

## Phase 5 — Dry-run trace (shown to user)

Input: 38 files (33 PDFs, 4 JPGs, 1 DOCX).

1. 38 extraction tasks fan out → 35 clean, 2 low-confidence re-read by primary
   (1 recovers, 1 → `_review/`), 1 OCR failure → `_unreadable/`.
2. Duplicate pass on the 36-row table: 2 dupes (same supplier+number+amount) →
   `_duplicates/`; one same-amount/different-number pair correctly NOT flagged.
3. Classification: 31 invoices, 3 receipts → `_not_invoices/`.
4. Validation BEFORE any move: 38 planned rows == 38 source files ✓; all 31 target
   names parse ✓; per-supplier totals recompute ✓.
5. Moves execute; index.xlsx written; summary reports 31 sorted / 3 receipts /
   2 dupes / 1 review / 1 unreadable = 38. Zero unaccounted.

User feedback after trace: also flag invoices >$5,000 in the sheet. Added as a
highlight rule (one refinement round); checklist re-run; accepted.

---

## Final generated skill (abridged frontmatter + distinctive sections)

```markdown
---
name: invoice-folder-triage
description: Sort a folder of supplier invoices — rename to
  YYYY-MM_supplier_amount.pdf, file by supplier, divert duplicates and
  non-invoices, and build index.xlsx with every file accounted for. Use when the
  user asks to sort/triage/organize an invoice or receipts folder. Do NOT use for
  bookkeeping categorization or tax coding.
---

(...Outcome, Required context, Inputs, Permissions as specified above...)

## Workflow
1. Inventory the folder (count = N; nothing moves until step 6).
2. Fan out per-file extraction (delegated; contract in Delegation).
3. Primary validates rows, re-reads low-confidence files, runs duplicate pass.
4. Classify: invoice / receipt / statement / unreadable / review.
5. Validate: planned rows == N; names parse; totals recompute. Fail twice → stop.
6. Execute moves; write index.xlsx (highlight rows > $5,000); report the ledger.

## Delegation
Per the delegation policy this skill was built under (rules restated here so the
skill is self-contained): per-file extraction is delegated to a smaller model
and is the only parallel fan-out (independent files, no shared state); context,
output schema, validation, and fallback defined per task. Duplicate detection
(cross-item), all file mutations, and final review stay with the primary agent.
Moves are batched after validation so no file changes state on a failed run.

## Setup
1. Grant the skill access to the invoice folder (Cowork: connect the folder).
2. Provide the canonical supplier-name list (or accept the starter list of 12).
3. First run happens with moves in "plan only" mode; user approves the plan once
   before hands-off runs are allowed.
```
