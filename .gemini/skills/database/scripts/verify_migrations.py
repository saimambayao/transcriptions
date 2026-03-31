#!/usr/bin/env python3
"""
Verify Django migration dependency chains.

Usage:
    python verify_migrations.py <backend_path>
    python verify_migrations.py /path/to/backend

Features:
- Detects circular dependencies
- Finds missing dependencies
- Identifies orphaned migrations
- Validates dependency order
- Checks for conflicting migrations
"""
import os
import re
import sys
import ast
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional


class MigrationVerifier:
    """Verify migration dependency chains."""

    def __init__(self, backend_path: str):
        self.backend_path = Path(backend_path)
        self.apps_path = self.backend_path / "apps"
        self.migrations: Dict[str, Dict[str, dict]] = {}  # app -> {migration_name -> data}
        self.issues: List[dict] = []

    def scan_migrations(self) -> None:
        """Scan all migration files in the backend."""
        if not self.apps_path.exists():
            print(f"Error: Apps directory not found at {self.apps_path}")
            sys.exit(1)

        for app_dir in self.apps_path.iterdir():
            if not app_dir.is_dir():
                continue
            migrations_dir = app_dir / "migrations"
            if not migrations_dir.exists():
                continue

            app_name = app_dir.name
            self.migrations[app_name] = {}

            for migration_file in migrations_dir.glob("*.py"):
                if migration_file.name == "__init__.py":
                    continue

                migration_name = migration_file.stem
                migration_data = self._parse_migration(migration_file)
                if migration_data:
                    self.migrations[app_name][migration_name] = migration_data

    def _parse_migration(self, filepath: Path) -> Optional[dict]:
        """Parse a migration file to extract dependencies."""
        try:
            with open(filepath, "r") as f:
                content = f.read()

            tree = ast.parse(content)

            dependencies = []
            operations = []

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name == "Migration":
                    for item in node.body:
                        if isinstance(item, ast.Assign):
                            for target in item.targets:
                                if isinstance(target, ast.Name):
                                    if target.id == "dependencies":
                                        dependencies = self._extract_dependencies(item.value)
                                    elif target.id == "operations":
                                        operations = self._extract_operations(item.value)

            return {
                "filepath": filepath,
                "dependencies": dependencies,
                "operations": operations,
            }
        except Exception as e:
            self.issues.append({
                "type": "parse_error",
                "severity": "error",
                "file": str(filepath),
                "message": f"Failed to parse migration: {e}",
            })
            return None

    def _extract_dependencies(self, node) -> List[Tuple[str, str]]:
        """Extract dependencies from AST node."""
        deps = []
        if isinstance(node, ast.List):
            for elt in node.elts:
                if isinstance(elt, ast.Tuple) and len(elt.elts) == 2:
                    app = self._get_string_value(elt.elts[0])
                    migration = self._get_string_value(elt.elts[1])
                    if app and migration:
                        deps.append((app, migration))
        return deps

    def _extract_operations(self, node) -> List[str]:
        """Extract operation types from AST node."""
        ops = []
        if isinstance(node, ast.List):
            for elt in node.elts:
                if isinstance(elt, ast.Call):
                    if isinstance(elt.func, ast.Attribute):
                        ops.append(elt.func.attr)
                    elif isinstance(elt.func, ast.Name):
                        ops.append(elt.func.id)
        return ops

    def _get_string_value(self, node) -> Optional[str]:
        """Extract string value from AST node."""
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Str):  # Python < 3.8
            return node.s
        return None

    def verify_dependencies(self) -> None:
        """Verify all migration dependencies."""
        self._check_missing_dependencies()
        self._check_circular_dependencies()
        self._check_orphaned_migrations()
        self._check_conflicting_migrations()
        self._check_dependency_order()

    def _check_missing_dependencies(self) -> None:
        """Check for missing dependencies."""
        for app, migrations in self.migrations.items():
            for migration_name, data in migrations.items():
                for dep_app, dep_migration in data["dependencies"]:
                    # Handle swappable dependencies (auth.User)
                    if dep_migration == "__first__":
                        continue
                    if dep_migration == "__latest__":
                        continue

                    # Check if dependency exists
                    if dep_app not in self.migrations:
                        # Could be an external app (auth, contenttypes, etc.)
                        if dep_app not in ["auth", "contenttypes", "sessions", "admin"]:
                            self.issues.append({
                                "type": "missing_app",
                                "severity": "warning",
                                "file": str(data["filepath"]),
                                "message": f"{app}.{migration_name} depends on unknown app '{dep_app}'",
                                "migration": f"{app}.{migration_name}",
                                "missing_app": dep_app,
                            })
                    elif dep_migration not in self.migrations[dep_app]:
                        self.issues.append({
                            "type": "missing_dependency",
                            "severity": "error",
                            "file": str(data["filepath"]),
                            "message": f"{app}.{migration_name} depends on missing migration '{dep_app}.{dep_migration}'",
                            "migration": f"{app}.{migration_name}",
                            "missing": f"{dep_app}.{dep_migration}",
                        })

    def _check_circular_dependencies(self) -> None:
        """Check for circular dependencies using DFS."""
        def find_cycle(app: str, migration: str, path: List[str], visited: Set[str]) -> Optional[List[str]]:
            key = f"{app}.{migration}"
            if key in path:
                cycle_start = path.index(key)
                return path[cycle_start:] + [key]
            if key in visited:
                return None

            visited.add(key)
            path = path + [key]

            if app in self.migrations and migration in self.migrations[app]:
                for dep_app, dep_migration in self.migrations[app][migration]["dependencies"]:
                    if dep_migration in ["__first__", "__latest__"]:
                        continue
                    if dep_app in self.migrations and dep_migration in self.migrations.get(dep_app, {}):
                        cycle = find_cycle(dep_app, dep_migration, path, visited)
                        if cycle:
                            return cycle
            return None

        visited: Set[str] = set()
        for app, migrations in self.migrations.items():
            for migration_name in migrations:
                cycle = find_cycle(app, migration_name, [], visited)
                if cycle:
                    self.issues.append({
                        "type": "circular_dependency",
                        "severity": "error",
                        "message": f"Circular dependency detected: {' -> '.join(cycle)}",
                        "cycle": cycle,
                    })
                    return  # One cycle is enough to report

    def _check_orphaned_migrations(self) -> None:
        """Check for migrations with no path to initial."""
        for app, migrations in self.migrations.items():
            # Find initial migration(s)
            initials = [m for m in migrations if m == "0001_initial" or m.endswith("_initial")]

            if not initials and migrations:
                # Check if any migration has no same-app dependencies (potential orphan)
                for migration_name, data in migrations.items():
                    same_app_deps = [d for d in data["dependencies"] if d[0] == app]
                    if not same_app_deps and migration_name != "0001_initial":
                        self.issues.append({
                            "type": "potential_orphan",
                            "severity": "warning",
                            "file": str(data["filepath"]),
                            "message": f"{app}.{migration_name} has no dependencies within same app",
                            "migration": f"{app}.{migration_name}",
                        })

    def _check_conflicting_migrations(self) -> None:
        """Check for migrations that might conflict (same dependencies)."""
        for app, migrations in self.migrations.items():
            # Group by dependencies
            by_deps: Dict[str, List[str]] = defaultdict(list)
            for migration_name, data in migrations.items():
                same_app_deps = sorted([d[1] for d in data["dependencies"] if d[0] == app])
                if same_app_deps:
                    key = ",".join(same_app_deps)
                    by_deps[key].append(migration_name)

            # Check for conflicts
            for deps, migs in by_deps.items():
                if len(migs) > 1:
                    self.issues.append({
                        "type": "conflicting_migrations",
                        "severity": "warning",
                        "message": f"Multiple migrations in '{app}' depend on same migration(s): {migs}",
                        "migrations": [f"{app}.{m}" for m in migs],
                    })

    def _check_dependency_order(self) -> None:
        """Check that migration numbers are in correct order."""
        for app, migrations in self.migrations.items():
            migration_nums = {}
            for migration_name in migrations:
                match = re.match(r"^(\d+)_", migration_name)
                if match:
                    num = int(match.group(1))
                    migration_nums[migration_name] = num

            # Check order consistency
            for migration_name, data in migrations.items():
                if migration_name not in migration_nums:
                    continue
                my_num = migration_nums[migration_name]

                for dep_app, dep_migration in data["dependencies"]:
                    if dep_app == app and dep_migration in migration_nums:
                        dep_num = migration_nums[dep_migration]
                        if dep_num >= my_num:
                            self.issues.append({
                                "type": "invalid_order",
                                "severity": "error",
                                "file": str(data["filepath"]),
                                "message": f"{app}.{migration_name} (#{my_num}) depends on later migration {dep_migration} (#{dep_num})",
                                "migration": f"{app}.{migration_name}",
                            })

    def report(self) -> int:
        """Print report and return exit code."""
        total_migrations = sum(len(m) for m in self.migrations.values())

        print("=" * 60)
        print("MIGRATION DEPENDENCY VERIFICATION REPORT")
        print("=" * 60)
        print(f"\nScanned: {len(self.migrations)} apps, {total_migrations} migrations")

        if not self.issues:
            print("\n[OK] No issues found. Migration dependency chain is valid.")
            return 0

        errors = [i for i in self.issues if i["severity"] == "error"]
        warnings = [i for i in self.issues if i["severity"] == "warning"]

        if errors:
            print(f"\n[ERRORS] ({len(errors)} found)")
            print("-" * 40)
            for issue in errors:
                print(f"  - {issue['type']}: {issue['message']}")
                if "file" in issue:
                    print(f"    File: {issue['file']}")

        if warnings:
            print(f"\n[WARNINGS] ({len(warnings)} found)")
            print("-" * 40)
            for issue in warnings:
                print(f"  - {issue['type']}: {issue['message']}")
                if "file" in issue:
                    print(f"    File: {issue['file']}")

        print("\n" + "=" * 60)

        # Return non-zero if there are errors
        return 1 if errors else 0

    def get_issues_json(self) -> List[dict]:
        """Return issues as JSON-serializable list."""
        return self.issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_migrations.py <backend_path>")
        print("Example: python verify_migrations.py /path/to/backend")
        sys.exit(1)

    backend_path = sys.argv[1]

    verifier = MigrationVerifier(backend_path)
    verifier.scan_migrations()
    verifier.verify_dependencies()
    exit_code = verifier.report()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
