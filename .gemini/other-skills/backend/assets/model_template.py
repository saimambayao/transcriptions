"""
Template for creating OBCMS Django models with standard patterns.
Copy and customize for new models.
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

# ==================== MIXINS ====================

class AuditMixin(models.Model):
    """Standard audit fields for all models."""
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(class)s_created',
        null=True
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(class)s_updated',
        null=True
    )
    
    class Meta:
        abstract = True

class OrganizationScopedMixin(models.Model):
    """Scope model to organization for multi-tenancy."""
    organization = models.ForeignKey(
        'common.Organization',
        on_delete=models.CASCADE,
        related_name='%(class)s_set'
    )
    
    class Meta:
        abstract = True

class SoftDeleteMixin(models.Model):
    """Soft delete pattern - keep deleted records."""
    is_active = models.BooleanField(default=True, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_deleted'
    )
    
    class Meta:
        abstract = True
    
    def soft_delete(self, user):
        """Soft delete this record."""
        self.is_active = False
        self.deleted_at = timezone.now()
        self.deleted_by = user
        self.save(update_fields=['is_active', 'deleted_at', 'deleted_by'])

# ==================== EXAMPLE MODEL ====================

class MyModel(OrganizationScopedMixin, AuditMixin, SoftDeleteMixin):
    """
    Example model with all standard OBCMS patterns.
    
    Replace 'MyModel' with your actual model name.
    Add your specific fields below.
    """
    # Basic fields
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    
    # Status field (common pattern)
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        db_index=True
    )
    
    # Foreign keys
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    
    # Optional fields
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    # JSON field for flexible data
    metadata = models.JSONField(default=dict, blank=True)
    
    class Meta:
        db_table = 'myapp_mymodel'
        verbose_name = 'My Model'
        verbose_name_plural = 'My Models'
        ordering = ['-created_at']
        
        indexes = [
            models.Index(fields=['organization', 'code']),
            models.Index(fields=['organization', 'status']),
            models.Index(fields=['-created_at']),
        ]
        
        constraints = [
            # Unique code per organization
            models.UniqueConstraint(
                fields=['organization', 'code'],
                condition=models.Q(is_active=True),
                name='unique_active_mymodel_code'
            ),
            # Date validation
            models.CheckConstraint(
                check=models.Q(end_date__gte=models.F('start_date')) | models.Q(end_date__isnull=True),
                name='mymodel_end_after_start'
            ),
        ]
    
    def __str__(self):
        return f"{self.code} - {self.name}"
    
    def save(self, *args, **kwargs):
        # Custom save logic if needed
        super().save(*args, **kwargs)
