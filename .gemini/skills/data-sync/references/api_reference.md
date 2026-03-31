# Sync API Reference

## Data Sync Endpoints

This reference documents all API endpoints involved in portal-storefront data synchronization.

## Portal Endpoints (Authenticated)

All portal endpoints require JWT authentication and enforce organization scoping.

### Profile Management

```
PUT /api/tenant/{shortname}/profile
```
Updates cooperative/SE profile data.

**Request:**
```json
{
  "name": "string",
  "tagline": "string",
  "description": "string",
  "logo": "string (URL)",
  "primaryColor": "string (hex)"
}
```

**Response:**
```json
{
  "id": "integer",
  "name": "string",
  "shortname": "string",
  "tagline": "string",
  "description": "string",
  "logo": "string",
  "primaryColor": "string",
  "updatedAt": "datetime"
}
```

### Business Information

```
PUT /api/tenant/{shortname}/business
```
Updates business details (address, contact, hours).

**Request:**
```json
{
  "address": "string",
  "phone": "string",
  "email": "string",
  "operatingHours": {
    "monday": {"open": "09:00", "close": "17:00"},
    "tuesday": {"open": "09:00", "close": "17:00"}
  }
}
```

### Products

```
GET /api/tenant/{shortname}/products
POST /api/tenant/{shortname}/products
PUT /api/tenant/{shortname}/products/{id}
DELETE /api/tenant/{shortname}/products/{id}
```

**Product Schema:**
```json
{
  "id": "integer",
  "name": "string",
  "description": "string",
  "price": "decimal",
  "images": ["string"],
  "category": "string",
  "stock": "integer",
  "isActive": "boolean"
}
```

### Publishing

```
POST /api/tenant/{shortname}/publish
```
Publishes current draft to live storefront.

**Response:**
```json
{
  "publishedAt": "datetime",
  "status": "published"
}
```

```
GET /api/tenant/{shortname}/publish-status
```
Gets current publish state.

**Response:**
```json
{
  "isDraft": "boolean",
  "lastPublishedAt": "datetime",
  "hasPendingChanges": "boolean"
}
```

## Storefront Endpoints (Public)

All storefront endpoints are public (no auth required) and only return published data.

### Cooperative/SE Profile

```
GET /api/public/cooperatives/{shortname}
GET /api/public/social-enterprises/{shortname}
```

**Response:**
```json
{
  "name": "string",
  "shortname": "string",
  "tagline": "string",
  "description": "string",
  "logo": "string",
  "primaryColor": "string",
  "address": "string",
  "phone": "string",
  "email": "string"
}
```

### Products

```
GET /api/public/cooperatives/{shortname}/products
GET /api/public/social-enterprises/{shortname}/products
```

**Query Parameters:**
- `category`: Filter by category
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20)

**Response:**
```json
{
  "items": [
    {
      "id": "integer",
      "name": "string",
      "description": "string",
      "price": "decimal",
      "images": ["string"],
      "category": "string"
    }
  ],
  "total": "integer",
  "page": "integer",
  "pages": "integer"
}
```

### Featured Products

```
GET /api/public/cooperatives/{shortname}/products/featured
```

Returns products marked as featured (max 6).

## Query Key Patterns

Consistent query keys ensure proper cache invalidation.

### Portal Query Keys

```typescript
// Profile
['tenant', 'profile', shortname]

// Business
['tenant', 'business', shortname]

// Products list
['tenant', 'products', shortname]

// Single product
['tenant', 'products', shortname, productId]

// Publish status
['tenant', 'publish-status', shortname]
```

### Storefront Query Keys

```typescript
// Cooperative profile
['cooperative', shortname]

// Social enterprise profile
['social-enterprise', shortname]

// Products
['cooperative', shortname, 'products']
['social-enterprise', shortname, 'products']

// Featured products
['cooperative', shortname, 'products', 'featured']
```

## Cache Invalidation Matrix

When data changes in portal, these storefront queries should be invalidated:

| Portal Change | Invalidate Storefront Queries |
|---------------|------------------------------|
| Profile update | `['cooperative', shortname]` |
| Business update | `['cooperative', shortname]` |
| Product create/update | `['cooperative', shortname, 'products']`, `['cooperative', shortname, 'products', 'featured']` |
| Publish action | ALL storefront queries for shortname |

## Error Codes

| Code | Meaning |
|------|---------|
| 400 | Invalid request data |
| 401 | Not authenticated (portal endpoints) |
| 403 | Not authorized for this organization |
| 404 | Cooperative/SE or product not found |
| 409 | Conflict (e.g., shortname already exists) |
| 500 | Server error |

## Rate Limits

- Portal endpoints: 100 requests/minute
- Public endpoints: 1000 requests/minute
- Publish endpoint: 10 requests/minute
