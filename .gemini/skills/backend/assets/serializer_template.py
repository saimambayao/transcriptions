"""
Complete DRF Serializer Template

Copy this template for API serialization.
"""

from rest_framework import serializers
from .models import TODOModelName


class TODOModelNameSerializer(serializers.ModelSerializer):
    """
    Serializer for TODOModelName.
    
    Handles conversion between model instances and JSON.
    """
    
    # Read-only computed fields
    organization_name = serializers.CharField(
        source='organization.name',
        read_only=True
    )
    created_by_name = serializers.CharField(
        source='created_by.get_full_name',
        read_only=True
    )
    
    # TODO: Add custom fields
    # days_active = serializers.SerializerMethodField()
    # total_amount = serializers.SerializerMethodField()
    
    class Meta:
        model = TODOModelName
        fields = [
            'id',
            'name',
            'description',
            'status',
            'organization',
            'organization_name',
            'created_by_name',
            'created_at',
            'updated_at',
            # TODO: Add your fields
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'created_by',
            'organization',
        ]
    
    # ========================================================================
    # FIELD VALIDATION
    # ========================================================================
    
    def validate_name(self, value):
        """
        Validate name field.
        
        Raises:
            ValidationError: If validation fails
        """
        # TODO: Add field-specific validation
        # if len(value) < 3:
        #     raise serializers.ValidationError("Name must be at least 3 characters")
        return value
    
    # TODO: Add more field validators
    # def validate_amount(self, value):
    #     """Validate amount is positive."""
    #     if value < 0:
    #         raise serializers.ValidationError("Amount cannot be negative")
    #     return value
    
    def validate(self, data):
        """
        Cross-field validation.
        
        Args:
            data: Dictionary of validated field data
        
        Returns:
            dict: Validated data
        
        Raises:
            ValidationError: If validation fails
        """
        # TODO: Add cross-field validation
        # if data.get('end_date') and data.get('start_date'):
        #     if data['end_date'] < data['start_date']:
        #         raise serializers.ValidationError({
        #             'end_date': 'End date must be after start date'
        #         })
        
        return data
    
    # ========================================================================
    # SERIALIZER METHOD FIELDS
    # ========================================================================
    
    # TODO: Add computed fields
    # def get_days_active(self, obj):
    #     """Calculate days active."""
    #     from datetime import date
    #     if obj.start_date:
    #         return (date.today() - obj.start_date).days
    #     return 0
    
    # def get_total_amount(self, obj):
    #     """Calculate total from related objects."""
    #     return obj.items.aggregate(total=Sum('amount'))['total'] or 0
    
    # ========================================================================
    # CREATE AND UPDATE
    # ========================================================================
    
    def create(self, validated_data):
        """
        Create new instance.
        
        Override if you need custom creation logic.
        """
        # TODO: Add custom creation logic if needed
        # Example: Extract nested data
        # tags_data = validated_data.pop('tags', [])
        # instance = TODOModelName.objects.create(**validated_data)
        # instance.tags.set(tags_data)
        # return instance
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        """
        Update existing instance.
        
        Override if you need custom update logic.
        """
        # TODO: Add custom update logic if needed
        return super().update(instance, validated_data)


# ============================================================================
# NESTED SERIALIZERS
# ============================================================================

# TODO: Create serializers for nested relationships
# class TODOModelNameDetailSerializer(TODOModelNameSerializer):
#     """Detailed serializer with nested relationships."""
#     
#     items = ItemSerializer(many=True, read_only=True)
#     tags = TagSerializer(many=True, read_only=True)
#     
#     class Meta(TODOModelNameSerializer.Meta):
#         fields = TODOModelNameSerializer.Meta.fields + ['items', 'tags']


# ============================================================================
# LIST SERIALIZERS
# ============================================================================

# TODO: Create simplified serializer for list views
# class TODOModelNameListSerializer(serializers.ModelSerializer):
#     """Simplified serializer for list views."""
#     
#     class Meta:
#         model = TODOModelName
#         fields = ['id', 'name', 'status', 'created_at']
