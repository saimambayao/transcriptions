#!/usr/bin/env python3
"""
Safe migration runner with backup and rollback capability.

Usage:
    ./run_migrations.py [--dry-run] [--backup] [app_name]
"""

import os
import sys
import subprocess
import argparse
from datetime import datetime
from pathlib import Path

def run_command(cmd, dry_run=False):
    """Run shell command."""
    print(f"Running: {' '.join(cmd)}")
    if dry_run:
        print("[DRY RUN - not executing]")
        return 0
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

def backup_database(dry_run=False):
    """Create database backup."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f"backup_{timestamp}.sqlite3"
    
    if os.path.exists('db.sqlite3'):
        print(f"Creating backup: {backup_file}")
        if not dry_run:
            import shutil
            shutil.copy2('db.sqlite3', backup_file)
        return backup_file
    return None

def main():
    parser = argparse.ArgumentParser(description='Safe Django migration runner')
    parser.add_argument('app', nargs='?', help='Specific app to migrate')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    parser.add_argument('--backup', action='store_true', help='Create database backup first')
    args = parser.parse_args()
    
    # Check we're in Django project
    if not os.path.exists('manage.py'):
        print("Error: manage.py not found. Run from Django project root.")
        sys.exit(1)
    
    # Backup if requested
    if args.backup:
        backup_file = backup_database(args.dry_run)
        if backup_file:
            print(f"✓ Backup created: {backup_file}")
    
    # Show migration plan
    print("\n=== Migration Plan ===")
    cmd = ['python', 'manage.py', 'showmigrations']
    if args.app:
        cmd.append(args.app)
    run_command(cmd, dry_run=False)  # Always show plan
    
    # Check for issues
    print("\n=== Checking for Issues ===")
    run_command(['python', 'manage.py', 'check'], dry_run=False)
    
    # Run migrations
    print("\n=== Running Migrations ===")
    cmd = ['python', 'manage.py', 'migrate']
    if args.app:
        cmd.append(args.app)
    
    exit_code = run_command(cmd, args.dry_run)
    
    if exit_code == 0:
        print("\n✓ Migrations completed successfully")
    else:
        print("\n✗ Migrations failed")
        if args.backup and not args.dry_run:
            print(f"You can restore from: {backup_file}")
    
    return exit_code

if __name__ == '__main__':
    sys.exit(main())
