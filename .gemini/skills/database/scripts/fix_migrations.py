#!/usr/bin/env python3
"""
Fix common Django migration issues.

Usage:
    python fix_migrations.py <backend_path> [--dry-run] [--app=<app_name>]

Features:
- Fix missing dependencies
- Renumber conflicting migrations
- Create merge migrations
- Update dependency references
"""
import os
import re
import sys
import ast
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional


class MigrationFixer:
    """Fix common migration issues."""

    def __init__(self, backend_path: str, dry_run: bool = True, target_app: Optional[str] = None):
        self.backend_path = Path(backend_path)
        self.apps_path = self.backend_path / "apps"
        self.dry_run = dry_run
        self.target_app = target_app
        self.migrations: Dict[str, Dict[str, dict]] = {}
        self.fixes_applied: List[str] = []

    def scan_migrations(self) -> None:
        """Scan all migration files."""
        if not self.apps_path.exists():
            print(f"Error: Apps directory not found at {self.apps_path}")
            sys.exit(1)

        for app_dir in self.apps_path.iterdir():
            if not app_dir.is_dir():
                continue
            if self.target_app and app_dir.name != self.target_app:
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
        """Parse a migration file."""
        try:
            with open(filepath, "r") as f:
                content = f.read()

            tree = ast.parse(content)
            dependencies = []

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name == "Migration":
                    for item in node.body:
                        if isinstance(item, ast.Assign):
                            for target in item.targets:
                                if isinstance(target, ast.Name) and target.id == "dependencies":
                                    dependencies = self._extract_dependencies(item.value)

            return {
                "filepath": filepath,
                "content": content,
                "dependencies": dependencies,
            }
        except Exception as e:
            print(f"Warning: Could not parse {filepath}: {e}")
            return None

    def _extract_dependencies(self, node) -> List[Tuple[str, str]]:
        """Extract dependencies from AST."""
        deps = []
        if isinstance(node, ast.List):
            for elt in node.elts:
                if isinstance(elt, ast.Tuple) and len(elt.elts) == 2:
                    app = self._get_string_value(elt.elts[0])
                    migration = self._get_string_value(elt.elts[1])
                    if app and migration:
                        deps.append((app, migration))
        return deps

    def _get_string_value(self, node) -> Optional[str]:
        """Extract string value from AST."""
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Str):
            return node.s
        return None

    def fix_conflicting_migrations(self) -> None:
        """Fix migrations that have the same number but different content."""
        for app, migrations in self.migrations.items():
            # Group by number
            by_number: Dict[int, List[str]] = {}
            for migration_name in migrations:
                match = re.match(r"^(\d+)_", migration_name)
                if match:
                    num = int(match.group(1))
                    if num not in by_number:
                        by_number[num] = []
                    by_number[num].append(migration_name)

            # Find conflicts
            for num, migs in by_number.items():
                if len(migs) > 1:
                    self._create_merge_migration(app, migs, num)

    def _create_merge_migration(self, app: str, migrations: List[str], base_num: int) -> None:
        """Create a merge migration for conflicting migrations."""
        migrations_dir = self.apps_path / app / "migrations"

        # Find next available number
        existing_nums = set()
        for m in self.migrations[app]:
            match = re.match(r"^(\d+)_", m)
            if match:
                existing_nums.add(int(match.group(1)))

        next_num = max(existing_nums) + 1 if existing_nums else 1

        # Create merge migration content
        merge_content = f'''# Generated merge migration
from django.db import migrations


class Migration(migrations.Migration):
    """Merge migration for conflicting migrations: {', '.join(migrations)}"""

    dependencies = [
        {', '.join([f"('{app}', '{m}')" for m in migrations])}
    ]

    operations = [
    ]
'''

        merge_filename = f"{next_num:04d}_merge_{datetime.now().strftime('%Y%m%d_%H%M')}.py"
        merge_path = migrations_dir / merge_filename

        if self.dry_run:
            self.fixes_applied.append(f"[DRY RUN] Would create merge migration: {merge_path}")
            print(f"[DRY RUN] Would create: {merge_path}")
        else:
            with open(merge_path, "w") as f:
                f.write(merge_content)
            self.fixes_applied.append(f"Created merge migration: {merge_path}")
            print(f"Created: {merge_path}")

    def fix_dependency_reference(self, app: str, migration_name: str,
                                  old_dep: Tuple[str, str], new_dep: Tuple[str, str]) -> None:
        """Update a dependency reference in a migration file."""
        if app not in self.migrations or migration_name not in self.migrations[app]:
            print(f"Migration not found: {app}.{migration_name}")
            return

        data = self.migrations[app][migration_name]
        filepath = data["filepath"]
        content = data["content"]

        # Create pattern to match the old dependency
        old_pattern = rf"\('{old_dep[0]}',\s*'{old_dep[1]}'\)"
        new_replacement = f"('{new_dep[0]}', '{new_dep[1]}')"

        if re.search(old_pattern, content):
            new_content = re.sub(old_pattern, new_replacement, content)

            if self.dry_run:
                self.fixes_applied.append(
                    f"[DRY RUN] Would update {filepath}: {old_dep} -> {new_dep}"
                )
                print(f"[DRY RUN] Would update {filepath}")
            else:
                # Backup original
                backup_path = filepath.with_suffix(".py.bak")
                shutil.copy(filepath, backup_path)

                with open(filepath, "w") as f:
                    f.write(new_content)

                self.fixes_applied.append(f"Updated {filepath}: {old_dep} -> {new_dep}")
                print(f"Updated: {filepath}")
        else:
            print(f"Dependency {old_dep} not found in {filepath}")

    def renumber_migrations(self, app: str, start_from: int = 1) -> None:
        """Renumber all migrations in an app sequentially."""
        if app not in self.migrations:
            print(f"App not found: {app}")
            return

        migrations_dir = self.apps_path / app / "migrations"

        # Get migrations sorted by current number
        numbered_migrations = []
        for migration_name, data in self.migrations[app].items():
            match = re.match(r"^(\d+)_(.+)$", migration_name)
            if match:
                num = int(match.group(1))
                suffix = match.group(2)
                numbered_migrations.append((num, suffix, migration_name, data))

        numbered_migrations.sort(key=lambda x: x[0])

        # Create renaming plan
        rename_map = {}  # old_name -> new_name
        for i, (old_num, suffix, old_name, data) in enumerate(numbered_migrations, start=start_from):
            new_name = f"{i:04d}_{suffix}"
            if old_name != new_name:
                rename_map[old_name] = new_name

        if not rename_map:
            print(f"No renumbering needed for {app}")
            return

        print(f"\nRenumbering plan for {app}:")
        for old, new in rename_map.items():
            print(f"  {old} -> {new}")

        if self.dry_run:
            self.fixes_applied.append(f"[DRY RUN] Would renumber {len(rename_map)} migrations in {app}")
            return

        # First pass: update all dependency references
        for migration_name, data in self.migrations[app].items():
            content = data["content"]
            new_content = content

            for old_name, new_name in rename_map.items():
                # Update dependency references
                old_pattern = rf"('{app}',\s*)'{old_name}'"
                new_replacement = rf"\1'{new_name}'"
                new_content = re.sub(old_pattern, new_replacement, new_content)

            if new_content != content:
                filepath = data["filepath"]
                with open(filepath, "w") as f:
                    f.write(new_content)
                print(f"Updated references in: {filepath}")

        # Second pass: rename files
        for old_name, new_name in rename_map.items():
            old_path = migrations_dir / f"{old_name}.py"
            new_path = migrations_dir / f"{new_name}.py"
            if old_path.exists():
                old_path.rename(new_path)
                print(f"Renamed: {old_name}.py -> {new_name}.py")

        self.fixes_applied.append(f"Renumbered {len(rename_map)} migrations in {app}")

    def add_missing_dependency(self, app: str, migration_name: str,
                                dep_app: str, dep_migration: str) -> None:
        """Add a missing dependency to a migration."""
        if app not in self.migrations or migration_name not in self.migrations[app]:
            print(f"Migration not found: {app}.{migration_name}")
            return

        data = self.migrations[app][migration_name]
        filepath = data["filepath"]
        content = data["content"]

        # Find dependencies list and add the new one
        deps_pattern = r"(dependencies\s*=\s*\[)"

        if re.search(deps_pattern, content):
            new_dep = f"\n        ('{dep_app}', '{dep_migration}'),"
            new_content = re.sub(deps_pattern, rf"\1{new_dep}", content)

            if self.dry_run:
                self.fixes_applied.append(
                    f"[DRY RUN] Would add dependency ({dep_app}, {dep_migration}) to {filepath}"
                )
                print(f"[DRY RUN] Would add dependency to {filepath}")
            else:
                backup_path = filepath.with_suffix(".py.bak")
                shutil.copy(filepath, backup_path)

                with open(filepath, "w") as f:
                    f.write(new_content)

                self.fixes_applied.append(
                    f"Added dependency ({dep_app}, {dep_migration}) to {filepath}"
                )
                print(f"Added dependency to: {filepath}")
        else:
            print(f"Could not find dependencies list in {filepath}")

    def generate_dependency_graph(self, output_file: Optional[str] = None) -> str:
        """Generate a DOT graph of migration dependencies."""
        lines = ["digraph migrations {", "  rankdir=LR;", "  node [shape=box];"]

        for app, migrations in self.migrations.items():
            # Subgraph for each app
            lines.append(f'  subgraph cluster_{app} {{')
            lines.append(f'    label="{app}";')

            for migration_name, data in migrations.items():
                node_id = f"{app}_{migration_name}".replace("-", "_")
                lines.append(f'    {node_id} [label="{migration_name}"];')

            lines.append("  }")

            # Add edges for dependencies
            for migration_name, data in migrations.items():
                node_id = f"{app}_{migration_name}".replace("-", "_")
                for dep_app, dep_migration in data["dependencies"]:
                    if dep_migration not in ["__first__", "__latest__"]:
                        dep_node_id = f"{dep_app}_{dep_migration}".replace("-", "_")
                        lines.append(f"  {dep_node_id} -> {node_id};")

        lines.append("}")
        graph = "\n".join(lines)

        if output_file:
            with open(output_file, "w") as f:
                f.write(graph)
            print(f"Dependency graph saved to: {output_file}")

        return graph

    def report(self) -> None:
        """Print summary of fixes applied."""
        print("\n" + "=" * 60)
        print("MIGRATION FIX REPORT")
        print("=" * 60)

        if not self.fixes_applied:
            print("\nNo fixes were applied.")
        else:
            print(f"\nFixes applied: {len(self.fixes_applied)}")
            for fix in self.fixes_applied:
                print(f"  - {fix}")

        if self.dry_run:
            print("\n[DRY RUN MODE] No actual changes were made.")
            print("Run without --dry-run to apply changes.")


def print_usage():
    print("""
Usage: python fix_migrations.py <backend_path> [options]

Options:
    --dry-run           Show what would be done without making changes
    --app=<name>        Only process specified app
    --renumber=<app>    Renumber all migrations in specified app
    --graph=<file>      Generate DOT dependency graph

Examples:
    python fix_migrations.py /path/to/backend --dry-run
    python fix_migrations.py /path/to/backend --app=accounts
    python fix_migrations.py /path/to/backend --renumber=accounts
    python fix_migrations.py /path/to/backend --graph=migrations.dot
""")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    backend_path = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    target_app = None
    renumber_app = None
    graph_file = None

    for arg in sys.argv[2:]:
        if arg.startswith("--app="):
            target_app = arg.split("=")[1]
        elif arg.startswith("--renumber="):
            renumber_app = arg.split("=")[1]
        elif arg.startswith("--graph="):
            graph_file = arg.split("=")[1]

    fixer = MigrationFixer(backend_path, dry_run=dry_run, target_app=target_app)
    fixer.scan_migrations()

    if renumber_app:
        fixer.renumber_migrations(renumber_app)
    elif graph_file:
        fixer.generate_dependency_graph(graph_file)
    else:
        fixer.fix_conflicting_migrations()

    fixer.report()


if __name__ == "__main__":
    main()
