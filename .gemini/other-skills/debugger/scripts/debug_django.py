#!/usr/bin/env python3
"""
Django Debugging Helper

Automated debugging assistant for Django applications.
Provides quick diagnostics for common Django issues.

Usage:
    python scripts/debug_django.py --check-permissions john@example.com
    python scripts/debug_django.py --check-query "MyModel.objects.filter(org=1)"
    python scripts/debug_django.py --check-migrations myapp
    python scripts/debug_django.py --check-org-scoping myapp.MyModel
    python scripts/debug_django.py --analyze-view myapp.views.my_view

Requires Django project to be in PYTHONPATH (run from src/ directory)
"""

import argparse
import os
import sys
import django
from pathlib import Path

# Setup Django environment
def setup_django():
    """Initialize Django settings."""
    # Add src directory to path
    src_path = Path(__file__).resolve().parent.parent.parent.parent / 'src'
    sys.path.insert(0, str(src_path))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'obc_management.settings.development')
    django.setup()


def check_user_permissions(email):
    """Check all permissions for a user."""
    from common.models import User

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        print(f"❌ User not found: {email}")
        return

    print(f"\n{'='*60}")
    print(f"USER PERMISSIONS: {user.username} ({email})")
    print(f"{'='*60}\n")

    print(f"Organization: {user.organization.name} (ID: {user.organization.id})")
    print(f"Role: {user.role.name if hasattr(user, 'role') and user.role else 'No role'}")
    print(f"Is Staff: {user.is_staff}")
    print(f"Is Superuser: {user.is_superuser}")
    print(f"Is Active: {user.is_active}")

    print(f"\n{'-'*60}")
    print("ALL PERMISSIONS:")
    print(f"{'-'*60}\n")

    permissions = user.get_all_permissions()
    if permissions:
        for perm in sorted(permissions):
            print(f"  ✅ {perm}")
    else:
        print("  ❌ No permissions assigned")

    # Group permissions
    print(f"\n{'-'*60}")
    print("GROUP PERMISSIONS:")
    print(f"{'-'*60}\n")

    if user.groups.exists():
        for group in user.groups.all():
            print(f"\n  Group: {group.name}")
            for perm in group.permissions.all():
                print(f"    ✅ {perm.content_type.app_label}.{perm.codename}")
    else:
        print("  No groups assigned")

    # Direct permissions
    print(f"\n{'-'*60}")
    print("DIRECT USER PERMISSIONS:")
    print(f"{'-'*60}\n")

    if user.user_permissions.exists():
        for perm in user.user_permissions.all():
            print(f"  ✅ {perm.content_type.app_label}.{perm.codename}")
    else:
        print("  No direct permissions")


def check_query(query_string):
    """Analyze a Django query for common issues."""
    print(f"\n{'='*60}")
    print(f"QUERY ANALYSIS")
    print(f"{'='*60}\n")

    print(f"Query: {query_string}\n")

    # Execute query in safe context
    try:
        # This is a simplified example - real implementation would parse safely
        print("⚠️  Note: For security, manually test queries in Django shell")
        print("Example:")
        print(f"  python manage.py shell")
        print(f"  >>> from myapp.models import MyModel")
        print(f"  >>> queryset = {query_string}")
        print(f"  >>> print(queryset.query)  # View SQL")
        print(f"  >>> print(queryset.count())  # Count results")
        print(f"  >>> print(list(queryset[:5]))  # View first 5")

    except Exception as e:
        print(f"❌ Error: {e}")


def check_migrations(app_name):
    """Check migration status for an app."""
    from django.db.migrations.recorder import MigrationRecorder
    from django.core.management import call_command
    from io import StringIO

    print(f"\n{'='*60}")
    print(f"MIGRATION STATUS: {app_name}")
    print(f"{'='*60}\n")

    # Show migrations
    out = StringIO()
    try:
        call_command('showmigrations', app_name, stdout=out)
        print(out.getvalue())
    except Exception as e:
        print(f"❌ Error checking migrations: {e}")
        return

    # Show unapplied migrations
    print(f"\n{'-'*60}")
    print("UNAPPLIED MIGRATIONS:")
    print(f"{'-'*60}\n")

    out = StringIO()
    try:
        call_command('showmigrations', app_name, plan=True, stdout=out)
        output = out.getvalue()

        unapplied = [line for line in output.split('\n') if '[ ]' in line]
        if unapplied:
            for migration in unapplied:
                print(f"  ⚠️  {migration}")
            print(f"\n  Run: python manage.py migrate {app_name}")
        else:
            print("  ✅ All migrations applied")

    except Exception as e:
        print(f"❌ Error: {e}")


def check_org_scoping(model_path):
    """Check if a model has proper organization scoping."""
    print(f"\n{'='*60}")
    print(f"ORGANIZATION SCOPING CHECK: {model_path}")
    print(f"{'='*60}\n")

    # Parse model path
    try:
        app_label, model_name = model_path.split('.')
    except ValueError:
        print("❌ Invalid model path. Use format: app.ModelName")
        return

    # Import model
    try:
        from django.apps import apps
        model = apps.get_model(app_label, model_name)
    except LookupError:
        print(f"❌ Model not found: {model_path}")
        return

    print(f"Model: {model.__name__}")
    print(f"App: {app_label}")
    print(f"Table: {model._meta.db_table}\n")

    # Check for organization field
    print(f"{'-'*60}")
    print("MULTI-TENANCY CHECKS:")
    print(f"{'-'*60}\n")

    has_org_field = False
    for field in model._meta.get_fields():
        if field.name == 'organization':
            has_org_field = True
            print(f"  ✅ Has 'organization' field")
            print(f"      Type: {field.get_internal_type()}")
            print(f"      Related: {field.related_model.__name__ if hasattr(field, 'related_model') else 'N/A'}")
            break

    if not has_org_field:
        print(f"  ❌ Missing 'organization' field")
        print(f"      This model may not be organization-scoped!")

    # Check for OrganizationScopedMixin
    print(f"\n{'-'*60}")
    print("MIXIN CHECKS:")
    print(f"{'-'*60}\n")

    bases = [base.__name__ for base in model.__bases__]
    print(f"  Inherits from: {', '.join(bases)}")

    if 'OrganizationScopedMixin' in bases:
        print(f"  ✅ Uses OrganizationScopedMixin")
    else:
        print(f"  ⚠️  Doesn't use OrganizationScopedMixin")

    if 'AuditMixin' in bases:
        print(f"  ✅ Uses AuditMixin (created_by, updated_by)")
    else:
        print(f"  ⚠️  Doesn't use AuditMixin")

    if 'SoftDeleteMixin' in bases:
        print(f"  ✅ Uses SoftDeleteMixin (is_active)")
    else:
        print(f"  ⚠️  Doesn't use SoftDeleteMixin")

    # Check sample queries
    print(f"\n{'-'*60}")
    print("SAMPLE DATA CHECK:")
    print(f"{'-'*60}\n")

    try:
        total_count = model.objects.count()
        print(f"  Total records: {total_count}")

        if has_org_field:
            from django.db.models import Count
            org_distribution = model.objects.values('organization').annotate(count=Count('id'))
            print(f"\n  Distribution by organization:")
            for item in org_distribution[:5]:
                print(f"    Org {item['organization']}: {item['count']} records")

    except Exception as e:
        print(f"  ⚠️  Cannot query: {e}")


def analyze_view(view_path):
    """Analyze a Django view for common issues."""
    print(f"\n{'='*60}")
    print(f"VIEW ANALYSIS: {view_path}")
    print(f"{'='*60}\n")

    # Parse view path
    try:
        module_path, view_name = view_path.rsplit('.', 1)
    except ValueError:
        print("❌ Invalid view path. Use format: myapp.views.my_view")
        return

    # Import view
    try:
        import importlib
        module = importlib.import_module(module_path)
        view_func = getattr(module, view_name)
    except (ImportError, AttributeError) as e:
        print(f"❌ View not found: {e}")
        return

    print(f"View: {view_name}")
    print(f"Module: {module_path}\n")

    # Check decorators
    print(f"{'-'*60}")
    print("DECORATOR CHECKS:")
    print(f"{'-'*60}\n")

    # Get source code
    import inspect
    source = inspect.getsource(view_func)

    decorators = []
    for line in source.split('\n'):
        line = line.strip()
        if line.startswith('@'):
            decorators.append(line)

    if decorators:
        for decorator in decorators:
            print(f"  {decorator}")
    else:
        print("  ⚠️  No decorators found")

    # Check for common security decorators
    print(f"\n{'-'*60}")
    print("SECURITY CHECKS:")
    print(f"{'-'*60}\n")

    if '@login_required' in source or 'login_required' in str(decorators):
        print("  ✅ Has @login_required")
    else:
        print("  ⚠️  Missing @login_required (if authentication needed)")

    if '@require_permission' in source:
        print("  ✅ Has @require_permission")
    else:
        print("  ⚠️  No permission check found")

    if '@csrf_exempt' in source:
        print("  ⚠️  Has @csrf_exempt (security risk!)")

    # Check organization scoping
    print(f"\n{'-'*60}")
    print("ORGANIZATION SCOPING:")
    print(f"{'-'*60}\n")

    if 'request.user.organization' in source:
        print("  ✅ Filters by request.user.organization")
    else:
        print("  ⚠️  May not filter by organization (multi-tenancy risk)")

    if '.filter(organization=' in source or '.filter(organization__' in source:
        print("  ✅ Uses organization filter in queryset")
    else:
        print("  ⚠️  No explicit organization filter found")

    # Check soft delete
    print(f"\n{'-'*60}")
    print("SOFT DELETE:")
    print(f"{'-'*60}\n")

    if 'is_active=True' in source or 'is_active__' in source:
        print("  ✅ Filters by is_active")
    else:
        print("  ⚠️  May include soft-deleted records")

    print(f"\n{'-'*60}")
    print("VIEW SOURCE (first 30 lines):")
    print(f"{'-'*60}\n")

    for i, line in enumerate(source.split('\n')[:30], 1):
        print(f"  {i:3}: {line}")


def main():
    parser = argparse.ArgumentParser(
        description='Django Debugging Helper',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/debug_django.py --check-permissions john@example.com
  python scripts/debug_django.py --check-migrations myapp
  python scripts/debug_django.py --check-org-scoping myapp.MyModel
  python scripts/debug_django.py --analyze-view myapp.views.my_view
        """
    )

    parser.add_argument('--check-permissions', metavar='EMAIL', help='Check permissions for user by email')
    parser.add_argument('--check-query', metavar='QUERY', help='Analyze Django query')
    parser.add_argument('--check-migrations', metavar='APP', help='Check migration status for app')
    parser.add_argument('--check-org-scoping', metavar='MODEL', help='Check organization scoping for model (app.Model)')
    parser.add_argument('--analyze-view', metavar='VIEW', help='Analyze view for common issues (app.views.view_name)')

    args = parser.parse_args()

    # Setup Django
    print("Setting up Django environment...")
    try:
        setup_django()
        print("✅ Django initialized\n")
    except Exception as e:
        print(f"❌ Failed to initialize Django: {e}")
        print("Make sure to run this script from the src/ directory")
        sys.exit(1)

    # Run requested checks
    if args.check_permissions:
        check_user_permissions(args.check_permissions)
    elif args.check_query:
        check_query(args.check_query)
    elif args.check_migrations:
        check_migrations(args.check_migrations)
    elif args.check_org_scoping:
        check_org_scoping(args.check_org_scoping)
    elif args.analyze_view:
        analyze_view(args.analyze_view)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
