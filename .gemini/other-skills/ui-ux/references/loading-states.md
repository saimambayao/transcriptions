# Loading States & Skeleton UI

Guide for implementing loading states in the Bangsamoro Development Platform using skeleton loaders and progressive loading patterns.

## Table of Contents
- [Why Skeletons Over Spinners](#why-skeletons-over-spinners)
- [Basic Skeleton Patterns](#basic-skeleton-patterns)
- [Component-Specific Skeletons](#component-specific-skeletons)
- [Loading State Management](#loading-state-management)
- [Accessibility](#accessibility)
- [Performance Considerations](#performance-considerations)

## Why Skeletons Over Spinners

| Aspect | Spinner | Skeleton |
|--------|---------|----------|
| Perceived speed | Feels slower | Feels faster |
| Layout shift | Causes CLS | No shift |
| User expectation | Vague | Shows structure |
| Engagement | Lower | Higher |

**Research shows**: Skeleton screens can reduce perceived wait time by up to 50%.

## Basic Skeleton Patterns

### Using shadcn/ui Skeleton

```tsx
import { Skeleton } from "@/components/ui/skeleton";

// Basic shapes
<Skeleton className="h-4 w-[250px]" />      // Text line
<Skeleton className="h-4 w-full" />          // Full width line
<Skeleton className="h-12 w-12 rounded-full" /> // Avatar
<Skeleton className="h-[200px] w-full rounded-lg" /> // Card/Image

// Multiple lines with varying widths
<div className="space-y-2">
  <Skeleton className="h-4 w-full" />
  <Skeleton className="h-4 w-4/5" />
  <Skeleton className="h-4 w-3/5" />
</div>
```

### Custom Skeleton Component

```tsx
// components/ui/skeleton-loader.tsx
import { cn } from "@/lib/utils";

interface SkeletonProps extends React.HTMLAttributes<HTMLDivElement> {
  animate?: boolean;
}

export function Skeleton({ className, animate = true, ...props }: SkeletonProps) {
  return (
    <div
      className={cn(
        "rounded-md bg-muted",
        animate && "animate-pulse",
        className
      )}
      {...props}
    />
  );
}
```

## Component-Specific Skeletons

### Product Card Skeleton

```tsx
export function ProductCardSkeleton() {
  return (
    <div className="rounded-lg border p-4 space-y-4">
      {/* Image */}
      <Skeleton className="h-48 w-full rounded-lg" />

      {/* Title */}
      <Skeleton className="h-5 w-3/4" />

      {/* Price */}
      <Skeleton className="h-6 w-1/3" />

      {/* Rating */}
      <div className="flex gap-1">
        {Array.from({ length: 5 }).map((_, i) => (
          <Skeleton key={i} className="h-4 w-4 rounded-full" />
        ))}
      </div>

      {/* Button */}
      <Skeleton className="h-10 w-full" />
    </div>
  );
}
```

### Product Grid Skeleton

```tsx
export function ProductGridSkeleton({ count = 8 }: { count?: number }) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      {Array.from({ length: count }).map((_, i) => (
        <ProductCardSkeleton key={i} />
      ))}
    </div>
  );
}
```

### Table Skeleton

```tsx
export function TableSkeleton({ rows = 5, columns = 4 }: { rows?: number; columns?: number }) {
  return (
    <div className="rounded-lg border">
      {/* Header */}
      <div className="flex border-b p-4 gap-4">
        {Array.from({ length: columns }).map((_, i) => (
          <Skeleton key={i} className="h-4 flex-1" />
        ))}
      </div>

      {/* Rows */}
      {Array.from({ length: rows }).map((_, rowIndex) => (
        <div key={rowIndex} className="flex p-4 gap-4 border-b last:border-0">
          {Array.from({ length: columns }).map((_, colIndex) => (
            <Skeleton
              key={colIndex}
              className="h-4 flex-1"
              style={{ width: `${60 + Math.random() * 40}%` }}
            />
          ))}
        </div>
      ))}
    </div>
  );
}
```

### Profile/User Card Skeleton

```tsx
export function UserCardSkeleton() {
  return (
    <div className="flex items-center gap-4 p-4">
      {/* Avatar */}
      <Skeleton className="h-12 w-12 rounded-full" />

      <div className="space-y-2 flex-1">
        {/* Name */}
        <Skeleton className="h-4 w-32" />
        {/* Email/subtitle */}
        <Skeleton className="h-3 w-48" />
      </div>
    </div>
  );
}
```

### Dashboard Stats Skeleton

```tsx
export function StatCardSkeleton() {
  return (
    <div className="rounded-lg border p-6 space-y-2">
      <Skeleton className="h-4 w-24" />
      <Skeleton className="h-8 w-32" />
      <Skeleton className="h-3 w-20" />
    </div>
  );
}

export function DashboardStatsSkeleton() {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {Array.from({ length: 4 }).map((_, i) => (
        <StatCardSkeleton key={i} />
      ))}
    </div>
  );
}
```

### Form Skeleton

```tsx
export function FormSkeleton({ fields = 4 }: { fields?: number }) {
  return (
    <div className="space-y-6">
      {Array.from({ length: fields }).map((_, i) => (
        <div key={i} className="space-y-2">
          <Skeleton className="h-4 w-24" /> {/* Label */}
          <Skeleton className="h-10 w-full" /> {/* Input */}
        </div>
      ))}
      <Skeleton className="h-10 w-32" /> {/* Submit button */}
    </div>
  );
}
```

## Loading State Management

### With TanStack Query

```tsx
import { useQuery } from '@tanstack/react-query';

function ProductList() {
  const { data, isLoading, isError, error } = useQuery({
    queryKey: ['products'],
    queryFn: fetchProducts,
  });

  if (isLoading) {
    return <ProductGridSkeleton count={8} />;
  }

  if (isError) {
    return <ErrorState message={error.message} />;
  }

  if (data.length === 0) {
    return <EmptyState message="No products found" />;
  }

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      {data.map(product => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}
```

### Suspense with Streaming

```tsx
// app/products/page.tsx
import { Suspense } from 'react';
import { ProductList } from './product-list';
import { ProductGridSkeleton } from '@/components/skeletons';

export default function ProductsPage() {
  return (
    <div>
      <h1>Products</h1>
      <Suspense fallback={<ProductGridSkeleton count={8} />}>
        <ProductList />
      </Suspense>
    </div>
  );
}
```

### Progressive Loading

Load content incrementally:

```tsx
function DashboardPage() {
  return (
    <div className="space-y-6">
      {/* Stats load first */}
      <Suspense fallback={<DashboardStatsSkeleton />}>
        <DashboardStats />
      </Suspense>

      {/* Chart loads second */}
      <Suspense fallback={<ChartSkeleton />}>
        <SalesChart />
      </Suspense>

      {/* Table loads last */}
      <Suspense fallback={<TableSkeleton rows={10} />}>
        <RecentOrders />
      </Suspense>
    </div>
  );
}
```

## Accessibility

### Required Attributes

```tsx
export function AccessibleSkeleton({ children }: { children: React.ReactNode }) {
  return (
    <div
      role="status"
      aria-busy="true"
      aria-live="polite"
    >
      <span className="sr-only">Loading...</span>
      {children}
    </div>
  );
}

// Usage
<AccessibleSkeleton>
  <ProductGridSkeleton />
</AccessibleSkeleton>
```

### Respect Reduced Motion

```tsx
import { useReducedMotion } from '@/hooks/use-reduced-motion';

export function Skeleton({ className, ...props }: SkeletonProps) {
  const prefersReducedMotion = useReducedMotion();

  return (
    <div
      className={cn(
        "rounded-md bg-muted",
        !prefersReducedMotion && "animate-pulse",
        className
      )}
      {...props}
    />
  );
}

// Hook implementation
export function useReducedMotion() {
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false);

  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReducedMotion(mediaQuery.matches);

    const handler = (e: MediaQueryListEvent) => setPrefersReducedMotion(e.matches);
    mediaQuery.addEventListener('change', handler);
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);

  return prefersReducedMotion;
}
```

## Performance Considerations

### Avoid Layout Shift

Match skeleton dimensions to actual content:

```tsx
// Good: Same height as actual card
<ProductCardSkeleton /> // h-[320px] total

// After loading
<ProductCard /> // Also ~320px

// Bad: Different heights cause CLS
<div className="h-20 animate-pulse" /> // Small skeleton
<ProductCard /> // Actual card is 320px - layout shift!
```

### Don't Overload with Skeletons

```tsx
// Good: Show a few skeletons to indicate loading
<ProductGridSkeleton count={8} />

// Bad: Show exact number (unnecessary)
<ProductGridSkeleton count={147} />
```

### Minimum Display Time

Prevent flash of skeleton for fast loads:

```tsx
import { useState, useEffect } from 'react';

function useMinimumLoadingTime(isLoading: boolean, minTime = 300) {
  const [showLoading, setShowLoading] = useState(isLoading);

  useEffect(() => {
    if (isLoading) {
      setShowLoading(true);
    } else {
      const timer = setTimeout(() => setShowLoading(false), minTime);
      return () => clearTimeout(timer);
    }
  }, [isLoading, minTime]);

  return showLoading;
}

// Usage
function ProductList() {
  const { data, isLoading } = useQuery({ ... });
  const showSkeleton = useMinimumLoadingTime(isLoading, 300);

  if (showSkeleton) {
    return <ProductGridSkeleton />;
  }

  return <div>{/* products */}</div>;
}
```

## Button Loading States

### Inline Loading

```tsx
import { Loader2 } from 'lucide-react';

<Button disabled={isSubmitting}>
  {isSubmitting ? (
    <>
      <Loader2 className="mr-2 h-4 w-4 animate-spin" />
      Saving...
    </>
  ) : (
    'Save Changes'
  )}
</Button>
```

### Loading Button Component

```tsx
interface LoadingButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  isLoading?: boolean;
  loadingText?: string;
}

export function LoadingButton({
  children,
  isLoading,
  loadingText = 'Loading...',
  disabled,
  ...props
}: LoadingButtonProps) {
  return (
    <Button disabled={disabled || isLoading} {...props}>
      {isLoading ? (
        <>
          <Loader2 className="mr-2 h-4 w-4 animate-spin" />
          {loadingText}
        </>
      ) : (
        children
      )}
    </Button>
  );
}

// Usage
<LoadingButton
  isLoading={isSubmitting}
  loadingText="Saving..."
>
  Save Changes
</LoadingButton>
```

## Error and Empty States

Always pair loading states with error and empty states:

```tsx
function DataDisplay() {
  const { data, isLoading, isError, error } = useQuery({ ... });

  // Loading
  if (isLoading) {
    return <DataSkeleton />;
  }

  // Error
  if (isError) {
    return (
      <div className="flex flex-col items-center py-12 text-center">
        <AlertCircle className="h-12 w-12 text-destructive mb-4" />
        <h3 className="text-lg font-medium">Something went wrong</h3>
        <p className="text-sm text-muted-foreground mt-1">
          {error.message}
        </p>
        <Button variant="outline" className="mt-4" onClick={() => refetch()}>
          Try Again
        </Button>
      </div>
    );
  }

  // Empty
  if (data.length === 0) {
    return (
      <div className="flex flex-col items-center py-12 text-center">
        <Package className="h-12 w-12 text-muted-foreground mb-4" />
        <h3 className="text-lg font-medium">No items yet</h3>
        <p className="text-sm text-muted-foreground mt-1">
          Get started by adding your first item
        </p>
        <Button className="mt-4">
          Add Item
        </Button>
      </div>
    );
  }

  // Success
  return <DataList data={data} />;
}
```
