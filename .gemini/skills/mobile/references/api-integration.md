# Django Ninja API Integration

## API Client Setup

Create `lib/api/client.ts`:

```typescript
import * as SecureStore from 'expo-secure-store'
import Constants from 'expo-constants'

const API_URL = Constants.expoConfig?.extra?.apiUrl || 'https://api.moromarket.bangsamoro.site'

interface RequestConfig extends RequestInit {
  params?: Record<string, string | number | boolean | undefined>
}

class ApiClient {
  private baseUrl: string

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl
  }

  private async getHeaders(): Promise<HeadersInit> {
    const token = await SecureStore.getItemAsync('accessToken')
    return {
      'Content-Type': 'application/json',
      ...(token && { Authorization: `Bearer ${token}` }),
    }
  }

  private buildUrl(endpoint: string, params?: Record<string, string | number | boolean | undefined>): string {
    const url = new URL(`${this.baseUrl}${endpoint}`)
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined) {
          url.searchParams.append(key, String(value))
        }
      })
    }
    return url.toString()
  }

  async request<T>(endpoint: string, config: RequestConfig = {}): Promise<T> {
    const { params, ...fetchConfig } = config
    const url = this.buildUrl(endpoint, params)
    const headers = await this.getHeaders()

    const response = await fetch(url, {
      ...fetchConfig,
      headers: { ...headers, ...fetchConfig.headers },
    })

    if (response.status === 401) {
      // Attempt token refresh
      const refreshed = await this.refreshToken()
      if (refreshed) {
        return this.request<T>(endpoint, config)
      }
      throw new Error('Session expired')
    }

    if (!response.ok) {
      const error = await response.json().catch(() => ({}))
      throw new Error(error.message || `Request failed: ${response.status}`)
    }

    return response.json()
  }

  private async refreshToken(): Promise<boolean> {
    try {
      const refreshToken = await SecureStore.getItemAsync('refreshToken')
      if (!refreshToken) return false

      const response = await fetch(`${this.baseUrl}/auth/refresh`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ refresh_token: refreshToken }),
      })

      if (response.ok) {
        const data = await response.json()
        await SecureStore.setItemAsync('accessToken', data.access_token)
        await SecureStore.setItemAsync('refreshToken', data.refresh_token)
        return true
      }
      return false
    } catch {
      return false
    }
  }

  get<T>(endpoint: string, params?: Record<string, string | number | boolean | undefined>): Promise<T> {
    return this.request<T>(endpoint, { method: 'GET', params })
  }

  post<T>(endpoint: string, data?: unknown): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'POST',
      body: JSON.stringify(data),
    })
  }

  patch<T>(endpoint: string, data?: unknown): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'PATCH',
      body: JSON.stringify(data),
    })
  }

  delete<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: 'DELETE' })
  }
}

export const apiClient = new ApiClient(API_URL)
```

## Authentication Service

Create `lib/services/auth.service.ts`:

```typescript
import * as SecureStore from 'expo-secure-store'
import { apiClient } from '@/lib/api/client'
import type { User, LoginCredentials, RegisterData, AuthResponse } from '@/lib/types/auth'

class AuthService {
  async login(credentials: LoginCredentials): Promise<AuthResponse> {
    const response = await fetch(`${API_URL}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        identifier: credentials.email,
        password: credentials.password,
      }),
    })

    const data = await response.json()

    if (response.ok) {
      const user: User = {
        id: data.user.id,
        email: data.user.email,
        firstName: data.user.first_name,
        lastName: data.user.last_name,
        role: data.user.role,
        roles: data.user.roles || [data.user.role],
        tenantId: data.user.tenant_id,
        tenantSlug: data.user.tenant_slug,
        tenantType: data.user.tenant_type,
        emailVerified: data.user.email_verified,
      }

      await SecureStore.setItemAsync('accessToken', data.access_token)
      await SecureStore.setItemAsync('refreshToken', data.refresh_token)
      await SecureStore.setItemAsync('user', JSON.stringify(user))

      return { success: true, user, token: data.access_token }
    }

    // Handle account lockout
    if (response.status === 429 && data.is_locked) {
      return {
        success: false,
        message: data.message,
        isLocked: true,
        remainingSeconds: data.remaining_seconds,
      }
    }

    return { success: false, message: data.message || 'Invalid credentials' }
  }

  async register(data: RegisterData): Promise<AuthResponse> {
    const response = await fetch(`${API_URL}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: data.email,
        password: data.password,
        confirm_password: data.confirmPassword,
        first_name: data.firstName,
        last_name: data.lastName,
        phone_number: data.phoneNumber,
        organization_name: data.organizationName,
        organization_type: data.organizationType,
        role: data.role || 'consumer',
      }),
    })

    const result = await response.json()

    if (response.status === 201) {
      const user: User = {
        id: result.user.id,
        email: result.user.email,
        firstName: result.user.first_name,
        lastName: result.user.last_name,
        role: result.user.role,
        roles: result.user.roles || [result.user.role],
        emailVerified: result.user.email_verified,
      }

      await SecureStore.setItemAsync('accessToken', result.access_token)
      await SecureStore.setItemAsync('refreshToken', result.refresh_token)
      await SecureStore.setItemAsync('user', JSON.stringify(user))

      return { success: true, user, token: result.access_token }
    }

    return { success: false, message: result.message || 'Registration failed' }
  }

  async logout(): Promise<void> {
    const token = await SecureStore.getItemAsync('accessToken')
    if (token) {
      try {
        await fetch(`${API_URL}/auth/logout`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          },
        })
      } catch {
        // Ignore errors - clear local tokens regardless
      }
    }

    await SecureStore.deleteItemAsync('accessToken')
    await SecureStore.deleteItemAsync('refreshToken')
    await SecureStore.deleteItemAsync('user')
  }

  async getCurrentUser(): Promise<User | null> {
    const userData = await SecureStore.getItemAsync('user')
    return userData ? JSON.parse(userData) : null
  }

  async isAuthenticated(): Promise<boolean> {
    const token = await SecureStore.getItemAsync('accessToken')
    return !!token
  }
}

export const authService = new AuthService()
```

## TanStack Query Hooks

Create `lib/hooks/useProducts.ts`:

```typescript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { apiClient } from '@/lib/api/client'
import type { Product, ProductFilters } from '@/lib/types/product'

// Query keys
export const productKeys = {
  all: ['products'] as const,
  lists: () => [...productKeys.all, 'list'] as const,
  list: (filters: ProductFilters) => [...productKeys.lists(), filters] as const,
  details: () => [...productKeys.all, 'detail'] as const,
  detail: (id: string) => [...productKeys.details(), id] as const,
}

// Fetch products list
export function useProducts(filters?: ProductFilters) {
  return useQuery({
    queryKey: productKeys.list(filters || {}),
    queryFn: () => apiClient.get<Product[]>('/public/products', filters),
    staleTime: 1000 * 60 * 5, // 5 minutes
  })
}

// Fetch single product
export function useProduct(id: string) {
  return useQuery({
    queryKey: productKeys.detail(id),
    queryFn: () => apiClient.get<Product>(`/public/products/${id}`),
    enabled: !!id,
  })
}

// Create product (seller)
export function useCreateProduct() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (data: Partial<Product>) =>
      apiClient.post<Product>('/tenant/products', data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: productKeys.lists() })
    },
  })
}

// Update product (seller)
export function useUpdateProduct() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: Partial<Product> }) =>
      apiClient.patch<Product>(`/tenant/products/${id}`, data),
    onSuccess: (_, { id }) => {
      queryClient.invalidateQueries({ queryKey: productKeys.detail(id) })
      queryClient.invalidateQueries({ queryKey: productKeys.lists() })
    },
  })
}
```

## API Endpoints Reference

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/login` | Login with email/password |
| POST | `/auth/register` | Register new user |
| POST | `/auth/logout` | Logout current user |
| POST | `/auth/refresh` | Refresh access token |
| POST | `/auth/request-password-reset` | Request password reset |
| POST | `/auth/reset-password` | Reset password with token |

### Consumer Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/consumer/profile` | Get consumer profile |
| PATCH | `/consumer/profile` | Update consumer profile |
| GET | `/consumer/orders` | List consumer orders |
| GET | `/consumer/orders/{id}` | Get order detail |
| GET | `/consumer/saved-items` | List saved/wishlist items |
| POST | `/consumer/saved-items` | Add to wishlist |
| DELETE | `/consumer/saved-items/{id}` | Remove from wishlist |

### Public/Marketplace Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/public/products` | List products |
| GET | `/public/products/{id}` | Get product detail |
| GET | `/public/cooperatives` | List cooperatives |
| GET | `/public/social-enterprises` | List social enterprises |
| GET | `/public/featured` | Get featured items |

### Tenant (Seller) Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tenant/dashboard/stats` | Get dashboard stats |
| GET | `/tenant/products` | List seller's products |
| POST | `/tenant/products` | Create product |
| PATCH | `/tenant/products/{id}` | Update product |
| DELETE | `/tenant/products/{id}` | Delete product |
| GET | `/tenant/orders` | List seller's orders |
| PATCH | `/tenant/orders/{id}/status` | Update order status |
| GET | `/tenant/inventory/alerts` | Get low stock alerts |

## Error Handling

```typescript
// lib/api/errors.ts
export class ApiError extends Error {
  status: number
  code?: string

  constructor(message: string, status: number, code?: string) {
    super(message)
    this.name = 'ApiError'
    this.status = status
    this.code = code
  }
}

// Handle in components
import { Alert } from 'react-native'

function handleApiError(error: unknown) {
  if (error instanceof ApiError) {
    if (error.status === 401) {
      // Redirect to login
      return
    }
    Alert.alert('Error', error.message)
  } else {
    Alert.alert('Error', 'Something went wrong. Please try again.')
  }
}
```
