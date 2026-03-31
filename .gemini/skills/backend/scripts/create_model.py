#!/usr/bin/env python3
"""
Generate Django model boilerplate with OBCMS patterns (audit fields, soft delete).

Usage:
    ./create_model.py <app_name> <model_name>
    ./create_model.py communities Community
"""

import sys
from pathlib import Path

TEMPLATE = '''from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class {model_name}(models.Model):
    """TODO: Add model description."""
    
    # TODO: Add your fields here
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('DRAFT', 'Draft'),
            ('ACTIVE', 'Active'),
            ('INACTIVE', 'Inactive'),
        ],
        default='DRAFT'
    )
    
    # Organization scoping
    organization = models.ForeignKey(
        'common.Organization',
        on_delete=models.PROTECT,
        related_name='{model_name_lower}s'
    )
    
    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='{model_name_lower}s_created'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='{model_name_lower}s_updated'
    )
    
    # Soft delete
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='{model_name_lower}s_deleted'
    )
    
    class Meta:
        db_table = '{app_name}_{model_name_lower}s'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['organization', 'status']),
        ]
    
    def __str__(self):
        return self.name
    
    def delete(self, using=None, keep_parents=False, user=None):
        """Soft delete."""
        self.deleted_at = timezone.now()
        if user:
            self.deleted_by = user
        self.save()
    
    def hard_delete(self):
        """Permanent delete."""
        super().delete()
'''

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    
    app_name = sys.argv[1]
    model_name = sys.argv[2]
    
    output = TEMPLATE.format(
        app_name=app_name,
        model_name=model_name,
        model_name_lower=model_name.lower()
    )
    
    print(output)
