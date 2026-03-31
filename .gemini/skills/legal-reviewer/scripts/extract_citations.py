#!/usr/bin/env python3
"""
Extract all legal citations from a Bangsamoro parliamentary resolution.

This script reads a resolution file (in markdown format) and systematically
extracts all legal citations, categorizing them by type (Constitutional,
Supreme Court, Republic Act, Bangsamoro Autonomy Act, etc.).

Usage:
    python3 extract_citations.py <resolution_file> [output_file]

Example:
    python3 extract_citations.py Internal-Shariah-Division-PRLS.md citations.txt
"""

import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple


class CitationExtractor:
    """Extract legal citations from resolution text."""

    def __init__(self):
        self.citations = []
        self.footnotes = {}
        self.whereas_clauses = []
        self.resolved_clauses = []

    def extract_from_file(self, filepath: str) -> Dict:
        """Extract citations from a resolution file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        return self.extract_citations(content)

    def extract_citations(self, text: str) -> Dict:
        """Extract all citations from resolution text."""

        # Extract WHEREAS clauses
        self._extract_whereas_clauses(text)

        # Extract RESOLVED clauses
        self._extract_resolved_clauses(text)

        # Extract footnotes
        self._extract_footnotes(text)

        # Find citations in WHEREAS clauses
        self._find_citations_in_text(text)

        return {
            'total_citations': len(self.citations),
            'citations': self.citations,
            'whereas_clauses': self.whereas_clauses,
            'resolved_clauses': self.resolved_clauses,
            'footnotes': self.footnotes
        }

    def _extract_whereas_clauses(self, text: str):
        """Extract all WHEREAS clauses."""
        pattern = r'WHEREAS,\s*(.+?)(?=\nWHEREAS,|\n\nRESOLVED|$)'
        matches = re.findall(pattern, text, re.DOTALL)

        for i, match in enumerate(matches, 1):
            self.whereas_clauses.append({
                'number': i,
                'text': match.strip()[:200] + '...' if len(match.strip()) > 200 else match.strip()
            })

    def _extract_resolved_clauses(self, text: str):
        """Extract all RESOLVED clauses."""
        pattern = r'(RESOLVED[^,]*),\s*(.+?)(?=\nRESOLVED|---|\n\n##|$)'
        matches = re.findall(pattern, text, re.DOTALL)

        for i, (clause_type, clause_text) in enumerate(matches, 1):
            self.resolved_clauses.append({
                'number': i,
                'type': clause_type.strip(),
                'text': clause_text.strip()[:200] + '...' if len(clause_text.strip()) > 200 else clause_text.strip()
            })

    def _extract_footnotes(self, text: str):
        """Extract footnotes from the resolution."""
        # Find footnote section
        footnote_section = re.search(r'## FOOTNOTES\n(.*?)(?=\n---|\Z)', text, re.DOTALL)
        if not footnote_section:
            return

        footnote_text = footnote_section.group(1)

        # Extract individual footnotes
        pattern = r'([¹²³⁴⁵⁶⁷⁸⁹⁰]+)\s+(.+?)(?=\n[¹²³⁴⁵⁶⁷⁸⁹⁰]+\s|\Z)'
        matches = re.findall(pattern, footnote_text, re.DOTALL)

        for superscript, content in matches:
            self.footnotes[superscript] = content.strip()

    def _find_citations_in_text(self, text: str):
        """Find legal citations in the text."""
        citations = []

        # Pattern 1: Constitutional citations
        const_pattern = r'(\d+\d{2}\s+Philippine\s+Constitution|Philippine\s+Constitution|CONST\.?),?\s+(?:Art\.?|Article)\s+([IVX]+),?\s+(?:Sec\.?|Section)\s+(\d+)'
        for match in re.finditer(const_pattern, text, re.IGNORECASE):
            citations.append({
                'type': 'Constitutional',
                'source': match.group(0),
                'article': match.group(2),
                'section': match.group(3),
                'location': self._find_location_in_text(text, match.start())
            })

        # Pattern 2: Republic Act citations
        ra_pattern = r'Republic\s+Act\s+(?:No\.?)\s+(\d+)|R\.?A\.?\s+(\d+)|Rep\.\s+Act\s+(?:No\.?)\s+(\d+)'
        for match in re.finditer(ra_pattern, text, re.IGNORECASE):
            ra_number = match.group(1) or match.group(2) or match.group(3)
            citations.append({
                'type': 'Republic Act',
                'source': match.group(0),
                'ra_number': ra_number,
                'location': self._find_location_in_text(text, match.start())
            })

        # Pattern 3: Supreme Court cases
        sc_pattern = r'(?P<case_name>[\w\s]+?)\s+(?:v\.|versus)\s+(?:[\w\s]+?),?\s+G\.?R\.?\s+(?:No\.?|Nos\.?)\s+(?P<gr_number>[\d\,\s]+?)(?:,\s+(?P<date>\d{4}))?'
        for match in re.finditer(sc_pattern, text):
            citations.append({
                'type': 'Supreme Court',
                'source': match.group(0),
                'case_name': match.group('case_name').strip(),
                'gr_number': match.group('gr_number').strip(),
                'date': match.group('date'),
                'location': self._find_location_in_text(text, match.start())
            })

        # Pattern 4: Bangsamoro Autonomy Acts
        baa_pattern = r'Bangsamoro\s+Autonomy\s+Act\s+(?:No\.?)\s+(\d+)|B\.?A\.?A\.?\s+(\d+)'
        for match in re.finditer(baa_pattern, text, re.IGNORECASE):
            baa_number = match.group(1) or match.group(2)
            citations.append({
                'type': 'Bangsamoro Autonomy Act',
                'source': match.group(0),
                'baa_number': baa_number,
                'location': self._find_location_in_text(text, match.start())
            })

        # Remove duplicates
        unique_citations = []
        seen = set()
        for citation in citations:
            key = (citation['type'], citation['source'])
            if key not in seen:
                unique_citations.append(citation)
                seen.add(key)

        self.citations = unique_citations

    def _find_location_in_text(self, text: str, position: int) -> str:
        """Find which WHEREAS/RESOLVED clause contains this position."""

        # Check WHEREAS clauses
        for clause_num, whereas in enumerate(self.whereas_clauses, 1):
            whereas_pattern = f'WHEREAS {clause_num}'
            if whereas_pattern in text[:position]:
                continue
            elif whereas_pattern in text[position:position+500]:
                return f'WHEREAS {clause_num}'

        # Check RESOLVED clauses
        if 'RESOLVED' in text[max(0, position-500):position+500]:
            return 'RESOLVED Clause'

        # Check Footnotes
        if '## FOOTNOTES' in text[max(0, position-1000):position]:
            return 'Footnote'

        return 'Unknown Location'

    def generate_report(self) -> str:
        """Generate a formatted citation extraction report."""
        report = []
        report.append("=" * 80)
        report.append("CITATION EXTRACTION REPORT")
        report.append("=" * 80)
        report.append("")

        # Summary
        report.append(f"Total Unique Citations Found: {len(self.citations)}")
        report.append(f"Total WHEREAS Clauses: {len(self.whereas_clauses)}")
        report.append(f"Total RESOLVED Clauses: {len(self.resolved_clauses)}")
        report.append(f"Total Footnotes: {len(self.footnotes)}")
        report.append("")

        # Citations by type
        report.append("CITATIONS BY TYPE:")
        report.append("-" * 80)

        citation_types = {}
        for citation in self.citations:
            ctype = citation['type']
            citation_types[ctype] = citation_types.get(ctype, 0) + 1

        for ctype, count in sorted(citation_types.items()):
            report.append(f"  {ctype}: {count}")
        report.append("")

        # Detailed citations
        report.append("DETAILED CITATION LIST:")
        report.append("-" * 80)

        for i, citation in enumerate(self.citations, 1):
            report.append(f"\n[{i}] {citation['type']}")
            report.append(f"    Source: {citation['source']}")
            report.append(f"    Location: {citation['location']}")

            # Type-specific details
            if citation['type'] == 'Constitutional':
                report.append(f"    Article: {citation.get('article', 'N/A')}")
                report.append(f"    Section: {citation.get('section', 'N/A')}")

            elif citation['type'] == 'Republic Act':
                report.append(f"    RA Number: {citation.get('ra_number', 'N/A')}")

            elif citation['type'] == 'Supreme Court':
                report.append(f"    Case: {citation.get('case_name', 'N/A')}")
                report.append(f"    G.R. Number: {citation.get('gr_number', 'N/A')}")
                report.append(f"    Date: {citation.get('date', 'N/A')}")

            elif citation['type'] == 'Bangsamoro Autonomy Act':
                report.append(f"    BAA Number: {citation.get('baa_number', 'N/A')}")

        report.append("\n" + "=" * 80)

        return "\n".join(report)

    def export_to_json(self, filepath: str):
        """Export citations to JSON format."""
        data = {
            'total_citations': len(self.citations),
            'citations_by_type': self._group_citations_by_type(),
            'citations': self.citations,
            'whereas_clauses': self.whereas_clauses,
            'resolved_clauses': self.resolved_clauses
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _group_citations_by_type(self) -> Dict[str, int]:
        """Group citations by type."""
        types = {}
        for citation in self.citations:
            ctype = citation['type']
            types[ctype] = types.get(ctype, 0) + 1
        return types


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python3 extract_citations.py <resolution_file> [output_file]")
        print("\nExample: python3 extract_citations.py resolution.md citations_report.txt")
        sys.exit(1)

    resolution_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    # Check file exists
    if not Path(resolution_file).exists():
        print(f"Error: File '{resolution_file}' not found")
        sys.exit(1)

    # Extract citations
    extractor = CitationExtractor()
    result = extractor.extract_from_file(resolution_file)

    # Generate and print report
    report = extractor.generate_report()
    print(report)

    # Save report if output file specified
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport saved to: {output_file}")

    # Also save JSON format for programmatic use
    json_file = output_file.replace('.txt', '.json') if output_file else 'citations.json'
    extractor.export_to_json(json_file)
    print(f"Citations exported to: {json_file}")


if __name__ == '__main__':
    main()
