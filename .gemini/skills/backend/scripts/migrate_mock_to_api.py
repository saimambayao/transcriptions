#!/usr/bin/env python3
"""
Mock to API Migration Script

Generates boilerplate code for migrating frontend mock data to Django Ninja API endpoints.

Usage:
    python migrate_mock_to_api.py <entity_name> [--app <app_name>]

Example:
    python migrate_mock_to_api.py Product --app products
    python migrate_mock_to_api.py Order --app orders

This will generate:
    - Django model template
    - Pydantic schemas template
    - Django Ninja router template
    - Frontend service template
"""

import argparse
import os
from pathlib import Path
from datetime import datetime


def to_snake_case(name: str) -> str:
    """Convert CamelCase to snake_case."""
    result = []
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result.append('_')
        result.append(char.lower())
    return ''.join(result)


def to_plural(name: str) -> str:
    """Simple pluralization."""
    if name.endswith('y'):
        return name[:-1] + 'ies'
    elif name.endswith('s'):
        return name + 'es'
    return name + 's'


def generate_model_template(entity_name: str, app_name: str) -> str:
    """Generate Django model template."""
    snake_name = to_snake_case(entity_name)
    return f'''# backend/apps/{app_name}/models.py
from django.db import models
from apps.core.models import BaseModel


class {entity_name}(BaseModel):
    """
    {entity_name} model - migrated from frontend mock data.

    TODO: Add fields matching your mock data structure.
    """

    # Multi-tenant support (required)
    organization = models.ForeignKey(
        'core.Organization',
        on_delete=models.CASCADE,
        related_name='{to_plural(snake_name)}'
    )

    # Example fields - customize based on mock data
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    # Add more fields here based on mock data structure...
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.CharField(max_length=100)
    # images = models.JSONField(default=list)

    class Meta:
        verbose_name = '{entity_name}'
        verbose_name_plural = '{to_plural(entity_name)}'
        indexes = [
            models.Index(fields=['organization', 'is_active']),
        ]

    def __str__(self):
        return self.name
'''


def generate_schemas_template(entity_name: str, app_name: str) -> str:
    """Generate Pydantic schemas template."""
    return f'''# backend/apps/{app_name}/schemas.py
from ninja import Schema
from typing import Optional, List
from datetime import datetime
from decimal import Decimal


class {entity_name}Out(Schema):
    """
    Output schema for {entity_name}.
    Maps Django model fields to frontend types.
    """
    id: str
    name: str
    description: str
    isActive: bool
    createdAt: datetime

    class Config:
        from_attributes = True

    @staticmethod
    def resolve_id(obj):
        return str(obj.id)

    @staticmethod
    def resolve_isActive(obj):
        return obj.is_active

    @staticmethod
    def resolve_createdAt(obj):
        return obj.created_at


class {entity_name}In(Schema):
    """
    Input schema for creating {entity_name}.
    """
    name: str
    description: str = ''
    isActive: bool = True


class {entity_name}Update(Schema):
    """
    Update schema - all fields optional.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    isActive: Optional[bool] = None


class {entity_name}Filters(Schema):
    """
    Query filters for listing {to_plural(entity_name)}.
    """
    search: Optional[str] = None
    isActive: Optional[bool] = None
'''


def generate_router_template(entity_name: str, app_name: str) -> str:
    """Generate Django Ninja router template."""
    snake_name = to_snake_case(entity_name)
    plural_name = to_plural(snake_name)
    return f'''# backend/apps/{app_name}/api.py
from ninja import Router, Query
from typing import List
from django.shortcuts import get_object_or_404
from apps.core.auth import AuthBearer
from .models import {entity_name}
from .schemas import {entity_name}Out, {entity_name}In, {entity_name}Update, {entity_name}Filters

router = Router(auth=AuthBearer(), tags=['{to_plural(entity_name)}'])


@router.get('/', response=List[{entity_name}Out])
def list_{plural_name}(request, filters: {entity_name}Filters = Query(...)):
    """List {plural_name} for current tenant."""
    qs = {entity_name}.objects.filter(
        organization=request.auth.organization,
        is_deleted=False
    )

    if filters.search:
        qs = qs.filter(name__icontains=filters.search)
    if filters.isActive is not None:
        qs = qs.filter(is_active=filters.isActive)

    return qs.order_by('-created_at')


@router.get('/{{id}}', response={entity_name}Out)
def get_{snake_name}(request, id: int):
    """Get single {snake_name} by ID."""
    return get_object_or_404(
        {entity_name},
        id=id,
        organization=request.auth.organization,
        is_deleted=False
    )


@router.post('/', response={entity_name}Out)
def create_{snake_name}(request, payload: {entity_name}In):
    """Create new {snake_name}."""
    data = payload.dict()
    # Map camelCase to snake_case
    data['is_active'] = data.pop('isActive', True)

    return {entity_name}.objects.create(
        **data,
        organization=request.auth.organization,
        created_by=request.auth
    )


@router.put('/{{id}}', response={entity_name}Out)
def update_{snake_name}(request, id: int, payload: {entity_name}Update):
    """Update existing {snake_name}."""
    obj = get_object_or_404(
        {entity_name},
        id=id,
        organization=request.auth.organization
    )

    data = payload.dict(exclude_unset=True)
    # Map camelCase to snake_case
    if 'isActive' in data:
        data['is_active'] = data.pop('isActive')

    for attr, value in data.items():
        setattr(obj, attr, value)
    obj.updated_by = request.auth
    obj.save()
    return obj


@router.delete('/{{id}}')
def delete_{snake_name}(request, id: int):
    """Soft delete {snake_name}."""
    obj = get_object_or_404(
        {entity_name},
        id=id,
        organization=request.auth.organization
    )
    obj.soft_delete()
    return {{'success': True}}
'''


def generate_frontend_service_template(entity_name: str) -> str:
    """Generate frontend service template."""
    snake_name = to_snake_case(entity_name)
    plural_name = to_plural(entity_name)
    plural_snake = to_plural(snake_name)
    return f'''// frontend/src/lib/services/{snake_name}.service.ts
import {{ apiClient }} from '@/lib/api/client'
import {{ ENDPOINTS }} from '@/lib/api/endpoints'

// ============================================================================
// TYPES
// ============================================================================

export interface {entity_name} {{
  id: string
  name: string
  description: string
  isActive: boolean
  createdAt: string
}}

export interface {entity_name}Input {{
  name: string
  description?: string
  isActive?: boolean
}}

export interface {entity_name}Filters {{
  search?: string
  isActive?: boolean
}}

// ============================================================================
// SERVICE INTERFACE
// ============================================================================

export interface I{entity_name}Service {{
  get{plural_name}(filters?: {entity_name}Filters): Promise<{entity_name}[]>
  get{entity_name}(id: string): Promise<{entity_name} | null>
  create{entity_name}(input: {entity_name}Input): Promise<{entity_name}>
  update{entity_name}(id: string, input: Partial<{entity_name}Input>): Promise<{entity_name}>
  delete{entity_name}(id: string): Promise<void>
}}

// ============================================================================
// API IMPLEMENTATION
// ============================================================================

class Api{entity_name}Service implements I{entity_name}Service {{
  async get{plural_name}(filters?: {entity_name}Filters): Promise<{entity_name}[]> {{
    const response = await apiClient.get<{{ data: {entity_name}[] }}>(
      ENDPOINTS.tenant.{plural_snake}.list,
      filters as Record<string, unknown>
    )
    return response.data ?? response as unknown as {entity_name}[]
  }}

  async get{entity_name}(id: string): Promise<{entity_name} | null> {{
    try {{
      return await apiClient.get<{entity_name}>(ENDPOINTS.tenant.{plural_snake}.detail(id))
    }} catch {{
      return null
    }}
  }}

  async create{entity_name}(input: {entity_name}Input): Promise<{entity_name}> {{
    return apiClient.post<{entity_name}>(ENDPOINTS.tenant.{plural_snake}.create, input)
  }}

  async update{entity_name}(id: string, input: Partial<{entity_name}Input>): Promise<{entity_name}> {{
    return apiClient.put<{entity_name}>(ENDPOINTS.tenant.{plural_snake}.update(id), input)
  }}

  async delete{entity_name}(id: string): Promise<void> {{
    return apiClient.delete<void>(ENDPOINTS.tenant.{plural_snake}.delete(id))
  }}
}}

// ============================================================================
// EXPORT
// ============================================================================

export const {snake_name}Service: I{entity_name}Service = new Api{entity_name}Service()
'''


def generate_endpoints_template(entity_name: str) -> str:
    """Generate endpoints.ts additions."""
    snake_name = to_snake_case(entity_name)
    plural_snake = to_plural(snake_name)
    return f'''// Add to frontend/src/lib/api/endpoints.ts under tenant:

{plural_snake}: {{
  list: '/tenant/{plural_snake}',
  create: '/tenant/{plural_snake}',
  detail: (id: string) => `/tenant/{plural_snake}/${{id}}`,
  update: (id: string) => `/tenant/{plural_snake}/${{id}}`,
  delete: (id: string) => `/tenant/{plural_snake}/${{id}}`,
}},
'''


def generate_url_config_template(entity_name: str, app_name: str) -> str:
    """Generate URL configuration addition."""
    plural_name = to_plural(entity_name)
    return f'''# Add to backend/config/urls.py

from apps.{app_name}.api import router as {app_name}_router

# In the api.add_router section:
api.add_router('/tenant/{to_plural(to_snake_case(entity_name))}/', {app_name}_router, tags=['{plural_name}'])
'''


def main():
    parser = argparse.ArgumentParser(
        description='Generate boilerplate for mock-to-API migration'
    )
    parser.add_argument('entity_name', help='Entity name in CamelCase (e.g., Product)')
    parser.add_argument('--app', default=None, help='Django app name (defaults to pluralized entity)')
    parser.add_argument('--output', '-o', default=None, help='Output directory for generated files')

    args = parser.parse_args()

    entity_name = args.entity_name
    app_name = args.app or to_plural(to_snake_case(entity_name))
    output_dir = args.output or '.'

    print(f"\n{'='*60}")
    print(f"Mock to API Migration Generator")
    print(f"{'='*60}")
    print(f"Entity: {entity_name}")
    print(f"App: {app_name}")
    print(f"{'='*60}\n")

    # Generate all templates
    templates = {
        f'{app_name}_model.py': generate_model_template(entity_name, app_name),
        f'{app_name}_schemas.py': generate_schemas_template(entity_name, app_name),
        f'{app_name}_api.py': generate_router_template(entity_name, app_name),
        f'{to_snake_case(entity_name)}_service.ts': generate_frontend_service_template(entity_name),
        f'{app_name}_endpoints.txt': generate_endpoints_template(entity_name),
        f'{app_name}_urls.txt': generate_url_config_template(entity_name, app_name),
    }

    # Create output directory if needed
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Write files
    for filename, content in templates.items():
        filepath = output_path / filename
        filepath.write_text(content)
        print(f"Generated: {filepath}")

    print(f"\n{'='*60}")
    print("Next steps:")
    print("1. Review and customize the generated templates")
    print("2. Copy model to backend/apps/{app_name}/models.py")
    print("3. Copy schemas to backend/apps/{app_name}/schemas.py")
    print("4. Copy api to backend/apps/{app_name}/api.py")
    print("5. Copy service to frontend/src/lib/services/")
    print("6. Add endpoints to frontend/src/lib/api/endpoints.ts")
    print("7. Add router to backend/config/urls.py")
    print("8. Run migrations: python manage.py makemigrations && python manage.py migrate")
    print("9. Test the API endpoints")
    print("10. Delete the mock data file")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
