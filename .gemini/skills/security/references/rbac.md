# Role-Based Access Control (RBAC)

Organize permissions using roles for easier access management.

## Implementation

```python
# models.py
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission)
    description = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)
    
    def has_permission(self, permission_code):
        return self.roles.filter(
            permissions__codename=permission_code
        ).exists()

# Create roles
admin_role = Role.objects.create(name='Administrator', description='Full access')
admin_role.permissions.add(
    Permission.objects.get(codename='add_workitem'),
    Permission.objects.get(codename='change_workitem'),
    Permission.objects.get(codename='delete_workitem'),
)

# Assign role
user.profile.roles.add(admin_role)

# Check permission
if user.profile.has_permission('add_workitem'):
    # Allow action
    pass
```

## OBCMS Roles

```python
# Predefined OBCMS roles
OOBC_ADMIN = 'oobc_admin'          # Full system access
ORG_ADMIN = 'org_admin'             # Organization admin
PROGRAM_MANAGER = 'program_manager' # Manage programs
DATA_ENCODER = 'data_encoder'       # Data entry only
VIEWER = 'viewer'                    # Read-only access
```

## Related Patterns

- See [permissions.md](permissions.md) for permission details
- See [object-permissions.md](object-permissions.md) for row-level security
