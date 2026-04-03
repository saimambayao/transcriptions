#!/usr/bin/env python3
"""
Generate DRF ViewSet and Serializer boilerplate.

Usage:
    ./create_api.py <app_name> <model_name>
    ./create_api.py communities Community
"""

import sys

SERIALIZER_TEMPLATE = '''from rest_framework import serializers
from .models import {model_name}


class {model_name}Serializer(serializers.ModelSerializer):
    """Serializer for {model_name}."""
    
    organization_name = serializers.CharField(source='organization.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    
    class Meta:
        model = {model_name}
        fields = [
            'id', 'name', 'description', 'status',
            'organization', 'organization_name',
            'created_by_name', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'created_by']
    
    def validate(self, data):
        """Add custom validation."""
        # TODO: Add validation logic
        return data
'''

VIEWSET_TEMPLATE = '''from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import {model_name}
from .serializers import {model_name}Serializer


class {model_name}ViewSet(viewsets.ModelViewSet):
    """API endpoints for {model_name}."""
    
    serializer_class = {model_name}Serializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'organization']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """Filter by user's organization."""
        return {model_name}.objects.filter(
            organization=self.request.user.organization,
            deleted_at__isnull=True
        ).select_related('organization', 'created_by')
    
    def perform_create(self, serializer):
        """Set organization and audit fields."""
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user,
            updated_by=self.request.user
        )
    
    def perform_update(self, serializer):
        """Update audit fields."""
        serializer.save(updated_by=self.request.user)
    
    def perform_destroy(self, instance):
        """Soft delete."""
        instance.delete(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get statistics."""
        qs = self.get_queryset()
        stats = {{
            'total': qs.count(),
            'by_status': qs.values('status').annotate(count=Count('id')),
        }}
        return Response(stats)
'''

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    
    app_name = sys.argv[1]
    model_name = sys.argv[2]
    
    print("# serializers.py")
    print(SERIALIZER_TEMPLATE.format(model_name=model_name))
    print("\n# views.py")
    print(VIEWSET_TEMPLATE.format(model_name=model_name))
