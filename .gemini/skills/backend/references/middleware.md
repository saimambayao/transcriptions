# Django Middleware

Guide for custom middleware patterns.

## Basic Middleware

```python
# common/middleware.py
class OrganizationMiddleware:
    """Add organization to request."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.organization = request.user.organization
        else:
            request.organization = None

        response = self.get_response(request)
        return response

# settings.py
MIDDLEWARE = [
    # ... other middleware ...
    'common.middleware.OrganizationMiddleware',
]
```

## Request Processing

```python
class RequestLoggingMiddleware:
    """Log all requests."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before view
        import logging
        logger = logging.getLogger('requests')
        logger.info(f'{request.method} {request.path} by {request.user}')

        response = self.get_response(request)

        # After view
        logger.info(f'Response: {response.status_code}')
        return response
```

## Error Handling

```python
class ErrorHandlingMiddleware:
    """Handle errors gracefully."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        """Handle exceptions."""
        import logging
        logger = logging.getLogger('errors')
        logger.error(f'Error processing {request.path}: {exception}')
        
        # Return custom error page
        if isinstance(exception, PermissionDenied):
            return render(request, '403.html', status=403)
        return None
```

For signals, see [signals.md](signals.md).
