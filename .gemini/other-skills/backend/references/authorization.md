# Django Authorization

Guide for permissions, roles, and access control.

## Django Permissions

```python
# Check permissions in views
from django.contrib.auth.decorators import permission_required

@permission_required('communities.add_community')
def create_community(request):
    # Only users with add_community permission can access
    pass

@permission_required(['communities.view_community', 'communities.change_community'])
def edit_community(request, pk):
    # Requires multiple permissions
    pass

# Check in code
if request.user.has_perm('communities.add_community'):
    # User has permission
    pass

if request.user.has_perms(['communities.view_community', 'communities.change_community']):
    # User has all permissions
    pass
```

## Custom Permissions

```python
class Community(models.Model):
    # ... fields ...

    class Meta:
        permissions = [
            ('approve_community', 'Can approve community registration'),
            ('export_community_data', 'Can export community data'),
        ]
```

## Role-Based Access Control

```python
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

# Usage
def user_has_role(user, role_name):
    return UserRole.objects.filter(
        user=user,
        role__name=role_name,
        organization=user.organization
    ).exists()
```

## Object-Level Permissions

```python
def can_edit_community(user, community):
    """Check if user can edit this community."""
    # Must be same organization
    if community.organization != user.organization:
        return False
    # Must have permission
    if not user.has_perm('communities.change_community'):
        return False
    # Must be creator or admin
    if community.created_by == user or user.is_staff:
        return True
    return False
```

For middleware patterns, see [middleware.md](middleware.md).
