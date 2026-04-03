# Password Security

Implement strong password policies and secure storage.

## Password Requirements

```python
# settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 12}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
]
```

## Password Reset

```python
from django.contrib.auth.views import PasswordResetView

# Secure password reset flow
class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    success_url = '/password-reset/done/'
    
    def form_valid(self, form):
        # Log password reset request
        logger.info(f"Password reset requested for {form.cleaned_data['email']}")
        return super().form_valid(form)
```

## Related Patterns

- See [authentication.md](authentication.md) for login
- See [mfa.md](mfa.md) for additional security
