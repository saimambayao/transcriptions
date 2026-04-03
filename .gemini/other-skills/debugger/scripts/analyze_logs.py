#!/usr/bin/env python3
"""
Log Analysis Tool

Automated log analysis for Django applications.
Helps identify patterns, errors, and issues in log files.

Usage:
    python scripts/analyze_logs.py production.log
    python scripts/analyze_logs.py --errors-only production.log
    python scripts/analyze_logs.py --time-range "14:00-15:00" production.log
    python scripts/analyze_logs.py --user-errors production.log
    python scripts/analyze_logs.py --top-errors 10 production.log
"""

import argparse
import re
from datetime import datetime
from collections import Counter, defaultdict
from pathlib import Path


class LogAnalyzer:
    """Analyzes Django log files for debugging."""

    def __init__(self, log_file):
        self.log_file = Path(log_file)
        self.lines = []
        self.errors = []
        self.warnings = []
        self.load_log()

    def load_log(self):
        """Load log file into memory."""
        if not self.log_file.exists():
            raise FileNotFoundError(f"Log file not found: {self.log_file}")

        with open(self.log_file, 'r', encoding='utf-8', errors='ignore') as f:
            self.lines = f.readlines()

        print(f"✅ Loaded {len(self.lines)} lines from {self.log_file}")

    def extract_errors(self):
        """Extract error and exception messages."""
        error_pattern = re.compile(r'(ERROR|CRITICAL|Exception|Traceback)', re.IGNORECASE)

        in_traceback = False
        current_error = []

        for i, line in enumerate(self.lines):
            if error_pattern.search(line):
                in_traceback = True
                current_error = [line]
            elif in_traceback:
                if line.strip() and (line.startswith(' ') or line.startswith('\t')):
                    current_error.append(line)
                else:
                    if current_error:
                        self.errors.append({
                            'line_num': i - len(current_error) + 1,
                            'message': ''.join(current_error),
                            'type': self._classify_error(current_error[0])
                        })
                    in_traceback = False
                    current_error = []

        if current_error:
            self.errors.append({
                'line_num': len(self.lines) - len(current_error) + 1,
                'message': ''.join(current_error),
                'type': self._classify_error(current_error[0])
            })

    def _classify_error(self, line):
        """Classify error type from first line."""
        if 'PermissionDenied' in line or '403' in line:
            return 'Permission'
        elif 'DoesNotExist' in line or '404' in line:
            return 'NotFound'
        elif 'IntegrityError' in line:
            return 'Database'
        elif 'ValidationError' in line:
            return 'Validation'
        elif 'KeyError' in line or 'AttributeError' in line:
            return 'Logic'
        elif 'ImportError' in line or 'ModuleNotFoundError' in line:
            return 'Import'
        else:
            return 'Other'

    def extract_warnings(self):
        """Extract warning messages."""
        warning_pattern = re.compile(r'WARNING|WARN', re.IGNORECASE)

        for i, line in enumerate(self.lines, 1):
            if warning_pattern.search(line):
                self.warnings.append({
                    'line_num': i,
                    'message': line.strip()
                })

    def analyze_error_frequency(self):
        """Count error types and messages."""
        error_types = Counter(error['type'] for error in self.errors)

        # Extract error messages (first line only)
        error_messages = []
        for error in self.errors:
            first_line = error['message'].split('\n')[0]
            # Remove timestamp and log level
            cleaned = re.sub(r'^\[.*?\]\s*', '', first_line)
            cleaned = re.sub(r'^(ERROR|CRITICAL|Exception):\s*', '', cleaned, flags=re.IGNORECASE)
            error_messages.append(cleaned.strip())

        message_counts = Counter(error_messages)

        return error_types, message_counts

    def analyze_by_time(self, time_range=None):
        """Analyze errors by time period."""
        time_pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]')

        errors_by_hour = defaultdict(int)

        for error in self.errors:
            match = time_pattern.search(error['message'])
            if match:
                timestamp_str = match.group(1)
                try:
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                    hour_key = timestamp.strftime('%Y-%m-%d %H:00')

                    if time_range:
                        start, end = time_range.split('-')
                        hour = timestamp.hour
                        if int(start.split(':')[0]) <= hour <= int(end.split(':')[0]):
                            errors_by_hour[hour_key] += 1
                    else:
                        errors_by_hour[hour_key] += 1
                except ValueError:
                    pass

        return dict(sorted(errors_by_hour.items()))

    def analyze_request_errors(self):
        """Analyze HTTP request errors."""
        request_pattern = re.compile(r'(GET|POST|PUT|DELETE|PATCH)\s+([^\s]+)')
        status_pattern = re.compile(r'(\d{3})')

        requests = []

        for i, line in enumerate(self.lines):
            request_match = request_pattern.search(line)
            if request_match:
                method = request_match.group(1)
                path = request_match.group(2)

                # Look for status code in same or next few lines
                status_code = None
                for j in range(i, min(i + 5, len(self.lines))):
                    status_match = status_pattern.search(self.lines[j])
                    if status_match:
                        status_code = status_match.group(1)
                        break

                if status_code and status_code.startswith(('4', '5')):
                    requests.append({
                        'method': method,
                        'path': path,
                        'status': status_code,
                        'line_num': i + 1
                    })

        # Count by path
        path_errors = Counter(f"{req['method']} {req['path']}" for req in requests)

        # Count by status
        status_errors = Counter(req['status'] for req in requests)

        return requests, path_errors, status_errors

    def find_user_errors(self):
        """Find errors associated with specific users."""
        user_pattern = re.compile(r'user[_\s]?(?:id|email)?[:\s=]+([^\s,\]]+)', re.IGNORECASE)

        user_errors = defaultdict(list)

        for error in self.errors:
            matches = user_pattern.findall(error['message'])
            for user_id in matches:
                user_errors[user_id].append(error)

        return user_errors

    def print_summary(self):
        """Print analysis summary."""
        print(f"\n{'='*70}")
        print("LOG ANALYSIS SUMMARY")
        print(f"{'='*70}\n")

        print(f"Total Lines: {len(self.lines)}")
        print(f"Total Errors: {len(self.errors)}")
        print(f"Total Warnings: {len(self.warnings)}")

        # Error types
        print(f"\n{'-'*70}")
        print("ERROR BREAKDOWN BY TYPE:")
        print(f"{'-'*70}\n")

        error_types, message_counts = self.analyze_error_frequency()

        for error_type, count in error_types.most_common():
            print(f"  {error_type:20s}: {count:4d} occurrences")

        # Top error messages
        print(f"\n{'-'*70}")
        print("TOP 10 ERROR MESSAGES:")
        print(f"{'-'*70}\n")

        for message, count in message_counts.most_common(10):
            print(f"  [{count:3d}x] {message[:60]}")

        # Time analysis
        print(f"\n{'-'*70}")
        print("ERRORS BY TIME PERIOD:")
        print(f"{'-'*70}\n")

        errors_by_time = self.analyze_by_time()
        for time_period, count in list(errors_by_time.items())[-10:]:
            print(f"  {time_period}: {count} errors")

        # Request errors
        print(f"\n{'-'*70}")
        print("HTTP REQUEST ERRORS:")
        print(f"{'-'*70}\n")

        requests, path_errors, status_errors = self.analyze_request_errors()

        print("By Status Code:")
        for status, count in status_errors.most_common():
            print(f"  {status}: {count} requests")

        print("\nTop Failing Endpoints:")
        for path, count in path_errors.most_common(5):
            print(f"  [{count:3d}x] {path}")

    def print_detailed_errors(self, top_n=10):
        """Print detailed error information."""
        print(f"\n{'='*70}")
        print(f"DETAILED ERROR REPORT (Top {top_n})")
        print(f"{'='*70}\n")

        for i, error in enumerate(self.errors[:top_n], 1):
            print(f"\nError #{i} (Line {error['line_num']}):")
            print(f"Type: {error['type']}")
            print(f"{'-'*70}")
            print(error['message'][:500])  # Limit to 500 chars
            print(f"{'-'*70}")

    def export_csv(self, output_file='error_analysis.csv'):
        """Export errors to CSV for further analysis."""
        import csv

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['line_num', 'type', 'message_preview']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for error in self.errors:
                # Get first line of error message
                preview = error['message'].split('\n')[0][:100]
                writer.writerow({
                    'line_num': error['line_num'],
                    'type': error['type'],
                    'message_preview': preview
                })

        print(f"\n✅ Exported {len(self.errors)} errors to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Log Analysis Tool for Django applications',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/analyze_logs.py production.log
  python scripts/analyze_logs.py --errors-only production.log
  python scripts/analyze_logs.py --detailed 5 production.log
  python scripts/analyze_logs.py --export errors.csv production.log
        """
    )

    parser.add_argument('logfile', help='Path to log file')
    parser.add_argument('--errors-only', action='store_true', help='Show only error summary')
    parser.add_argument('--detailed', type=int, metavar='N', help='Show top N detailed errors')
    parser.add_argument('--time-range', metavar='HH:MM-HH:MM', help='Filter by time range (e.g., 14:00-15:00)')
    parser.add_argument('--user-errors', action='store_true', help='Group errors by user')
    parser.add_argument('--export', metavar='FILE', help='Export errors to CSV file')

    args = parser.parse_args()

    # Analyze log
    try:
        analyzer = LogAnalyzer(args.logfile)
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return

    print("Analyzing logs...")
    analyzer.extract_errors()
    analyzer.extract_warnings()

    # Print summary
    analyzer.print_summary()

    # Detailed errors
    if args.detailed:
        analyzer.print_detailed_errors(args.detailed)

    # User errors
    if args.user_errors:
        print(f"\n{'='*70}")
        print("ERRORS BY USER:")
        print(f"{'='*70}\n")

        user_errors = analyzer.find_user_errors()
        for user_id, errors in sorted(user_errors.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
            print(f"  User {user_id}: {len(errors)} errors")

    # Export
    if args.export:
        analyzer.export_csv(args.export)


if __name__ == "__main__":
    main()
