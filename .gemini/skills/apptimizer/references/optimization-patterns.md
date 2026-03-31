# OBCMS Optimization Patterns

Common optimization patterns across all OBCMS domains.

## Database Patterns

### Pattern 1: select_related() for ForeignKey
```python
# ❌ N+1 queries
communities = Community.objects.all()
for community in communities:
    print(community.municipality.name)  # Queries DB for each!

# ✅ One query with JOIN
communities = Community.objects.select_related('municipality').all()
for community in communities:
    print(community.municipality.name)  # No additional queries
```

### Pattern 2: prefetch_related() for Reverse FK
```python
# ❌ N+1 queries
communities = Community.objects.all()
for community in communities:
    households = community.households.all()  # Queries DB for each!

# ✅ Two queries total
communities = Community.objects.prefetch_related('households').all()
for community in communities:
    households = community.households.all()  # From cache
```

### Pattern 3: Database Indexing
```python
class Task(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.CharField(max_length=50, db_index=True)
```

## Frontend Patterns

### Pattern 4: Pagination
```python
# View
from django.core.paginator import Paginator

def list_communities(request):
    all_communities = Community.objects.filter(organization=request.user.organization)
    paginator = Paginator(all_communities, 25)
    page_number = request.GET.get('page', 1)
    communities = paginator.get_page(page_number)
    return render(request, 'list.html', {'communities': communities})
```

```django
<!-- Template -->
{% for community in communities %}
    ...
{% endfor %}

<div class="pagination">
    {% if communities.has_previous %}
        <a hx-get="?page={{ communities.previous_page_number }}">Previous</a>
    {% endif %}
    {% if communities.has_next %}
        <a hx-get="?page={{ communities.next_page_number }}">Next</a>
    {% endif %}
</div>
```

### Pattern 5: HTMX Request Consolidation
```django
<!-- ❌ Multiple requests -->
<div hx-get="/api/stats/" hx-trigger="load"></div>
<div hx-get="/api/recent/" hx-trigger="load"></div>

<!-- ✅ One request -->
<div hx-get="/api/dashboard/" hx-trigger="load">
    <!-- Returns stats + recent in one response -->
</div>
```

## Backend Patterns

### Pattern 6: View-Level Caching
```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # 5 minutes
def dashboard(request):
    # Expensive operations
    stats = compute_stats()
    return render(request, 'dashboard.html', {'stats': stats})
```

### Pattern 7: DRF Serializer Optimization
```python
# ❌ Slow serializer
class CommunitySerializer(serializers.ModelSerializer):
    municipality_name = serializers.CharField(source='municipality.name')  # N+1!

# ✅ Optimized with select_related in view
class CommunityViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Community.objects.select_related('municipality').filter(organization=self.request.user.organization)
```

## AI Patterns

### Pattern 8: Redis Caching for AI Responses
```python
import redis
from django.core.cache import cache

def query_obcai(query, organization):
    cache_key = f"obcai:{organization.id}:{hash(query)}"
    cached_response = cache.get(cache_key)
    if cached_response:
        return cached_response
    
    response = coordinator.query(query, organization=organization)
    cache.set(cache_key, response, 3600)  # 1 hour
    return response
```

### Pattern 9: Token Usage Reduction
```python
# ❌ Sending full context every time
response = coordinator.query(f"User: {user.username}, Org: {org.name}, Query: {query}")

# ✅ Minimal context
response = coordinator.query(query, organization_id=org.id)
```
