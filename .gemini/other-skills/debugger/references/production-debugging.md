# Production Debugging Guide

Fast-track debugging procedures for critical production issues in Railway-deployed Django applications.

## Emergency Response Protocol

### Phase 1: Immediate Triage (0-5 minutes)

**Goal:** Determine severity and impact

**Actions:**

1. **Check Service Status**
```bash
railway status
railway logs --tail 50
```

2. **Assess Impact**
```
Questions to answer:
- Is the entire site down or just one feature?
- How many users are affected?
- Is data at risk of corruption?
- Is this a security incident?
```

3. **Severity Classification**

**CRITICAL (P0):**
- Site completely down
- Data corruption occurring
- Security breach detected
- Payment processing broken

**Action:** Immediate rollback + all hands on deck

**HIGH (P1):**
- Major feature broken (affects >50% users)
- No workaround available
- Revenue impact

**Action:** Hotfix within 2 hours

**MEDIUM (P2):**
- Feature partially broken
- Workaround exists
- Affects specific user group

**Action:** Fix within 24 hours

**LOW (P3):**
- Minor UI issue
- Edge case bug
- Cosmetic problem

**Action:** Include in next release

### Phase 2: Emergency Rollback (if P0/P1)

**When to rollback immediately:**
- Site is completely down
- Data corruption in progress
- Security vulnerability being exploited

**Railway Rollback Procedure:**

```bash
# Option 1: Railway CLI rollback to previous deployment
railway rollback

# Option 2: Railway Dashboard
# 1. Go to Deployments tab
# 2. Find last working deployment
# 3. Click "..." → Redeploy

# Option 3: Git revert
git log --oneline -10  # Find last working commit
git revert HEAD  # Revert last commit
git push origin main  # Triggers new deployment

# Verify rollback successful
railway logs --tail 50
# Check that errors have stopped
```

**Post-Rollback:**
- Announce rollback to team/users
- Mark investigation as "ongoing"
- Proceed to Phase 3 for root cause analysis

### Phase 3: Log Analysis (5-15 minutes)

**Capture Production Logs:**

```bash
# Save last 500 lines
railway logs --tail 500 > production-$(date +%Y%m%d-%H%M%S).log

# Save last hour (if Railway supports time filtering)
railway logs --since 1h > production-1h.log

# Monitor in real-time
railway logs --tail
```

**Critical Log Patterns:**

```bash
# Find errors
grep -i "error\|exception\|traceback" production.log

# Find specific error type
grep "PermissionDenied\|DoesNotExist\|IntegrityError" production.log

# Find affected URLs
grep "GET\|POST" production.log | grep "500\|403\|404"

# Find affected users (if user ID logged)
grep "user_id" production.log

# Count error frequency
grep -i "error" production.log | wc -l
```

**Error Pattern Examples:**

```
# Permission errors
PermissionDenied at /budget/requests/123/approve/
→ Permission issue, check RBAC

# Database errors
django.db.utils.IntegrityError: duplicate key value
→ Unique constraint violation, check migration

# HTMX errors
AttributeError: 'NoneType' object has no attribute 'organization'
→ Missing organization scoping, check queryset filter
```

### Phase 4: Reproduce in Staging (if possible)

**Why staging reproduction is critical:**
- Safe environment for testing fixes
- Can use real production data (anonymized)
- Validates fix before production deployment

**Staging Reproduction Steps:**

```bash
# Switch to staging environment
railway --environment staging

# Deploy current main to staging
git push origin staging

# Monitor staging logs
railway logs --environment staging --tail

# Test the failing scenario in staging
# If bug reproduces → investigate in staging
# If bug doesn't reproduce → production-specific issue
```

**If bug is production-only:**
```
Possible causes:
- Environment variable differences
- Production data specific (large dataset, edge cases)
- DEBUG=False behavior
- PostgreSQL vs. SQLite differences
- Concurrent request handling
```

### Phase 5: Quick Diagnosis (15-30 minutes)

**Use structured diagnosis checklist:**

**Recent Changes Check:**
```bash
# What was deployed recently?
git log --oneline -10
git diff HEAD~5..HEAD  # Changes in last 5 commits

# When did the error start?
# Compare deployment timestamp to first error in logs
railway deployments  # List recent deployments
```

**Database State Check:**

```python
# Connect to production Django shell (if Railway allows)
railway run python manage.py shell

# Quick checks
from django.contrib.auth.models import User
from myapp.models import MyModel

# Count records
MyModel.objects.count()

# Check recent records
MyModel.objects.order_by('-created_at')[:5]

# Check for NULL values
MyModel.objects.filter(field__isnull=True).count()

# Check migrations applied
from django.db.migrations.recorder import MigrationRecorder
MigrationRecorder.Migration.objects.filter(app='myapp').order_by('-id')[:5]
```

**Environment Variable Check:**

```bash
# List production environment variables
railway variables --environment production

# Check critical variables
railway variables | grep -E "DATABASE_URL|SECRET_KEY|DEBUG|ALLOWED_HOSTS"

# Compare with staging
railway variables --environment staging > staging-vars.txt
railway variables --environment production > production-vars.txt
diff staging-vars.txt production-vars.txt
```

**Quick HTTP Tests:**

```bash
# Test endpoint directly
curl -I https://your-app.railway.app/health/
# Should return 200 OK

# Test failing endpoint
curl -I https://your-app.railway.app/budget/requests/123/approve/
# Note status code and headers

# Test with authentication
curl -X POST https://your-app.railway.app/api/endpoint/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

## Production-Specific Debugging Techniques

### 1. Structured Logging Analysis

**Log aggregation patterns:**

```bash
# Error frequency by type
grep "Error:" production.log | cut -d: -f2 | sort | uniq -c | sort -rn

# Top failing URLs
grep "500" production.log | awk '{print $7}' | sort | uniq -c | sort -rn

# Errors by time period
grep "Error" production.log | awk '{print $1, $2}' | cut -d: -f1 | uniq -c

# User IDs encountering errors (if logged)
grep "Error" production.log | grep -oP 'user_id=\K\d+' | sort | uniq -c
```

### 2. Performance Profiling

**Django query logging (temporary):**

```python
# settings/production.py - TEMPORARY FOR DEBUGGING
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',  # ONLY ENABLE TEMPORARILY
        },
    },
}
```

**After adding logging:**
```bash
# Deploy to production
git commit -am "temp: enable query logging"
git push origin main

# Monitor query logs
railway logs --tail | grep "SELECT\|INSERT\|UPDATE"

# Look for:
# - Duplicate queries (N+1 problem)
# - Slow queries (> 100ms)
# - Missing indexes

# IMPORTANT: Remove query logging after investigation
git revert HEAD
git push origin main
```

### 3. Database Connection Debugging

**Check connection pool:**

```python
# Django shell on production
railway run python manage.py shell

from django.db import connection
print(f"Database: {connection.settings_dict['NAME']}")
print(f"Host: {connection.settings_dict['HOST']}")

# Test query
from django.db import connections
for conn_name in connections:
    conn = connections[conn_name]
    try:
        conn.cursor()
        print(f"{conn_name}: Connected")
    except Exception as e:
        print(f"{conn_name}: Failed - {e}")
```

### 4. Memory/Resource Issues

**Railway metrics:**
```bash
# Check memory usage (if Railway provides)
railway metrics

# Signs of memory issues in logs:
grep -i "memory\|oom\|killed" production.log

# Database connection pool exhaustion:
grep -i "too many connections\|connection pool" production.log
```

## Hotfix Deployment Process

### 1. Create Hotfix Branch

```bash
# From main branch
git checkout main
git pull origin main

# Create hotfix branch
git checkout -b hotfix/budget-approval-403
```

### 2. Minimal Fix Implementation

**Principles:**
- Fix ONLY the critical bug
- No refactoring
- No new features
- Minimal code changes

**Example Hotfix:**
```python
# ❌ DON'T: Large refactor
# Refactor entire view with new architecture

# ✅ DO: Minimal fix
# myapp/views.py
@login_required
@require_permission('myapp.approve_budgetrequest')  # Add missing decorator
def budget_approval_approve(request, pk):
    # Existing code unchanged
    pass
```

### 3. Test Hotfix Locally

```bash
# Run tests
cd src && pytest myapp/tests/ -v

# Manual test
python manage.py runserver
# Manually verify fix works
```

### 4. Deploy to Staging First

```bash
# Push to staging
git push origin hotfix/budget-approval-403:staging

# Monitor staging
railway logs --environment staging --tail

# Manual test in staging
# Verify fix works with production-like data
```

### 5. Deploy to Production

```bash
# Merge to main
git checkout main
git merge hotfix/budget-approval-403

# Push to production
git push origin main

# Monitor deployment
railway logs --tail 100

# Immediate verification
# Test the fixed scenario in production
```

### 6. Post-Deploy Monitoring

```bash
# Monitor for 15-30 minutes after deploy
railway logs --tail | grep -i "error"

# Check error rate decreased
# Compare:
# - Before deploy: X errors/minute
# - After deploy: 0 errors/minute

# Verify fix in production
# Test the scenario that was failing
```

## Production Data Debugging

### Safe Production Data Access

**Principles:**
- Never modify production data directly
- Use read-only queries
- Export samples for local testing
- Anonymize sensitive data

**Export specific records:**
```bash
# Export failing record for local testing
railway run python manage.py dumpdata myapp.BudgetRequest --pks 123 \
  --indent 2 > failing_request.json

# Load locally
python manage.py loaddata failing_request.json

# Debug locally with real data structure
```

**Anonymize sensitive data:**
```python
# Django shell on local with production data
python manage.py shell

from myapp.models import BudgetRequest

# Anonymize
request = BudgetRequest.objects.get(id=123)
request.created_by.email = "test@example.com"
request.created_by.username = "testuser"
request.created_by.save()
```

## Monitoring and Alerting

### Post-Incident Monitoring

```bash
# Set up monitoring for similar errors
# Create script to check logs periodically

#!/bin/bash
# monitor_errors.sh

while true; do
    ERROR_COUNT=$(railway logs --tail 100 | grep -c "PermissionDenied")

    if [ $ERROR_COUNT -gt 5 ]; then
        echo "ALERT: $ERROR_COUNT permission errors in last 100 logs"
        # Send alert (email, Slack, etc.)
    fi

    sleep 300  # Check every 5 minutes
done
```

## Common Production-Only Issues

### Issue 1: DEBUG=False Errors

**Symptom:** Works locally (DEBUG=True) but fails in production (DEBUG=False)

**Cause:** Django behavior changes when DEBUG=False

**Investigation:**
```python
# Local test with DEBUG=False
# settings/development.py
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

python manage.py runserver --insecure  # Serve static files

# Test locally - should reproduce production error
```

**Common DEBUG=False issues:**
- Static files not served (need collectstatic)
- Error pages not customized (500.html, 404.html)
- ALLOWED_HOSTS misconfigured

### Issue 2: PostgreSQL vs SQLite Differences

**Symptom:** Works with SQLite locally, fails with PostgreSQL in production

**Common differences:**
```python
# Case sensitivity
# SQLite: case-insensitive
# PostgreSQL: case-sensitive

# ❌ Works in SQLite, fails in PostgreSQL
MyModel.objects.filter(name__contains='Test')

# ✅ Works in both
MyModel.objects.filter(name__icontains='Test')
```

**Investigation:**
```bash
# Test locally with PostgreSQL
# Update .env
DATABASE_URL=postgresql://user:pass@localhost/testdb

python manage.py migrate
python manage.py runserver
# Should reproduce production error
```

### Issue 3: Concurrent Request Issues

**Symptom:** Intermittent errors under load

**Investigation:**
```python
# Test with concurrent requests
from concurrent.futures import ThreadPoolExecutor
from django.test import Client

client = Client()

def make_request():
    return client.post('/api/endpoint/', data)

# Simulate 10 concurrent requests
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(make_request) for _ in range(10)]
    results = [f.result() for f in futures]

# Check for race conditions, transaction issues
```

## Documentation Template

```markdown
# Production Incident Report: [Incident Title]

## Incident Summary
- **Date:** [YYYY-MM-DD HH:MM UTC]
- **Severity:** P0 / P1 / P2 / P3
- **Duration:** [time from start to resolution]
- **Affected users:** [number / percentage]

## Timeline
- **[Time]:** Incident detected
- **[Time]:** Team notified
- **[Time]:** Investigation started
- **[Time]:** Root cause identified
- **[Time]:** Fix deployed to staging
- **[Time]:** Fix deployed to production
- **[Time]:** Incident resolved

## Impact
- Users affected: [number]
- Requests failed: [number]
- Data corrupted: YES / NO
- Revenue impact: $[amount] (if applicable)

## Root Cause
[Detailed explanation of what caused the incident]

## Resolution
[What was changed to fix the incident]

## Preventive Measures
1. [How to prevent similar incidents]
2. [Process improvements]
3. [Monitoring/alerts to add]

## Action Items
- [ ] [Action 1 - owner]
- [ ] [Action 2 - owner]

## Lessons Learned
[What did we learn from this incident]
```

## Emergency Contacts & Resources

**Railway Documentation:**
- Deployments: https://docs.railway.app/guides/deployments
- Logs: https://docs.railway.app/guides/logs
- Rollback: https://docs.railway.app/guides/deployments#rollback

**Django Production Debugging:**
- Django deployment checklist: `python manage.py check --deploy`
- Django logging: https://docs.djangoproject.com/en/5.2/topics/logging/

**OBCMS-Specific:**
- Error documentation: `/docs/error-logs/README.md`
- Deployment guide: `/docs/deployment/railway-deployment.md`
- Emergency runbook: `/docs/deployment/emergency-runbook.md` (if exists)
