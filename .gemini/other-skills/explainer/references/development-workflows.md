# OBCMS Development Workflows

**Purpose**: Step-by-step guides for common development tasks.

---

## Workflow 1: Add a New Feature

**Steps**:

1. **Choose App**: Decide which app owns this feature
   - Existing app? Add to that app
   - New domain? Create new app

2. **Design Models**: Create models with multi-tenant in mind
   ```python
   class MyModel(BaseModel):
       organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
       # ... fields
   ```

3. **Create Migrations**:
   ```bash
   cd src
   python manage.py makemigrations my_app
   python manage.py migrate
   ```

4. **Implement Views**: Add organization filtering
   ```python
   def list_items(request):
       items = MyModel.objects.filter(organization=request.user.organization)
       return render(request, 'my_app/list.html', {'items': items})
   ```

5. **Build Templates**: HTMX + Tailwind, CSP-compliant
   ```django
   <button hx-delete="/api/items/{{ item.id }}/" hx-target="#item-{{ item.id }}">
       Delete
   </button>
   ```

6. **Add API Endpoints** (if needed): DRF ViewSets with organization scoping

7. **Write Tests**: Unit + integration tests

8. **Audit**: Run `/coditor` before deployment

9. **Deploy**: Push to staging, test, then production

---

## Workflow 2: Create a New Django App

```bash
# Step 1: Create app
cd src
python manage.py startapp my_app

# Step 2: Add to INSTALLED_APPS
# Edit obc_management/settings/base.py
INSTALLED_APPS = [
    ...
    'my_app',
]

# Step 3: Create models extending BaseModel
# Edit my_app/models.py
from common.models import BaseModel

class MyModel(BaseModel):
    name = models.CharField(max_length=255)

# Step 4: Create migrations
python manage.py makemigrations my_app

# Step 5: Add URLs
# Create my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_items, name='list_items'),
]

# Edit obc_management/urls.py
urlpatterns += [
    path('my-app/', include('my_app.urls')),
]

# Step 6: Create views, templates, tests
```

---

## Workflow 3: Implement HTMX Pattern

**Delete Button with Confirmation**:

```html
<!-- Template -->
<button
    hx-delete="/api/tasks/{{ task.id }}/"
    hx-target="#task-{{ task.id }}"
    hx-swap="outerHTML"
    hx-confirm="Delete this task?"
    class="btn btn-danger">
    Delete
</button>

<div id="task-{{ task.id }}">
    <!-- Task content -->
</div>
```

```python
# View
from django.views.decorators.http import require_http_methods

@require_http_methods(["DELETE"])
def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        organization=request.user.organization
    )
    task.soft_delete()
    return HttpResponse(status=200)  # Triggers hx-swap to remove element
```

---

## Workflow 4: Add RBAC Permission

**Step 1**: Define permission in models.py
```python
class Task(BaseModel):
    class Meta:
        permissions = [
            ("can_assign_tasks", "Can assign tasks to users"),
        ]
```

**Step 2**: Create migration
```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 3**: Use permission in view
```python
from django.contrib.auth.decorators import permission_required

@permission_required('tasks.can_assign_tasks')
def assign_task(request, task_id):
    # ...
```

**Step 4**: Assign permission in Django admin

---

## Workflow 5: Deploy to Staging/Production

**Staging**:
```bash
# Step 1: Commit changes
git add .
git commit -m "Feature: Add resource booking"

# Step 2: Push to staging branch
git push origin staging

# Step 3: Railway auto-deploys
# Wait for deployment, monitor logs

# Step 4: Test on staging
# Verify critical features

# Step 5: If successful, proceed to production
```

**Production**:
```bash
# Step 1: Merge staging to main
git checkout main
git merge staging

# Step 2: Push to main
git push origin main

# Step 3: Railway auto-deploys to production

# Step 4: Monitor for 1 hour
railway logs --tail 100
```

---

**See also**: `common-conventions.md` for naming and code standards
