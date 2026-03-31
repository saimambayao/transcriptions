#!/usr/bin/env python3
"""
OBCMS Safety Validator

Validates operations against GEMINI.md critical rules.
Blocks dangerous operations and requires explicit approval.

Usage:
    python validate-operation.py --type git --operation commit --branch staging
    python validate-operation.py --type db --operation migrate
    python validate-operation.py --type file --operation delete --file db.sqlite3
"""

import sys
import argparse
from enum import Enum
from typing import Dict, List, Tuple

class OperationType(Enum):
    GIT = "git"
    DB = "db"
    FILE = "file"

class Risk(Enum):
    SAFE = "safe"
    MEDIUM = "medium"
    HIGH = "high"
    BLOCKED = "blocked"

class Operation:
    def __init__(self, op_type: OperationType, op_name: str, risk: Risk, reason: str):
        self.type = op_type
        self.name = op_name
        self.risk = risk
        self.reason = reason

# Define blocked operations
BLOCKED_OPERATIONS = {
    ("file", "delete", "db.sqlite3"): "Database deletion is BLOCKED - db.sqlite3 contains user development data",
    ("file", "delete", "src/db.sqlite3"): "Database deletion is BLOCKED - db.sqlite3 contains user development data",
    ("git", "commit", None): "Git commit requires explicit user approval",
    ("git", "push", "main"): "Push to main (production) requires THREE confirmations",
    ("git", "push-force", None): "Force push requires explicit user approval and reason",
    ("git", "reset-hard", None): "Hard reset requires explicit user approval",
}

# Define high-risk operations
HIGH_RISK_OPERATIONS = {
    ("db", "migrate", None): "Database migrations can modify schema or data",
    ("db", "flush", None): "Database flush deletes all data",
    ("file", "delete-multiple", None): "Bulk file deletion without user review",
    ("git", "reset", None): "Git reset can lose commits",
    ("git", "merge", "main"): "Merging main into current branch",
}

# Define medium-risk operations
MEDIUM_RISK_OPERATIONS = {
    ("git", "push", "staging"): "Push to staging should be intentional",
    ("git", "commit", None): "Commit should have user approval",
    ("db", "migrate", None): "Migration should be reviewed",
}

def validate_git_operation(operation: str, branch: str = None, args: Dict = None) -> Tuple[Risk, str]:
    """Validate git operations"""

    if operation == "commit":
        return (Risk.HIGH, "Commit requires explicit user approval per GEMINI.md Rule 1")

    if operation == "push":
        if branch == "main":
            return (Risk.BLOCKED, "Push to main (production) is BLOCKED - requires THREE confirmations and explicit approval")
        elif branch == "staging":
            return (Risk.HIGH, "Push to staging - verify branch and commits")
        return (Risk.MEDIUM, f"Push to {branch} - verify correct branch")

    if operation == "push-force" or operation == "push:force":
        return (Risk.BLOCKED, "Force push is BLOCKED - requires explicit reason and approval")

    if operation == "reset-hard" or operation == "reset:hard":
        return (Risk.BLOCKED, "Hard reset is BLOCKED - can lose commits permanently")

    if operation == "reset":
        return (Risk.HIGH, "Git reset can lose commits - requires explicit approval")

    if operation == "merge":
        if branch == "main":
            return (Risk.HIGH, "Merging main into current branch - verify this is intentional")
        return (Risk.MEDIUM, f"Merge branch {branch}")

    if operation == "revert":
        return (Risk.HIGH, "Git revert modifies history - requires explicit approval")

    return (Risk.SAFE, f"Git operation {operation} is safe")

def validate_database_operation(operation: str, target: str = None, args: Dict = None) -> Tuple[Risk, str]:
    """Validate database operations"""

    if operation == "delete" or operation == "flush":
        return (Risk.BLOCKED, "Database deletion is BLOCKED - db.sqlite3 contains user development data (Rule 3)")

    if operation == "migrate":
        return (Risk.HIGH, "Database migrations can modify schema - requires review and approval")

    if operation == "reset":
        return (Risk.BLOCKED, "Database reset is BLOCKED without explicit user approval (Rule 3)")

    if operation == "makemigrations":
        return (Risk.MEDIUM, "Creating migrations - review for data loss before applying")

    if operation == "showmigrations":
        return (Risk.SAFE, "Showing migration status is safe")

    return (Risk.SAFE, f"Database operation {operation} is safe")

def validate_file_operation(operation: str, file_path: str = None, args: Dict = None) -> Tuple[Risk, str]:
    """Validate file operations"""

    blocked_files = [
        "db.sqlite3",
        "src/db.sqlite3",
        "GEMINI.md",
        "AGENTS.md",
        "GEMINI.md",
        ".env",
        ".env.local",
        ".env.example",
    ]

    if operation == "delete" or operation == "remove" or operation == "rm":
        # Check for blocked files
        if file_path:
            for blocked in blocked_files:
                if blocked in file_path:
                    reason = "Blocked file deletion"
                    if "db.sqlite3" in file_path:
                        reason = "Database deletion is BLOCKED - db.sqlite3 contains user development data (Rule 3)"
                    elif any(x in file_path for x in ["GEMINI.md", "AGENTS.md", "GEMINI.md"]):
                        reason = "Configuration file deletion is BLOCKED - critical for project"
                    elif ".env" in file_path:
                        reason = "Environment file deletion is BLOCKED - contains secrets/configuration"
                    return (Risk.BLOCKED, reason)

        return (Risk.HIGH, "File deletion requires explicit user approval (Rule 4)")

    return (Risk.SAFE, f"File operation {operation} is safe")

def validate_operation(op_type: OperationType, operation: str, target: str = None, **kwargs) -> Tuple[Risk, str]:
    """
    Validate an operation and return risk level and message

    Args:
        op_type: Type of operation (git, db, file)
        operation: Specific operation (commit, push, migrate, delete, etc)
        target: Target of operation (branch, file, table, etc)
        **kwargs: Additional arguments

    Returns:
        Tuple of (Risk level, message)
    """

    if op_type == OperationType.GIT:
        return validate_git_operation(operation, target, kwargs)
    elif op_type == OperationType.DB:
        return validate_database_operation(operation, target, kwargs)
    elif op_type == OperationType.FILE:
        return validate_file_operation(operation, target, kwargs)
    else:
        return (Risk.SAFE, f"Unknown operation type {op_type}")

def print_result(risk: Risk, message: str, op_type: OperationType, operation: str, target: str = None):
    """Print validation result"""

    symbols = {
        Risk.SAFE: "✅",
        Risk.MEDIUM: "⚠️",
        Risk.HIGH: "🔴",
        Risk.BLOCKED: "🚫",
    }

    print(f"\n{symbols[risk]} {risk.value.upper()}: {op_type.value.upper()} {operation}")
    print(f"   {message}")

    if target:
        print(f"   Target: {target}")

    if risk == Risk.BLOCKED:
        print(f"\n   ❌ This operation is BLOCKED")
        print(f"   Reason: {message}")
        return False

    if risk == Risk.HIGH:
        print(f"\n   ⚠️ This operation requires explicit user approval")
        print(f"   User must confirm before proceeding")

    return True

def main():
    parser = argparse.ArgumentParser(
        description="Validate OBCMS operations against GEMINI.md rules"
    )
    parser.add_argument("--type", choices=["git", "db", "file"], required=True)
    parser.add_argument("--operation", required=True)
    parser.add_argument("--target", default=None)
    parser.add_argument("--file", default=None, dest="file_path")
    parser.add_argument("--branch", default=None)
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    op_type = OperationType[args.type.upper()]
    risk, message = validate_operation(
        op_type,
        args.operation,
        args.target or args.file_path or args.branch
    )

    if args.json:
        import json
        print(json.dumps({
            "type": args.type,
            "operation": args.operation,
            "target": args.target or args.file_path or args.branch,
            "risk": risk.value,
            "message": message,
            "allowed": risk != Risk.BLOCKED
        }))
    else:
        allowed = print_result(
            risk,
            message,
            op_type,
            args.operation,
            args.target or args.file_path or args.branch
        )
        sys.exit(0 if allowed else 1)

if __name__ == "__main__":
    main()
