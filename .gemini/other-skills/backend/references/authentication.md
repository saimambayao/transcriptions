# Django Authentication

Guide for user authentication, login/logout, and session management.

## Login View

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.get_full_name()}!')
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')
```

## Password Management

```python
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            messages.success(request, 'Password changed successfully.')
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {'form': form})
```

## Custom User Model

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    organization = models.ForeignKey('Organization', on_delete=models.PROTECT, null=True)
    mobile = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=100, blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username
```

For permissions, see [authorization.md](authorization.md).
