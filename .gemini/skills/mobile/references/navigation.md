# React Navigation Patterns

## Navigation Structure

MoroMarket Mobile uses a role-based navigation structure with shared authentication.

```
App
├── (auth)                    # Unauthenticated screens
│   ├── login
│   ├── register
│   ├── forgot-password
│   └── verify-email
│
├── (consumer)                # Consumer role screens
│   └── (tabs)
│       ├── home              # Marketplace home
│       ├── search            # Product search
│       ├── cart              # Shopping cart
│       ├── orders            # Order history
│       └── profile           # Consumer profile
│
└── (seller)                  # Seller role screens
    └── (tabs)
        ├── dashboard         # Sales overview
        ├── products          # Product management
        ├── orders            # Order management
        ├── inventory         # Stock management
        └── profile           # Business profile
```

## File-Based Routing (Expo Router)

### Auth Group: `app/(auth)/_layout.tsx`

```typescript
import { Stack } from 'expo-router'

export default function AuthLayout() {
  return (
    <Stack
      screenOptions={{
        headerStyle: { backgroundColor: '#0056D2' },
        headerTintColor: '#fff',
        headerTitleStyle: { fontWeight: '600' },
      }}
    >
      <Stack.Screen name="login" options={{ title: 'Sign In' }} />
      <Stack.Screen name="register" options={{ title: 'Create Account' }} />
      <Stack.Screen name="forgot-password" options={{ title: 'Reset Password' }} />
    </Stack>
  )
}
```

### Consumer Tabs: `app/(consumer)/(tabs)/_layout.tsx`

```typescript
import { Tabs } from 'expo-router'
import { Home, Search, ShoppingCart, Package, User } from 'lucide-react-native'
import { Colors } from '@/constants/Colors'

export default function ConsumerTabsLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors.primary,
        tabBarInactiveTintColor: Colors.gray[400],
        tabBarStyle: {
          borderTopWidth: 1,
          borderTopColor: Colors.gray[200],
        },
        headerStyle: { backgroundColor: Colors.primary },
        headerTintColor: '#fff',
      }}
    >
      <Tabs.Screen
        name="home"
        options={{
          title: 'Home',
          tabBarIcon: ({ color, size }) => <Home size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="search"
        options={{
          title: 'Search',
          tabBarIcon: ({ color, size }) => <Search size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="cart"
        options={{
          title: 'Cart',
          tabBarIcon: ({ color, size }) => <ShoppingCart size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="orders"
        options={{
          title: 'Orders',
          tabBarIcon: ({ color, size }) => <Package size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          title: 'Profile',
          tabBarIcon: ({ color, size }) => <User size={size} color={color} />,
        }}
      />
    </Tabs>
  )
}
```

### Seller Tabs: `app/(seller)/(tabs)/_layout.tsx`

```typescript
import { Tabs } from 'expo-router'
import { LayoutDashboard, Package, ClipboardList, Warehouse, Building2 } from 'lucide-react-native'
import { Colors } from '@/constants/Colors'

export default function SellerTabsLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors.primary,
        tabBarInactiveTintColor: Colors.gray[400],
        headerStyle: { backgroundColor: Colors.primary },
        headerTintColor: '#fff',
      }}
    >
      <Tabs.Screen
        name="dashboard"
        options={{
          title: 'Dashboard',
          tabBarIcon: ({ color, size }) => <LayoutDashboard size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="products"
        options={{
          title: 'Products',
          tabBarIcon: ({ color, size }) => <Package size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="orders"
        options={{
          title: 'Orders',
          tabBarIcon: ({ color, size }) => <ClipboardList size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="inventory"
        options={{
          title: 'Inventory',
          tabBarIcon: ({ color, size }) => <Warehouse size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          title: 'Business',
          tabBarIcon: ({ color, size }) => <Building2 size={size} color={color} />,
        }}
      />
    </Tabs>
  )
}
```

## Protected Routes

### Auth Guard: `lib/providers/AuthProvider.tsx`

```typescript
import { createContext, useContext, useEffect, useState } from 'react'
import { useRouter, useSegments } from 'expo-router'
import * as SecureStore from 'expo-secure-store'
import type { User } from '@/lib/types/auth'

interface AuthContextType {
  user: User | null
  isLoading: boolean
  signIn: (email: string, password: string) => Promise<void>
  signOut: () => Promise<void>
}

const AuthContext = createContext<AuthContextType | null>(null)

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const router = useRouter()
  const segments = useSegments()

  // Check authentication state on mount
  useEffect(() => {
    checkAuth()
  }, [])

  // Handle navigation based on auth state
  useEffect(() => {
    if (isLoading) return

    const inAuthGroup = segments[0] === '(auth)'

    if (!user && !inAuthGroup) {
      router.replace('/login')
    } else if (user && inAuthGroup) {
      // Redirect based on role
      const destination = user.role === 'tenant' ? '/(seller)/dashboard' : '/(consumer)/home'
      router.replace(destination)
    }
  }, [user, segments, isLoading])

  async function checkAuth() {
    try {
      const token = await SecureStore.getItemAsync('accessToken')
      const userData = await SecureStore.getItemAsync('user')

      if (token && userData) {
        setUser(JSON.parse(userData))
      }
    } catch (error) {
      console.error('Auth check failed:', error)
    } finally {
      setIsLoading(false)
    }
  }

  async function signIn(email: string, password: string) {
    // Implementation in api-integration.md
  }

  async function signOut() {
    await SecureStore.deleteItemAsync('accessToken')
    await SecureStore.deleteItemAsync('refreshToken')
    await SecureStore.deleteItemAsync('user')
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, isLoading, signIn, signOut }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (!context) throw new Error('useAuth must be used within AuthProvider')
  return context
}
```

## Deep Linking

Configure deep linking in `app.config.ts`:

```typescript
{
  scheme: 'moromarket',
  web: {
    bundler: 'metro',
  },
}
```

Example deep links:
- `moromarket://product/123` - Open product detail
- `moromarket://order/456` - Open order detail
- `moromarket://seller/dashboard` - Open seller dashboard

## Navigation Helpers

```typescript
// lib/navigation/helpers.ts
import { router } from 'expo-router'

export const navigation = {
  // Consumer navigation
  toProduct: (id: string) => router.push(`/(consumer)/product/${id}`),
  toCart: () => router.push('/(consumer)/cart'),
  toCheckout: () => router.push('/(consumer)/checkout'),
  toOrder: (id: string) => router.push(`/(consumer)/orders/${id}`),

  // Seller navigation
  toProductEdit: (id: string) => router.push(`/(seller)/products/${id}/edit`),
  toOrderDetail: (id: string) => router.push(`/(seller)/orders/${id}`),
  toInventoryAlert: () => router.push('/(seller)/inventory/alerts'),

  // Auth navigation
  toLogin: () => router.replace('/login'),
  toRegister: () => router.push('/register'),

  // Common
  goBack: () => router.back(),
}
```
