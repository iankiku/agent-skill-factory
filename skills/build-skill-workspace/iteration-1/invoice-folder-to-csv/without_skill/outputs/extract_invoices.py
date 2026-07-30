#!/usr/bin/env python3
"""
extract_invoices.py

Walk a folder of vendor-invoice PDFs, pull out the fields a bookkeeper needs
(vendor name, invoice number, amount due, due date, PO number), and write a
single reconciliation CSV. Invoices with no PO number are flagged separately
so they can be routed for manager approval before payment.

USAGE
    python3 extract_invoices.py /path/to/vendor-invoices
    python3 extract_invoices.py /path/to/vendor-invoices -o invoices_2026-07.csv

    (If no folder is given, defaults to "./vendor-invoices" in the current dir.)

OUTPUT
    - <output>.csv                 one row per invoice, ALL invoices
    - <output>_needs_approval.csv  the subset with no PO number found (subset
                                    of the same rows, for handing to a manager)

DEPENDENCIES
    Prefers, in order, whichever of these is already installed:
        PyMuPDF (fitz)  ->  pip install pymupdf
        pypdf           ->  pip install pypdf
        pdfplumber      ->  pip install pdfplumber
    Falls back to the `pdftotext` command-line tool (poppler-utils) if none
    of the Python libraries are available. If NONE of the above are present,
    the script tells you exactly what to install and exits.

    No third-party dependency is hard-required to LAUNCH the script; it
    degrades gracefully and tells you what's missing.

IMPORTANT CAVEATS (read this before trusting the output)
    1. This is regex/heuristic extraction over PDF text, not a trained
       invoice-parsing model. It will get most well-formed invoices right,
       but vendor layouts vary a lot. Every row includes a `confidence` and
       `notes` column -- always skim rows marked "low" before handing the
       CSV to the bookkeeper.
    2. Scanned/image-only PDFs (no embedded text layer) cannot be read by
       this script at all -- there's no OCR step. Those rows will show
       "NO TEXT EXTRACTED" in notes and must be entered by hand. If this is
       common for your vendors, tell me and I'll wire in an OCR fallback
       (pytesseract) rather than assuming you want that dependency.
    3. Multi-currency amounts are not converted -- the raw amount string is
       captured as found (currency symbol stripped, thousands separators
       removed). If invoices come in multiple currencies, add a "currency"
       column need before reconciling in one ledger.
    4. "PO number not found" is a text-search result, not proof the PO
       genuinely doesn't exist -- e.g. it could be in an image/logo area, or
       use a term this script doesn't recognize (see PO_LABEL_PATTERNS
       below). Spot-check a few flagged rows the first time you run this
       against a new vendor mix.
"""

import argparse
import csv
import os
import re
import subprocess
import sys
from datetime import datetime

# --------------------------------------------------------------------------
# PDF text extraction backend (tries several libraries, falls back to CLI)
# --------------------------------------------------------------------------

_BACKEND = None


def _detect_backend():
    global _BACKEND
    if _BACKEND is not None:
        return _BACKEND
    try:
        import fitz  # PyMuPDF
        _BACKEND = ("fitz", fitz)
        return _BACKEND
    except ImportError:
        pass
    try:
        import pypdf
        _BACKEND = ("pypdf", pypdf)
        return _BACKEND
    except ImportError:
        pass
    try:
        import pdfplumber
        _BACKEND = ("pdfplumber", pdfplumber)
        return _BACKEND
    except ImportError:
        pass
    # CLI fallback
    from shutil import which
    if which("pdftotext"):
        _BACKEND = ("pdftotext_cli", None)
        return _BACKEND
    _BACKEND = (None, None)
    return _BACKEND


def extract_text(pdf_path):
    """Return best-effort plain text for a PDF, or '' if nothing extractable."""
    backend_name, mod = _detect_backend()

    if backend_name == "fitz":
        text_parts = []
        with mod.open(pdf_path) as doc:
            for page in doc:
                text_parts.append(page.get_text())
        return "\n".join(text_parts)

    if backend_name == "pypdf":
        reader = mod.PdfReader(pdf_path)
        return "\n".join((page.extract_text() or "") for page in reader.pages)

    if backend_name == "pdfplumber":
        text_parts = []
        with mod.open(pdf_path) as pdf:
            for page in pdf.pages:
                text_parts.append(page.extract_text() or "")
        return "\n".join(text_parts)

    if backend_name == "pdftotext_cli":
        result = subprocess.run(
            ["pdftotext", "-layout", pdf_path, "-"],
            capture_output=True, text=True
        )
        return result.stdout or ""

    raise RuntimeError(
        "No PDF text backend available. Install one of:\n"
        "  pip install pymupdf\n"
        "  pip install pypdf\n"
        "  pip install pdfplumber\n"
        "or install poppler's `pdftotext` CLI (brew install poppler)."
    )


# --------------------------------------------------------------------------
# Field parsing heuristics
# --------------------------------------------------------------------------

AMOUNT_RE = r"\$?\s?([0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]{2})?|[0-9]+(?:\.[0-9]{2})?)"

INVOICE_NUM_LABELS = [
    r"invoice\s*(?:number|no\.?|#)\s*[:\-]?\s*",
    r"invoice\s*[:\-]\s*",
]
AMOUNT_DUE_LABELS = [
    r"amount\s*due\s*[:\-]?\s*",
    r"balance\s*due\s*[:\-]?\s*",
    r"total\s*due\s*[:\-]?\s*",
    r"total\s*amount\s*due\s*[:\-]?\s*",
    r"grand\s*total\s*[:\-]?\s*",
    r"total\s*[:\-]\s*",
]
DUE_DATE_LABELS = [
    r"payment\s*due\s*date\s*[:\-]?\s*",
    r"due\s*date\s*[:\-]?\s*",
    r"payment\s*due\s*[:\-]?\s*",
    r"due\s*[:\-]\s*",
]
PO_LABELS = [
    r"purchase\s*order\s*(?:number|no\.?|#)?\s*[:\-]?\s*",
    r"p\.?\s?o\.?\s*(?:number|no\.?|#)?\s*[:\-]?\s*",
]
VENDOR_LABELS = [
    r"vendor\s*(?:name)?\s*[:\-]\s*",
    r"remit\s*to\s*[:\-]\s*",
    r"bill\s*from\s*[:\-]\s*",
    r"from\s*[:\-]\s*",
    r"sold\s*by\s*[:\-]\s*",
    r"company\s*[:\-]\s*",
]

DATE_PATTERNS = [
    # 01/05/2026, 1-5-26
    (r"\b(\d{1,2})[/\-](\d{1,2})[/\-](\d{2,4})\b", "mdy_slash"),
    # 2026-01-05
    (r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b", "ymd_dash"),
    # January 5, 2026 / Jan 5 2026
    (r"\b(January|February|March|April|May|June|July|August|September|"
     r"October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\.?\s+"
     r"(\d{1,2}),?\s+(\d{4})\b", "month_name"),
    # 5 January 2026
    (r"\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|"
     r"October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\.?,?\s+(\d{4})\b",
     "day_month_name"),
]

MONTHS = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3,
    "apr": 4, "april": 4, "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7,
    "aug": 8, "august": 8, "sep": 9, "sept": 9, "september": 9, "oct": 10,
    "october": 10, "nov": 11, "november": 11, "dec": 12, "december": 12,
}


def _normalize_date(raw):
    """Try each date pattern against raw text near a label; return ISO date or None."""
    if not raw:
        return None
    for pattern, kind in DATE_PATTERNS:
        m = re.search(pattern, raw, re.IGNORECASE)
        if not m:
            continue
        try:
            if kind == "mdy_slash":
                mm, dd, yy = m.groups()
                yy = int(yy)
                if yy < 100:
                    yy += 2000
                return f"{yy:04d}-{int(mm):02d}-{int(dd):02d}"
            if kind == "ymd_dash":
                yy, mm, dd = m.groups()
                return f"{int(yy):04d}-{int(mm):02d}-{int(dd):02d}"
            if kind == "month_name":
                mon, dd, yy = m.groups()
                mm = MONTHS.get(mon.lower().rstrip("."))
                if mm:
                    return f"{int(yy):04d}-{mm:02d}-{int(dd):02d}"
            if kind == "day_month_name":
                dd, mon, yy = m.groups()
                mm = MONTHS.get(mon.lower().rstrip("."))
                if mm:
                    return f"{int(yy):04d}-{mm:02d}-{int(dd):02d}"
        except ValueError:
            continue
    return None


def _find_after_label(text, label_patterns, window=60):
    """Find text following any of label_patterns; return the snippet after the label."""
    for label in label_patterns:
        m = re.search(label, text, re.IGNORECASE)
        if m:
            snippet = text[m.end(): m.end() + window]
            return snippet.strip(), m
    return None, None


def parse_amount(text):
    snippet, _ = _find_after_label(text, AMOUNT_DUE_LABELS, window=25)
    if snippet:
        m = re.match(AMOUNT_RE, snippet)
        if m:
            return m.group(1).replace(",", "")
    return None


def parse_due_date(text):
    snippet, _ = _find_after_label(text, DUE_DATE_LABELS, window=40)
    if snippet:
        d = _normalize_date(snippet)
        if d:
            return d
    return None


def parse_invoice_number(text):
    snippet, _ = _find_after_label(text, INVOICE_NUM_LABELS, window=30)
    if snippet:
        # stop at first run of whitespace-delimited token, strip trailing junk
        m = re.match(r"([A-Za-z0-9\-\_/]{2,25})", snippet)
        if m:
            candidate = m.group(1)
            # avoid accidentally grabbing "Date" if label match was "Invoice:"
            # followed immediately by a date field on same line
            if not re.match(r"^\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4}$", candidate):
                return candidate
    return None


def parse_po_number(text):
    snippet, m = _find_after_label(text, PO_LABELS, window=30)
    if snippet:
        match = re.match(r"([A-Za-z0-9\-\_/]{2,25})", snippet)
        if match:
            candidate = match.group(1)
            # guard against matching the label word itself or "N/A"/"None"
            if candidate.lower() in ("n/a", "na", "none", "-", "tbd"):
                return None
            return candidate
    return None


def parse_vendor_name(text, filename):
    snippet, _ = _find_after_label(text, VENDOR_LABELS, window=60)
    if snippet:
        line = snippet.splitlines()[0].strip(" ,.-")
        # Labels like "Remit To:"/"Bill From:" are often followed by
        # "Company Name, Street Address, City ST" on one line -- keep just
        # the company segment before the address starts.
        if "," in line:
            line = line.split(",")[0].strip()
        if line:
            return line, "label-matched"

    # Fallback: first non-trivial line of the document (often the letterhead)
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        low = line.lower()
        if low.startswith("invoice") or low in ("bill to", "ship to"):
            continue
        if re.match(r"^\d", line):  # skip lines that are just numbers/dates
            continue
        if len(line) < 2:
            continue
        return line, "first-line-fallback (low confidence)"

    # Last resort: derive from filename
    stem = os.path.splitext(os.path.basename(filename))[0]
    guess = re.sub(r"[_\-]+", " ", stem).strip()
    return guess, "filename-fallback (low confidence)"


def parse_invoice(text, filename):
    vendor, vendor_conf = parse_vendor_name(text, filename)
    invoice_number = parse_invoice_number(text)
    amount_due = parse_amount(text)
    due_date = parse_due_date(text)
    po_number = parse_po_number(text)

    notes = []
    confidence = "high"

    if not text.strip():
        notes.append("NO TEXT EXTRACTED (likely scanned/image PDF) -- enter manually")
        confidence = "none"
    if "low confidence" in vendor_conf:
        notes.append(f"vendor name via {vendor_conf}")
        confidence = "low"
    if invoice_number is None:
        notes.append("invoice number not found")
        confidence = "low"
    if amount_due is None:
        notes.append("amount due not found")
        confidence = "low"
    if due_date is None:
        notes.append("due date not found")
        confidence = "low"

    needs_approval = po_number is None
    if needs_approval and text.strip():
        notes.append("no PO number found -- needs manager approval")

    return {
        "source_file": os.path.basename(filename),
        "vendor_name": vendor,
        "invoice_number": invoice_number or "",
        "amount_due": amount_due or "",
        "due_date": due_date or "",
        "po_number": po_number or "",
        "needs_manager_approval": "TRUE" if needs_approval else "FALSE",
        "confidence": confidence,
        "notes": "; ".join(notes),
    }


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

FIELDNAMES = [
    "source_file", "vendor_name", "invoice_number", "amount_due",
    "due_date", "po_number", "needs_manager_approval", "confidence", "notes",
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", nargs="?", default="vendor-invoices",
                         help="Folder of PDF invoices (default: ./vendor-invoices)")
    parser.add_argument("-o", "--output", default="invoices.csv",
                         help="Output CSV path (default: invoices.csv)")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"ERROR: folder not found: {args.folder}", file=sys.stderr)
        sys.exit(1)

    pdf_files = sorted(
        f for f in os.listdir(args.folder) if f.lower().endswith(".pdf")
    )
    if not pdf_files:
        print(f"No PDF files found in {args.folder}", file=sys.stderr)
        sys.exit(1)

    try:
        _detect_backend()
    except Exception as e:
        print(str(e), file=sys.stderr)

    rows = []
    for fname in pdf_files:
        full_path = os.path.join(args.folder, fname)
        try:
            text = extract_text(full_path)
        except Exception as e:
            rows.append({
                "source_file": fname, "vendor_name": "", "invoice_number": "",
                "amount_due": "", "due_date": "", "po_number": "",
                "needs_manager_approval": "TRUE", "confidence": "none",
                "notes": f"FAILED TO READ PDF: {e}",
            })
            continue
        rows.append(parse_invoice(text, fname))

    with open(args.output, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    approval_rows = [r for r in rows if r["needs_manager_approval"] == "TRUE"]
    approval_path = re.sub(r"\.csv$", "", args.output) + "_needs_approval.csv"
    with open(approval_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(approval_rows)

    low_conf = [r for r in rows if r["confidence"] in ("low", "none")]

    print(f"Processed {len(rows)} invoice(s) from {args.folder}")
    print(f"  -> {args.output}")
    print(f"  -> {approval_path}  ({len(approval_rows)} flagged, no PO number found)")
    if low_conf:
        print(f"\n{len(low_conf)} row(s) need a manual double-check (low/no confidence):")
        for r in low_conf:
            print(f"  - {r['source_file']}: {r['notes']}")


if __name__ == "__main__":
    main()
