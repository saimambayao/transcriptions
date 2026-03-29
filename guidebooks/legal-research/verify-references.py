#!/usr/bin/env python3
"""
Verify legislative references in guidebook markdown files against authoritative sources.

Usage:
    python3 verify-references.py [--dir PATH] [--ref PATH]

Defaults:
    --dir   Current directory (scans 0*.md and 1*.md)
    --ref   ~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md
"""

import re
import os
import sys
import glob
import argparse
from pathlib import Path
from collections import defaultdict


def parse_baa_reference(ref_path: str) -> dict[int, str]:
    """Parse the BAA quick-reference markdown and return {number: short_title}."""
    baa_map = {}
    with open(os.path.expanduser(ref_path), "r", encoding="utf-8") as f:
        content = f.read()

    # Match rows in the Master Table: | BAA_NUM | [[...|Short Title]] | ... |
    # Pattern handles both [[BAA-N|Title]] and plain text titles
    row_pattern = re.compile(
        r"^\|\s*(\d+)\s*\|\s*"
        r"(?:\[\[.*?\|(.+?)\]\]|([^|]+?))"
        r"\s*\|",
        re.MULTILINE,
    )
    for m in row_pattern.finditer(content):
        num = int(m.group(1))
        title = (m.group(2) or m.group(3)).strip()
        baa_map[num] = title

    return baa_map


# Known wrong mappings people commonly make
KNOWN_WRONG_PATTERNS = {
    11: {
        "wrong_claims": ["Education Code", "Bangsamoro Education Code"],
        "actual": "Power of Appointment",
    },
    13: {
        "wrong_claims": ["Local Governance Code", "Bangsamoro Local Governance Code"],
        "actual": "Bangsamoro Administrative Code",
    },
    14: {
        "wrong_claims": ["Civil Service Code", "Bangsamoro Civil Service Code", "Civil Service"],
        "actual": "Extension of 2020 Appropriations",
    },
    15: {
        "wrong_claims": ["Administrative Code", "Bangsamoro Administrative Code"],
        "actual": "GAA FY 2021",
    },
    25: {
        "wrong_claims": ["Environment Code", "Bangsamoro Environment Code", "Environmental Code"],
        "actual": "Datu Blah Sinsuat Hospital Upgrade",
    },
}


def extract_baa_references(text: str) -> list[dict]:
    """Extract all BAA references with context and any claimed title."""
    refs = []
    # Patterns: BAA No. N, BAA N, BAA-N, Bangsamoro Autonomy Act No. N
    baa_pattern = re.compile(
        r"(?:BAA\s*(?:No\.?\s*)?|Bangsamoro\s+Autonomy\s+Act\s*(?:No\.?\s*)?)(\d+)"
        r"(?:\s*[-,]\s*|\s*\(|\s+)"
        r"(?:(?:the\s+|or\s+the\s+)?[\"']?([A-Z][^\"'\n\[\]]{3,80}?)[\"']?)?"
        r"(?:\s*\)|[,.\s])",
        re.IGNORECASE,
    )
    # Simpler pattern for just BAA number references
    simple_baa = re.compile(
        r"(?:BAA\s*(?:No\.?\s*)?|Bangsamoro\s+Autonomy\s+Act\s*(?:No\.?\s*)?)(\d+)",
        re.IGNORECASE,
    )

    lines = text.split("\n")
    for line_num, line in enumerate(lines, 1):
        for m in simple_baa.finditer(line):
            num = int(m.group(1))
            # Try to find a claimed title nearby
            claimed_title = extract_claimed_title(line, m.end(), num)
            context = line.strip()[:200]
            refs.append({
                "number": num,
                "claimed_title": claimed_title,
                "line": line_num,
                "context": context,
            })

    return refs


def extract_claimed_title(line: str, pos: int, baa_num: int) -> str | None:
    """Try to extract a claimed title for a BAA from surrounding text."""
    # Look for patterns like:
    # BAA No. 13 (Bangsamoro Administrative Code)
    # BAA No. 13, the Bangsamoro Administrative Code
    # BAA No. 13 or the "Bangsamoro Administrative Code"
    # BAA 13 — Bangsamoro Administrative Code
    rest = line[pos:]

    patterns = [
        # (Title) or (the Title)
        re.compile(r'^\s*\((?:the\s+)?["\']?([A-Z][^)"\']{3,80}?)["\']?\)'),
        # , the Title or "Title"
        re.compile(r'^\s*,?\s*(?:the\s+|or\s+the\s+)?["\']([A-Z][^"\']{3,80}?)["\']'),
        re.compile(r'^\s*,?\s*(?:the\s+|or\s+the\s+)?([A-Z][A-Za-z\s&-]{3,80}?)(?:\s*[,.\)\]]|$)'),
        # — Title or - Title
        re.compile(r'^\s*[—–-]\s*([A-Z][A-Za-z\s&-]{3,80}?)(?:\s*[,.\)\]]|$)'),
    ]

    for p in patterns:
        m = p.match(rest)
        if m:
            title = m.group(1).strip().rstrip(".,;:")
            # Filter out things that aren't titles
            if len(title) > 5 and not title.startswith("Section") and not title.startswith("Article"):
                return title

    return None


def extract_bol_references(text: str) -> list[dict]:
    """Extract Republic Act / BOL references."""
    refs = []
    # Rep. Act No. NNNNN, Republic Act No. NNNNN, RA NNNNN, R.A. NNNNN, R.A. No. NNNNN
    ra_pattern = re.compile(
        r"(?:Rep(?:ublic)?\.?\s*Act\.?\s*(?:No\.?\s*)?|R\.?A\.?\s*(?:No\.?\s*)?)(\d{4,5})"
        r"(?:[,\s]+(?:Art(?:icle)?\.?\s*(\w+)))?(?:[,\s]+(?:Sec(?:tion)?\.?\s*(\d+[\w.]*)))?",
        re.IGNORECASE,
    )
    # BOL Article/Section references
    bol_pattern = re.compile(
        r"(?:BOL|Bangsamoro\s+Organic\s+Law)\s*,?\s*"
        r"(?:Art(?:icle)?\.?\s*(\w+))?\s*,?\s*"
        r"(?:Sec(?:tion)?\.?\s*(\d+[\w.]*))?",
        re.IGNORECASE,
    )

    lines = text.split("\n")
    for line_num, line in enumerate(lines, 1):
        for m in ra_pattern.finditer(line):
            refs.append({
                "type": "RA",
                "number": m.group(1),
                "article": m.group(2),
                "section": m.group(3),
                "line": line_num,
                "context": line.strip()[:200],
            })
        for m in bol_pattern.finditer(line):
            if m.group(1) or m.group(2):  # Only if article or section captured
                refs.append({
                    "type": "BOL",
                    "number": "11054",
                    "article": m.group(1),
                    "section": m.group(2),
                    "line": line_num,
                    "context": line.strip()[:200],
                })

    return refs


def extract_footnotes(text: str) -> dict[str, str]:
    """Extract footnote definitions: {footnote_id: content}."""
    footnotes = {}
    fn_pattern = re.compile(r"^\[\^(\d+)\]:\s*(.+)$", re.MULTILINE)
    for m in fn_pattern.finditer(text):
        footnotes[m.group(1)] = m.group(2).strip()
    return footnotes


def extract_footnote_refs(text: str) -> list[dict]:
    """Extract inline footnote references [^N] with their context."""
    refs = []
    lines = text.split("\n")
    # Skip footnote definition lines
    fn_ref_pattern = re.compile(r"\[\^(\d+)\](?!:)")
    for line_num, line in enumerate(lines, 1):
        for m in fn_ref_pattern.finditer(line):
            refs.append({
                "id": m.group(1),
                "line": line_num,
                "context": line.strip()[:200],
            })
    return refs


def extract_percentages(text: str) -> list[dict]:
    """Extract percentage figures and statistics with context."""
    stats = []
    pct_pattern = re.compile(r"(\d+(?:\.\d+)?)\s*%")
    lines = text.split("\n")
    for line_num, line in enumerate(lines, 1):
        for m in pct_pattern.finditer(line):
            # Check if there's a footnote reference on this line
            fn_refs = re.findall(r"\[\^(\d+)\](?!:)", line)
            stats.append({
                "value": m.group(1) + "%",
                "line": line_num,
                "context": line.strip()[:200],
                "footnotes": fn_refs if fn_refs else None,
            })
    return stats


def check_baa_reference(baa_num: int, claimed_title: str | None, baa_map: dict[int, str]) -> dict:
    """Check a BAA reference against the authoritative map."""
    result = {"number": baa_num, "claimed_title": claimed_title}

    if baa_num not in baa_map:
        result["status"] = "NOT_FOUND"
        result["actual_title"] = None
        result["note"] = f"BAA {baa_num} does not exist in the authoritative reference (1-89)"
        return result

    actual = baa_map[baa_num]
    result["actual_title"] = actual

    # Check known wrong patterns first
    if baa_num in KNOWN_WRONG_PATTERNS and claimed_title:
        for wrong in KNOWN_WRONG_PATTERNS[baa_num]["wrong_claims"]:
            if wrong.lower() in claimed_title.lower():
                result["status"] = "MISMATCH"
                result["note"] = (
                    f"KNOWN ERROR: BAA {baa_num} is commonly misattributed as "
                    f"'{claimed_title}' but is actually '{actual}'"
                )
                return result

    if claimed_title is None:
        result["status"] = "MATCH"
        result["note"] = "Number-only reference (no title claimed)"
        return result

    # Fuzzy match: check if key words overlap
    actual_words = set(actual.lower().split())
    claimed_words = set(claimed_title.lower().split())
    # Remove common filler words
    filler = {"the", "of", "for", "and", "a", "an", "in", "act", "no", "no."}
    actual_key = actual_words - filler
    claimed_key = claimed_words - filler

    if actual_key & claimed_key:  # Any overlap in key words
        result["status"] = "MATCH"
        result["note"] = "Title keywords match"
    elif actual.lower() in claimed_title.lower() or claimed_title.lower() in actual.lower():
        result["status"] = "MATCH"
        result["note"] = "Title substring match"
    else:
        result["status"] = "MISMATCH"
        result["note"] = f"Claimed '{claimed_title}' but actual is '{actual}'"

    return result


def process_file(filepath: str, baa_map: dict[int, str]) -> dict:
    """Process a single markdown file and return verification results."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    filename = os.path.basename(filepath)

    # Extract all references
    baa_refs = extract_baa_references(text)
    bol_refs = extract_bol_references(text)
    footnotes = extract_footnotes(text)
    footnote_refs = extract_footnote_refs(text)
    percentages = extract_percentages(text)

    # Deduplicate BAA refs by (number, line)
    seen = set()
    unique_baa = []
    for ref in baa_refs:
        key = (ref["number"], ref["line"])
        if key not in seen:
            seen.add(key)
            unique_baa.append(ref)

    # Verify BAA references
    baa_results = []
    for ref in unique_baa:
        result = check_baa_reference(ref["number"], ref["claimed_title"], baa_map)
        result["line"] = ref["line"]
        result["context"] = ref["context"]
        baa_results.append(result)

    # Check footnotes for BAA/RA references
    footnote_baa_refs = []
    for fn_id, fn_content in footnotes.items():
        baa_in_fn = re.findall(r"BAA\s*(?:No\.?\s*)?(\d+)", fn_content, re.IGNORECASE)
        ra_in_fn = re.findall(r"(?:R\.?A\.?|Rep(?:ublic)?\.?\s*Act)\s*(?:No\.?\s*)?(\d+)", fn_content, re.IGNORECASE)
        for baa_num_str in baa_in_fn:
            baa_num = int(baa_num_str)
            result = check_baa_reference(baa_num, None, baa_map)
            result["source"] = f"Footnote [^{fn_id}]"
            result["context"] = fn_content[:200]
            footnote_baa_refs.append(result)

    # Check for statistics without footnotes
    stats_results = []
    for stat in percentages:
        has_footnote = stat["footnotes"] is not None and len(stat["footnotes"]) > 0
        footnote_exists = False
        if has_footnote:
            for fn_id in stat["footnotes"]:
                if fn_id in footnotes:
                    footnote_exists = True
                    break
        stats_results.append({
            "value": stat["value"],
            "line": stat["line"],
            "context": stat["context"],
            "has_footnote": has_footnote,
            "footnote_valid": footnote_exists if has_footnote else False,
            "source_status": "CITED" if footnote_exists else ("REF_MISSING_DEF" if has_footnote else "MISSING"),
        })

    return {
        "filename": filename,
        "filepath": filepath,
        "baa_results": baa_results,
        "footnote_baa_results": footnote_baa_refs,
        "bol_refs": bol_refs,
        "stats": stats_results,
        "footnotes": footnotes,
    }


def generate_report(results: list[dict], baa_map: dict[int, str], output_path: str):
    """Generate the VERIFICATION-REPORT.md."""
    lines = []
    total_baa = 0
    total_match = 0
    total_mismatch = 0
    total_not_found = 0
    total_bol = 0
    total_stats = 0
    total_stats_missing = 0

    lines.append("# Verification Report")
    lines.append("")
    lines.append(f"**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Reference:** BAA Quick-Reference Index ({len(baa_map)} BAAs)")
    lines.append(f"**Files scanned:** {len(results)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for res in results:
        lines.append(f"## {res['filename']}")
        lines.append("")

        # BAA References
        all_baa = res["baa_results"] + res["footnote_baa_results"]
        if all_baa:
            lines.append("### BAA References")
            lines.append("")
            lines.append("| Line | BAA | Claimed Title | Actual Title | Status | Note |")
            lines.append("|------|-----|---------------|--------------|--------|------|")

            for r in res["baa_results"]:
                claimed = r.get("claimed_title") or "_(number only)_"
                actual = r.get("actual_title") or "_(not in reference)_"
                status_icon = {"MATCH": "MATCH", "MISMATCH": "**MISMATCH**", "NOT_FOUND": "**NOT_FOUND**"}
                status = status_icon.get(r["status"], r["status"])
                note = r.get("note", "")
                lines.append(f"| {r.get('line', '-')} | {r['number']} | {claimed} | {actual} | {status} | {note} |")

                total_baa += 1
                if r["status"] == "MATCH":
                    total_match += 1
                elif r["status"] == "MISMATCH":
                    total_mismatch += 1
                elif r["status"] == "NOT_FOUND":
                    total_not_found += 1

            if res["footnote_baa_results"]:
                lines.append("")
                lines.append("**In Footnotes:**")
                lines.append("")
                for r in res["footnote_baa_results"]:
                    actual = r.get("actual_title") or "_(not in reference)_"
                    status = r["status"]
                    lines.append(f"- {r.get('source', 'Footnote')}: BAA {r['number']} = {actual} [{status}]")
                    total_baa += 1
                    if status == "MATCH":
                        total_match += 1
                    elif status == "MISMATCH":
                        total_mismatch += 1
                    elif status == "NOT_FOUND":
                        total_not_found += 1

            lines.append("")

        # BOL / RA References
        if res["bol_refs"]:
            lines.append("### BOL / Republic Act References")
            lines.append("")
            lines.append("| Line | Type | Number | Article | Section | Context |")
            lines.append("|------|------|--------|---------|---------|---------|")
            for r in res["bol_refs"]:
                art = r.get("article") or "-"
                sec = r.get("section") or "-"
                ctx = r["context"][:100].replace("|", "\\|")
                lines.append(f"| {r['line']} | {r['type']} | {r['number']} | {art} | {sec} | {ctx} |")
                total_bol += 1
            lines.append("")

        # Statistics
        if res["stats"]:
            lines.append("### Statistics / Percentages")
            lines.append("")
            lines.append("| Line | Value | Source | Context |")
            lines.append("|------|-------|--------|---------|")
            for s in res["stats"]:
                ctx = s["context"][:120].replace("|", "\\|")
                lines.append(f"| {s['line']} | {s['value']} | {s['source_status']} | {ctx} |")
                total_stats += 1
                if s["source_status"] == "MISSING":
                    total_stats_missing += 1
            lines.append("")

        if not all_baa and not res["bol_refs"] and not res["stats"]:
            lines.append("_No legislative references or statistics found._")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| **BAA references checked** | {total_baa} |")
    lines.append(f"| Matches | {total_match} |")
    lines.append(f"| **Mismatches** | **{total_mismatch}** |")
    lines.append(f"| **Not Found** | **{total_not_found}** |")
    lines.append(f"| BOL/RA references | {total_bol} |")
    lines.append(f"| Statistics found | {total_stats} |")
    lines.append(f"| Statistics without footnote | {total_stats_missing} |")
    lines.append("")

    # Highlight all mismatches and not-found at the end
    mismatches = []
    not_founds = []
    for res in results:
        for r in res["baa_results"] + res["footnote_baa_results"]:
            if r["status"] == "MISMATCH":
                mismatches.append((res["filename"], r))
            elif r["status"] == "NOT_FOUND":
                not_founds.append((res["filename"], r))

    if mismatches:
        lines.append("### All Mismatches")
        lines.append("")
        for fname, r in mismatches:
            lines.append(
                f"- **{fname}** line {r.get('line', '?')}: BAA {r['number']} "
                f"claimed as \"{r.get('claimed_title', '?')}\" "
                f"but actually \"{r.get('actual_title', '?')}\" "
                f"-- {r.get('note', '')}"
            )
        lines.append("")

    if not_founds:
        lines.append("### All Not Found")
        lines.append("")
        for fname, r in not_founds:
            lines.append(
                f"- **{fname}** line {r.get('line', '?')}: BAA {r['number']} "
                f"-- {r.get('note', 'not in authoritative reference')}"
            )
        lines.append("")

    report = "\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report written to: {output_path}")
    print(f"\nSummary: {total_baa} BAA refs checked | "
          f"{total_match} match | {total_mismatch} mismatch | {total_not_found} not found")
    print(f"         {total_bol} BOL/RA refs | {total_stats} stats ({total_stats_missing} without footnote)")

    if mismatches:
        print(f"\n!! {len(mismatches)} MISMATCH(ES) FOUND -- review report for details")
    if not_founds:
        print(f"!! {len(not_founds)} NOT_FOUND -- BAA numbers outside authoritative range")


def main():
    parser = argparse.ArgumentParser(description="Verify legislative references in guidebook markdown files")
    parser.add_argument("--dir", default=".", help="Directory containing guidebook markdown files")
    parser.add_argument(
        "--ref",
        default="~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md",
        help="Path to BAA quick-reference markdown",
    )
    parser.add_argument("--output", default=None, help="Output report path (default: VERIFICATION-REPORT.md in --dir)")
    args = parser.parse_args()

    guidebook_dir = os.path.abspath(args.dir)
    ref_path = os.path.expanduser(args.ref)
    output_path = args.output or os.path.join(guidebook_dir, "VERIFICATION-REPORT.md")

    # Validate paths
    if not os.path.isdir(guidebook_dir):
        print(f"Error: Directory not found: {guidebook_dir}")
        sys.exit(1)
    if not os.path.isfile(ref_path):
        print(f"Error: BAA reference file not found: {ref_path}")
        sys.exit(1)

    # Load BAA reference
    print(f"Loading BAA reference from: {ref_path}")
    baa_map = parse_baa_reference(ref_path)
    print(f"Loaded {len(baa_map)} BAA entries")

    # Find guidebook files
    patterns = [os.path.join(guidebook_dir, "0*.md"), os.path.join(guidebook_dir, "1*.md")]
    files = []
    for p in patterns:
        files.extend(sorted(glob.glob(p)))

    if not files:
        print(f"No guidebook files found matching 0*.md or 1*.md in {guidebook_dir}")
        sys.exit(1)

    print(f"Scanning {len(files)} files...")

    # Process each file
    results = []
    for f in files:
        print(f"  Processing: {os.path.basename(f)}")
        results.append(process_file(f, baa_map))

    # Generate report
    generate_report(results, baa_map, output_path)


if __name__ == "__main__":
    main()
