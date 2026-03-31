# Data Protection

## Encryption

```python
from django.conf import settings
from cryptography.fernet import Fernet

def encrypt_data(data):
    f = Fernet(settings.ENCRYPTION_KEY)
    return f.encrypt(data.encode())

def decrypt_data(encrypted):
    f = Fernet(settings.ENCRYPTION_KEY)
    return f.decrypt(encrypted).decode()
```

## Sensitive Fields

```python
class Beneficiary(models.Model):
    ssn = models.CharField(max_length=20)  # Encrypt this
    
    def save(self, *args, **kwargs):
        if self.ssn and not self.ssn.startswith('enc:'):
            self.ssn = 'enc:' + encrypt_data(self.ssn)
        super().save(*args, **kwargs)
```
