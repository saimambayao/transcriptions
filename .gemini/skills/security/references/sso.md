# Single Sign-On (SSO)

Integrate with external identity providers.

## OAuth2 Implementation

```python
# Install: pip install django-allauth

# settings.py
INSTALLED_APPS = [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    }
}
```

## Related Patterns

- See [authentication.md](authentication.md) for standard auth
