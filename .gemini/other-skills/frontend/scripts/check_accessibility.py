#!/usr/bin/env python3
"""
Accessibility audit script for React/TSX components.
Checks for WCAG 2.1 AA compliance issues in CSEA codebase.

Usage: python check_accessibility.py [directory]
"""

import os
import re
import sys
from pathlib import Path

CHECKS = {
    'missing_alt': {
        'pattern': r'<(?:img|Image)[^>]*(?<!/)\s*>|<(?:img|Image)[^>]+(?<!alt=)[^>]*(?<!/)\s*>',
        'alt_pattern': r'<(?:img|Image)[^>]*alt\s*=',
        'message': 'Image may be missing alt attribute',
        'severity': 'HIGH'
    },
    'missing_aria_label': {
        'pattern': r'<Button[^>]*(?:variant\s*=\s*["\']ghost["\']|size\s*=\s*["\']icon["\'])[^>]*>(?![^<]*aria-label)',
        'message': 'Icon button may be missing aria-label',
        'severity': 'MEDIUM'
    },
    'missing_htmlfor': {
        'pattern': r'<Label(?![^>]*htmlFor\s*=)[^>]*>',
        'message': 'Label may be missing htmlFor attribute',
        'severity': 'HIGH'
    },
    'low_contrast_text': {
        'pattern': r'text-gray-[123]00',
        'message': 'Potentially low contrast text (verify manually)',
        'severity': 'MEDIUM'
    },
    'missing_focus_ring': {
        'pattern': r'<(?:Button|Input|Select)[^>]*(?<!focus-visible:ring)[^>]*>',
        'message': 'Interactive element may need focus ring (check if shadcn handles it)',
        'severity': 'LOW'
    },
    'empty_link': {
        'pattern': r'<(?:Link|a)[^>]*>\s*<(?:Icon|Svg|img)[^>]*/?\s*>\s*</(?:Link|a)>',
        'message': 'Link with only icon needs aria-label or sr-only text',
        'severity': 'HIGH'
    },
}

def scan_file(filepath):
    """Scan TSX file for accessibility issues."""
    issues = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

            for check_name, check in CHECKS.items():
                # Special handling for alt attribute check
                if check_name == 'missing_alt':
                    img_matches = re.finditer(r'<(?:img|Image)[^>]*(?:/>|>)', content, re.MULTILINE)
                    for match in img_matches:
                        img_tag = match.group()
                        if 'alt=' not in img_tag and 'alt =' not in img_tag:
                            line_num = content[:match.start()].count('\n') + 1
                            issues.append({
                                'file': filepath,
                                'line': line_num,
                                'check': check_name,
                                'message': check['message'],
                                'severity': check['severity'],
                                'code': lines[line_num-1].strip()[:80]
                            })
                else:
                    matches = re.finditer(check['pattern'], content, re.MULTILINE | re.DOTALL)
                    for match in matches:
                        line_num = content[:match.start()].count('\n') + 1
                        issues.append({
                            'file': filepath,
                            'line': line_num,
                            'check': check_name,
                            'message': check['message'],
                            'severity': check['severity'],
                            'code': lines[line_num-1].strip()[:80]
                        })
    except Exception as e:
        print(f"Error scanning {filepath}: {e}")

    return issues

def scan_directory(directory):
    """Scan directory recursively for TSX files."""
    all_issues = []

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.next', '.git', 'dist']]

        for file in files:
            if file.endswith('.tsx') or file.endswith('.jsx'):
                filepath = os.path.join(root, file)
                issues = scan_file(filepath)
                all_issues.extend(issues)

    return all_issues

def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else 'frontend/src'

    print(f"Scanning {directory} for accessibility issues...")
    issues = scan_directory(directory)

    if not issues:
        print("\n[OK] No accessibility issues found!")
        sys.exit(0)

    # Group by severity
    by_severity = {}
    for issue in issues:
        severity = issue['severity']
        if severity not in by_severity:
            by_severity[severity] = []
        by_severity[severity].append(issue)

    # Print report
    print(f"\n[A11Y] Found {len(issues)} accessibility issues:\n")

    for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        if severity in by_severity:
            print(f"{severity} ({len(by_severity[severity])} issues):")
            for issue in by_severity[severity]:
                print(f"  {issue['file']}:{issue['line']}")
                print(f"    {issue['message']}")
                print()

    # Exit with error if HIGH or CRITICAL issues found
    has_critical = 'CRITICAL' in by_severity or 'HIGH' in by_severity
    sys.exit(1 if has_critical else 0)

if __name__ == '__main__':
    main()
