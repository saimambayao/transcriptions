# Mobile-First Design

Comprehensive guide for building mobile-first responsive interfaces in the Bangsamoro Development Platform.

## Table of Contents
- [Why Mobile-First](#why-mobile-first)
- [Responsive Breakpoints](#responsive-breakpoints)
- [Touch-Friendly Design](#touch-friendly-design)
- [Layout Patterns](#layout-patterns)
- [Navigation Patterns](#navigation-patterns)
- [Performance Optimization](#performance-optimization)
- [Testing](#testing)

## Why Mobile-First

### Statistics (2025)
- 59-64% of global web traffic is mobile
- 73% of e-commerce traffic comes from mobile devices
- 74% of users return to mobile-friendly sites
- 67% increase in purchase likelihood on mobile-optimized sites
- Google uses mobile-first indexing for SEO

### Benefits
1. **Forces prioritization** - Limited space means focusing on essential content
2. **Progressive enhancement** - Add complexity as screen size increases
3. **Better performance** - Leaner base code, faster initial load
4. **SEO advantages** - Google prioritizes mobile-friendly sites

## Responsive Breakpoints

### Tailwind CSS v4 Default Breakpoints

```css
/* Mobile-first: No prefix = mobile */
/* sm: 640px and up */
/* md: 768px and up */
/* lg: 1024px and up */
/* xl: 1280px and up */
/* 2xl: 1536px and up */
```

### Usage Pattern

Always start with mobile, then add larger breakpoints:

```tsx
// Good: Mobile-first
<div className="
  grid grid-cols-1      /* Mobile: 1 column */
  sm:grid-cols-2        /* Small: 2 columns */
  lg:grid-cols-4        /* Large: 4 columns */
  gap-4                 /* Consistent gap */
">

// Bad: Desktop-first (harder to maintain)
<div className="
  grid grid-cols-4
  md:grid-cols-2
  sm:grid-cols-1
">
```

### Content-Based Breakpoints

Let content determine breakpoints, not devices:

```tsx
// Good: Break when content needs it
<div className="
  max-w-prose            /* Optimal reading width */
  mx-auto
  px-4 sm:px-6 lg:px-8   /* Progressive padding */
">

// Product grid that breaks based on card minimum width
<div className="
  grid
  grid-cols-[repeat(auto-fill,minmax(280px,1fr))]
  gap-6
">
```

## Touch-Friendly Design

### Minimum Touch Targets

**WCAG 2.2 requires minimum 44x44px touch targets, but 48x48px is recommended.**

```tsx
// Good: Adequate touch target
<Button className="h-12 px-6">  {/* 48px height */}
  Add to Cart
</Button>

// Good: Icon button with padding
<Button variant="ghost" size="icon" className="h-12 w-12">
  <Menu className="h-6 w-6" />
</Button>

// Bad: Too small
<Button className="h-8 px-2">  {/* Only 32px */}
  Add
</Button>
```

### Touch Target Spacing

```tsx
// Good: Adequate spacing between targets
<div className="flex gap-4">  {/* 16px gap */}
  <Button>Option 1</Button>
  <Button>Option 2</Button>
</div>

// Bad: Targets too close
<div className="flex gap-1">  {/* Only 4px gap */}
  <Button>Option 1</Button>
  <Button>Option 2</Button>
</div>
```

### Thumb-Friendly Zones

Place primary actions in easy-to-reach areas:

```tsx
// Bottom action bar for mobile
<div className="
  fixed bottom-0 left-0 right-0
  p-4
  bg-background border-t
  md:hidden  /* Hide on desktop */
">
  <Button className="w-full h-12">
    Add to Cart - PHP 1,200
  </Button>
</div>
```

## Layout Patterns

### Stack to Grid

```tsx
// Cards: Stack on mobile, grid on larger screens
<div className="
  flex flex-col          /* Mobile: stack */
  md:grid md:grid-cols-2 /* Tablet: 2 columns */
  lg:grid-cols-3         /* Desktop: 3 columns */
  gap-6
">
  {products.map(product => (
    <ProductCard key={product.id} product={product} />
  ))}
</div>
```

### Sidebar to Drawer

```tsx
// Desktop: sidebar, Mobile: drawer/sheet
function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex">
      {/* Desktop sidebar */}
      <aside className="hidden lg:block w-64 border-r min-h-screen p-4">
        <Navigation />
      </aside>

      {/* Mobile drawer */}
      <Sheet>
        <SheetTrigger asChild className="lg:hidden">
          <Button variant="ghost" size="icon">
            <Menu className="h-6 w-6" />
          </Button>
        </SheetTrigger>
        <SheetContent side="left" className="w-64">
          <Navigation />
        </SheetContent>
      </Sheet>

      <main className="flex-1 p-4 lg:p-8">
        {children}
      </main>
    </div>
  );
}
```

### Responsive Typography

```tsx
<h1 className="
  text-2xl           /* Mobile: 24px */
  sm:text-3xl        /* Small: 30px */
  lg:text-4xl        /* Large: 36px */
  font-bold
">
  Page Title
</h1>

<p className="
  text-sm            /* Mobile: 14px */
  sm:text-base       /* Small+: 16px */
  text-muted-foreground
">
  Description text that adjusts based on screen size.
</p>
```

### Responsive Spacing

```tsx
<section className="
  py-8               /* Mobile: 32px vertical */
  md:py-12           /* Tablet: 48px */
  lg:py-16           /* Desktop: 64px */
  px-4               /* Mobile: 16px horizontal */
  sm:px-6            /* Small: 24px */
  lg:px-8            /* Large: 32px */
">
  {/* Content */}
</section>
```

## Navigation Patterns

### Mobile Navigation Header

```tsx
function MobileHeader() {
  return (
    <header className="
      sticky top-0 z-50
      bg-background/95 backdrop-blur
      border-b
      lg:hidden
    ">
      <div className="flex items-center justify-between h-14 px-4">
        {/* Menu trigger */}
        <Sheet>
          <SheetTrigger asChild>
            <Button variant="ghost" size="icon" className="h-10 w-10">
              <Menu className="h-5 w-5" />
              <span className="sr-only">Open menu</span>
            </Button>
          </SheetTrigger>
          <SheetContent side="left">
            <MobileNav />
          </SheetContent>
        </Sheet>

        {/* Logo */}
        <Link href="/" className="font-bold text-lg">
          CSEA
        </Link>

        {/* Cart */}
        <Button variant="ghost" size="icon" className="h-10 w-10">
          <ShoppingCart className="h-5 w-5" />
          <span className="sr-only">Cart</span>
        </Button>
      </div>
    </header>
  );
}
```

### Bottom Navigation (Mobile App Pattern)

```tsx
function BottomNav() {
  const pathname = usePathname();

  const links = [
    { href: '/', icon: Home, label: 'Home' },
    { href: '/products', icon: Package, label: 'Products' },
    { href: '/cart', icon: ShoppingCart, label: 'Cart' },
    { href: '/account', icon: User, label: 'Account' },
  ];

  return (
    <nav className="
      fixed bottom-0 left-0 right-0
      bg-background border-t
      safe-area-inset-bottom  /* iOS safe area */
      md:hidden
    ">
      <div className="flex justify-around">
        {links.map(({ href, icon: Icon, label }) => (
          <Link
            key={href}
            href={href}
            className={cn(
              "flex flex-col items-center py-2 px-4 min-w-[64px]",
              pathname === href
                ? "text-primary"
                : "text-muted-foreground"
            )}
          >
            <Icon className="h-5 w-5" />
            <span className="text-xs mt-1">{label}</span>
          </Link>
        ))}
      </div>
    </nav>
  );
}
```

### Breadcrumbs (Collapsible on Mobile)

```tsx
function Breadcrumbs({ items }: { items: BreadcrumbItem[] }) {
  // Show all on desktop, collapse middle items on mobile
  const visibleItems = items.length > 3
    ? [items[0], { label: '...', href: '' }, items[items.length - 1]]
    : items;

  return (
    <nav aria-label="Breadcrumb">
      <ol className="flex items-center gap-2 text-sm">
        {/* Mobile: collapsed */}
        <div className="flex items-center gap-2 sm:hidden">
          {visibleItems.map((item, i) => (
            <BreadcrumbItem key={i} item={item} isLast={i === visibleItems.length - 1} />
          ))}
        </div>

        {/* Desktop: full */}
        <div className="hidden sm:flex items-center gap-2">
          {items.map((item, i) => (
            <BreadcrumbItem key={i} item={item} isLast={i === items.length - 1} />
          ))}
        </div>
      </ol>
    </nav>
  );
}
```

## Performance Optimization

### Responsive Images

```tsx
import Image from 'next/image';

// Use srcset for responsive images
<Image
  src="/product.jpg"
  alt="Product"
  width={800}
  height={600}
  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
  className="w-full h-auto object-cover"
  priority={isAboveFold}
/>
```

### Lazy Loading

```tsx
// Lazy load below-fold images
<Image
  src="/product.jpg"
  alt="Product"
  loading="lazy"  // Default in Next.js Image
/>

// Lazy load components
const HeavyComponent = dynamic(
  () => import('@/components/heavy-component'),
  { loading: () => <Skeleton className="h-[400px]" /> }
);
```

### Conditional Rendering

```tsx
// Only render complex components on desktop
function ProductPage() {
  return (
    <div>
      {/* Always show */}
      <ProductInfo />

      {/* Desktop only: 3D viewer */}
      <div className="hidden lg:block">
        <Product3DViewer />
      </div>

      {/* Mobile: simpler image gallery */}
      <div className="lg:hidden">
        <ProductImageCarousel />
      </div>
    </div>
  );
}
```

### Reduce Motion on Mobile

```tsx
// Simpler animations on mobile
<div className="
  transition-transform duration-200
  hover:scale-105
  md:hover:scale-110  /* Larger effect on desktop */
">
```

## Testing

### Device Emulation

```bash
# Chrome DevTools
1. Open DevTools (F12)
2. Toggle device toolbar (Ctrl+Shift+M)
3. Select device or set custom dimensions
4. Test at: 320px, 375px, 414px, 768px, 1024px, 1280px
```

### Real Device Testing

| Platform | Browsers to Test |
|----------|-----------------|
| iOS | Safari, Chrome |
| Android | Chrome, Samsung Internet |
| Desktop | Chrome, Firefox, Safari, Edge |

### Testing Checklist

- [ ] Test at 320px width (smallest phones)
- [ ] Test at 375px width (iPhone SE)
- [ ] Test at 414px width (iPhone Plus)
- [ ] Test at 768px width (tablets)
- [ ] Test in landscape orientation
- [ ] Test with on-screen keyboard
- [ ] Test touch interactions (tap, swipe, pinch)
- [ ] Test with slow 3G network throttling
- [ ] Verify touch targets are 48x48px minimum
- [ ] Check content doesn't require horizontal scroll
- [ ] Verify forms are usable on mobile

### Common Mobile Issues

| Issue | Solution |
|-------|----------|
| Horizontal scroll | Use `overflow-x-hidden` on body, check for fixed widths |
| Tiny text | Minimum 16px for body text on mobile |
| Small touch targets | Minimum 48x48px for interactive elements |
| Slow load | Optimize images, lazy load, reduce JS |
| Keyboard covers input | Use `scroll-margin-bottom` or scroll into view |
| Double-tap zoom | Add `touch-action: manipulation` |

### iOS Safe Areas

Handle the notch and home indicator:

```css
/* In global CSS */
.safe-area-inset-top {
  padding-top: env(safe-area-inset-top);
}

.safe-area-inset-bottom {
  padding-bottom: env(safe-area-inset-bottom);
}
```

```tsx
// Usage
<header className="safe-area-inset-top">
  {/* Header content */}
</header>

<nav className="fixed bottom-0 pb-[env(safe-area-inset-bottom)]">
  {/* Bottom nav */}
</nav>
```
