"""
Complete DRF ViewSet Template with OBCMS Patterns

Copy this template for REST API endpoints.
"""

from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Sum, Avg
from .models import TODOModelName
from .serializers import TODOModelNameSerializer


class TODOModelNameViewSet(viewsets.ModelViewSet):
    """
    API endpoints for TODOModelName.
    
    List: GET /api/todomodelnames/
    Create: POST /api/todomodelnames/
    Retrieve: GET /api/todomodelnames/{id}/
    Update: PUT/PATCH /api/todomodelnames/{id}/
    Delete: DELETE /api/todomodelnames/{id}/
    """
    
    serializer_class = TODOModelNameSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Filtering and search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'organization']  # TODO: Add filterable fields
    search_fields = ['name', 'description']  # TODO: Add searchable fields
    ordering_fields = ['name', 'created_at', 'updated_at']  # TODO: Add sortable fields
    ordering = ['-created_at']
    
    # Pagination
    # pagination_class = StandardResultsSetPagination  # TODO: Uncomment if custom pagination
    
    def get_queryset(self):
        """
        Filter queryset by user's organization.
        Exclude soft-deleted records.
        Use select_related/prefetch_related for performance.
        """
        qs = TODOModelName.objects.filter(
            organization=self.request.user.organization,
            deleted_at__isnull=True
        )
        
        # TODO: Add select_related for foreign keys
        # qs = qs.select_related('parent', 'category')
        
        # TODO: Add prefetch_related for reverse relationships
        # qs = qs.prefetch_related('items', 'tags')
        
        return qs
    
    def perform_create(self, serializer):
        """Set organization and audit fields on create."""
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user,
            updated_by=self.request.user
        )
    
    def perform_update(self, serializer):
        """Update audit fields on update."""
        serializer.save(updated_by=self.request.user)
    
    def perform_destroy(self, instance):
        """Soft delete instead of hard delete."""
        instance.delete(user=self.request.user)
    
    # ========================================================================
    # CUSTOM ACTIONS
    # ========================================================================
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """
        Get aggregate statistics.
        
        GET /api/todomodelnames/statistics/
        """
        qs = self.get_queryset()
        
        stats = {
            'total': qs.count(),
            'by_status': list(
                qs.values('status')
                .annotate(count=Count('id'))
                .order_by('-count')
            ),
            # TODO: Add custom aggregations
            # 'total_amount': qs.aggregate(total=Sum('amount'))['total'],
            # 'average_score': qs.aggregate(avg=Avg('score'))['avg'],
        }
        
        return Response(stats)
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """
        Approve a record.
        
        POST /api/todomodelnames/{id}/approve/
        """
        instance = self.get_object()
        
        # TODO: Add approval logic
        # if instance.status != 'PENDING':
        #     return Response(
        #         {'error': 'Only pending records can be approved'},
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        
        instance.status = 'APPROVED'
        instance.updated_by = request.user
        instance.save()
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def export(self, request):
        """
        Export data as CSV.
        
        GET /api/todomodelnames/export/
        """
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['ID', 'Name', 'Status', 'Created'])  # TODO: Customize headers
        
        for obj in self.get_queryset():
            writer.writerow([obj.id, obj.name, obj.status, obj.created_at])  # TODO: Customize data
        
        return response
    
    # TODO: Add more custom actions as needed
    # @action(detail=True, methods=['post'])
    # def custom_action(self, request, pk=None):
    #     """Custom action."""
    #     instance = self.get_object()
    #     # Your logic here
    #     return Response({'status': 'success'})
