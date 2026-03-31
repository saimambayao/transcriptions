# Object-Level Permissions

Row-level security for fine-grained access control.

## Implementation

```python
# Install: pip install django-guardian

from guardian.shortcuts import assign_perm, get_objects_for_user

# Assign permission to user for specific object
assign_perm('change_workitem', user, work_item)

# Check permission
if user.has_perm('change_workitem', work_item):
    work_item.status = 'approved'
    work_item.save()

# Get objects user can access
work_items = get_objects_for_user(
    user,
    'common.change_workitem'
)
```

## OBCMS Pattern

```python
class WorkItemViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # Only show work items user can view
        return get_objects_for_user(
            self.request.user,
            'common.view_workitem'
        ).filter(organization=self.request.user.organization)
```

## Related Patterns

- See [permissions.md](permissions.md) for model permissions
- See [rbac.md](rbac.md) for role-based access
