# Accessibility Patterns

WCAG 2.1 AA accessibility patterns for CSEA with React and shadcn/ui.

## Semantic HTML

```tsx
// Use semantic elements
<header>Navigation</header>
<main>Main content</main>
<nav>Navigation links</nav>
<aside>Sidebar</aside>
<footer>Footer</footer>

// Headings in logical order
<h1>Page Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
```

## Images

```tsx
// Always include alt text
<Image src="/logo.png" alt="CSEA Logo" width={120} height={40} />

// Decorative images
<Image src="/bg-pattern.png" alt="" aria-hidden="true" />
```

## Forms

```tsx
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"

// Associate labels with inputs
<div className="space-y-2">
  <Label htmlFor="email">
    Email <span className="text-red-600" aria-hidden="true">*</span>
    <span className="sr-only">(required)</span>
  </Label>
  <Input
    id="email"
    type="email"
    aria-required="true"
    aria-describedby="email-error email-hint"
    className="focus-visible:ring-negosyo-blue"
  />
  <p id="email-hint" className="text-sm text-gray-500">We'll never share your email.</p>
  <p id="email-error" className="text-sm text-red-600" role="alert">
    Please enter a valid email address.
  </p>
</div>

// Error handling with aria-invalid
<Input
  aria-invalid={!!errors.email}
  aria-describedby={errors.email ? "email-error" : undefined}
/>
```

## Buttons

```tsx
import { Button } from "@/components/ui/button"

// Icon buttons need aria-label
<Button variant="ghost" size="icon" aria-label="Close menu">
  <X className="h-5 w-5" />
</Button>

// Loading state
<Button disabled aria-busy="true">
  <Loader2 className="mr-2 h-4 w-4 animate-spin" aria-hidden="true" />
  Saving...
</Button>
```

## Focus Management

```tsx
// Focus ring for keyboard navigation
<Button className="focus-visible:ring-2 focus-visible:ring-negosyo-blue focus-visible:ring-offset-2">
  Submit
</Button>

// Focus trap in modals (shadcn/ui handles this)
<Dialog>
  <DialogContent>
    {/* Focus is trapped inside */}
  </DialogContent>
</Dialog>
```

## Screen Reader Utilities

```tsx
// Visually hidden but accessible
<span className="sr-only">Open navigation menu</span>

// Hide decorative content
<Icon className="h-5 w-5" aria-hidden="true" />

// Live regions for dynamic updates
<div aria-live="polite" aria-atomic="true">
  {statusMessage}
</div>
```

## Touch Targets

```tsx
// Minimum 44x44px touch targets
<Button className="min-h-[44px] min-w-[44px]">
  Submit
</Button>

<Link href="/page" className="inline-flex items-center p-3 min-h-[44px]">
  Link text
</Link>
```

## Color Contrast

```tsx
// Negosyo Blue (#0056D2) on white passes AA for normal text
// Ensure text contrast ratio >= 4.5:1 for normal text
// Ensure text contrast ratio >= 3:1 for large text (18px+ or 14px+ bold)

// Good contrast
<p className="text-gray-700">Body text (high contrast)</p>
<p className="text-gray-600">Secondary text (meets AA)</p>

// Avoid low contrast
// <p className="text-gray-400">Too light for body text</p>
```

## Skip Links

```tsx
// Add to layout for keyboard users
<a
  href="#main-content"
  className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:bg-white focus:px-4 focus:py-2 focus:text-negosyo-blue focus:shadow-lg"
>
  Skip to main content
</a>

<main id="main-content" tabIndex={-1}>
  {/* Main content */}
</main>
```

## Testing Checklist

- [ ] All images have alt text
- [ ] Forms have associated labels
- [ ] Color contrast meets AA standards
- [ ] Focus indicators are visible
- [ ] Modals trap focus correctly
- [ ] Skip links work for keyboard users
- [ ] Screen reader announces dynamic content
- [ ] Touch targets are at least 44x44px

