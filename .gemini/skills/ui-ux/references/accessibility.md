# Accessibility Guidelines (WCAG 2.2)

Comprehensive accessibility guide for Bangsamoro Development Platform, targeting WCAG 2.2 Level AA compliance.

## Table of Contents
- [Color & Contrast](#color--contrast)
- [Keyboard Navigation](#keyboard-navigation)
- [Screen Readers](#screen-readers)
- [Focus Management](#focus-management)
- [Forms & Inputs](#forms--inputs)
- [Images & Media](#images--media)
- [Motion & Animation](#motion--animation)
- [Testing Tools](#testing-tools)

## Color & Contrast

### Minimum Contrast Ratios

| Element | Minimum Ratio | Tool |
|---------|---------------|------|
| Normal text (<18px) | 4.5:1 | WebAIM Contrast Checker |
| Large text (>=18px or 14px bold) | 3:1 | WebAIM Contrast Checker |
| UI components & graphics | 3:1 | WebAIM Contrast Checker |
| Focus indicators | 3:1 | WebAIM Contrast Checker |

### Negosyo Color Accessibility

```css
/* Accessible color combinations */
--negosyo-blue: #0056D2;     /* On white: 4.63:1 - PASS */
--success: #16a34a;          /* On white: 4.52:1 - PASS */
--error: #dc2626;            /* On white: 4.64:1 - PASS */

/* Never use color alone to convey information */
```

### Don't Rely on Color Alone

Always pair color with another indicator:

```tsx
// Good: Color + Icon
<Badge variant="destructive">
  <XCircle className="h-3 w-3 mr-1" />
  Rejected
</Badge>

// Bad: Color only
<Badge className="bg-red-500">Rejected</Badge>
```

## Keyboard Navigation

### All Interactive Elements Must Be Focusable

```tsx
// Buttons are focusable by default
<Button>Click me</Button>

// Custom interactive elements need tabIndex
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleClick();
    }
  }}
>
  Custom Button
</div>
```

### Keyboard Shortcuts

| Action | Key |
|--------|-----|
| Activate button/link | Enter or Space |
| Close modal/dropdown | Escape |
| Navigate options | Arrow keys |
| Select option | Enter |
| Move focus | Tab / Shift+Tab |

### Skip Links

Add skip links for keyboard users:

```tsx
// At the very top of the page
<a
  href="#main-content"
  className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:bg-background focus:px-4 focus:py-2 focus:rounded"
>
  Skip to main content
</a>

// Main content area
<main id="main-content">
  {/* Page content */}
</main>
```

## Screen Readers

### Semantic HTML

Use proper HTML elements:

```tsx
// Good: Semantic HTML
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/products">Products</a></li>
  </ul>
</nav>

<main>
  <article>
    <h1>Page Title</h1>
    <section aria-labelledby="section-heading">
      <h2 id="section-heading">Section</h2>
    </section>
  </article>
</main>

// Bad: Div soup
<div class="nav">
  <div class="nav-item">Home</div>
</div>
```

### ARIA Labels

```tsx
// Icon-only buttons MUST have labels
<Button variant="ghost" size="icon" aria-label="Close dialog">
  <X className="h-4 w-4" />
</Button>

// Links with non-descriptive text
<a href="/profile" aria-label="View your profile">
  View <span aria-hidden="true">&rarr;</span>
</a>

// Form fields
<Input
  id="email"
  aria-label="Email address"
  aria-describedby="email-hint"
/>
<p id="email-hint" className="text-sm text-muted-foreground">
  We'll never share your email
</p>
```

### Live Regions

Announce dynamic content changes:

```tsx
// Toast notifications
<div
  role="status"
  aria-live="polite"
  aria-atomic="true"
>
  {message}
</div>

// Error announcements (more urgent)
<div
  role="alert"
  aria-live="assertive"
>
  {errorMessage}
</div>

// Loading states
<div
  role="status"
  aria-busy={isLoading}
  aria-live="polite"
>
  {isLoading ? 'Loading...' : content}
</div>
```

### Hiding Decorative Content

```tsx
// Hide from screen readers
<Icon aria-hidden="true" />

// Visually hidden but readable by screen readers
<span className="sr-only">Additional context</span>

// Price formatting
<span>
  <span className="sr-only">Price:</span>
  PHP <span aria-label="one thousand two hundred">1,200</span>
</span>
```

## Focus Management

### Visible Focus Indicators

```css
/* Global focus styles */
:focus-visible {
  outline: 2px solid var(--negosyo-blue);
  outline-offset: 2px;
}

/* Remove default for custom focus */
:focus {
  outline: none;
}

/* Tailwind classes */
.focus-visible:outline-none
.focus-visible:ring-2
.focus-visible:ring-ring
.focus-visible:ring-offset-2
```

### Focus Trapping in Modals

```tsx
// Using Radix UI Dialog (built-in focus trap)
<Dialog>
  <DialogTrigger asChild>
    <Button>Open</Button>
  </DialogTrigger>
  <DialogContent>
    {/* Focus is automatically trapped here */}
    <DialogHeader>
      <DialogTitle>Modal Title</DialogTitle>
    </DialogHeader>
    {/* First focusable element receives focus */}
    <Input autoFocus />
    <DialogFooter>
      <Button>Save</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

### Focus on Route Changes

```tsx
// In Next.js App Router
'use client';

import { useEffect, useRef } from 'react';
import { usePathname } from 'next/navigation';

export function RouteAnnouncer() {
  const pathname = usePathname();
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Focus main content on route change
    ref.current?.focus();
  }, [pathname]);

  return (
    <div
      ref={ref}
      tabIndex={-1}
      className="sr-only"
      role="status"
      aria-live="polite"
    >
      Navigated to {pathname}
    </div>
  );
}
```

## Forms & Inputs

### Labels

Every input MUST have a label:

```tsx
// Good: Explicit label association
<div className="space-y-2">
  <Label htmlFor="email">Email</Label>
  <Input id="email" type="email" />
</div>

// Good: Implicit association
<Label>
  Email
  <Input type="email" className="mt-2" />
</Label>

// Bad: No label
<Input type="email" placeholder="Email" />
```

### Error States

```tsx
<div className="space-y-2">
  <Label htmlFor="password">Password</Label>
  <Input
    id="password"
    type="password"
    aria-invalid={!!errors.password}
    aria-describedby={errors.password ? "password-error" : "password-hint"}
  />
  {errors.password ? (
    <p id="password-error" role="alert" className="text-sm text-destructive">
      {errors.password.message}
    </p>
  ) : (
    <p id="password-hint" className="text-sm text-muted-foreground">
      Must be at least 8 characters
    </p>
  )}
</div>
```

### Required Fields

```tsx
<Label htmlFor="name">
  Name <span aria-hidden="true">*</span>
  <span className="sr-only">(required)</span>
</Label>
<Input id="name" required aria-required="true" />
```

## Images & Media

### Alt Text

```tsx
// Informative images: Describe the content
<Image
  src="/products/halal-coffee.jpg"
  alt="Arabica coffee beans from Sulu, packaged in a traditional woven bag"
/>

// Decorative images: Empty alt
<Image
  src="/decorative-pattern.svg"
  alt=""
  aria-hidden="true"
/>

// Images with text: Include all text in alt
<Image
  src="/banner-sale.jpg"
  alt="Summer Sale: Up to 50% off on all products until December 31"
/>

// Complex images: Use figcaption
<figure>
  <Image src="/chart.png" alt="Sales chart" aria-describedby="chart-desc" />
  <figcaption id="chart-desc">
    Bar chart showing monthly sales from January to December 2024.
    Highest sales in December at PHP 500,000.
  </figcaption>
</figure>
```

### Videos

```tsx
<video controls>
  <source src="/tutorial.mp4" type="video/mp4" />
  <track
    kind="captions"
    src="/tutorial-captions.vtt"
    srcLang="en"
    label="English"
    default
  />
  <track
    kind="captions"
    src="/tutorial-captions-fil.vtt"
    srcLang="fil"
    label="Filipino"
  />
  Your browser does not support video.
</video>
```

## Motion & Animation

### Respect User Preferences

```tsx
// CSS approach
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

// React hook
function usePrefersReducedMotion() {
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false);

  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReducedMotion(mediaQuery.matches);

    const handler = (e: MediaQueryListEvent) => {
      setPrefersReducedMotion(e.matches);
    };

    mediaQuery.addEventListener('change', handler);
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);

  return prefersReducedMotion;
}

// Usage
const prefersReducedMotion = usePrefersReducedMotion();

return (
  <Skeleton
    className={prefersReducedMotion ? '' : 'animate-pulse'}
  />
);
```

### Safe Animation Patterns

```css
/* Safe: Opacity and transform */
.fade-in {
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Avoid: Large movements, flashing */
/* Never animate more than 3 flashes per second */
```

## Testing Tools

### Automated Testing

| Tool | Purpose |
|------|---------|
| axe DevTools | Browser extension for accessibility testing |
| Lighthouse | Performance + accessibility audit |
| WAVE | Visual accessibility feedback |
| eslint-plugin-jsx-a11y | Linting for React accessibility |

### Manual Testing Checklist

- [ ] Navigate entire page with keyboard only
- [ ] Test with screen reader (VoiceOver, NVDA)
- [ ] Check color contrast with browser DevTools
- [ ] Disable CSS and verify content structure
- [ ] Test at 200% zoom
- [ ] Test with reduced motion preference

### Screen Reader Testing

```bash
# macOS: VoiceOver
# Enable: Cmd + F5
# Navigate: Ctrl + Option + Arrow Keys

# Windows: NVDA (free)
# Download from nvaccess.org
# Navigate: Tab, Arrow Keys

# Chrome: ChromeVox extension
```

### Lighthouse Audit

```bash
# Run in Chrome DevTools
# 1. Open DevTools (F12)
# 2. Go to Lighthouse tab
# 3. Select "Accessibility" category
# 4. Click "Generate report"
# Target: 90+ score
```

## Quick Reference

### Minimum Requirements (Level AA)

- [ ] 4.5:1 contrast for text
- [ ] 3:1 contrast for UI components
- [ ] All functionality keyboard accessible
- [ ] Focus visible on all interactive elements
- [ ] All images have appropriate alt text
- [ ] Form inputs have labels
- [ ] Error messages are clear and specific
- [ ] Page has proper heading hierarchy
- [ ] Language is specified (`<html lang="en">`)
- [ ] Motion can be disabled
