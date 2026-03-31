# API Authentication

Secure REST API endpoints with token authentication.

## Token Authentication

```python
# Install: pip install djangorestframework

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class WorkItemViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkItem.objects.all()

# Generate token for user
from rest_framework.authtoken.models import Token
token = Token.objects.create(user=user)
print(token.key)

# API request
curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
     http://localhost:8000/api/work-items/
```

## Rate Limiting

```python
from rest_framework.throttling import UserRateThrottle

class BurstRateThrottle(UserRateThrottle):
    rate = '100/hour'

class WorkItemViewSet(viewsets.ModelViewSet):
    throttle_classes = [BurstRateThrottle]
```

## Related Patterns

- See [authentication.md](authentication.md) for web auth
