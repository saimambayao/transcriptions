# Mock Data to Real API Migration

Workflow for replacing frontend mock data with real Django Ninja API endpoints and database-backed data.

## Table of Contents

- [Overview](#overview)
- [Migration Workflow](#migration-workflow)
- [Step 1: Analyze Mock Data Structure](#step-1-analyze-mock-data-structure)
- [Step 2: Design Django Models](#step-2-design-django-models)
- [Step 3: Create Django Ninja API Endpoints](#step-3-create-django-ninja-api-endpoints)
- [Step 4: Update Frontend Service](#step-4-update-frontend-service)
- [Step 5: Verify and Test](#step-5-verify-and-test)
- [Patterns and Examples](#patterns-and-examples)

## Overview

Frontend-first development creates mock data in `frontend/src/lib/mock/` that powers the UI during initial development. This workflow systematically migrates that mock data to real API endpoints.

**Key principle**: The frontend service interface (`IServiceName`) should NOT change during migration. Only the implementation switches from mock to API.

## Migration Workflow

```
Mock Data Analysis
       |
       v
Django Model Design  <---> Pydantic Schemas
       |
       v
Django Ninja Router (API endpoints)
       |
       v
Update Frontend Service (Mock -> API)
       |
       v
Test End-to-End
       |
       v
Delete Mock Data File
```

## Step 1: Analyze Mock Data Structure

Examine the mock data file to understand:
- Data shape and types
- Relationships between entities
- Required vs optional fields
- Filters and query patterns used

**Example mock file** (`frontend/src/lib/mock/products.ts`):

```typescript
export const mockProducts = [
  {
    id: 'prod-001',
    name: 'Organic Coffee Beans',
    description: 'Premium arabica coffee',
    category: 'food',
    price: 450.00,
    stock: 100,
    images: ['/images/coffee.jpg'],
    isActive: true,
    createdAt: '2024-01-15T00:00:00Z',
  },
]
```

**Extract requirements**:
- Fields: id, name, description, category, price, stock, images, isActive, createdAt
- Types: string id, decimal price, integer stock, string[] images, boolean isActive
- Relationships: category could be FK to Category model

## Step 2: Design Django Models

Create model matching the mock data structure:

```python
# backend/apps/products/models.py
from django.db import models
from apps.core.models import BaseModel

class Product(BaseModel):
    """Product model matching frontend mock data structure."""

    organization = models.ForeignKey(
        'core.Organization',
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compare_at_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    sku = models.CharField(max_length=100, blank=True)
    stock = models.IntegerField(default=0)
    low_stock_threshold = models.IntegerField(default=10)
    images = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['organization', 'is_active']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return self.name
```

**Migration**:

```bash
python manage.py makemigrations products
python manage.py migrate
```

## Step 3: Create Django Ninja API Endpoints

### 3.1 Define Pydantic Schemas

```python
# backend/apps/products/schemas.py
from ninja import Schema
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

class ProductOut(Schema):
    """Output schema matching frontend Product type."""
    id: str
    name: str
    description: str
    category: str
    price: Decimal
    compareAtPrice: Optional[Decimal] = None
    sku: str
    stock: int
    lowStockThreshold: int
    images: List[str]
    isActive: bool
    isFeatured: bool
    createdAt: datetime

    class Config:
        from_attributes = True

    @staticmethod
    def resolve_id(obj):
        return str(obj.id)

    @staticmethod
    def resolve_compareAtPrice(obj):
        return obj.compare_at_price

    @staticmethod
    def resolve_lowStockThreshold(obj):
        return obj.low_stock_threshold

    @staticmethod
    def resolve_isActive(obj):
        return obj.is_active

    @staticmethod
    def resolve_isFeatured(obj):
        return obj.is_featured

    @staticmethod
    def resolve_createdAt(obj):
        return obj.created_at

class ProductIn(Schema):
    """Input schema for creating products."""
    name: str
    description: str = ''
    category: str
    price: Decimal
    compareAtPrice: Optional[Decimal] = None
    sku: str = ''
    stock: int = 0
    lowStockThreshold: int = 10
    images: List[str] = []
    isActive: bool = True
    isFeatured: bool = False

class ProductUpdate(Schema):
    """Update schema - all fields optional."""
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[Decimal] = None
    compareAtPrice: Optional[Decimal] = None
    sku: Optional[str] = None
    stock: Optional[int] = None
    lowStockThreshold: Optional[int] = None
    images: Optional[List[str]] = None
    isActive: Optional[bool] = None
    isFeatured: Optional[bool] = None

class ProductFilters(Schema):
    """Query filters matching frontend ProductFilters type."""
    category: Optional[str] = None
    isActive: Optional[bool] = None
    isFeatured: Optional[bool] = None
    search: Optional[str] = None
    minStock: Optional[int] = None
    maxStock: Optional[int] = None
```

### 3.2 Create Router with CRUD Operations

```python
# backend/apps/products/api.py
from ninja import Router, Query
from typing import List
from django.shortcuts import get_object_or_404
from apps.core.auth import AuthBearer
from .models import Product
from .schemas import ProductOut, ProductIn, ProductUpdate, ProductFilters

router = Router(auth=AuthBearer(), tags=['Products'])

@router.get('/', response=List[ProductOut])
def list_products(request, filters: ProductFilters = Query(...)):
    """List products for current tenant."""
    qs = Product.objects.filter(
        organization=request.auth.organization,
        is_deleted=False
    )

    if filters.category:
        qs = qs.filter(category=filters.category)
    if filters.isActive is not None:
        qs = qs.filter(is_active=filters.isActive)
    if filters.isFeatured is not None:
        qs = qs.filter(is_featured=filters.isFeatured)
    if filters.search:
        qs = qs.filter(name__icontains=filters.search)
    if filters.minStock is not None:
        qs = qs.filter(stock__gte=filters.minStock)
    if filters.maxStock is not None:
        qs = qs.filter(stock__lte=filters.maxStock)

    return qs.order_by('-created_at')

@router.get('/{product_id}', response=ProductOut)
def get_product(request, product_id: int):
    """Get single product by ID."""
    return get_object_or_404(
        Product,
        id=product_id,
        organization=request.auth.organization,
        is_deleted=False
    )

@router.post('/', response=ProductOut)
def create_product(request, payload: ProductIn):
    """Create new product."""
    data = payload.dict()
    # Map camelCase to snake_case
    data['compare_at_price'] = data.pop('compareAtPrice', None)
    data['low_stock_threshold'] = data.pop('lowStockThreshold', 10)
    data['is_active'] = data.pop('isActive', True)
    data['is_featured'] = data.pop('isFeatured', False)

    return Product.objects.create(
        **data,
        organization=request.auth.organization,
        created_by=request.auth
    )

@router.put('/{product_id}', response=ProductOut)
def update_product(request, product_id: int, payload: ProductUpdate):
    """Update existing product."""
    product = get_object_or_404(
        Product,
        id=product_id,
        organization=request.auth.organization
    )

    data = payload.dict(exclude_unset=True)
    # Map camelCase to snake_case
    if 'compareAtPrice' in data:
        data['compare_at_price'] = data.pop('compareAtPrice')
    if 'lowStockThreshold' in data:
        data['low_stock_threshold'] = data.pop('lowStockThreshold')
    if 'isActive' in data:
        data['is_active'] = data.pop('isActive')
    if 'isFeatured' in data:
        data['is_featured'] = data.pop('isFeatured')

    for attr, value in data.items():
        setattr(product, attr, value)
    product.updated_by = request.auth
    product.save()
    return product

@router.delete('/{product_id}')
def delete_product(request, product_id: int):
    """Soft delete product."""
    product = get_object_or_404(
        Product,
        id=product_id,
        organization=request.auth.organization
    )
    product.soft_delete()
    return {'success': True}
```

### 3.3 Register Router

```python
# backend/config/urls.py
from apps.products.api import router as products_router

api.add_router('/tenant/products/', products_router)
```

## Step 4: Update Frontend Service

### 4.1 Add Endpoint Constants

```typescript
// frontend/src/lib/api/endpoints.ts
export const ENDPOINTS = {
  tenant: {
    products: {
      list: '/tenant/products',
      create: '/tenant/products',
      detail: (id: string) => `/tenant/products/${id}`,
      update: (id: string) => `/tenant/products/${id}`,
      delete: (id: string) => `/tenant/products/${id}`,
    },
  },
}
```

### 4.2 Replace Mock Implementation with API

**Before** (Mock):

```typescript
// frontend/src/lib/services/shop.service.ts
import { mockProducts } from '@/lib/mock/products'

class MockShopService implements IShopService {
  async getProducts(filters?: ProductFilters): Promise<Product[]> {
    let products = [...mockProducts]
    if (filters?.category) {
      products = products.filter(p => p.category === filters.category)
    }
    return products
  }
}

export const shopService: IShopService = new MockShopService()
```

**After** (API):

```typescript
// frontend/src/lib/services/shop.service.ts
import { apiClient } from '@/lib/api/client'
import { ENDPOINTS } from '@/lib/api/endpoints'

class ApiShopService implements IShopService {
  async getProducts(filters?: ProductFilters): Promise<Product[]> {
    const response = await apiClient.get<{ data: Product[] }>(
      ENDPOINTS.tenant.products.list,
      filters as Record<string, unknown>
    )
    return response.data ?? response as unknown as Product[]
  }

  async getProduct(id: string): Promise<Product | null> {
    try {
      return await apiClient.get<Product>(ENDPOINTS.tenant.products.detail(id))
    } catch {
      return null
    }
  }

  async createProduct(input: ProductInput): Promise<Product> {
    return apiClient.post<Product>(ENDPOINTS.tenant.products.create, input)
  }

  async updateProduct(id: string, input: Partial<ProductInput>): Promise<Product> {
    return apiClient.put<Product>(ENDPOINTS.tenant.products.update(id), input)
  }

  async deleteProduct(id: string): Promise<void> {
    return apiClient.delete<void>(ENDPOINTS.tenant.products.delete(id))
  }
}

export const shopService: IShopService = new ApiShopService()
```

### 4.3 Type Alignment Checklist

Ensure these match between frontend and backend:

| Frontend Type | Backend Schema | Notes |
|--------------|----------------|-------|
| `id: string` | `id: str` (resolved from int) | Use resolver in schema |
| `createdAt: string` | `createdAt: datetime` | Serializes to ISO string |
| `price: number` | `price: Decimal` | Auto-converts |
| `isActive: boolean` | `isActive: bool` | Use resolver for snake_case |

## Step 5: Create Seed Data

After creating the model and API, populate the database with sample data for testing. This data can be used locally and deployed to production.

### 5.1 Django Management Command (Recommended)

```python
# backend/apps/products/management/commands/seed_products.py
from django.core.management.base import BaseCommand
from apps.products.models import Product
from apps.core.models import Organization
import random

class Command(BaseCommand):
    help = 'Seed database with sample products'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding',
        )
        parser.add_argument(
            '--count',
            type=int,
            default=20,
            help='Number of products to create',
        )

    def handle(self, *args, **options):
        if options['clear']:
            Product.objects.all().delete()
            self.stdout.write('Cleared existing products')

        # Get or create default organization
        org, _ = Organization.objects.get_or_create(
            shortname='demo',
            defaults={'name': 'Demo Cooperative'}
        )

        categories = ['food', 'handicraft', 'agriculture', 'textile', 'health']
        sample_products = [
            {'name': 'Organic Coffee Beans', 'price': 450.00},
            {'name': 'Handwoven Basket', 'price': 350.00},
            {'name': 'Fresh Vegetables Bundle', 'price': 150.00},
            {'name': 'Traditional Malong', 'price': 1200.00},
            {'name': 'Herbal Tea Collection', 'price': 280.00},
            {'name': 'Coconut Oil 500ml', 'price': 180.00},
            {'name': 'Dried Fish Pack', 'price': 220.00},
            {'name': 'Banana Chips 250g', 'price': 85.00},
            {'name': 'Woven Placemat Set', 'price': 420.00},
            {'name': 'Organic Honey 300ml', 'price': 350.00},
        ]

        created_count = 0
        for i in range(options['count']):
            sample = random.choice(sample_products)
            Product.objects.create(
                organization=org,
                name=f"{sample['name']} #{i+1}",
                description=f"High-quality {sample['name'].lower()} from local producers.",
                category=random.choice(categories),
                price=sample['price'] + random.uniform(-50, 50),
                stock=random.randint(10, 100),
                low_stock_threshold=10,
                is_active=True,
                is_featured=random.random() > 0.7,
            )
            created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Created {created_count} products')
        )
```

**Usage:**

```bash
# Create 20 sample products
python manage.py seed_products

# Create 50 products, clearing existing first
python manage.py seed_products --count 50 --clear
```

### 5.2 Data Migration (For Production Deployment)

For data that must exist in production (like initial categories, statuses):

```python
# backend/apps/products/migrations/0002_seed_categories.py
from django.db import migrations

def seed_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    categories = [
        {'name': 'Food & Beverages', 'slug': 'food'},
        {'name': 'Handicrafts', 'slug': 'handicraft'},
        {'name': 'Agriculture', 'slug': 'agriculture'},
        {'name': 'Textiles', 'slug': 'textile'},
        {'name': 'Health & Wellness', 'slug': 'health'},
    ]
    for cat in categories:
        Category.objects.get_or_create(slug=cat['slug'], defaults=cat)

def remove_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Category.objects.filter(slug__in=['food', 'handicraft', 'agriculture', 'textile', 'health']).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_categories, remove_categories),
    ]
```

### 5.3 Fixtures (JSON/YAML)

Export mock data structure to Django fixtures:

```json
// backend/apps/products/fixtures/sample_products.json
[
  {
    "model": "products.product",
    "pk": 1,
    "fields": {
      "name": "Organic Coffee Beans",
      "description": "Premium arabica coffee from Bangsamoro highlands",
      "category": "food",
      "price": "450.00",
      "stock": 100,
      "is_active": true,
      "is_featured": true,
      "created_at": "2024-01-15T00:00:00Z"
    }
  },
  {
    "model": "products.product",
    "pk": 2,
    "fields": {
      "name": "Handwoven Basket",
      "description": "Traditional handcrafted basket",
      "category": "handicraft",
      "price": "350.00",
      "stock": 50,
      "is_active": true,
      "is_featured": false,
      "created_at": "2024-01-16T00:00:00Z"
    }
  }
]
```

**Load fixtures:**

```bash
python manage.py loaddata sample_products
```

### 5.4 Factory Boy (For Testing)

```python
# backend/apps/products/factories.py
import factory
from factory.django import DjangoModelFactory
from .models import Product
from apps.core.models import Organization

class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Sequence(lambda n: f'Organization {n}')
    shortname = factory.Sequence(lambda n: f'org{n}')

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    organization = factory.SubFactory(OrganizationFactory)
    name = factory.Faker('product_name')
    description = factory.Faker('sentence', nb_words=10)
    category = factory.Iterator(['food', 'handicraft', 'agriculture'])
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    stock = factory.Faker('random_int', min=0, max=100)
    is_active = True
    is_featured = factory.Faker('boolean', chance_of_getting_true=30)
```

**Usage in tests:**

```python
from apps.products.factories import ProductFactory

# Create single product
product = ProductFactory()

# Create multiple products
products = ProductFactory.create_batch(10)

# Create with specific attributes
featured_product = ProductFactory(is_featured=True, price=1000)
```

### 5.5 Automatic Seeding on Deploy

Add to your deployment script or Railway start command:

```bash
# backend/start.sh
#!/bin/bash

# Run migrations
python manage.py migrate --noinput

# Seed data if database is empty
python manage.py shell -c "
from apps.products.models import Product
if Product.objects.count() == 0:
    from django.core.management import call_command
    call_command('seed_products', count=20)
    print('Seeded initial products')
"

# Start server
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

### 5.6 Convert Mock Data to Seed Data

Script to convert frontend mock data to Django fixtures:

```python
# scripts/convert_mock_to_fixtures.py
import json
import re
from pathlib import Path

def convert_mock_to_fixture(mock_file: str, model_name: str, app_name: str) -> list:
    """
    Convert TypeScript mock data to Django fixture format.
    """
    # Read mock file
    content = Path(mock_file).read_text()

    # Extract array data (simplified - may need adjustment)
    match = re.search(r'export const \w+ = (\[[\s\S]*?\]);', content)
    if not match:
        raise ValueError("Could not find mock data array")

    # Parse as JSON (TypeScript is close enough for simple cases)
    data_str = match.group(1)
    # Remove trailing commas
    data_str = re.sub(r',(\s*[}\]])', r'\1', data_str)
    mock_data = json.loads(data_str)

    # Convert to fixture format
    fixtures = []
    for i, item in enumerate(mock_data, 1):
        fixture = {
            "model": f"{app_name}.{model_name.lower()}",
            "pk": i,
            "fields": {}
        }

        # Map fields (convert camelCase to snake_case)
        for key, value in item.items():
            if key == 'id':
                continue  # Skip ID, use sequential pk
            snake_key = re.sub(r'([A-Z])', r'_\1', key).lower()
            fixture["fields"][snake_key] = value

        fixtures.append(fixture)

    return fixtures

# Usage
# fixtures = convert_mock_to_fixture(
#     'frontend/src/lib/mock/products.ts',
#     'Product',
#     'products'
# )
# with open('backend/apps/products/fixtures/products.json', 'w') as f:
#     json.dump(fixtures, f, indent=2)
```

## Step 6: Verify and Test

### 6.1 Backend Testing

```python
# backend/apps/products/tests/test_api.py
from django.test import TestCase
from ninja.testing import TestClient
from apps.products.api import router
from apps.core.models import Organization, User

class ProductAPITests(TestCase):
    def setUp(self):
        self.client = TestClient(router)
        self.org = Organization.objects.create(name='Test Org')
        self.user = User.objects.create_user(
            username='test',
            organization=self.org
        )

    def test_list_products_empty(self):
        response = self.client.get('/', user=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_create_product(self):
        response = self.client.post('/', json={
            'name': 'Test Product',
            'category': 'test',
            'price': '100.00'
        }, user=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Test Product')

    def test_organization_isolation(self):
        """Verify multi-tenant data isolation."""
        other_org = Organization.objects.create(name='Other Org')
        Product.objects.create(
            name='Other Product',
            organization=other_org,
            category='test',
            price=100
        )

        response = self.client.get('/', user=self.user)
        self.assertEqual(len(response.json()), 0)
```

### 6.2 Frontend Testing

```typescript
// Manual verification checklist:
// 1. List view shows data from API (check Network tab)
// 2. Create form submits to API and updates list
// 3. Edit form loads data and saves changes
// 4. Delete removes item from list
// 5. Filters work correctly
// 6. Error states display properly (API down, validation errors)
```

### 6.3 Delete Mock Data

Once verified working, delete the mock file:

```bash
rm frontend/src/lib/mock/products.ts
```

## Patterns and Examples

### Response Transformation

When API response shape differs from frontend type:

```typescript
async getOrders(): Promise<Order[]> {
  const response = await apiClient.get<ApiOrderResponse[]>(ENDPOINTS.orders)

  // Transform API response to frontend type
  return response.map(o => ({
    id: o.id,
    customer: {
      id: o.customer_id,
      name: o.customer_name,
      email: o.customer_email,
    },
    total: o.total_amount,
    status: o.status as OrderStatus,
    createdAt: o.created_at,
  }))
}
```

### Graceful Degradation

Return sensible defaults when API fails:

```typescript
async getProfile(): Promise<Profile> {
  try {
    return await apiClient.get<Profile>(ENDPOINTS.profile)
  } catch {
    return this.getDefaultProfile()
  }
}

private getDefaultProfile(): Profile {
  return {
    id: '',
    name: '',
    email: '',
  }
}
```

### Pagination Support

```typescript
interface PaginatedResponse<T> {
  data: T[]
  total: number
  page: number
  pageSize: number
}

async getProducts(page = 1, pageSize = 20): Promise<PaginatedResponse<Product>> {
  return apiClient.get<PaginatedResponse<Product>>(
    ENDPOINTS.products,
    { page, page_size: pageSize }
  )
}
```

## Testing Frontend-Backend Connection

### Prerequisites Setup

#### 1. CORS Configuration

```python
# backend/config/settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3090",  # Frontend dev server
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "origin",
    "x-csrftoken",
    "x-requested-with",
]
```

#### 2. Frontend API Client Configuration

```typescript
// frontend/src/lib/api/config.ts
export const API_CONFIG = {
  baseUrl: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8090/api',
  timeout: 30000,
}
```

```typescript
// frontend/src/lib/api/client.ts
import { API_CONFIG } from './config'

class ApiClient {
  private baseUrl: string

  constructor() {
    this.baseUrl = API_CONFIG.baseUrl
  }

  private async request<T>(
    method: string,
    endpoint: string,
    data?: unknown,
    params?: Record<string, unknown>
  ): Promise<T> {
    const url = new URL(`${this.baseUrl}${endpoint}`)

    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null) {
          url.searchParams.append(key, String(value))
        }
      })
    }

    const headers: HeadersInit = {
      'Content-Type': 'application/json',
    }

    // Add auth token if available
    const token = this.getAuthToken()
    if (token) {
      headers['Authorization'] = `Bearer ${token}`
    }

    const response = await fetch(url.toString(), {
      method,
      headers,
      body: data ? JSON.stringify(data) : undefined,
      credentials: 'include',
    })

    if (!response.ok) {
      throw new Error(`API Error: ${response.status}`)
    }

    return response.json()
  }

  private getAuthToken(): string | null {
    // Get from cookie, localStorage, or auth context
    return localStorage.getItem('auth_token')
  }

  get<T>(endpoint: string, params?: Record<string, unknown>): Promise<T> {
    return this.request<T>('GET', endpoint, undefined, params)
  }

  post<T>(endpoint: string, data?: unknown): Promise<T> {
    return this.request<T>('POST', endpoint, data)
  }

  put<T>(endpoint: string, data?: unknown): Promise<T> {
    return this.request<T>('PUT', endpoint, data)
  }

  delete<T>(endpoint: string): Promise<T> {
    return this.request<T>('DELETE', endpoint)
  }
}

export const apiClient = new ApiClient()
```

### Connection Testing Workflow

#### Step 1: Verify Backend is Running

```bash
# Terminal 1: Start backend
cd backend
python manage.py runserver 0.0.0.0:8090

# Verify API is accessible
curl http://localhost:8090/api/docs  # Should return OpenAPI docs
```

#### Step 2: Verify Frontend Can Reach Backend

```typescript
// Add to any page for quick debugging
useEffect(() => {
  const testConnection = async () => {
    try {
      const response = await fetch('http://localhost:8090/api/health')
      console.log('API Connection:', response.ok ? 'OK' : 'FAILED')
    } catch (error) {
      console.error('API Connection Error:', error)
    }
  }
  testConnection()
}, [])
```

#### Step 3: Test Authentication Flow

```typescript
// Test auth endpoint
const testAuth = async () => {
  // 1. Login to get token
  const loginResponse = await apiClient.post<{ token: string }>('/auth/login', {
    username: 'test@example.com',
    password: 'testpassword',
  })
  console.log('Login token:', loginResponse.token)

  // 2. Store token
  localStorage.setItem('auth_token', loginResponse.token)

  // 3. Test authenticated endpoint
  const profile = await apiClient.get('/auth/me')
  console.log('Profile:', profile)
}
```

#### Step 4: Test CRUD Operations

```typescript
// Comprehensive CRUD test
const testCRUD = async () => {
  console.log('=== Testing CRUD Operations ===')

  // CREATE
  console.log('1. Creating product...')
  const created = await apiClient.post<Product>('/tenant/products', {
    name: 'Test Product',
    category: 'test',
    price: 100,
    stock: 50,
  })
  console.log('Created:', created.id)

  // READ (list)
  console.log('2. Listing products...')
  const list = await apiClient.get<Product[]>('/tenant/products')
  console.log('List count:', list.length)

  // READ (single)
  console.log('3. Getting single product...')
  const single = await apiClient.get<Product>(`/tenant/products/${created.id}`)
  console.log('Single:', single.name)

  // UPDATE
  console.log('4. Updating product...')
  const updated = await apiClient.put<Product>(`/tenant/products/${created.id}`, {
    name: 'Updated Product',
  })
  console.log('Updated name:', updated.name)

  // DELETE
  console.log('5. Deleting product...')
  await apiClient.delete(`/tenant/products/${created.id}`)
  console.log('Deleted successfully')

  console.log('=== All CRUD tests passed ===')
}
```

### Debugging Common Issues

#### Issue: CORS Errors

```
Access to fetch at 'http://localhost:8090/api/...' from origin
'http://localhost:3090' has been blocked by CORS policy
```

**Fix**: Verify CORS settings in Django:

```python
# settings.py
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be high in list
    ...
]
```

#### Issue: 401 Unauthorized

**Fix**: Check token is being sent:

```typescript
// Debug: Log request headers
const response = await fetch(url, {
  headers: {
    'Authorization': `Bearer ${token}`,  // Verify token exists
  },
})
```

#### Issue: 500 Internal Server Error

**Fix**: Check Django logs for stack trace:

```bash
# Watch Django logs
tail -f backend/logs/django.log

# Or check terminal output where runserver is running
```

#### Issue: Network Error / Connection Refused

**Fix**: Verify backend is running and ports match:

```bash
# Check if backend is listening
lsof -i :8090

# Verify frontend is using correct URL
echo $NEXT_PUBLIC_API_URL
```

### Integration Test Script

Create a test script for automated verification:

```typescript
// frontend/src/lib/utils/api-test.ts
export async function runApiIntegrationTests() {
  const results: { test: string; passed: boolean; error?: string }[] = []

  const addResult = (test: string, passed: boolean, error?: string) => {
    results.push({ test, passed, error })
    console.log(`${passed ? 'PASS' : 'FAIL'}: ${test}${error ? ` - ${error}` : ''}`)
  }

  // Test 1: API Health
  try {
    const health = await fetch(`${API_CONFIG.baseUrl}/health`)
    addResult('API Health Check', health.ok)
  } catch (e) {
    addResult('API Health Check', false, String(e))
  }

  // Test 2: Public Endpoints (no auth)
  try {
    const public = await apiClient.get('/public/products')
    addResult('Public Endpoint Access', Array.isArray(public))
  } catch (e) {
    addResult('Public Endpoint Access', false, String(e))
  }

  // Test 3: Auth Endpoints
  try {
    const token = localStorage.getItem('auth_token')
    if (token) {
      const me = await apiClient.get('/auth/me')
      addResult('Authenticated Request', !!me)
    } else {
      addResult('Authenticated Request', false, 'No auth token')
    }
  } catch (e) {
    addResult('Authenticated Request', false, String(e))
  }

  // Test 4: Multi-tenant Isolation
  try {
    const tenantData = await apiClient.get('/tenant/products')
    addResult('Tenant Data Isolation', Array.isArray(tenantData))
  } catch (e) {
    addResult('Tenant Data Isolation', false, String(e))
  }

  // Summary
  const passed = results.filter(r => r.passed).length
  const total = results.length
  console.log(`\n=== Results: ${passed}/${total} tests passed ===`)

  return results
}
```

### Browser DevTools Checklist

When testing API connection in browser:

1. **Network Tab**
   - [ ] Request URL is correct
   - [ ] Request method is correct (GET/POST/PUT/DELETE)
   - [ ] Request headers include Authorization (for auth endpoints)
   - [ ] Request body is valid JSON (for POST/PUT)
   - [ ] Response status is 200/201/204
   - [ ] Response body matches expected shape

2. **Console Tab**
   - [ ] No CORS errors
   - [ ] No uncaught exceptions
   - [ ] Data logs match expectations

3. **Application Tab**
   - [ ] Auth token is stored (localStorage/cookies)
   - [ ] Token is not expired

### End-to-End Verification Script

```bash
#!/bin/bash
# scripts/verify-api-connection.sh

echo "=== API Connection Verification ==="

# 1. Check backend health
echo "1. Checking backend health..."
HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8090/api/health)
if [ "$HEALTH" = "200" ]; then
  echo "   Backend: OK"
else
  echo "   Backend: FAILED (HTTP $HEALTH)"
  exit 1
fi

# 2. Check public endpoint
echo "2. Checking public endpoint..."
PUBLIC=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8090/api/public/products)
if [ "$PUBLIC" = "200" ]; then
  echo "   Public API: OK"
else
  echo "   Public API: FAILED (HTTP $PUBLIC)"
fi

# 3. Check OpenAPI docs
echo "3. Checking OpenAPI docs..."
DOCS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8090/api/docs)
if [ "$DOCS" = "200" ]; then
  echo "   API Docs: OK"
else
  echo "   API Docs: FAILED (HTTP $DOCS)"
fi

echo "=== Verification Complete ==="
```

## Migration Checklist

For each mock data file:

- [ ] Analyze mock data structure and types
- [ ] Create Django model with appropriate fields
- [ ] Run migrations
- [ ] Create Pydantic schemas (In/Out/Update/Filters)
- [ ] Create Django Ninja router with CRUD operations
- [ ] Register router in urls.py
- [ ] **Create seed data (management command or fixtures)**
- [ ] **Run seed command to populate database**
- [ ] Add endpoint constants to `endpoints.ts`
- [ ] Replace Mock service class with API service class
- [ ] **Test frontend-backend connection (DevTools Network tab)**
- [ ] Test all CRUD operations
- [ ] Verify error handling
- [ ] Delete mock data file
- [ ] Commit changes


---

# Mock to API Migration (from SKILL.md)

## Mock to API Migration Workflow

For frontend-first development, use this workflow to replace mock data with real API endpoints.

### Quick Migration Steps

```
1. Analyze mock file → Extract types and data shape
2. Create Django model → Match mock structure
3. Create Pydantic schemas → In/Out/Update/Filters
4. Create Django Ninja router → CRUD endpoints
5. Create seed data → Management command or fixtures
6. Populate database → Run seed command
7. Add endpoint to endpoints.ts
8. Replace MockService with ApiService
9. Test connection → Verify data flows (DevTools)
10. Delete mock file
```

### Migration Pattern

**Frontend Service Interface** (unchanged):

```typescript
// This interface stays the same during migration
export interface IShopService {
  getProducts(filters?: ProductFilters): Promise<Product[]>
  getProduct(id: string): Promise<Product | null>
  createProduct(input: ProductInput): Promise<Product>
  updateProduct(id: string, input: Partial<ProductInput>): Promise<Product>
  deleteProduct(id: string): Promise<void>
}
```

**Before (Mock Implementation)**:

```typescript
class MockShopService implements IShopService {
  async getProducts(): Promise<Product[]> {
    return mockProducts  // from @/lib/mock/products
  }
}
export const shopService: IShopService = new MockShopService()
```

**After (API Implementation)**:

```typescript
class ApiShopService implements IShopService {
  async getProducts(filters?: ProductFilters): Promise<Product[]> {
    return apiClient.get<Product[]>(ENDPOINTS.tenant.products.list, filters)
  }
}
export const shopService: IShopService = new ApiShopService()
```

### Type Alignment

| Frontend | Django Model | Pydantic Schema |
|----------|--------------|-----------------|
| `id: string` | `id: AutoField` | `id: str` (resolved) |
| `createdAt: string` | `created_at: DateTimeField` | `createdAt: datetime` |
| `isActive: boolean` | `is_active: BooleanField` | `isActive: bool` |
| `price: number` | `price: DecimalField` | `price: Decimal` |

### Seed Data Pattern

```python