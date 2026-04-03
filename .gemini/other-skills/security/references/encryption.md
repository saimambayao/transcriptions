# Field Encryption

Encrypt sensitive data at rest.

## Implementation

```python
from cryptography.fernet import Fernet
from django.conf import settings

class EncryptedField(models.Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fernet = Fernet(settings.ENCRYPTION_KEY)
    
    def get_prep_value(self, value):
        if value is None:
            return value
        return self.fernet.encrypt(value.encode()).decode()
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.fernet.decrypt(value.encode()).decode()

# Usage
class Beneficiary(models.Model):
    ssn = EncryptedField(max_length=500)  # Encrypted
    name = models.CharField(max_length=200)  # Not encrypted
```

## Related Patterns

- See [data-protection.md](data-protection.md) for sensitive data handling
