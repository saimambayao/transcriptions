# Performance Patterns

Next.js and React performance optimization for CSEA.

## Image Optimization

```tsx
import Image from "next/image"

// Automatic optimization with next/image
<Image
  src="/products/item.jpg"
  alt="Product"
  width={300}
  height={200}
  placeholder="blur"
  blurDataURL="/placeholder.svg"
/>

// Priority for above-the-fold images
<Image src="/hero.jpg" alt="Hero" priority />

// Responsive images
<Image
  src="/hero.jpg"
  alt="Hero"
  sizes="(max-width: 768px) 100vw, 50vw"
  fill
  className="object-cover"
/>
```

## Code Splitting

```tsx
import dynamic from "next/dynamic"

// Lazy load heavy components
const Chart = dynamic(() => import("@/components/Chart"), {
  loading: () => <Skeleton className="h-[300px]" />,
  ssr: false, // Disable SSR for client-only components
})

// Lazy load modal content
const ProductModal = dynamic(() => import("./ProductModal"))
```

## Data Fetching with TanStack Query

```tsx
import { useQuery } from "@tanstack/react-query"

// Efficient data fetching with caching
const { data, isLoading } = useQuery({
  queryKey: ["cooperatives", filters],
  queryFn: () => fetchCooperatives(filters),
  staleTime: 5 * 60 * 1000, // 5 minutes
  gcTime: 10 * 60 * 1000, // 10 minutes
})

// Prefetch on hover
const queryClient = useQueryClient()
const prefetch = () => {
  queryClient.prefetchQuery({
    queryKey: ["cooperative", id],
    queryFn: () => fetchCooperative(id),
  })
}

<Link href={`/coop/${id}`} onMouseEnter={prefetch}>
  View Details
</Link>
```

## React Optimization

```tsx
import { memo, useMemo, useCallback } from "react"

// Memoize expensive computations
const sortedItems = useMemo(() => {
  return items.sort((a, b) => a.name.localeCompare(b.name))
}, [items])

// Memoize callbacks for child components
const handleClick = useCallback(() => {
  setSelected(id)
}, [id])

// Memoize components that receive stable props
const MemoizedCard = memo(function Card({ item }) {
  return <div>{item.name}</div>
})
```

## Virtualization

```tsx
import { useVirtualizer } from "@tanstack/react-virtual"

// Virtualize long lists
export function VirtualList({ items }) {
  const parentRef = useRef(null)

  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
  })

  return (
    <div ref={parentRef} className="h-[400px] overflow-auto">
      <div style={{ height: virtualizer.getTotalSize() }}>
        {virtualizer.getVirtualItems().map((virtualRow) => (
          <div
            key={virtualRow.key}
            style={{
              height: virtualRow.size,
              transform: `translateY(${virtualRow.start}px)`,
            }}
          >
            {items[virtualRow.index].name}
          </div>
        ))}
      </div>
    </div>
  )
}
```

## Bundle Optimization

```tsx
// Import only what you need from libraries
import { format } from "date-fns" // Good
// import * as dateFns from "date-fns" // Bad

// Use tree-shakable icons
import { Building2 } from "lucide-react" // Good
// import * as Icons from "lucide-react" // Bad
```

## Loading States

```tsx
import { Skeleton } from "@/components/ui/skeleton"

// Skeleton loading for better perceived performance
export function CardSkeleton() {
  return (
    <Card>
      <CardHeader>
        <Skeleton className="h-6 w-1/2" />
      </CardHeader>
      <CardContent>
        <Skeleton className="h-4 w-full mb-2" />
        <Skeleton className="h-4 w-3/4" />
      </CardContent>
    </Card>
  )
}

// Suspense for component loading
<Suspense fallback={<CardSkeleton />}>
  <AsyncComponent />
</Suspense>
```

## Font Optimization

```tsx
// In layout.tsx - Next.js font optimization
import { Inter } from "next/font/google"

const inter = Inter({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-inter",
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.variable}>
      <body>{children}</body>
    </html>
  )
}
```

## Performance Metrics

```tsx
// Web Vitals targets for CSEA
// LCP (Largest Contentful Paint): < 2.5s
// FID (First Input Delay): < 100ms
// CLS (Cumulative Layout Shift): < 0.1

// Use next/web-vitals for monitoring
export function reportWebVitals(metric) {
  console.log(metric)
}
```

