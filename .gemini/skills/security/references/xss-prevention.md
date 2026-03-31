# XSS Prevention

Cross-Site Scripting (XSS) prevention in OBCMS using Django template escaping, input sanitization, and Content Security Policy.

## Template Escaping

Django automatically escapes all template variables to prevent XSS attacks:

```django
{# Auto-escaped by default #}
{{ user_input }}
{{ task.description }}
{{ comment.text }}

{# Manual escape for extra safety #}
{{ untrusted_data|escape }}

{# Mark safe - ONLY for trusted HTML #}
{{ admin_generated_html|safe }}

{# NEVER mark user input as safe #}
{# ❌ WRONG: {{ user_input|safe }} #}
```

## Input Sanitization

Sanitize user input before storing in the database:

```python
from django.utils.html import escape, strip_tags

def clean_user_input(raw_input):
    """Remove HTML tags and escape special characters"""
    # Strip all HTML tags
    cleaned = strip_tags(raw_input)
    # Escape special characters
    return escape(cleaned)

# In views or forms
def create_task(request):
    title = clean_user_input(request.POST.get('title'))
    description = clean_user_input(request.POST.get('description'))
    Task.objects.create(title=title, description=description)
```

## Rich Text Handling

For user-submitted rich text (e.g., WYSIWYG editors), use bleach to allow only safe HTML:

```python
import bleach

ALLOWED_TAGS = ['p', 'br', 'strong', 'em', 'u', 'ul', 'ol', 'li', 'a']
ALLOWED_ATTRIBUTES = {'a': ['href', 'title']}

def sanitize_rich_text(html):
    """Sanitize user-submitted HTML"""
    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        strip=True
    )

# In forms
class ArticleForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data['content']
        return sanitize_rich_text(content)
```

## URL Validation

Validate and sanitize URLs to prevent javascript: and data: URL attacks:

```python
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_safe_url(url):
    """Ensure URL is safe (http/https only)"""
    validator = URLValidator(schemes=['http', 'https'])
    try:
        validator(url)
        return url
    except ValidationError:
        raise ValidationError("Invalid or unsafe URL")

# In views
redirect_url = validate_safe_url(request.GET.get('next', '/'))
```

## JSON Response Escaping

When returning JSON with user data, Django Rest Framework handles escaping automatically:

```python
from rest_framework.response import Response

def api_view(request):
    # DRF automatically escapes data
    return Response({
        'message': user_input,  # Safely escaped
        'tasks': Task.objects.filter(user=request.user).values()
    })
```

## Template Context Processors

Ensure context processors don't expose unsafe data:

```python
# ❌ WRONG - Exposing raw user input
def bad_context_processor(request):
    return {
        'user_search': request.GET.get('q')  # Unsafe!
    }

# ✅ CORRECT - Escape user input
from django.utils.html import escape

def safe_context_processor(request):
    return {
        'user_search': escape(request.GET.get('q', ''))
    }
```

## Content Security Policy (CSP)

**For comprehensive CSP implementation, see [csp.md](csp.md).**

CSP is **mandatory** for all OBCMS code (GEMINI.md Rule 12). It provides an additional layer of XSS protection by controlling which scripts and styles can execute.

Key CSP requirements:
- No inline scripts without nonces
- No inline styles without nonces
- No inline event handlers (onclick, onload, etc.)
- Use HTMX for dynamic interactions
- Use Tailwind for styling

**See [csp.md](csp.md) for complete CSP implementation patterns, HTMX integration, and debugging guides.**

## Testing XSS Prevention

```python
from django.test import TestCase

class XSSPreventionTest(TestCase):
    def test_xss_in_template(self):
        """Verify XSS payload is escaped"""
        xss_payload = '<script>alert("XSS")</script>'
        response = self.client.post('/comments/', {'text': xss_payload})

        # Verify payload is escaped in HTML
        self.assertContains(response, '&lt;script&gt;')
        self.assertNotContains(response, '<script>alert')

    def test_javascript_url_blocked(self):
        """Verify javascript: URLs are rejected"""
        response = self.client.post('/links/', {
            'url': 'javascript:alert("XSS")'
        })
        self.assertEqual(response.status_code, 400)
```

## XSS Prevention Checklist

- [ ] All user input is escaped in templates ({{ variable }})
- [ ] Never use |safe on user input
- [ ] Rich text is sanitized with bleach
- [ ] URLs are validated (http/https only)
- [ ] Context processors escape user data
- [ ] JSON responses use DRF (auto-escaping)
- [ ] CSP is configured and enforced (see csp.md)
- [ ] No inline scripts without nonces
- [ ] XSS tests added for user input fields
