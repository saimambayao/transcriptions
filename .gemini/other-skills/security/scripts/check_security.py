#!/usr/bin/env python3
"""
Security audit script for Django templates and Python files.
Scans for common security issues including CSP violations, XSS risks, and missing CSRF tokens.

Usage: python check_security.py [directory]
"""

import os
import re
import sys
from pathlib import Path

CHECKS = {
    'inline_styles': {
        'pattern': r'style="[^"]*"',
        'message': 'Inline styles found (CSP violation)',
        'severity': 'HIGH',
        'extensions': ['.html']
    },
    'inline_onclick': {
        'pattern': r'on\w+="[^"]*"',
        'message': 'Inline event handlers found (CSP violation)',
        'severity': 'HIGH',
        'extensions': ['.html']
    },
    'missing_csrf': {
        'pattern': r'<form[^>]*method=["\']post[^>]*>(?![\s\S]*?{%\s*csrf_token\s*%})',
        'message': 'Form without CSRF token',
        'severity': 'CRITICAL',
        'extensions': ['.html']
    },
    'raw_html': {
        'pattern': r'{{\s*[\w.]+\s*\|\s*safe\s*}}',
        'message': 'Unescaped HTML output (XSS risk)',
        'severity': 'HIGH',
        'extensions': ['.html']
    },
    'hardcoded_secret': {
        'pattern': r'(SECRET_KEY|PASSWORD|API_KEY)\s*=\s*["\'][^"\']+["\']',
        'message': 'Hardcoded secret/password',
        'severity': 'CRITICAL',
        'extensions': ['.py']
    },
}

def scan_file(filepath):
    """Scan file for security issues."""
    issues = []
    ext = Path(filepath).suffix
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
            for check_name, check in CHECKS.items():
                if ext not in check['extensions']:
                    continue
                    
                matches = re.finditer(check['pattern'], content, re.MULTILINE | re.DOTALL)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    issues.append({
                        'file': filepath,
                        'line': line_num,
                        'check': check_name,
                        'message': check['message'],
                        'severity': check['severity'],
                        'code': lines[line_num-1].strip() if line_num <= len(lines) else ''
                    })
    except Exception as e:
        print(f"Error scanning {filepath}: {e}")
    
    return issues

def scan_directory(directory, extensions=['.html', '.py']):
    """Scan directory recursively."""
    all_issues = []
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ['venv', 'node_modules', '.git', '__pycache__']]
        
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, file)
                issues = scan_file(filepath)
                all_issues.extend(issues)
    
    return all_issues

def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else 'src/templates'
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found")
        sys.exit(1)
    
    print(f"Scanning {directory}...")
    issues = scan_directory(directory)
    
    if not issues:
        print("\n✅ No security issues found!")
        sys.exit(0)
    
    # Group by severity
    by_severity = {}
    for issue in issues:
        severity = issue['severity']
        if severity not in by_severity:
            by_severity[severity] = []
        by_severity[severity].append(issue)
    
    # Print report
    print(f"\n🔍 Found {len(issues)} security issues:\n")
    
    for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        if severity in by_severity:
            print(f"{severity} ({len(by_severity[severity])} issues):")
            for issue in by_severity[severity]:
                print(f"  {issue['file']}:{issue['line']}")
                print(f"    {issue['message']}")
                print(f"    Code: {issue['code']}")
                print()
    
    sys.exit(1)  # Exit with error code

if __name__ == '__main__':
    main()
