# Tutorial: [Title]

**Level**: [ ] Beginner [ ] Intermediate [ ] Advanced
**Time**: ~X hours
**Last Updated**: YYYY-MM-DD

---

## Prerequisites

Before starting this tutorial, you should have:

- [ ] Prerequisite 1 (e.g., "Basic Django knowledge")
- [ ] Prerequisite 2 (e.g., "Understanding of OBCMS multi-tenant architecture")
- [ ] Prerequisite 3 (e.g., "Development environment set up")

**Recommended Prior Tutorials**:
- [Tutorial Name](link-to-tutorial)

---

## Learning Objectives

By the end of this tutorial, you will be able to:

1. Learning objective 1
2. Learning objective 2
3. Learning objective 3

---

## What We're Building

[Brief description of what will be built in this tutorial]

**Feature Overview**:
- Feature point 1
- Feature point 2
- Feature point 3

**Final Result**:
[Description or screenshot of final result]

---

## Step 1: [First Step Title]

**What You'll Do**: [Brief description]

**Why**: [Explanation of why this step is important]

### Instructions

1. Sub-step 1
   ```bash
   # Command to run
   command here
   ```

2. Sub-step 2
   ```python
   # Code example
   code here
   ```

3. Sub-step 3

### Code Example

```python
# Full code example for this step
def example_function():
    """Docstring explaining what this does"""
    pass
```

**File Location**: `src/app_name/file.py`

### Expected Outcome

After completing this step:
- Expected outcome 1
- Expected outcome 2

**Verification**:
```bash
# Command to verify this step worked
python manage.py check
```

### Common Issues

**Issue 1**: [Description of common issue]
- **Cause**: [Why this happens]
- **Solution**: [How to fix it]

**Issue 2**: [Description of another issue]
- **Cause**: [Why this happens]
- **Solution**: [How to fix it]

---

## Step 2: [Second Step Title]

[Repeat structure from Step 1]

---

## Step 3: [Third Step Title]

[Repeat structure from Step 1]

---

## Testing Your Implementation

### Unit Tests

Create tests to verify functionality:

```python
# File: src/app_name/tests/test_feature.py
from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def test_feature(self):
        """Test that feature works correctly"""
        # Test code
        pass
```

**Run Tests**:
```bash
cd src
pytest app_name/tests/test_feature.py
```

### Integration Tests

```python
# Integration test example
def test_workflow(self):
    """Test complete workflow"""
    pass
```

### Browser Testing

1. Start development server:
   ```bash
   python manage.py runserver
   ```

2. Navigate to: `http://localhost:8000/feature-url/`

3. Test scenarios:
   - Scenario 1: [What to test]
   - Scenario 2: [What to test]
   - Scenario 3: [What to test]

4. Verify:
   - [ ] Feature works as expected
   - [ ] No console errors
   - [ ] CSP compliance (no CSP violations)
   - [ ] Multi-tenant isolation (can't see other org's data)

---

## Security Considerations

### Multi-Tenant Isolation

**Critical**: Verify organization filtering

```python
# ✅ CORRECT: Filter by organization
items = Item.objects.filter(organization=request.user.organization)

# ❌ WRONG: Missing organization filter
items = Item.objects.all()
```

**Test**:
```python
def test_organization_isolation(self):
    """Verify users can't see other organizations' data"""
    # Create two orgs, test isolation
    pass
```

### CSP Compliance

**Critical**: All scripts must have nonces

```django
{# ✅ CORRECT #}
<script nonce="{{ request.csp_nonce }}">
    console.log('Safe');
</script>

{# ❌ WRONG #}
<script>console.log('Violation!');</script>
```

### RBAC Permissions

**Add permission checks**:

```python
@permission_required('app.permission_name')
def view_name(request):
    pass
```

---

## Deployment

### Pre-Deployment Checklist

Before deploying to staging:

- [ ] All tests pass (`pytest`)
- [ ] Test coverage > 80%
- [ ] No CSP violations
- [ ] Multi-tenant isolation verified
- [ ] Coditor audit completed (Critical/High = 0)
- [ ] UI tested in browser (3 times)
- [ ] Migrations created and tested

### Deploy to Staging

```bash
# Commit changes
git add .
git commit -m "Feature: [Feature name]"

# Push to staging
git push origin staging

# Monitor deployment
railway logs --tail 100
```

### Verify on Staging

- [ ] Feature works on staging
- [ ] No errors in logs
- [ ] Critical user journeys tested

---

## Troubleshooting

### Common Issues and Solutions

**Issue 1: [Common problem]**
- **Symptom**: [What users see]
- **Cause**: [Why it happens]
- **Solution**: [How to fix]
  ```bash
  # Commands to fix
  ```

**Issue 2: [Another problem]**
- **Symptom**: [What users see]
- **Cause**: [Why it happens]
- **Solution**: [How to fix]

**Issue 3: Multi-tenant data leak**
- **Symptom**: Seeing other organizations' data
- **Cause**: Missing organization filter
- **Solution**: Add organization filter to all queries
  ```python
  # ✅ Add organization filter
  items = Item.objects.filter(organization=request.user.organization)
  ```

---

## Next Steps

After completing this tutorial:

1. **Next Tutorial**: [Tutorial Name](link) - [What it covers]
2. **Practice**: Implement [related feature]
3. **Explore**: Read [related documentation]

---

## Summary

**What You Learned**:
- Learning point 1
- Learning point 2
- Learning point 3

**Key Takeaways**:
- Always filter by organization (multi-tenant isolation)
- Use CSP-compliant patterns (nonce-based scripts)
- Test organization isolation
- Follow OBCMS conventions

---

## Additional Resources

**Documentation**:
- [OBCMS Architecture Overview](../../references/obcms-architecture-overview.md)
- [Tech Stack Guide](../../references/tech-stack-guide.md)
- [Design Patterns](../../references/design-patterns.md)

**Related Skills**:
- `/featuredev` - Feature development workflow
- `/backend` - Django backend patterns
- `/frontend` - HTMX + Tailwind UI patterns
- `/coditor` - Code auditing

**Django Documentation**:
- [Django Models](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/5.2/topics/http/views/)
- [Django Templates](https://docs.djangoproject.com/en/5.2/topics/templates/)

---

## Feedback

Have questions or suggestions for this tutorial?
- Submit feedback via OBCMS issue tracker
- Suggest improvements to tutorial content

---

**Tutorial Version**: 1.0
**Tested With**: Django 5.2, OBCMS latest
