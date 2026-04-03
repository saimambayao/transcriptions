# Architecture Pattern Detection

Pattern detection rules for OBCMS architecture compliance.

## RBAC Patterns

**Severity**: High

### Pattern: Missing Role-Based Permission Checks

**Detection**: Sensitive views without `@role_required` or `@permission_required` decorators.

**Sensitive Operations**:
- Create/Update/Delete views
- Bulk operations
- Export/Import data
- Admin functions
- Budget modifications

**Example Violation**:
```python
# ❌ HIGH: No permission check
@login_required
def delete_community(request, community_id):
    community.delete()  # Anyone can delete!
```

**Remediation**:
```python
# ✅ CORRECT: Role-based permission
from common.decorators import role_required

@login_required
@role_required('community_manager')
def delete_community(request, community_id):
    community = get_object_or_404(
        Community,
        id=community_id,
        organization=request.user.organization
    )
    community.delete()
```

---

## Organization Scoping Patterns

**Severity**: Critical

See [security-patterns.md](security-patterns.md#multi-tenant-data-leak-patterns) for comprehensive multi-tenant patterns.

**Quick Checklist**:
- [ ] Models have `organization` ForeignKey
- [ ] All queries filter by organization
- [ ] get_object_or_404 includes organization
- [ ] ViewSets override get_queryset with org filter
- [ ] Forms limit ForeignKey choices to org
- [ ] Admin queryset filtered by org (unless superuser)

---

## Soft Delete Patterns

**Severity**: Medium

### Pattern: Hard Delete Instead of Soft Delete

**Detection**: Models that should use soft delete but use hard delete.

**Models Requiring Soft Delete**:
- User-facing data (tasks, communities, assessments)
- Audit trail data
- Referenced data (organizations, users)

**Example Violation**:
```python
# ❌ MEDIUM: Hard delete on user data
class Task(models.Model):
    # No deleted_at field!
    pass

# Later
task.delete()  # Permanently deleted, can't audit!
```

**Remediation**:
```python
# ✅ CORRECT: Soft delete
class Task(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()
```

---

## Model Relationship Patterns

**Severity**: Medium

### Pattern: Incorrect Cascade Behavior

**Detection**: on_delete=CASCADE where it should be PROTECT or SET_NULL.

**OBCMS Rules**:
- **CASCADE**: Only for truly dependent data (comments → task)
- **PROTECT**: For critical relationships (task → organization)
- **SET_NULL**: For optional references (task → assigned_to)

**Example Violation**:
```python
# ❌ MEDIUM: Wrong cascade delete
class Task(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE  # Deletes all tasks if org deleted!
    )
```

**Remediation**:
```python
# ✅ CORRECT: Use PROTECT
class Task(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT  # Prevents org deletion if tasks exist
    )
```

---

## Audit Trail Patterns

**Severity**: Medium

### Pattern: Missing Audit Fields

**Detection**: Models without created_at/updated_at/created_by/updated_by.

**Required Audit Fields**:
```python
class AuditedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')

    class Meta:
        abstract = True
```

**Models Requiring Audit Trail**:
- All user-facing models
- Budget data
- Planning data
- Assessment data

---

## Index Optimization Patterns

**Severity**: Medium

### Pattern: Missing Indexes on Frequently Queried Fields

**Detection**: Fields used in filter()/order_by() without db_index=True.

**Fields Requiring Indexes**:
- Foreign keys (auto-indexed)
- Status fields (if frequently filtered)
- Date fields (if used for date ranges)
- organization field (critical!)

**Example Violation**:
```python
# ❌ MEDIUM: No index on status field
class Task(models.Model):
    status = models.CharField(max_length=20)  # No db_index!

# Later: Slow query
Task.objects.filter(status='completed')  # Full table scan!
```

**Remediation**:
```python
# ✅ CORRECT: Add index
class Task(models.Model):
    status = models.CharField(max_length=20, db_index=True)

# Or composite index
class Meta:
    indexes = [
        models.Index(fields=['organization', 'status']),
    ]
```

---

## Audit Checklist

- [ ] Sensitive views have RBAC decorators
- [ ] All models have organization field
- [ ] Soft delete implemented where needed
- [ ] Proper cascade behavior (PROTECT/SET_NULL)
- [ ] Audit trail fields present
- [ ] Indexes on frequently queried fields
- [ ] Foreign key relationships documented
