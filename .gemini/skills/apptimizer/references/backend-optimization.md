# Backend Optimization Guide

Django view caching, DRF serializer optimization, async processing.

## View-Level Caching

### 1. Cache Entire View (@cache_page)

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # Cache for 5 minutes
def dashboard(request):
    stats = compute_expensive_stats()
    return render(request, 'dashboard.html', {'stats': stats})
```

### 2. Cache Specific Data

```python
from django.core.cache import cache

def get_dashboard_stats(organization):
    cache_key = f"dashboard_stats:{organization.id}"
    stats = cache.get(cache_key)
    if not stats:
        stats = compute_expensive_stats(organization)
        cache.set(cache_key, stats, 300)  # 5 min
    return stats
```

### 3. Cache Invalidation

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Community)
def invalidate_dashboard_cache(sender, instance, **kwargs):
    cache_key = f"dashboard_stats:{instance.organization.id}"
    cache.delete(cache_key)
```

## DRF Serializer Optimization

### 1. Avoid N+1 in Serializers

```python
# ❌ N+1 queries
class CommunitySerializer(serializers.ModelSerializer):
    municipality_name = serializers.CharField(source='municipality.name')

# ✅ Optimize in ViewSet
class CommunityViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Community.objects.select_related('municipality')
```

### 2. Use SerializerMethodField Sparingly

```python
# ❌ Expensive method called for each object
class CommunitySerializer(serializers.ModelSerializer):
    household_count = serializers.SerializerMethodField()
    
    def get_household_count(self, obj):
        return obj.households.count()  # Query for each!

# ✅ Annotate in queryset
class CommunityViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Community.objects.annotate(household_count=Count('households'))

class CommunitySerializer(serializers.ModelSerializer):
    household_count = serializers.IntegerField(read_only=True)
```

### 3. Limit Serialized Fields

```python
# ❌ Serializing all fields
class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

# ✅ Only fields needed by frontend
class CommunityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['id', 'name', 'municipality_name']
```

## Async Processing (Celery)

### 1. Move Long Tasks to Background

```python
# tasks.py
from celery import shared_task

@shared_task
def generate_report(assessment_id):
    assessment = Assessment.objects.get(id=assessment_id)
    # Generate PDF (5-10 seconds)
    pdf = create_pdf_report(assessment)
    return pdf.save()

# views.py
def request_report(request, assessment_id):
    generate_report.delay(assessment_id)
    return JsonResponse({'status': 'Report generation started'})
```

### 2. Batch Processing

```python
@shared_task
def send_notification_batch(user_ids):
    users = User.objects.filter(id__in=user_ids)
    for user in users:
        send_email(user)
```

## Response Compression

```python
# settings/production.py
MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',  # Add this
    ...
]
```

## Backend Performance Checklist

- [ ] Cache expensive views (@cache_page)
- [ ] Cache database query results
- [ ] Implement cache invalidation
- [ ] Optimize DRF serializers (select_related in queryset)
- [ ] Use annotate() instead of SerializerMethodField
- [ ] Move long tasks to Celery
- [ ] Enable GZip compression
- [ ] Use only/defer for large models
