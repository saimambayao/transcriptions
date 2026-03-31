---
name: ui-ux
description: UI/UX design and user journey optimization skill for Bangsamoro Development Platform (Negosyo Portal). Use when building, reviewing, or optimizing user interfaces across all portals - Public marketplace, Coop/SE Portal, Storefronts, MoroAcademy, and CSEA admin. Covers complete user journeys, conversion optimization, shadcn/ui components with Tailwind CSS v4, WCAG 2.2 compliance, and FRAMES compliance interfaces. Integrates with /frontend for implementation and /academy for learning UIs.
argument-hint: "[topic]"
---

# UI/UX Design & User Journey Skill

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's UI/UX request                            ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

## This Skill's Purpose

**`/ui-ux` is for DESIGN & UX DECISIONS:**
- User journey mapping and optimization
- Interaction patterns (modal vs full-page decisions)
- Accessibility requirements (WCAG 2.2)
- Layout planning and component selection
- Conversion optimization strategies

### When to Use This Skill

| Task | Use /ui-ux? |
|------|-------------|
| "Plan the checkout user journey" | Yes |
| "Design the new dashboard layout" | Yes |
| "Review UX of the onboarding flow" | Yes |
| "Add a button to the header" | No → use `/frontend` |
| "Build the product grid component" | No → use `/frontend` |

### Related Skill

**`/frontend`** - For code implementation (React, Next.js, shadcn/ui)

If you need to implement after designing, invoke `/frontend` separately.

---

Specialized guidance for building exceptional user experiences across the entire Negosyo Platform ecosystem using Next.js 16+, React 19+, shadcn/ui, and Tailwind CSS v4.

## Quick Reference

### User Journey Guides

| Portal/User | Journey File | Key Flows |
|-------------|--------------|-----------|
| **Public Portal** | [journeys-public.md](references/journeys-public.md) | Discovery, purchase, account, browsing |
| **Coop/SE Portal** | [journeys-seller.md](references/journeys-seller.md) | Onboarding, products, orders, dashboard |
| **Storefronts** | [journeys-storefront.md](references/journeys-storefront.md) | Setup, customization, analytics |
| **MoroAcademy** | [journeys-moroacademy.md](references/journeys-moroacademy.md) | Enrollment, learning, certification |
| **CSEA Admin** | [journeys-csea.md](references/journeys-csea.md) | Review, monitoring, analytics |
| **Compliance** | [journeys-compliance.md](references/journeys-compliance.md) | Registration, FRAMES, renewals |

### Component & Pattern Guides

| Topic | Reference File |
|-------|---------------|
| Form Design | [references/forms.md](references/forms.md) |
| Accessibility (WCAG 2.2) | [references/accessibility.md](references/accessibility.md) |
| Loading States | [references/loading-states.md](references/loading-states.md) |
| Mobile-First Design | [references/mobile-first.md](references/mobile-first.md) |
| Component Patterns | [references/component-patterns.md](references/component-patterns.md) |

## Core Principles

### 1. Journey-Centric Design
- Map complete user flows before building components
- Identify friction points and optimize for conversion
- Progressive disclosure for complex processes
- Context-aware interfaces based on user state

### 2. Mobile-First Always
- 59-64% of web traffic is mobile in 2025
- Design for small screens first, then enhance for larger ones
- Touch targets: minimum 48x48px with adequate spacing
- Test on Safari, Chrome, Firefox mobile browsers

### 3. Performance = UX
- Page load under 2 seconds (desktop and mobile)
- 53% of mobile users abandon sites taking >3 seconds
- Use skeleton loaders instead of spinners
- Lazy load images, use WebP/AVIF formats

### 4. Accessibility is Non-Negotiable
- Target WCAG 2.2 Level AA compliance
- Color contrast: 4.5:1 for normal text, 3:1 for large text
- All interactive elements keyboard accessible
- Screen reader support with proper ARIA attributes

### 5. Trust Through Design
- Display ratings, reviews, verified badges prominently
- Clear pricing with no hidden fees
- Transparent seller/cooperative information
- Visible security indicators at checkout

## Negosyo Design Standards

### Brand Colors (Never Use Purple)
```css
/* Primary - Negosyo Blue */
--negosyo-blue: #0056D2;

/* Hero/Promotional - Negosyo Red */
--negosyo-red: #D30A28;

/* Semantic */
--success: #16a34a;
--warning: #f59e0b;
--error: #dc2626;
--info: #0ea5e9;
```

### Using Negosyo Blue in Tailwind
```tsx
// Primary buttons and interactive elements
<Button className="bg-negosyo-blue hover:bg-negosyo-blue/90">Primary Action</Button>

// Links and accents
<Link className="text-negosyo-blue hover:text-negosyo-blue/80">View Details</Link>

// Badges and highlights
<Badge className="bg-negosyo-blue">Active</Badge>

// Borders and outlines
<Card className="border-negosyo-blue">Featured Content</Card>
```

### Using Negosyo Red in Tailwind
```tsx
// Hero sections and promotional banners
<section className="bg-negosyo-red text-white py-16">
  <h1 className="text-4xl font-bold">Main Headline</h1>
  <p className="text-red-100">Supporting description</p>
</section>

// Hero CTA buttons (white on red background)
<Button className="bg-white text-negosyo-red hover:bg-red-50">Shop Now</Button>

// Featured product highlights
<Badge className="bg-negosyo-red text-white">Featured</Badge>
```

### Typography Scale
```css
/* Use with Tailwind */
text-xs: 0.75rem    /* Labels, captions */
text-sm: 0.875rem   /* Secondary text */
text-base: 1rem     /* Body text */
text-lg: 1.125rem   /* Emphasized text */
text-xl: 1.25rem    /* Section headers */
text-2xl: 1.5rem    /* Page titles */
```

### Spacing System
```css
/* Consistent spacing with Tailwind */
p-1: 0.25rem  p-2: 0.5rem   p-3: 0.75rem
p-4: 1rem     p-6: 1.5rem   p-8: 2rem
```

### Layout Width Standard

**Standard Container: `max-w-7xl` (1280px / 80rem)**

Use this as the standard container width for all pages. Optimized for ~88.9% content width on standard 1440px laptops.

| Screen Width | Content Width | Percentage Used |
|--------------|---------------|-----------------|
| 1920px (Full HD) | 1280px | 66.7% |
| 1536px (Large laptop) | 1280px | 83.3% |
| **1440px (Standard laptop)** | **1280px** | **88.9%** ← Target |
| 1280px or smaller | 100% minus padding | ~100% |

```tsx
// Standard container pattern for all pages
<div className="container mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl">
  {/* Page content */}
</div>

// For sections (homepage, landing pages)
<section className="bg-white py-12 lg:py-16">
  <div className="container mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl">
    {/* Section content */}
  </div>
</section>
```

**Why 1440px Target:**
- Most common laptop resolution in 2024-2025
- ~88.9% content width provides good readability
- Sufficient whitespace for visual breathing room
- Responsive down to mobile without issues

## User Journey Best Practices

### Journey Mapping Approach
1. **Define Persona** - Who is the user? What are their goals?
2. **Map Touchpoints** - Every interaction from entry to completion
3. **Identify Emotions** - Anxiety, confusion, satisfaction points
4. **Find Friction** - Drop-off points and pain areas
5. **Optimize Flow** - Reduce steps, clarify actions, build confidence

### Portal-Specific Guidance

#### Public Marketplace (Buyers)
- **Browse without barriers** - No mandatory login to explore
- **Clear product information** - Images, price, seller ratings visible
- **Social proof everywhere** - Reviews, ratings, purchase counts
- **Simple checkout** - 3 steps or fewer, guest checkout option
- **One-tap payments** - Digital wallets (GCash, PayMaya, etc.)
- See [journeys-public.md](references/journeys-public.md)

#### Coop/SE Portal (Sellers)
- **Easy onboarding** - Progressive disclosure, step-by-step setup
- **Quick product listing** - Minimal required fields, bulk upload
- **Dashboard clarity** - Key metrics at a glance
- **Immediate support access** - Help center, live chat visible
- See [journeys-seller.md](references/journeys-seller.md)

#### Storefronts
- **Quick setup** - Template-driven with live preview
- **Brand customization** - Colors, logo, domain in one place
- **Customer engagement** - Chat, reviews, notifications
- **Performance insights** - Traffic, sales, conversion metrics
- See [journeys-storefront.md](references/journeys-storefront.md)

#### MoroAcademy (Learners)
- **Easy discovery** - Browse courses without login
- **Simple enrollment** - One-click for free courses
- **Distraction-free learning** - Focus mode player
- **Progress visibility** - Clear tracking and achievements
- See [journeys-moroacademy.md](references/journeys-moroacademy.md)

#### CSEA Admin
- **Efficient workflows** - Batch actions, keyboard shortcuts
- **Data visibility** - Filters, search, export options
- **Alert systems** - Clear notification hierarchy
- **Audit trails** - Action history, change logs
- See [journeys-csea.md](references/journeys-csea.md)

#### Compliance (FRAMES)
- **Clear requirements** - Visible checklists per category
- **Document management** - Upload, track, remind
- **Status visibility** - Dashboard with compliance percentages
- **Proactive reminders** - Expiry warnings, action items
- See [journeys-compliance.md](references/journeys-compliance.md)

## FRAMES Compliance UI

See [component-patterns.md](references/component-patterns.md) for FRAMES categories and compliance dashboard patterns.

## Interaction Pattern Guidelines

### The Golden Rule
> **If it has an input field, it should NOT be a modal.**

Modals are overused and create poor UX, especially on mobile. Use this decision matrix:

### Pattern Decision Matrix

| Pattern | USE FOR | NEVER USE FOR |
|---------|---------|---------------|
| **Modal/Dialog** | Delete confirmations, logout prompts, "are you sure?" alerts, simple yes/no choices | ANY form with input fields, editing content, creation flows |
| **Inline Editing** | Single-field updates (title, status), toggle switches, quick edits in lists/tables | Multi-field forms, complex data entry |
| **Drawer/Sheet** | Filters, mobile navigation, quick info preview, secondary panels | Forms, primary workflows, content creation |
| **Full-Page Navigation** | All forms, all content creation/editing, multi-step flows, complex workflows | Simple confirmations |

### Why Modals Are Problematic

**Mobile-Specific Issues:**
- Full-screen takeover - becomes a page anyway but without URL/history
- Keyboard problems - virtual keyboard causes layout issues
- Back button confusion - Android back closes modal instead of navigating
- Accidental dismissal - tap outside = lose all work
- No deep linking - can't bookmark or share the state

**General UX Issues:**
- Context blindness - user can't see what they're editing relative to parent
- Cognitive load - "trapped" feeling, especially with complex content
- Scroll trapping - feels unnatural on touch devices
- No URL state - refresh = gone, can't share link

### Correct Pattern Examples

**DELETE CONFIRMATION (Modal - Correct)**
```tsx
<AlertDialog>
  <AlertDialogContent>
    <AlertDialogTitle>Delete this item?</AlertDialogTitle>
    <AlertDialogDescription>This cannot be undone.</AlertDialogDescription>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction className="bg-destructive">Delete</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

**EDIT FORM (Full-Page - Correct)**
```tsx
// Navigate to /items/[id]/edit instead of opening a modal
router.push(`/items/${item.id}/edit`)
```

**QUICK TITLE EDIT (Inline - Correct)**
```tsx
{isEditing ? (
  <Input value={title} onChange={...} onBlur={handleSave} autoFocus />
) : (
  <span onClick={() => setIsEditing(true)}>{title}</span>
)}
```

**FILTERS (Drawer/Sheet - Correct)**
```tsx
<Sheet>
  <SheetTrigger>Filters</SheetTrigger>
  <SheetContent side="right">
    <FilterControls />
  </SheetContent>
</Sheet>
```

### Anti-Patterns to Avoid

| Anti-Pattern | Problem | Correct Pattern |
|--------------|---------|-----------------|
| Form in modal | Poor mobile UX, no URL, keyboard issues | Full-page form |
| Multi-step wizard in modal | Complex flow trapped in overlay | Full-page with progress indicator |
| Content editor in modal | No context, scroll issues | Full-page or inline editing |
| Create new item modal | User loses context, can't deep-link | Full-page `/items/new` |
| Settings modal | Complex forms in overlay | Full-page settings, or inline toggles |

---

## Component Usage Guidelines

### Buttons
```tsx
// Primary action - one per view (use negosyo-blue)
<Button className="bg-negosyo-blue hover:bg-negosyo-blue/90">Submit</Button>

// Secondary actions
<Button variant="outline">Cancel</Button>
<Button variant="ghost">Learn More</Button>

// Destructive with confirmation
<Button variant="destructive">Delete</Button>
```

### Forms
- Use inline validation (after field blur)
- Show error messages below fields with icon
- Keep submit button enabled (show errors on submit)
- Mark required fields with asterisk (*)
- **Forms belong on full pages, NOT in modals**
- See [references/forms.md](references/forms.md) for detailed patterns

### Data Tables
```tsx
// Always include:
// - Sortable columns
// - Search/filter
// - Pagination (10, 25, 50, 100)
// - Row actions (view, edit, delete)
// - Empty state with helpful message
// - Inline editing for simple fields (status, toggles)
// - Full-page navigation for complex editing
```

### Dialogs (Confirmation Only)
```tsx
// ONLY use for confirmations - never for forms
<AlertDialog>
  <AlertDialogTrigger asChild>
    <Button variant="destructive">Delete</Button>
  </AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you sure?</AlertDialogTitle>
      <AlertDialogDescription>This cannot be undone.</AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction>Delete</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

### Loading States
- Use skeleton loaders matching content structure
- Add `aria-busy="true"` and `role="status"`
- Respect `prefers-reduced-motion` preference
- See [references/loading-states.md](references/loading-states.md)

## Conversion Optimization

### Key Metrics to Target
| Metric | Good | Excellent |
|--------|------|-----------|
| Conversion Rate | 2-4% | >4% |
| Cart Abandonment | <70% | <50% |
| Page Load | <3s | <2s |
| Form Completion | >50% | >75% |
| Onboarding Completion | >60% | >80% |

### Quick Wins
1. Add progress indicators to multi-step processes
2. Show shipping cost early (not at checkout)
3. Display trust badges near payment buttons
4. Use urgency cues sparingly (stock levels, limited offers)
5. Implement smart defaults (auto-select shipping, remember preferences)
6. Reduce form fields to essential minimum
7. Pre-fill data where possible (address autocomplete)

## Review Checklist

Before shipping any UI:

### Functionality
- [ ] All user flows tested end-to-end
- [ ] Error states handled gracefully
- [ ] Empty states designed
- [ ] Loading states implemented
- [ ] Forms have inline validation
- [ ] Actions have feedback (toast, status change)
- [ ] Destructive actions require confirmation

### Design
- [ ] Mobile responsive (test on actual devices)
- [ ] Touch targets >= 48x48px
- [ ] Uses negosyo-blue (#0056D2) for primary actions
- [ ] No purple colors used
- [ ] Icons used instead of emojis
- [ ] Consistent spacing and typography

### Accessibility
- [ ] Color contrast passes WCAG AA
- [ ] Keyboard navigation works
- [ ] Screen reader tested
- [ ] Focus indicators visible
- [ ] Alt text for images

### Performance
- [ ] Page load under 3 seconds
- [ ] Images optimized (WebP/AVIF)
- [ ] Lazy loading implemented
- [ ] No layout shifts

## Common Patterns

See [component-patterns.md](references/component-patterns.md) for empty states, confirmation dialogs, status badges, and progress indicators.

## Tools & Testing

### Design Tools
- Figma with shadcn/ui design system
- Tailwind CSS IntelliSense (VS Code)

### Testing
- Chrome DevTools device emulation
- axe DevTools for accessibility
- Lighthouse for performance
- Real device testing (iOS Safari, Android Chrome)

### Browser Support
- Chrome/Edge (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Mobile Safari, Chrome for Android

