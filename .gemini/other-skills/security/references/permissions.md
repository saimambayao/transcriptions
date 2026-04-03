# Permissions

## Check Permissions

```python
@permission_required('app.add_model')
def create_view(request):
    pass

# In code
if request.user.has_perm('app.change_model'):
    # Allow edit
    pass
```

## Custom Permissions

```python
class Meta:
    permissions = [
        ('approve_item', 'Can approve items'),
    ]
```
