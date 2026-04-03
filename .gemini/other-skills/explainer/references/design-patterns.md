# OBCMS Design Patterns

**Purpose**: Common design patterns used throughout OBCMS.

---

## 1. Multi-Tenant Pattern

**Pattern**: Organization-scoped data isolation

**Implementation**:
```python
# Every model extends BaseModel
class Task(BaseModel):
    title = models.CharField(max_length=255)
    # organization field inherited from BaseModel

# Always filter by organization
tasks = Task.objects.filter(organization=request.user.organization)
```

**Rules**:
- NEVER use `.all()` without organization filter
- ALWAYS include organization in get_object_or_404
- Test organization isolation

---

## 2. Soft Delete Pattern

**Pattern**: Mark as deleted, don't hard delete

**Implementation**:
```python
class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='+')

    objects = ActiveManager()  # Excludes is_deleted=True
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
```

**Benefits**:
- Audit trail
- Recovery possible
- Referential integrity

---

## 3. Audit Trail Pattern

**Pattern**: Track who created/modified data

**Implementation**:
```python
class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
```

**Benefits**:
- Compliance
- Forensic analysis
- User accountability

---

## 4. RBAC Pattern

**Pattern**: Role-Based Access Control

**Implementation**:
```python
# Permission decorator
@permission_required('communities.view_community')
def view_community(request, pk):
    community = get_object_or_404(Community, pk=pk, organization=request.user.organization)
    return render(request, 'communities/detail.html', {'community': community})

# DRF permission class
class CommunityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
```

**Levels**:
- Model-level: `communities.view_community`
- Row-level: Organization filtering
- Field-level: Custom permission logic

---

## 5. CSP Compliance Pattern (MANDATORY)

**Pattern**: Nonce-based script/style loading

**Implementation**:
```django
{# ✅ CORRECT #}
<script nonce="{{ request.csp_nonce }}">
    console.log('Safe');
</script>

{# ❌ WRONG #}
<script>
    console.log('CSP violation!');
</script>
```

**HTMX Pattern**:
```html
<button hx-delete="/api/tasks/123/">Delete</button>
```

**Alpine.js CSP**:
- Requires 'unsafe-eval' in CSP (already configured)

---

## 6. HTMX Interaction Pattern

**Pattern**: Server-driven dynamic updates

**Implementation**:
```html
<!-- Frontend -->
<form hx-post="/api/communities/" hx-target="#community-list" hx-swap="beforeend">
    ...
</form>

<!-- Backend -->
def create_community(request):
    # ... save community ...
    return render(request, 'communities/community_row.html', {'community': community})
```

**Patterns**:
- `hx-get`: Load content
- `hx-post`: Submit forms
- `hx-delete`: Delete with confirmation
- `hx-swap`: Control where content goes

---

## 7. BaseModel Pattern

**Pattern**: Abstract model with common fields

```python
class BaseModel(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='+')

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True
```

**All models extend BaseModel**

---

## 8. QuerySet Optimization Pattern

**Pattern**: Reduce database queries

**Implementation**:
```python
# ✅ CORRECT: select_related for ForeignKey
communities = Community.objects.select_related('municipality', 'barangay').filter(organization=org)

# ✅ CORRECT: prefetch_related for ManyToMany
assessments = Assessment.objects.prefetch_related('indicators').filter(organization=org)

# ❌ WRONG: N+1 queries
for community in Community.objects.all():
    print(community.municipality.name)  # Queries database for each community!
```

---

**See also**: `multi-tenant-architecture.md` for detailed multi-tenant patterns
