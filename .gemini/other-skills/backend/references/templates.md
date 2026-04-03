# Django Templates

Guide for Django template patterns, context processors, custom tags, and template organization for OBCMS.

## Base Template Pattern

```django
{# templates/base.html #}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}OBCMS{% endblock %}</title>

    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2/dist/tailwind.min.css" rel="stylesheet">
    {% block extra_css %}{% endblock %}
</head>
<body class="bg-gray-100">
    {% include 'partials/navbar.html' %}

    <main class="container mx-auto px-4 py-8">
        {% include 'partials/messages.html' %}

        {% block content %}{% endblock %}
    </main>

    {% include 'partials/footer.html' %}

    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    <script src="https://unpkg.com/alpinejs@3" defer></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

## Template Inheritance

```django
{# templates/communities/list.html #}
{% extends 'base.html' %}

{% block title %}Communities - OBCMS{% endblock %}

{% block content %}
<div class="bg-white rounded-lg shadow p-6">
    <h1 class="text-2xl font-bold mb-4">Communities</h1>

    {% include 'communities/partials/filters.html' %}

    <div class="mt-6">
        {% include 'communities/partials/list_table.html' %}
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script nonce="{{ request.csp_nonce }}">
    // Page-specific JavaScript
    console.log('Communities page loaded');
</script>
{% endblock %}
```

## Context Variables

```django
{# Accessing context in templates #}

{# User and organization #}
<p>Welcome, {{ user.get_full_name }}</p>
<p>Organization: {{ user.organization.name }}</p>

{# Object attributes #}
<h2>{{ community.name }}</h2>
<p>Region: {{ community.region.name }}</p>
<p>Population: {{ community.population|default:"N/A" }}</p>

{# Looping #}
{% for assessment in assessments %}
    <div class="assessment">
        <h3>{{ assessment.community.name }}</h3>
        <p>Date: {{ assessment.assessment_date }}</p>
    </div>
{% empty %}
    <p>No assessments found.</p>
{% endfor %}

{# Conditionals #}
{% if community.population > 1000 %}
    <span class="badge badge-large">Large Community</span>
{% elif community.population > 500 %}
    <span class="badge badge-medium">Medium Community</span>
{% else %}
    <span class="badge badge-small">Small Community</span>
{% endif %}
```

## Template Filters

```django
{# Built-in filters #}
{{ community.name|upper }}
{{ community.name|lower }}
{{ community.name|title }}
{{ community.description|truncatewords:50 }}
{{ assessment_date|date:"F j, Y" }}
{{ created_at|timesince }} ago
{{ budget|floatformat:2 }}
{{ budget|intcomma }}

{# Chaining filters #}
{{ community.name|upper|truncatewords:10 }}

{# Custom filter usage #}
{% load custom_filters %}
{{ amount|peso }}  {# Outputs: ₱1,234.56 #}
{{ phone|phone_format }}  {# Outputs: (123) 456-7890 #}
```

## Template Tags

```django
{# URL tag #}
<a href="{% url 'communities:detail' pk=community.pk %}">View</a>
<a href="{% url 'communities:update' pk=community.pk %}">Edit</a>

{# URL with query params #}
<a href="{% url 'communities:list' %}?region={{ region.code }}">Filter</a>

{# Static files #}
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
<link rel="stylesheet" href="{% static 'css/custom.css' %}">

{# Include tag #}
{% include 'partials/community_card.html' with community=community %}

{# With tag #}
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}

{# Cycle tag #}
{% for item in items %}
    <tr class="{% cycle 'row1' 'row2' %}">
        <td>{{ item.name }}</td>
    </tr>
{% endfor %}
```

## Forms in Templates

```django
{# Form rendering #}
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}

    {# Render entire form #}
    {{ form.as_p }}

    {# Or render fields individually #}
    <div class="mb-4">
        {{ form.name.label_tag }}
        {{ form.name }}
        {% if form.name.errors %}
            <p class="text-red-500 text-sm">{{ form.name.errors.0 }}</p>
        {% endif %}
    </div>

    <div class="mb-4">
        <label for="{{ form.region.id_for_label }}" class="block text-sm font-medium">
            {{ form.region.label }}
        </label>
        <select name="{{ form.region.html_name }}"
                id="{{ form.region.id_for_label }}"
                class="mt-1 block w-full rounded-md border-gray-300">
            {{ form.region }}
        </select>
        {{ form.region.errors }}
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
</form>

{# Non-field errors #}
{% if form.non_field_errors %}
    <div class="alert alert-error">
        {{ form.non_field_errors }}
    </div>
{% endif %}
```

## HTMX Templates

```django
{# HTMX-enabled links #}
<a href="{% url 'communities:list_partial' %}"
   hx-get="{% url 'communities:list_partial' %}"
   hx-target="#community-list"
   hx-swap="innerHTML"
   class="btn">
    Load Communities
</a>

{# HTMX forms #}
<form hx-post="{% url 'communities:create' %}"
      hx-target="#result"
      hx-swap="innerHTML">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
</form>

{# HTMX with indicators #}
<button hx-get="{% url 'api:data' %}"
        hx-indicator="#loading">
    Load Data
</button>
<div id="loading" class="htmx-indicator">
    Loading...
</div>
```

## Custom Template Tags

```python
# communities/templatetags/community_tags.py
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def peso(value):
    """Format number as Philippine Peso."""
    try:
        return f"₱{value:,.2f}"
    except (ValueError, TypeError):
        return value

@register.filter
def phone_format(value):
    """Format phone number."""
    if not value:
        return ''
    # Remove non-digits
    digits = ''.join(c for c in str(value) if c.isdigit())
    if len(digits) == 11:
        return f"+63 {digits[1:4]} {digits[4:7]} {digits[7:]}"
    return value

@register.simple_tag
def status_badge(status):
    """Render status badge."""
    colors = {
        'DRAFT': 'gray',
        'PENDING': 'yellow',
        'APPROVED': 'green',
        'REJECTED': 'red',
    }
    color = colors.get(status, 'gray')
    html = f'<span class="badge badge-{color}">{status}</span>'
    return mark_safe(html)

@register.inclusion_tag('partials/community_card.html')
def community_card(community):
    """Render community card."""
    return {'community': community}
```

```django
{# Using custom tags #}
{% load community_tags %}

<p>Budget: {{ program.budget|peso }}</p>
<p>Contact: {{ beneficiary.mobile|phone_format }}</p>
{% status_badge program.status %}
{% community_card community=community %}
```

## Context Processors

```python
# common/context_processors.py
def organization_context(request):
    """Add organization data to all templates."""
    if request.user.is_authenticated:
        return {
            'user_organization': request.user.organization,
            'organization_name': request.user.organization.name,
        }
    return {}

def site_settings(request):
    """Add site-wide settings."""
    return {
        'SITE_NAME': 'OBCMS',
        'SUPPORT_EMAIL': 'support@obcms.gov.ph',
        'VERSION': '1.0.0',
    }
```

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'common.context_processors.organization_context',
                'common.context_processors.site_settings',
            ],
        },
    },
]
```

## Partial Templates

```django
{# partials/messages.html #}
{% if messages %}
    <div class="messages">
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    </div>
{% endif %}

{# partials/pagination.html #}
{% if is_paginated %}
    <nav class="pagination">
        {% if page_obj.has_previous %}
            <a href="?page=1">First</a>
            <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
        {% endif %}

        <span class="current-page">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
        </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">Next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
        {% endif %}
    </nav>
{% endif %}
```

## Template Organization

```
templates/
├── base.html                   # Base template
├── partials/                   # Reusable components
│   ├── navbar.html
│   ├── footer.html
│   ├── messages.html
│   └── pagination.html
├── communities/                # App templates
│   ├── list.html
│   ├── detail.html
│   ├── create.html
│   ├── update.html
│   └── partials/               # App-specific partials
│       ├── filters.html
│       ├── list_table.html
│       └── community_card.html
├── mana/
│   ├── assessment_list.html
│   └── partials/
└── components/                 # Reusable UI components
    ├── stat_card.html
    ├── data_table.html
    └── modal.html
```

This provides the foundation for Django templates in OBCMS. For REST API responses, see [apis.md](apis.md).
