# Django REST Framework APIs

Guide for building REST APIs with Django REST Framework for OBCMS.

## ViewSet Patterns

```python
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class CommunityViewSet(viewsets.ModelViewSet):
    """API endpoints for communities."""
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['region', 'municipality', 'barangay']
    search_fields = ['name', 'barangay__name']
    ordering_fields = ['name', 'population', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        return Community.objects.filter(
            organization=self.request.user.organization
        ).select_related('region', 'municipality', 'barangay')

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user,
            updated_by=self.request.user
        )

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    @action(detail=True, methods=['get'])
    def assessments(self, request, pk=None):
        """Get assessments for this community."""
        community = self.get_object()
        assessments = community.assessment_set.all()
        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get community statistics."""
        qs = self.get_queryset()
        stats = {
            'total': qs.count(),
            'by_region': qs.values('region__name').annotate(count=Count('id')),
            'total_population': qs.aggregate(total=Sum('population'))['total']
        }
        return Response(stats)
```

## Router Configuration

```python
# urls.py
from rest_framework.routers import DefaultRouter
from .views import CommunityViewSet, AssessmentViewSet, ProgramViewSet

router = DefaultRouter()
router.register(r'communities', CommunityViewSet, basename='community')
router.register(r'assessments', AssessmentViewSet, basename='assessment')
router.register(r'programs', ProgramViewSet, basename='program')

urlpatterns = router.urls
```

## Custom Actions

```python
@action(detail=True, methods=['post'])
def approve(self, request, pk=None):
    """Approve an assessment."""
    assessment = self.get_object()
    assessment.status = 'APPROVED'
    assessment.approved_by = request.user
    assessment.approved_at = timezone.now()
    assessment.save()
    return Response({'status': 'approved'})

@action(detail=False, methods=['get'], url_path='recent')
def recent_items(self, request):
    """Get recently created items."""
    recent = self.get_queryset()[:10]
    serializer = self.get_serializer(recent, many=True)
    return Response(serializer.data)
```

## Pagination

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# Custom paginator
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class CommunityViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
```

## Filtering

```python
# Install django-filter
# pip install django-filter

from django_filters import rest_framework as filters

class CommunityFilter(filters.FilterSet):
    min_population = filters.NumberFilter(field_name='population', lookup_expr='gte')
    max_population = filters.NumberFilter(field_name='population', lookup_expr='lte')
    created_after = filters.DateFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Community
        fields = ['region', 'municipality', 'min_population', 'max_population']

class CommunityViewSet(viewsets.ModelViewSet):
    filterset_class = CommunityFilter
```

## Response Formats

```python
# Success response
return Response({
    'status': 'success',
    'data': serializer.data
}, status=status.HTTP_200_OK)

# Error response
return Response({
    'status': 'error',
    'message': 'Invalid data provided',
    'errors': serializer.errors
}, status=status.HTTP_400_BAD_REQUEST)

# Custom status codes
return Response(data, status=status.HTTP_201_CREATED)
return Response(status=status.HTTP_204_NO_CONTENT)
return Response(errors, status=status.HTTP_404_NOT_FOUND)
```

For serializer patterns, see [serializers.md](serializers.md).
