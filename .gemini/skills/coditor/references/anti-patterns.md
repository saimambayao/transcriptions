# Anti-Patterns Catalog

Common mistakes in OBCMS development and how to avoid them.

## Security Anti-Patterns

### 1. The "Forgotten Organization Filter"

**Description**: Querying data without filtering by organization.

**Severity**: Critical

**Example**:
```python
# ❌ Data leak!
tasks = Task.objects.all()
```

**Fix**: Always filter by organization:
```python
# ✅ Correct
tasks = Task.objects.filter(organization=request.user.organization)
```

**GEMINI.md Rule**: Multi-tenant data isolation (implied in Rule 3 & database rules)

---

### 2. The "Safe-ish" Input

**Description**: Marking user input as safe without sanitization.

**Severity**: Critical

**Example**:
```django
{# ❌ XSS vulnerability! #}
{{ user_comment|safe }}
```

**Fix**: Escape or sanitize:
```django
{# ✅ Correct #}
{{ user_comment }}  {# Auto-escaped #}
```

**GEMINI.md Rule**: Rule 12 (CSP Compliance)

---

### 3. The "I'll Add Nonces Later" Script

**Description**: Inline scripts without CSP nonces.

**Severity**: High

**Example**:
```html
<!-- ❌ CSP violation! -->
<script>
    console.log('TODO: add nonce');
</script>
```

**Fix**: Add nonce immediately:
```html
<!-- ✅ Correct -->
<script nonce="{{ request.csp_nonce }}">
    console.log('Has nonce');
</script>
```

**GEMINI.md Rule**: Rule 12 (CSP Compliance is Mandatory)

---

## Architecture Anti-Patterns

### 4. The "God Model"

**Description**: Model with too many responsibilities and relationships.

**Severity**: Medium

**Symptoms**:
- >20 fields
- >10 foreign keys
- Business logic in model methods that belongs in services

**Fix**: Split into multiple models, extract to service layer.

---

### 5. The "Missing Permission Check"

**Description**: Sensitive operations without RBAC checks.

**Severity**: High

**Example**:
```python
# ❌ Anyone can delete!
@login_required
def delete_task(request, task_id):
    task.delete()
```

**Fix**: Add role check:
```python
# ✅ Correct
@login_required
@role_required('task_manager')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id,
                             organization=request.user.organization)
    task.delete()
```

---

### 6. The "Hard Delete"

**Description**: Permanently deleting user data instead of soft delete.

**Severity**: Medium

**Example**:
```python
# ❌ Can't recover!
task.delete()
```

**Fix**: Implement soft delete:
```python
# ✅ Correct
task.deleted_at = timezone.now()
task.save()
```

---

## Code Quality Anti-Patterns

### 7. The "Copy-Pasta"

**Description**: Duplicate code instead of abstraction.

**Severity**: Medium

**Example**: Same organization-filtering code in 10 views.

**Fix**: Create mixin or utility function.

---

### 8. The "Mystery Function"

**Description**: Functions without docstrings or unclear names.

**Severity**: Low

**Example**:
```python
# ❌ What does this do?
def process(data):
    return data.filter(x=True).aggregate(y='sum')
```

**Fix**: Clear name + docstring:
```python
# ✅ Correct
def calculate_active_budget_total(budget_items):
    """
    Calculate total amount for active budget items.

    Args:
        budget_items: QuerySet of BudgetItem instances

    Returns:
        Decimal: Sum of amounts for active items
    """
    return budget_items.filter(is_active=True).aggregate(
        total=models.Sum('amount')
    )['total']
```

---

### 9. The "Nested Hell"

**Description**: Deeply nested if/else blocks (>3 levels).

**Severity**: Medium

**Example**:
```python
# ❌ Hard to read
if user:
    if user.is_authenticated:
        if user.has_role('admin'):
            if organization.is_active:
                # 10 more lines
```

**Fix**: Use early returns:
```python
# ✅ Correct
if not user or not user.is_authenticated:
    return HttpResponseForbidden()

if not user.has_role('admin'):
    return HttpResponseForbidden()

if not organization.is_active:
    return HttpResponse("Organization inactive")

# Main logic here
```

---

## Frontend Anti-Patterns

### 10. The "Inline Everything"

**Description**: Inline styles and scripts violating CSP.

**Severity**: High

**Example**:
```html
<!-- ❌ Multiple CSP violations -->
<div style="color: red;" onclick="alert('Hi')">
    Click me
</div>
```

**Fix**: Use Tailwind + HTMX:
```html
<!-- ✅ Correct -->
<div class="text-red-500" hx-get="/api/greet" hx-swap="innerHTML">
    Click me
</div>
```

**GEMINI.md Rule**: Rule 12 (CSP Compliance)

---

### 11. The "jQuery Refugee"

**Description**: Using jQuery patterns instead of HTMX/Alpine.js.

**Severity**: Medium

**Example**:
```javascript
// ❌ Old pattern
$('#myButton').click(function() {
    $.post('/api/submit', data, function(response) {
        $('#result').html(response);
    });
});
```

**Fix**: Use HTMX:
```html
<!-- ✅ Correct -->
<button id="myButton" hx-post="/api/submit" hx-target="#result">
    Submit
</button>
```

---

### 12. The "Accessibility Afterthought"

**Description**: Missing ARIA labels, alt text, keyboard navigation.

**Severity**: Medium

**Example**:
```html
<!-- ❌ No label, can't use keyboard -->
<div onclick="doSomething()">
    <i class="icon"></i>
</div>
```

**Fix**: Proper semantic HTML:
```html
<!-- ✅ Correct -->
<button type="button" aria-label="Perform action" hx-post="/api/action">
    <i class="icon" aria-hidden="true"></i>
</button>
```

---

## Database Anti-Patterns

### 13. The "N+1 Query"

**Description**: Loop that triggers a database query per iteration.

**Severity**: High

**Example**:
```python
# ❌ N+1 queries!
for task in Task.objects.all():
    print(task.assigned_to.username)  # Query per task!
```

**Fix**: Use select_related:
```python
# ✅ Correct - Single query
for task in Task.objects.select_related('assigned_to'):
    print(task.assigned_to.username)
```

---

### 14. The "Index? What Index?"

**Description**: Frequently queried fields without indexes.

**Severity**: Medium

**Example**:
```python
# ❌ No index on status
class Task(models.Model):
    status = models.CharField(max_length=20)

# Later: Slow!
Task.objects.filter(status='completed')  # Full table scan
```

**Fix**: Add index:
```python
# ✅ Correct
class Task(models.Model):
    status = models.CharField(max_length=20, db_index=True)
```

---

## Testing Anti-Patterns

### 15. The "It Works On My Machine"

**Description**: No tests, manual testing only.

**Severity**: High

**Fix**: Write tests for all new code. Minimum coverage: 80%.

---

### 16. The "Happy Path Only"

**Description**: Tests that only check success cases.

**Severity**: Medium

**Example**:
```python
# ❌ Only tests success
def test_create_task(self):
    response = self.client.post('/tasks/create/', valid_data)
    self.assertEqual(response.status_code, 200)
```

**Fix**: Test edge cases:
```python
# ✅ Correct - Test failures too
def test_create_task_without_permission(self):
    response = self.client.post('/tasks/create/', valid_data)
    self.assertEqual(response.status_code, 403)

def test_create_task_cross_org_data_leak(self):
    # Verify user can't create task for different org
    pass
```

---

## Migration Anti-Patterns

### 17. The "Data Migration Without Backup"

**Description**: Running migrations on production without backup.

**Severity**: Critical

**Fix**: Always backup database before migrations.

**GEMINI.md Rule**: Rule 13 (Migration Management)

---

### 18. The "I'll Squash Later"

**Description**: Hundreds of small migrations never squashed.

**Severity**: Low

**Fix**: Regularly squash migrations (after merging to main).

---

## Deployment Anti-Patterns

### 19. The "YOLO Deploy"

**Description**: Deploying to production without testing on staging.

**Severity**: Critical

**Fix**: Always deploy to staging first.

**GEMINI.md Rules**: Pre-deployment checklist

---

### 20. The "Static Files? What Static Files?"

**Description**: Forgetting to run collectstatic before deployment.

**Severity**: High

**Symptoms**: Missing CSS, JS, images in production.

**Fix**: Add to deployment checklist:
```bash
python manage.py collectstatic --noinput
```

---

## GEMINI.md Rule Violations

### 21. The "db.sqlite3 Deleter"

**Description**: Deleting db.sqlite3 file (user development data).

**Severity**: Critical

**GEMINI.md Rule**: Rule 3 (Never delete db.sqlite3)

---

### 22. The "Surprise Commit"

**Description**: Committing without user permission.

**Severity**: High

**GEMINI.md Rule**: Rule 1 (Always ask permission before committing)

---

### 23. The "Temporary Fix"

**Description**: Bypassing errors instead of fixing root cause.

**Severity**: High

**Example**:
```python
# ❌ Hiding the error
try:
    risky_operation()
except Exception:
    pass  # TODO: fix later
```

**GEMINI.md Rule**: Rule 5 (No temporary fixes - fix root causes)

---

## Prevention Checklist

Run coditor regularly to catch anti-patterns early:

- [ ] Before committing
- [ ] Before deploying to staging
- [ ] After implementing new features
- [ ] During code reviews
- [ ] Monthly comprehensive audits
