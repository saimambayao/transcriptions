# Debugging Quick Reference Card

One-page reference for common debugging commands and patterns.

## Django Commands

```bash
# Django shell
python manage.py shell

# Check deployment readiness
python manage.py check --deploy

# Show migrations
python manage.py showmigrations
python manage.py showmigrations myapp

# Database shell
python manage.py dbshell

# Run tests
pytest
pytest myapp/tests/
pytest --cov

# Collect static files
python manage.py collectstatic
```

## Django Shell Quick Commands

```python
# Import models
from myapp.models import MyModel
from common.models import User, Organization

# Count records
MyModel.objects.count()

# Get specific record
obj = MyModel.objects.get(id=123)

# Filter records
MyModel.objects.filter(organization_id=1)

# View SQL query
queryset = MyModel.objects.filter(status='active')
print(queryset.query)

# Check user permissions
user = User.objects.get(username='testuser')
user.get_all_permissions()
user.has_perm('myapp.view_mymodel')

# Validate model instance
obj.full_clean()  # Raises ValidationError if invalid

# Debug queryset
for obj in MyModel.objects.all()[:5]:
    print(obj.__dict__)
```

## Python Debugger (pdb)

```python
# Add breakpoint in code
import pdb; pdb.set_trace()

# pdb commands
n          # Next line
s          # Step into function
c          # Continue execution
l          # List code context
p variable # Print variable value
pp obj     # Pretty-print object
h          # Help
q          # Quit debugger
```

## Browser DevTools

```javascript
// Console commands

// Enable HTMX logging
htmx.logAll();

// Monitor events
monitorEvents(document.body, 'htmx:afterSwap');

// Stop monitoring
unmonitorEvents(document.body);

// Find element
document.querySelector('#element-id');

// Check element existence
document.getElementById('my-element') === null

// View all HTMX elements
document.querySelectorAll('[hx-get], [hx-post]');
```

## Railway Commands

```bash
# View logs
railway logs --tail 100
railway logs --tail 200 > debug.log

# Check status
railway status

# List deployments
railway deployments

# Rollback
railway rollback

# Environment variables
railway variables
railway variables --environment production

# Connect to database
railway connect postgresql

# Run command in production
railway run python manage.py shell
```

## Git Commands for Debugging

```bash
# View recent commits
git log --oneline -10

# What changed in last commit
git diff HEAD~1..HEAD

# Find when bug was introduced
git bisect start
git bisect bad           # Current commit is bad
git bisect good abc123   # This commit was good
# Git will checkout middle commit - test it
git bisect good  # or bad
# Repeat until bug-introducing commit found

# View file history
git log --follow -p -- path/to/file.py

# Who changed this line?
git blame path/to/file.py
```

## Log Analysis

```bash
# Find errors in log
grep -i "error" production.log

# Count errors
grep -i "error" production.log | wc -l

# Find specific error type
grep "PermissionDenied\|DoesNotExist" production.log

# Errors in time range
awk '/14:00/,/15:00/' production.log | grep -i error

# Top errors
grep ERROR production.log | cut -d: -f3 | sort | uniq -c | sort -rn

# View last 50 errors
grep -i error production.log | tail -50
```

## Database Debugging

```sql
-- View table structure
\d myapp_mymodel

-- Count records
SELECT COUNT(*) FROM myapp_mymodel;

-- Check for NULL values
SELECT COUNT(*) FROM myapp_mymodel WHERE field IS NULL;

-- Find orphaned records
SELECT * FROM myapp_budgetrequest br
LEFT JOIN myapp_workitem wi ON br.work_item_id = wi.id
WHERE wi.id IS NULL;

-- Check indexes
SELECT * FROM pg_indexes WHERE tablename = 'myapp_mymodel';

-- Slow queries
SELECT * FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;
```

## HTMX Debugging Patterns

```html
<!-- Add to template for debugging -->
<script nonce="{{ request.csp_nonce }}">
// Log all HTMX events
htmx.logAll();

// Custom event logging
document.body.addEventListener('htmx:afterSwap', function(event) {
    console.log('Swapped:', event.detail.target.id);
});

document.body.addEventListener('htmx:responseError', function(event) {
    console.error('HTMX Error:', event.detail);
});
</script>

<!-- Verify element existence -->
<div id="target-element">
    <!-- This is what hx-target should point to -->
</div>

<!-- Debug HTMX attributes -->
<button
    hx-get="/api/endpoint/"
    hx-target="#target-element"
    hx-swap="innerHTML"
    hx-indicator="#loading"
    onclick="console.log('Button clicked')"
>
    Test
</button>
```

## Common Django Queries

```python
# Organization-scoped query
MyModel.objects.filter(
    organization=request.user.organization,
    is_active=True
)

# Avoid N+1 queries
MyModel.objects.select_related('foreign_key_field')
MyModel.objects.prefetch_related('many_to_many_field')

# Get or create
obj, created = MyModel.objects.get_or_create(
    name='test',
    defaults={'description': 'Test object'}
)

# Update multiple records
MyModel.objects.filter(status='pending').update(status='active')

# Bulk create
MyModel.objects.bulk_create([
    MyModel(name='obj1'),
    MyModel(name='obj2'),
])

# Check existence
if MyModel.objects.filter(name='test').exists():
    # ...

# Aggregation
from django.db.models import Count, Sum
MyModel.objects.aggregate(
    total=Count('id'),
    sum_amount=Sum('amount')
)
```

## Environment Variable Debugging

```bash
# Check if variable is set
echo $DATABASE_URL

# List all env vars
env

# Compare environments
railway variables --environment staging > staging.txt
railway variables --environment production > production.txt
diff staging.txt production.txt

# Test with different env
export DEBUG=False
python manage.py runserver
```

## Permission Debugging

```python
# Django shell
from django.contrib.auth.models import Permission, User

# List all permissions for app
Permission.objects.filter(content_type__app_label='myapp')

# Check user's permissions
user = User.objects.get(username='testuser')
list(user.get_all_permissions())

# Add permission to user
permission = Permission.objects.get(codename='view_mymodel')
user.user_permissions.add(permission)

# Check if user has permission
user.has_perm('myapp.view_mymodel')

# Get users with permission
Permission.objects.get(codename='view_mymodel').user_set.all()
```

## Multi-Tenancy Debugging

```python
# Verify organization scoping
queryset = MyModel.objects.all()
print(list(queryset.values_list('organization_id', flat=True).distinct()))

# Check for data leakage
org1_data = MyModel.objects.filter(organization_id=1)
org2_data = MyModel.objects.filter(organization_id=2)

# Should be no overlap
assert not org1_data.filter(id__in=org2_data.values_list('id', flat=True)).exists()

# Test as different user
from django.test import Client
client = Client()
client.force_login(user1)
response = client.get('/api/data/')
# Verify response only contains user1's org data
```

## Performance Debugging

```python
# Enable query logging temporarily
import logging
logging.getLogger('django.db.backends').setLevel(logging.DEBUG)

# Count queries
from django.db import connection
len(connection.queries)

# View queries
from django.db import connection
for query in connection.queries:
    print(query['sql'])

# Profile view
import cProfile
cProfile.run('my_view(request)')

# Time query
import time
start = time.time()
result = MyModel.objects.filter(status='active').count()
print(f"Query took {time.time() - start:.3f}s")
```

## Error Pattern Recognition

| Error Type | Common Cause | Quick Fix |
|------------|--------------|-----------|
| 403 Forbidden | Missing permission | Check `user.has_perm()` |
| 404 Not Found | Wrong URL or DoesNotExist | Verify URL pattern, object exists |
| 500 Server Error | Unhandled exception | Check Django logs, stack trace |
| IntegrityError | Constraint violation | Check unique/foreign key constraints |
| DoesNotExist | Object not in database | Use get_object_or_404 or try/except |
| MultipleObjectsReturned | Query not unique | Add more filters or use .first() |
| CSRF verification failed | Missing CSRF token | Add {% csrf_token %} to form |
| HTMX swap not working | Target element missing | Verify element ID exists |

## Emergency Commands

```bash
# PRODUCTION EMERGENCY

# 1. Check if service is running
railway status

# 2. View recent errors
railway logs --tail 100 | grep -i error

# 3. Rollback if needed
railway rollback

# 4. Check database connectivity
railway run python manage.py check

# 5. Monitor in real-time
railway logs --tail
```

## Cheat Sheet URLs

- Django Docs: https://docs.djangoproject.com/
- HTMX Docs: https://htmx.org/docs/
- Railway Docs: https://docs.railway.app/
- PostgreSQL Docs: https://www.postgresql.org/docs/
