# Multi-Factor Authentication (MFA)

Add additional security layer beyond passwords using TOTP, SMS, or backup codes.

## Table of Contents
- [TOTP (Time-Based One-Time Password)](#totp)
- [Backup Codes](#backup-codes)
- [MFA Enforcement](#mfa-enforcement)
- [Common Pitfalls](#common-pitfalls)
- [OBCMS-Specific Implementation](#obcms-specific-implementation)
- [Testing](#testing)
- [Related Patterns](#related-patterns)

## TOTP (Time-Based One-Time Password)

Most common MFA using authenticator apps (Google Authenticator, Authy).

```python
# Install: pip install pyotp qrcode

from django.db import models
import pyotp
import qrcode
from io import BytesIO
import base64

class UserMFA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=32)
    is_enabled = models.BooleanField(default=False)
    backup_codes = models.JSONField(default=list)
    
    def generate_secret(self):
        """Generate new secret key."""
        self.secret_key = pyotp.random_base32()
        self.save()
        return self.secret_key
    
    def get_totp_uri(self):
        """Get URI for QR code."""
        return pyotp.totp.TOTP(self.secret_key).provisioning_uri(
            name=self.user.email,
            issuer_name='OBCMS'
        )
    
    def get_qr_code(self):
        """Generate QR code image."""
        uri = self.get_totp_uri()
        qr = qrcode.make(uri)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        return base64.b64encode(buffer.getvalue()).decode()
    
    def verify_token(self, token):
        """Verify TOTP token."""
        totp = pyotp.TOTP(self.secret_key)
        return totp.verify(token, valid_window=1)  # 30 second window
```

**Setup view:**
```python
@login_required
def setup_mfa(request):
    user_mfa, created = UserMFA.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        token = request.POST.get('token')
        
        if user_mfa.verify_token(token):
            user_mfa.is_enabled = True
            user_mfa.generate_backup_codes()
            user_mfa.save()
            return redirect('mfa_success')
        else:
            return render(request, 'mfa_setup.html', {
                'error': 'Invalid token',
                'qr_code': user_mfa.get_qr_code()
            })
    
    user_mfa.generate_secret()
    return render(request, 'mfa_setup.html', {
        'qr_code': user_mfa.get_qr_code(),
        'manual_code': user_mfa.secret_key
    })
```

**Login with MFA:**
```python
def login_with_mfa(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user:
            try:
                if user.usermfa.is_enabled:
                    request.session['pre_mfa_user_id'] = user.id
                    return redirect('verify_mfa')
            except UserMFA.DoesNotExist:
                pass
            
            login(request, user)
            return redirect('dashboard')
    
    return render(request, 'login.html')

def verify_mfa(request):
    user_id = request.session.get('pre_mfa_user_id')
    if not user_id:
        return redirect('login')
    
    user = User.objects.get(id=user_id)
    user_mfa = user.usermfa
    
    if request.method == 'POST':
        token = request.POST.get('token')
        backup_code = request.POST.get('backup_code')
        
        if token and user_mfa.verify_token(token):
            login(request, user)
            del request.session['pre_mfa_user_id']
            return redirect('dashboard')
        elif backup_code and user_mfa.use_backup_code(backup_code):
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'mfa_verify.html', {
                'error': 'Invalid code'
            })
    
    return render(request, 'mfa_verify.html')
```

## Backup Codes

Recovery codes if user loses authenticator device.

```python
import secrets
import hashlib

class UserMFA(models.Model):
    # ... existing fields ...
    
    def generate_backup_codes(self, count=10):
        """Generate hashed backup codes."""
        codes = [secrets.token_hex(4) for _ in range(count)]
        # Hash before storing
        self.backup_codes = [
            hashlib.sha256(code.encode()).hexdigest()
            for code in codes
        ]
        self.save()
        return codes  # Return unhashed to show user once
    
    def use_backup_code(self, code):
        """Use and remove backup code."""
        hashed = hashlib.sha256(code.encode()).hexdigest()
        if hashed in self.backup_codes:
            self.backup_codes.remove(hashed)
            self.save()
            return True
        return False
```

## MFA Enforcement

Require MFA for specific roles or permissions.

```python
from django.contrib.auth.decorators import user_passes_test

def mfa_required(view_func):
    """Decorator requiring MFA."""
    def check_mfa(user):
        if not user.is_authenticated:
            return False
        try:
            return user.usermfa.is_enabled
        except UserMFA.DoesNotExist:
            return False
    
    return user_passes_test(
        check_mfa,
        login_url='/setup-mfa/'
    )(view_func)

@mfa_required
def sensitive_data_view(request):
    """View requiring MFA."""
    return render(request, 'sensitive_data.html')
```

## Common Pitfalls

**Pitfall 1: Not rate-limiting MFA attempts**
```python
# ❌ BAD - Unlimited attempts allows brute force
def verify_mfa(request):
    if user_mfa.verify_token(token):
        login(request, user)

# ✅ GOOD - Rate limit attempts
from django.core.cache import cache

def verify_mfa(request):
    attempts_key = f'mfa_attempts_{user_id}'
    attempts = cache.get(attempts_key, 0)
    
    if attempts >= 5:
        return render(request, 'mfa_locked.html')
    
    if user_mfa.verify_token(token):
        cache.delete(attempts_key)
        login(request, user)
    else:
        cache.set(attempts_key, attempts + 1, 300)  # 5 min lockout
```

**Pitfall 2: Not providing backup codes**
- Users WILL lose their devices
- Always generate backup codes during MFA setup

**Pitfall 3: Storing backup codes in plaintext**
```python
# ❌ BAD - Plaintext backup codes
backup_codes = ['abc123', 'def456']

# ✅ GOOD - Hash backup codes
backup_codes = [hashlib.sha256(code.encode()).hexdigest() for code in codes]
```

## OBCMS-Specific Implementation

**MFA for organization admins:**
```python
class OrganizationMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    mfa_required = models.BooleanField(default=False)

# Middleware to enforce MFA
class MFAMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            member = OrganizationMember.objects.filter(
                user=request.user,
                mfa_required=True
            ).first()
            
            if member:
                try:
                    if not request.user.usermfa.is_enabled:
                        return redirect('setup_mfa')
                except UserMFA.DoesNotExist:
                    return redirect('setup_mfa')
        
        return self.get_response(request)
```

## Testing

```python
from django.test import TestCase
import pyotp

class MFATestCase(TestCase):
    def test_totp_verification(self):
        user = User.objects.create_user('test', 'test@example.com')
        mfa = UserMFA.objects.create(user=user)
        mfa.generate_secret()
        
        totp = pyotp.TOTP(mfa.secret_key)
        token = totp.now()
        
        self.assertTrue(mfa.verify_token(token))
    
    def test_backup_code_usage(self):
        user = User.objects.create_user('test', 'test@example.com')
        mfa = UserMFA.objects.create(user=user)
        codes = mfa.generate_backup_codes()
        
        self.assertTrue(mfa.use_backup_code(codes[0]))
        self.assertFalse(mfa.use_backup_code(codes[0]))  # Can't reuse
```

## Related Patterns

- See [authentication.md](authentication.md) for basic login
- See [passwords.md](passwords.md) for password security
