# Security Pattern Detection

Pattern detection rules for identifying security vulnerabilities in OBCMS code.

## Table of Contents

1. [CSP Violations](#csp-violations)
2. [Multi-Tenant Data Leak Patterns](#multi-tenant-data-leak-patterns)
3. [XSS Vulnerability Patterns](#xss-vulnerability-patterns)
4. [SQL Injection Patterns](#sql-injection-patterns)
5. [Authentication & Authorization Issues](#authentication--authorization-issues)
6. [CSRF Protection Issues](#csrf-protection-issues)
7. [Sensitive Data Exposure](#sensitive-data-exposure)

---

## CSP Violations

**Severity**: High
**GEMINI.md Rule**: Rule 12 - CSP Compliance is Mandatory

### Pattern 1: Inline Script Without Nonce

**Detection Pattern**:
```regex
<script>(?!.*nonce=)
```

**Example Violation**:
```django
{# ❌ CRITICAL: Inline script without nonce #}
<script>
    console.log('No nonce!');
</script>
```

**Remediation**:
```django
{# ✅ CORRECT: Inline script with nonce #}
<script nonce="{{ request.csp_nonce }}">
    console.log('Has nonce!');
</script>
```

### Pattern 2: Inline Style Without Nonce

**Detection Pattern**:
```regex
<style>(?!.*nonce=)
```

**Example Violation**:
```django
{# ❌ CRITICAL: Inline style without nonce #}
<style>
    .custom { color: red; }
</style>
```

**Remediation**:
```django
{# ✅ CORRECT: Inline style with nonce #}
<style nonce="{{ request.csp_nonce }}">
    .custom { color: red; }
</style>
```

### Pattern 3: Inline Event Handlers

**Detection Pattern**:
```regex
\s(onclick|onload|onsubmit|onerror|onchange)=["']
```

**Example Violation**:
```django
{# ❌ CRITICAL: Inline event handler #}
<button onclick="deleteTask()">Delete</button>
```

**Remediation**:
```django
{# ✅ CORRECT: Use HTMX instead #}
<button hx-delete="/api/tasks/123/">Delete</button>
```

### Pattern 4: Inline Style Attributes

**Detection Pattern**:
```regex
\sstyle=["'][^"']+["']
```

**Example Violation**:
```django
{# ❌ HIGH: Inline style attribute #}
<div style="color: red; background: blue;">Content</div>
```

**Remediation**:
```django
{# ✅ CORRECT: Use Tailwind classes #}
<div class="text-red-500 bg-blue-500">Content</div>
```

---

## Multi-Tenant Data Leak Patterns

**Severity**: Critical
**Impact**: Cross-organization data exposure

### Pattern 1: Missing Organization Filter in QuerySet

**Detection Pattern**:
```python
# Look for .all() or .filter() without organization parameter
Model.objects.all()
Model.objects.filter(...) # where organization not in filter
```

**Example Violation**:
```python
# ❌ CRITICAL: No organization filter
def list_tasks(request):
    tasks = Task.objects.all()  # LEAKS ALL ORGANIZATIONS' DATA!
    return render(request, 'tasks.html', {'tasks': tasks})
```

**Remediation**:
```python
# ✅ CORRECT: Filter by organization
def list_tasks(request):
    tasks = Task.objects.filter(organization=request.user.organization)
    return render(request, 'tasks.html', {'tasks': tasks})
```

### Pattern 2: Missing Organization Filter in get_object_or_404

**Detection Pattern**:
```python
get_object_or_404(Model, id=...) # where organization not in kwargs
```

**Example Violation**:
```python
# ❌ CRITICAL: No organization check
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # CAN ACCESS OTHER ORG'S TASKS!
    return render(request, 'task.html', {'task': task})
```

**Remediation**:
```python
# ✅ CORRECT: Include organization in lookup
def task_detail(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        organization=request.user.organization
    )
    return render(request, 'task.html', {'task': task})
```

### Pattern 3: Missing Organization Filter in DRF ViewSet

**Detection Pattern**:
```python
class SomeViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()  # Static queryset
    # OR
    def get_queryset(self):
        return Model.objects.all()  # No org filter
```

**Example Violation**:
```python
# ❌ CRITICAL: No organization scoping
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # LEAKS ALL DATA!
    serializer_class = TaskSerializer
```

**Remediation**:
```python
# ✅ CORRECT: Override get_queryset with org filter
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(
            organization=self.request.user.organization
        )
```

### Pattern 4: Missing Organization Assignment in Create

**Detection Pattern**:
```python
# Look for save() or create() without organization assignment
Model.objects.create(...)  # organization not in kwargs
form.save()  # organization not set
```

**Example Violation**:
```python
# ❌ CRITICAL: No organization assignment
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()  # ORGANIZATION IS NULL OR WRONG!
        return redirect('tasks')
```

**Remediation**:
```python
# ✅ CORRECT: Assign organization
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.organization = request.user.organization
        task.save()
        return redirect('tasks')
```

### Pattern 5: ForeignKey Choices Not Limited by Organization

**Detection Pattern**:
```python
# In forms, look for ForeignKey fields without queryset override
class SomeForm(forms.ModelForm):
    some_field = forms.ModelChoiceField(queryset=Model.objects.all())
```

**Example Violation**:
```python
# ❌ CRITICAL: Shows users from all organizations
class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all()  # LEAKS USER LIST!
    )
```

**Remediation**:
```python
# ✅ CORRECT: Limit to same organization
class TaskForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(
            organization=user.organization
        )
```

---

## XSS Vulnerability Patterns

**Severity**: Critical/High

### Pattern 1: User Input Marked as Safe

**Detection Pattern**:
```django
{{ variable|safe }}  # where variable contains user input
```

**Example Violation**:
```django
{# ❌ CRITICAL: User input marked safe #}
{{ user_comment.text|safe }}  {# Allows XSS! #}
```

**Remediation**:
```django
{# ✅ CORRECT: Auto-escaped or explicitly escaped #}
{{ user_comment.text }}  {# Auto-escaped #}
{{ user_comment.text|escape }}  {# Explicitly escaped #}
```

### Pattern 2: Unescaped User Input in JavaScript

**Detection Pattern**:
```javascript
var data = "{{ user_input }}";  // Unescaped in JS context
```

**Example Violation**:
```django
<script nonce="{{ request.csp_nonce }}">
    {# ❌ CRITICAL: XSS in JavaScript context #}
    var search = "{{ request.GET.q }}";
</script>
```

**Remediation**:
```django
<script nonce="{{ request.csp_nonce }}">
    {# ✅ CORRECT: Use escapejs filter #}
    var search = "{{ request.GET.q|escapejs }}";
</script>
```

### Pattern 3: Rendering Unescaped HTML from Database

**Detection Pattern**:
```python
# Look for render_to_string or mark_safe on user-generated content
mark_safe(user_content)
```

**Example Violation**:
```python
# ❌ CRITICAL: Marking user content as safe
from django.utils.safestring import mark_safe

def render_comment(comment):
    return mark_safe(comment.text)  # XSS if user enters <script>!
```

**Remediation**:
```python
# ✅ CORRECT: Sanitize or escape user content
import bleach

def render_comment(comment):
    clean_text = bleach.clean(
        comment.text,
        tags=['p', 'br', 'strong', 'em'],
        strip=True
    )
    return mark_safe(clean_text)  # Now safe
```

---

## SQL Injection Patterns

**Severity**: Critical

### Pattern 1: Raw SQL with String Formatting

**Detection Pattern**:
```python
cursor.execute("SELECT * FROM table WHERE id = %s" % value)
cursor.execute(f"SELECT * FROM table WHERE id = {value}")
cursor.execute("... WHERE id = " + value)
```

**Example Violation**:
```python
# ❌ CRITICAL: SQL injection via string formatting
def get_task_raw(task_id):
    cursor.execute(f"SELECT * FROM tasks WHERE id = {task_id}")
    # If task_id = "1 OR 1=1", returns all tasks!
```

**Remediation**:
```python
# ✅ CORRECT: Use parameterized query
def get_task_raw(task_id):
    cursor.execute("SELECT * FROM tasks WHERE id = %s", [task_id])
```

### Pattern 2: Raw SQL in ORM extra()

**Detection Pattern**:
```python
Model.objects.extra(where=[f"field = {value}"])
```

**Example Violation**:
```python
# ❌ CRITICAL: SQL injection in extra()
tasks = Task.objects.extra(
    where=[f"status = '{user_status}'"]
)
```

**Remediation**:
```python
# ✅ CORRECT: Use parameterized extra() or Q objects
tasks = Task.objects.extra(
    where=["status = %s"],
    params=[user_status]
)

# ✅ BETTER: Use Django ORM
tasks = Task.objects.filter(status=user_status)
```

---

## Authentication & Authorization Issues

**Severity**: Critical/High

### Pattern 1: Missing Login Required Decorator

**Detection Pattern**:
```python
# Views that access user data without @login_required
def some_view(request):
    user_data = request.user.some_field  # No @login_required!
```

**Example Violation**:
```python
# ❌ CRITICAL: No authentication check
def my_tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    # If user not authenticated, crashes or shows wrong data!
```

**Remediation**:
```python
# ✅ CORRECT: Require login
from django.contrib.auth.decorators import login_required

@login_required
def my_tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user)
```

### Pattern 2: Missing Permission Checks

**Detection Pattern**:
```python
# Views that modify/delete data without permission checks
def delete_task(request, task_id):
    task.delete()  # No permission check!
```

**Example Violation**:
```python
# ❌ CRITICAL: Anyone can delete any task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()  # NO PERMISSION CHECK!
    return redirect('tasks')
```

**Remediation**:
```python
# ✅ CORRECT: Check permissions
from common.decorators import role_required

@login_required
@role_required('task_manager')
def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        organization=request.user.organization
    )
    # Verify user can delete
    if task.created_by != request.user and not request.user.has_role('admin'):
        return HttpResponseForbidden()

    task.delete()
    return redirect('tasks')
```

### Pattern 3: API Endpoints Without Authentication

**Detection Pattern**:
```python
# DRF views without permission_classes
class SomeViewSet(viewsets.ModelViewSet):
    # No permission_classes defined!
```

**Example Violation**:
```python
# ❌ CRITICAL: Unauthenticated API access
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # ANYONE CAN ACCESS!
```

**Remediation**:
```python
# ✅ CORRECT: Require authentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(
            organization=self.request.user.organization
        )
```

---

## CSRF Protection Issues

**Severity**: High

### Pattern 1: CSRF Exempt on Unsafe Methods

**Detection Pattern**:
```python
@csrf_exempt
def some_view(request):
    if request.method == 'POST':  # Unsafe!
```

**Example Violation**:
```python
# ❌ HIGH: CSRF exempt on POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        # CSRF attack possible!
```

**Remediation**:
```python
# ✅ CORRECT: Remove @csrf_exempt, use CSRF token
def create_task(request):
    if request.method == 'POST':
        # Django automatically checks CSRF token
```

### Pattern 2: Missing CSRF Token in Forms

**Detection Pattern**:
```django
<form method="post">
    {# No {% csrf_token %} #}
</form>
```

**Example Violation**:
```django
{# ❌ HIGH: Missing CSRF token #}
<form method="post" action="/tasks/create/">
    <input type="text" name="title">
    <button type="submit">Create</button>
</form>
```

**Remediation**:
```django
{# ✅ CORRECT: Include CSRF token #}
<form method="post" action="/tasks/create/">
    {% csrf_token %}
    <input type="text" name="title">
    <button type="submit">Create</button>
</form>
```

---

## Sensitive Data Exposure

**Severity**: Critical/High

### Pattern 1: Passwords in Logs

**Detection Pattern**:
```python
logger.info(f"User {username} password: {password}")
print(f"Password: {password}")
```

**Example Violation**:
```python
# ❌ CRITICAL: Logging passwords
import logging
logger = logging.getLogger(__name__)

def create_user(username, password):
    logger.info(f"Creating user {username} with password {password}")  # LEAKED!
```

**Remediation**:
```python
# ✅ CORRECT: Never log passwords
def create_user(username, password):
    logger.info(f"Creating user {username}")  # Password omitted
```

### Pattern 2: Hardcoded Secrets

**Detection Pattern**:
```python
API_KEY = "sk-1234567890abcdef"
SECRET_KEY = 'hardcoded-secret'
```

**Example Violation**:
```python
# ❌ CRITICAL: Hardcoded API key
GEMINI_API_KEY = "AIzaSy..."  # EXPOSED IN VERSION CONTROL!
```

**Remediation**:
```python
# ✅ CORRECT: Load from environment
import os
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
```

### Pattern 3: Exposing Sensitive Data in API Responses

**Detection Pattern**:
```python
# Serializers that expose password_hash, secret_key, etc.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Exposes password!
```

**Example Violation**:
```python
# ❌ CRITICAL: Exposing all user fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Includes password_hash!
```

**Remediation**:
```python
# ✅ CORRECT: Explicitly list safe fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        # Password excluded!
```

---

## Audit Checklist

When auditing for security issues, verify:

- [ ] All templates use CSP-compliant patterns (nonces, no inline handlers)
- [ ] All queries filter by `organization=request.user.organization`
- [ ] All `get_object_or_404` calls include organization parameter
- [ ] All user input is escaped in templates
- [ ] No user input is marked as |safe
- [ ] All raw SQL uses parameterized queries
- [ ] All views require authentication (@login_required)
- [ ] All sensitive operations check permissions
- [ ] All POST/PUT/DELETE forms include {% csrf_token %}
- [ ] No passwords or secrets in logs or version control
- [ ] API endpoints require authentication
- [ ] Serializers don't expose sensitive fields
