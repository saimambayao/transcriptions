# Reproduction Techniques

Comprehensive guide to reproducing bugs consistently - the critical first step in debugging.

## Why Reproduction is Critical

**"If you can't reproduce it, you can't fix it."**

Consistent reproduction:
- Confirms the bug exists and isn't a one-time glitch
- Identifies the exact conditions that trigger the issue
- Allows verification that your fix actually works
- Prevents wasting time on unreproducible "ghost" bugs

## Basic Reproduction Process

### 1. Document Initial Report

**Gather from user/error report:**
```
Who: User ID, role, organization
What: What they were trying to do
When: Timestamp, date
Where: URL, page, feature
How: Steps they took
Result: What happened (error message, unexpected behavior)
Expected: What should have happened
```

**Example:**
```
Who: john@example.com (Admin, Org #42)
What: Approve budget request
When: 2025-10-31 14:30 UTC
Where: /budget/requests/123/
How: Clicked "Approve" button
Result: 403 Forbidden error
Expected: Request should be approved, status changes to "Approved"
```

### 2. Recreate Exact Conditions

**Environment matching:**
- Same user role and permissions
- Same organization (multi-tenancy)
- Same data state (empty DB vs. populated)
- Same browser and version (for frontend issues)
- Same deployment environment (local/staging/production)

**Data state matching:**
```python
# Django shell - recreate data conditions
python manage.py shell

from common.models import Organization, User
from myapp.models import BudgetRequest

# Find the exact object
request = BudgetRequest.objects.get(id=123)

# Check state
print(f"Status: {request.status}")
print(f"Created by: {request.created_by}")
print(f"Organization: {request.organization}")
```

### 3. Test Reproducibility

**Verify bug occurs consistently:**
```
Attempt 1: ✅ Bug reproduced
Attempt 2: ✅ Bug reproduced
Attempt 3: ✅ Bug reproduced

Result: Consistently reproducible
```

**If not consistent:**
- Note conditions when it does/doesn't occur
- Look for timing-dependent issues
- Check for race conditions or caching

## Advanced Reproduction Techniques

### Minimal Reproduction Case

Reduce to the simplest possible steps that trigger the bug.

**Before (complex):**
```
1. Login as admin
2. Navigate to dashboard
3. Click "Work Items"
4. Filter by status "Active"
5. Click on work item #456
6. Click "Budget" tab
7. Click "New Request"
8. Fill form with $50,000
9. Submit request
10. Click "Approve" → Error
```

**After (minimal):**
```
1. Login as admin
2. Navigate to /budget/requests/123/
3. Click "Approve" → Error

(Steps 1-9 were not necessary to reproduce)
```

### Environment-Specific Issues

**Local vs. Production:**

```bash
# Check if environment-specific
# Test in local:
python manage.py runserver
# Navigate to feature → Works fine

# Test in staging:
# Navigate to staging URL → Bug reproduces

# Conclusion: Production-only bug (environment-specific)
```

**Common environment differences:**
- DEBUG=True vs. DEBUG=False
- SQLite vs. PostgreSQL
- Different SECRET_KEY
- Different ALLOWED_HOSTS
- Missing environment variables

### Timing-Dependent Bugs

**Symptoms:**
- Bug occurs sometimes but not always
- Related to concurrent requests
- Cache-related issues

**Reproduction strategy:**
```python
# Test with different delays
import time

# Attempt 1: Immediate
response = client.post(url, data)

# Attempt 2: After 1 second
time.sleep(1)
response = client.post(url, data)

# Attempt 3: Concurrent requests
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(client.post, url, data) for _ in range(5)]
    results = [f.result() for f in futures]
```

### Data-Dependent Bugs

**Symptoms:**
- Bug occurs with specific data values
- Works with test data, fails with production data

**Reproduction:**
```python
# Django shell - test with specific data
from myapp.models import BudgetRequest

# Works with small amount
request = BudgetRequest.objects.create(amount=1000)
request.approve(user)  # Success

# Fails with large amount
request2 = BudgetRequest.objects.create(amount=999999999)
request2.approve(user)  # Error: Amount exceeds budget

# Or fails with specific characters
community = Community.objects.create(name="Test's Community")  # SQL error

# Or fails with NULL values
item = WorkItem.objects.create(title=None)  # Constraint error
```

## Browser-Specific Reproduction (Frontend)

### Using Browser DevTools

**Chrome DevTools (F12):**

1. **Console Tab**
   - Clear console (`Ctrl+L`)
   - Perform action
   - Note any JavaScript errors
   - Check HTMX events (if `htmx.logAll()` enabled)

2. **Network Tab**
   - Enable "Preserve log"
   - Perform action
   - Check failed requests (red status codes)
   - Inspect request/response headers and payload

3. **Elements Tab**
   - Inspect DOM state before action
   - Perform action
   - Check if DOM updated correctly

**Example reproduction:**
```javascript
// In console, before reproducing bug
htmx.logAll();  // Enable HTMX logging
console.log("Starting reproduction test");

// Perform action (click approve button)

// Check console output:
// htmx:configRequest
// htmx:beforeRequest
// htmx:afterRequest → Status 403
// Console error: "Permission denied"
```

### Emulating Different Devices

```javascript
// Chrome DevTools → Device Toolbar (Ctrl+Shift+M)
// Select device: iPhone 12 Pro
// Perform action → Bug reproduces

// Change to Desktop
// Perform action → Bug doesn't reproduce

// Conclusion: Mobile-specific bug
```

## Multi-Tenancy Reproduction

**OBCMS-specific: Test with different organizations**

```python
# Django shell
from common.models import Organization, User

# Test with Org 1
user1 = User.objects.get(username='user_org1')
client.force_login(user1)
response = client.post(url, data)  # Bug reproduces

# Test with Org 2
user2 = User.objects.get(username='user_org2')
client.force_login(user2)
response = client.post(url, data)  # Bug doesn't reproduce

# Conclusion: Organization-specific data or permissions issue
```

## Permission-Based Reproduction

**Test with different roles:**

```python
# Test as admin
admin = User.objects.get(username='admin')
client.force_login(admin)
response = client.post(url)  # Works

# Test as staff
staff = User.objects.get(username='staff')
client.force_login(staff)
response = client.post(url)  # Bug reproduces (403 Forbidden)

# Conclusion: Permission issue
```

## Production-Only Issues

### Capturing Production State

**Railway logs:**
```bash
# Save production logs
railway logs --tail 500 > production-error.log

# Search for error
grep -i "error\|exception" production-error.log

# Find request context
grep -B 10 "error" production-error.log
```

**Django shell on production:**
```bash
# Connect to production database (if Railway allows)
railway run python manage.py shell

# Check data state
from myapp.models import BudgetRequest
request = BudgetRequest.objects.get(id=123)
print(request.__dict__)
```

**Recreate locally with production data:**
```bash
# Export production data (specific records)
railway run python manage.py dumpdata myapp.BudgetRequest --pks 123 > fixture.json

# Load locally
python manage.py loaddata fixture.json

# Test locally with production data
```

## Documenting Reproduction Steps

**Template:**

```markdown
# Bug Reproduction: [Bug Title]

## Environment
- **Where:** Development / Staging / Production
- **Django:** 5.2
- **Database:** PostgreSQL / SQLite
- **Browser:** Chrome 120 (if frontend)
- **User Role:** Admin / Manager / Staff
- **Organization:** Org #42

## Prerequisites
1. Database must have at least 1 budget request in "pending" status
2. User must have "view_budgetrequest" permission
3. User must NOT have "approve_budgetrequest" permission

## Reproduction Steps
1. Login as staff user (username: teststaff, password: test123)
2. Navigate to http://localhost:8000/budget/requests/
3. Click on any pending request
4. Click "Approve" button

## Expected Result
- Error message: "You don't have permission to approve requests"
- User redirected to list page

## Actual Result
- 403 Forbidden error page
- No user-friendly error message
- User stuck on detail page

## Reproduction Rate
✅ 5/5 attempts (100% consistent)

## Additional Notes
- Error only occurs for staff role
- Admin users can approve successfully
- Bug does not occur in production (different permission setup)

## Screenshots/Logs
[Attach error screenshot, stack trace, console logs]
```

## Common Reproduction Challenges

### Challenge 1: "Works on My Machine"

**Causes:**
- Different environment variables
- Different database state
- Different dependencies versions
- Different OS or Python version

**Solution:**
```bash
# Reproduce in clean environment
python3 -m venv fresh-venv
source fresh-venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Test again
```

### Challenge 2: Intermittent Bugs

**Causes:**
- Race conditions
- Caching issues
- Time-dependent logic

**Solution:**
- Run test 10+ times
- Use automated testing with loops
- Add logging to track timing
- Test with different delays

### Challenge 3: Data Corruption

**Causes:**
- Invalid data in database
- Missing foreign key relationships
- Soft-deleted references

**Solution:**
```python
# Check data integrity
python manage.py check
python manage.py makemigrations --check --dry-run

# Validate specific records
instance = MyModel.objects.get(id=123)
instance.full_clean()  # Raises ValidationError if invalid
```

## Summary Checklist

Before moving to Step 2 (Isolation):

- [ ] Bug reproduced at least 3 times consistently
- [ ] Exact steps documented
- [ ] Environment conditions noted
- [ ] User role and permissions identified
- [ ] Data state documented
- [ ] Error messages captured
- [ ] Expected vs. actual behavior clear
- [ ] Screenshots/logs collected

**If you can't check all boxes, keep working on reproduction before proceeding.**
