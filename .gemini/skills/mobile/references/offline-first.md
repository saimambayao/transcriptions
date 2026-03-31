# Offline-First Patterns

## Overview

BARMM regions may have limited or intermittent connectivity. The mobile app implements offline-first patterns to ensure users can browse products, manage inventory, and queue orders even without internet.

## Network Status Detection

Create `lib/hooks/useNetworkStatus.ts`:

```typescript
import { useEffect, useState } from 'react'
import NetInfo, { NetInfoState } from '@react-native-community/netinfo'

export interface NetworkStatus {
  isConnected: boolean
  isInternetReachable: boolean | null
  type: string
}

export function useNetworkStatus(): NetworkStatus {
  const [status, setStatus] = useState<NetworkStatus>({
    isConnected: true,
    isInternetReachable: true,
    type: 'unknown',
  })

  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener((state: NetInfoState) => {
      setStatus({
        isConnected: state.isConnected ?? false,
        isInternetReachable: state.isInternetReachable,
        type: state.type,
      })
    })

    return () => unsubscribe()
  }, [])

  return status
}
```

## Offline Storage with MMKV

Install: `npx expo install react-native-mmkv`

Create `lib/storage/mmkv.ts`:

```typescript
import { MMKV } from 'react-native-mmkv'

export const storage = new MMKV()

// Typed storage helpers
export const offlineStorage = {
  // Products cache
  getProducts: (): Product[] => {
    const data = storage.getString('cached_products')
    return data ? JSON.parse(data) : []
  },
  setProducts: (products: Product[]) => {
    storage.set('cached_products', JSON.stringify(products))
    storage.set('cached_products_timestamp', Date.now().toString())
  },
  getProductsTimestamp: (): number => {
    const ts = storage.getString('cached_products_timestamp')
    return ts ? parseInt(ts, 10) : 0
  },

  // Pending orders (for sellers)
  getPendingOrderUpdates: (): OrderUpdate[] => {
    const data = storage.getString('pending_order_updates')
    return data ? JSON.parse(data) : []
  },
  addPendingOrderUpdate: (update: OrderUpdate) => {
    const pending = offlineStorage.getPendingOrderUpdates()
    pending.push(update)
    storage.set('pending_order_updates', JSON.stringify(pending))
  },
  clearPendingOrderUpdates: () => {
    storage.delete('pending_order_updates')
  },

  // Cart (for consumers)
  getCart: (): CartItem[] => {
    const data = storage.getString('cart')
    return data ? JSON.parse(data) : []
  },
  setCart: (items: CartItem[]) => {
    storage.set('cart', JSON.stringify(items))
  },

  // Search history
  getSearchHistory: (): string[] => {
    const data = storage.getString('search_history')
    return data ? JSON.parse(data) : []
  },
  addSearchTerm: (term: string) => {
    const history = offlineStorage.getSearchHistory()
    const updated = [term, ...history.filter(t => t !== term)].slice(0, 10)
    storage.set('search_history', JSON.stringify(updated))
  },
}
```

## TanStack Query Offline Persistence

Create `lib/api/queryClient.ts`:

```typescript
import { QueryClient } from '@tanstack/react-query'
import { createSyncStoragePersister } from '@tanstack/query-sync-storage-persister'
import { persistQueryClient } from '@tanstack/react-query-persist-client'
import { storage } from '@/lib/storage/mmkv'

// MMKV adapter for TanStack Query
const mmkvStorageAdapter = {
  getItem: (key: string) => storage.getString(key) ?? null,
  setItem: (key: string, value: string) => storage.set(key, value),
  removeItem: (key: string) => storage.delete(key),
}

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5, // 5 minutes
      gcTime: 1000 * 60 * 60 * 24, // 24 hours (formerly cacheTime)
      networkMode: 'offlineFirst',
      retry: (failureCount, error) => {
        // Don't retry on 4xx errors
        if (error instanceof Error && error.message.includes('4')) {
          return false
        }
        return failureCount < 3
      },
    },
    mutations: {
      networkMode: 'offlineFirst',
    },
  },
})

// Persist queries to MMKV
const persister = createSyncStoragePersister({
  storage: mmkvStorageAdapter,
})

persistQueryClient({
  queryClient,
  persister,
  maxAge: 1000 * 60 * 60 * 24, // 24 hours
})
```

## Optimistic Updates for Cart

```typescript
// lib/hooks/useCart.ts
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { offlineStorage } from '@/lib/storage/mmkv'

export function useAddToCart() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (item: CartItem) => {
      // Save to local storage immediately
      const cart = offlineStorage.getCart()
      const existingIndex = cart.findIndex(i => i.productId === item.productId)

      if (existingIndex >= 0) {
        cart[existingIndex].quantity += item.quantity
      } else {
        cart.push(item)
      }

      offlineStorage.setCart(cart)

      // Try to sync with server (non-blocking)
      try {
        await apiClient.post('/consumer/cart', item)
      } catch {
        // Queue for later sync
        console.log('Cart will sync when online')
      }

      return cart
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['cart'] })
    },
  })
}
```

## Background Sync for Pending Operations

```typescript
// lib/sync/backgroundSync.ts
import { useEffect } from 'react'
import { useNetworkStatus } from '@/lib/hooks/useNetworkStatus'
import { offlineStorage } from '@/lib/storage/mmkv'
import { apiClient } from '@/lib/api/client'

export function useSyncPendingOperations() {
  const { isConnected, isInternetReachable } = useNetworkStatus()

  useEffect(() => {
    if (isConnected && isInternetReachable) {
      syncPendingOrderUpdates()
    }
  }, [isConnected, isInternetReachable])
}

async function syncPendingOrderUpdates() {
  const pending = offlineStorage.getPendingOrderUpdates()
  if (pending.length === 0) return

  const results = await Promise.allSettled(
    pending.map(update =>
      apiClient.patch(`/tenant/orders/${update.orderId}/status`, {
        status: update.status,
      })
    )
  )

  // Remove successfully synced updates
  const stillPending = pending.filter((_, index) =>
    results[index].status === 'rejected'
  )

  if (stillPending.length > 0) {
    offlineStorage.clearPendingOrderUpdates()
    stillPending.forEach(update => offlineStorage.addPendingOrderUpdate(update))
  } else {
    offlineStorage.clearPendingOrderUpdates()
  }
}
```

## Offline UI Indicator

Create `components/ui/OfflineBanner.tsx`:

```typescript
import { View, Text, StyleSheet } from 'react-native'
import { WifiOff } from 'lucide-react-native'
import { useNetworkStatus } from '@/lib/hooks/useNetworkStatus'
import { Colors } from '@/constants/Colors'

export function OfflineBanner() {
  const { isConnected, isInternetReachable } = useNetworkStatus()

  if (isConnected && isInternetReachable) return null

  return (
    <View style={styles.banner}>
      <WifiOff size={16} color={Colors.white} />
      <Text style={styles.text}>
        You're offline. Some features may be limited.
      </Text>
    </View>
  )
}

const styles = StyleSheet.create({
  banner: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: Colors.warning,
    paddingVertical: 8,
    paddingHorizontal: 16,
    gap: 8,
  },
  text: {
    color: Colors.white,
    fontSize: 13,
    fontWeight: '500',
  },
})
```

## Cache Strategies by Data Type

| Data Type | Strategy | TTL | Offline Access |
|-----------|----------|-----|----------------|
| Products | Cache-first | 5 min | Yes (stale OK) |
| Categories | Cache-first | 1 hour | Yes |
| User Profile | Network-first | 1 min | Yes (cached) |
| Orders | Network-first | 30 sec | Limited |
| Cart | Local-first | N/A | Yes |
| Inventory | Network-first | 1 min | Read-only |
