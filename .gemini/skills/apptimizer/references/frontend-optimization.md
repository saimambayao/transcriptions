# Frontend Optimization Guide

HTMX optimization, pagination, asset optimization, lazy loading.

## HTMX Optimization

### 1. Consolidate Requests

```django
<!-- ❌ Multiple requests -->
<div hx-get="/api/stats/"></div>
<div hx-get="/api/recent-tasks/"></div>
<div hx-get="/api/community-count/"></div>

<!-- ✅ One request -->
<div hx-get="/api/dashboard/"></div>
```

### 2. Use hx-trigger Wisely

```django
<!-- ❌ Poll too frequently -->
<div hx-get="/api/updates/" hx-trigger="every 1s"></div>

<!-- ✅ Reasonable polling -->
<div hx-get="/api/updates/" hx-trigger="every 30s"></div>

<!-- ✅ Even better: Only poll when page visible -->
<div hx-get="/api/updates/" hx-trigger="every 30s[document.visibilityState === 'visible']"></div>
```

### 3. Use hx-swap Efficiently

```django
<!-- ✅ Swap only what changes -->
<button hx-delete="/api/tasks/123/" hx-target="#task-123" hx-swap="outerHTML">
    Delete
</button>

<!-- ❌ Re-render entire list -->
<button hx-delete="/api/tasks/123/" hx-target="#task-list" hx-swap="innerHTML">
    Delete
</button>
```

## Pagination

### 1. Server-Side Pagination

```python
from django.core.paginator import Paginator

def list_communities(request):
    all_communities = Community.objects.filter(organization=request.user.organization)
    paginator = Paginator(all_communities, 25)  # 25 per page
    page_number = request.GET.get('page', 1)
    communities = paginator.get_page(page_number)
    return render(request, 'list.html', {'communities': communities})
```

### 2. HTMX-Compatible Pagination

```django
<div id="community-list">
    {% for community in communities %}
        <div>{{ community.name }}</div>
    {% endfor %}
</div>

<div class="pagination">
    {% if communities.has_previous %}
        <button hx-get="?page={{ communities.previous_page_number }}" hx-target="#community-list">
            Previous
        </button>
    {% endif %}
    <span>Page {{ communities.number }} of {{ communities.paginator.num_pages }}</span>
    {% if communities.has_next %}
        <button hx-get="?page={{ communities.next_page_number }}" hx-target="#community-list">
            Next
        </button>
    {% endif %}
</div>
```

## Asset Optimization

### 1. CSS Optimization

```bash
# Purge unused Tailwind CSS
npm run build  # Uses PurgeCSS to remove unused classes
```

### 2. Minify CSS/JS (Django Compressor)

```python
# settings/production.py
INSTALLED_APPS += ['compressor']

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
```

```django
{% load compress %}

{% compress css %}
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
{% endcompress %}
```

### 3. Serve Static Files via CDN (Production)

```python
# settings/production.py
STATIC_URL = 'https://cdn.example.com/static/'
```

## Lazy Loading

### 1. Lazy Load Images

```django
<img src="{{ community.image.url }}" loading="lazy" alt="{{ community.name }}">
```

### 2. Lazy Load HTMX Content

```django
<!-- Load content only when visible -->
<div hx-get="/api/heavy-content/" hx-trigger="revealed"></div>
```

### 3. Infinite Scroll

```django
<div id="community-list">
    {% for community in communities %}
        <div>{{ community.name }}</div>
    {% endfor %}
</div>

<!-- Load more when scrolled into view -->
{% if communities.has_next %}
    <div hx-get="?page={{ communities.next_page_number }}" hx-trigger="revealed" hx-swap="afterend"></div>
{% endif %}
```

## Frontend Performance Checklist

- [ ] Consolidate HTMX requests
- [ ] Implement pagination (25-50 items/page)
- [ ] Use lazy loading for images
- [ ] Minify CSS/JS in production
- [ ] Purge unused Tailwind CSS
- [ ] Use CDN for static files
- [ ] Optimize poll intervals
- [ ] Use hx-swap efficiently
