# OBCMS Multi-Tenant Architecture

**Purpose**: Deep dive into OBCMS multi-tenant implementation, patterns, and best practices.

---

## Multi-Tenant Concepts

### Organization (Tenant)

**Definition**: Primary isolation boundary in OBCMS

**Types**:
- OOBC (Office of Bangsamoro Communities)
- Partner Ministries (MOLE, MOH, MENRE, etc.)
- Local Government Units (LGUs)

**Model**:
```python
class Organization(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    organization_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
```

### User-Organization Relationship

**One-to-One**: Each user belongs to exactly one organization

```python
class User(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
```

### Data Scoping

**Rule**: All data is scoped to an organization

```python
class Community(BaseModel):
    name = models.CharField(max_length=255)
    # organization field inherited from BaseModel
```

---

## Multi-Tenant Patterns

### Pattern 1: QuerySet Filtering

**✅ CORRECT**:
```python
def list_communities(request):
    communities = Community.objects.filter(
        organization=request.user.organization
    )
    return render(request, 'communities/list.html', {'communities': communities})
```

**❌ WRONG**:
```python
def list_communities(request):
    communities = Community.objects.all()  # Data leak!
    return render(request, 'communities/list.html', {'communities': communities})
```

### Pattern 2: Detail View with Organization Check

**✅ CORRECT**:
```python
def view_community(request, pk):
    community = get_object_or_404(
        Community,
        pk=pk,
        organization=request.user.organization  # Critical check
    )
    return render(request, 'communities/detail.html', {'community': community})
```

**❌ WRONG**:
```python
def view_community(request, pk):
    community = get_object_or_404(Community, pk=pk)  # Missing org check!
    return render(request, 'communities/detail.html', {'community': community})
```

### Pattern 3: DRF ViewSet

**✅ CORRECT**:
```python
class CommunityViewSet(viewsets.ModelViewSet):
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Community.objects.filter(
            organization=self.request.user.organization
        )

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user
        )
```

### Pattern 4: Django Admin

**✅ CORRECT**:
```python
class CommunityAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organization=request.user.organization)
```

---

## Testing Multi-Tenant Isolation

```python
def test_organization_isolation(self):
    # Create two organizations
    org1 = Organization.objects.create(name="OOBC")
    org2 = Organization.objects.create(name="Partner Ministry")

    # Create users
    user1 = User.objects.create(username="user1", organization=org1)
    user2 = User.objects.create(username="user2", organization=org2)

    # Create communities
    comm1 = Community.objects.create(name="Comm1", organization=org1)
    comm2 = Community.objects.create(name="Comm2", organization=org2)

    # Test isolation
    self.client.force_login(user1)
    response = self.client.get('/communities/')
    self.assertContains(response, "Comm1")
    self.assertNotContains(response, "Comm2")  # Critical: user1 can't see org2 data
```

---

## Common Multi-Tenant Mistakes

**Mistake 1**: Using `.all()` without filter
```python
# ❌ WRONG
tasks = Task.objects.all()
```

**Mistake 2**: Missing organization in get_object_or_404
```python
# ❌ WRONG
task = get_object_or_404(Task, id=task_id)
```

**Mistake 3**: Hardcoding organization
```python
# ❌ WRONG
org = Organization.objects.get(code='OOBC')
tasks = Task.objects.filter(organization=org)
```

**Mistake 4**: Admin without organization filter
```python
# ❌ WRONG
class TaskAdmin(admin.ModelAdmin):
    pass  # Shows all organizations' tasks!
```

---

**Prevention**: Run `/coditor` to detect multi-tenant data leaks
