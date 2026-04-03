# Django REST Framework Serializers

Guide for DRF serializers, validation, and nested relationships.

## Basic Serializers

```python
from rest_framework import serializers
from .models import Community, Assessment, Beneficiary

class CommunitySerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='region.name', read_only=True)
    municipality_name = serializers.CharField(source='municipality.name', read_only=True)

    class Meta:
        model = Community
        fields = ['id', 'name', 'region', 'region_name', 'municipality', 
                  'municipality_name', 'population', 'created_at']
        read_only_fields = ['created_at', 'updated_at']
```

## Nested Serializers

```python
class AssessmentSerializer(serializers.ModelSerializer):
    community = CommunitySerializer(read_only=True)
    community_id = serializers.IntegerField(write_only=True)
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)

    class Meta:
        model = Assessment
        fields = ['id', 'community', 'community_id', 'assessment_date', 
                  'status', 'created_by_name', 'created_at']
```

## Validation

```python
class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = '__all__'

    def validate_birth_date(self, value):
        """Validate birth date is not in future."""
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError("Birth date cannot be in the future")
        return value

    def validate(self, data):
        """Cross-field validation."""
        if data.get('household_size', 0) < 1:
            raise serializers.ValidationError({
                'household_size': 'Household size must be at least 1'
            })
        return data
```

## Create and Update

```python
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'description', 'budget', 'status']

    def create(self, validated_data):
        """Custom create logic."""
        validated_data['created_by'] = self.context['request'].user
        validated_data['organization'] = self.context['request'].user.organization
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Custom update logic."""
        validated_data['updated_by'] = self.context['request'].user
        return super().update(instance, validated_data)
```

## SerializerMethodField

```python
class CommunityDetailSerializer(serializers.ModelSerializer):
    assessment_count = serializers.SerializerMethodField()
    latest_assessment_date = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = ['id', 'name', 'population', 'assessment_count', 'latest_assessment_date']

    def get_assessment_count(self, obj):
        return obj.assessment_set.count()

    def get_latest_assessment_date(self, obj):
        latest = obj.assessment_set.order_by('-assessment_date').first()
        return latest.assessment_date if latest else None
```

For API authentication, see [api-auth.md](api-auth.md).
