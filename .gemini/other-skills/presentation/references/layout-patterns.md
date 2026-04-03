# Layout Patterns

Layout patterns and responsive design for presentation slides.

---

## Content Width Standards

**CRITICAL: Use 85% screen width on desktop, full width on mobile.**

| Screen Size | Content Width | Padding | Behavior |
|-------------|---------------|---------|----------|
| Mobile (<768px) | 100% | px-4 (16px) | Full width for readability |
| Desktop (≥768px) | 85% centered | px-12 (48px) | Centered for projector focus |
| Desktop + Sidebar | 100% | px-12 (48px) | Expands when sidebar opens |

### Implementation

```tsx
// FullPageSection content wrapper
<div className={cn(
    "transition-all duration-500 mx-auto",
    "max-w-full md:max-w-[85%]",
    isSidebarOpen && "md:max-w-none",
)}>
    {children}
</div>
```

**Why 85%?**
- Provides visual breathing room on wide screens
- Centers content for projector/screen focus
- Prevents content from stretching too wide on ultrawide monitors
- Maintains readability while using available space

---

## Full-Width Slide

```tsx
<FullPageSection id="intro" title="Introduction">
  <h2 className="text-3xl md:text-5xl font-black mb-8 tracking-tighter">
    Section Title
  </h2>
  <p className="text-xl md:text-3xl font-light leading-relaxed max-w-4xl">
    Opening paragraph with key context...
  </p>
</FullPageSection>
```

---

## Two-Column Layout

```tsx
<FullPageSection id="comparison" title="Comparison">
  <div className="grid lg:grid-cols-2 gap-8 md:gap-16">
    <div className="space-y-6">
      {/* Left column content */}
    </div>
    <div>
      {/* Right column content */}
    </div>
  </div>
</FullPageSection>
```

---

## Grid Cards

```tsx
<FullPageSection id="traits" title="Key Traits">
  <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
    {items.map(item => (
      <div className="p-6 bg-white rounded-3xl border-2 shadow-sm">
        <h4 className="text-xl font-black mb-2">{item.title}</h4>
        <p className="text-lg text-gray-600">{item.desc}</p>
      </div>
    ))}
  </div>
</FullPageSection>
```

---

## Flow Diagram

```tsx
<FullPageSection id="flow" title="Money Flow">
  <div className="flex flex-col items-center space-y-4">
    <div className="p-8 bg-gray-900 text-white rounded-3xl text-center">
      <p className="text-4xl font-black">SOURCE</p>
    </div>
    <div className="h-16 w-1 bg-gray-300"></div>
    <div className="p-8 bg-blue-600 text-white rounded-3xl text-center">
      <p className="text-4xl font-black">DESTINATION</p>
    </div>
  </div>
</FullPageSection>
```

---

## Color System

### Semantic Colors

| Purpose | Background | Border | Text |
|---------|------------|--------|------|
| Primary | bg-[var(--negosyo-blue)] | border-blue-100 | text-[var(--negosyo-blue)] |
| Success | bg-emerald-50 | border-emerald-200 | text-emerald-700 |
| Warning | bg-amber-50 | border-amber-200 | text-amber-700 |
| Danger | bg-rose-50 | border-rose-200 | text-rose-700 |
| Info | bg-blue-50 | border-blue-200 | text-blue-700 |
| Neutral | bg-gray-50 | border-gray-200 | text-gray-700 |

### Team/Entity Colors (Simulations)

```tsx
const teamColors = {
  agri: 'bg-green-100 text-green-800',
  fishermen: 'bg-blue-100 text-blue-800',
  producer: 'bg-amber-100 text-amber-800',
  consumer: 'bg-indigo-100 text-indigo-800',
  service: 'bg-yellow-100 text-yellow-800'
}
```

---

## Responsive Design

### Breakpoints

- Mobile: `< 768px` (default styles)
- Desktop: `md:` prefix (`>= 768px`)

### Scaling Pattern

```tsx
// Text sizes
className="text-xl md:text-3xl"

// Padding
className="p-4 md:p-8"

// Rounded corners
className="rounded-2xl md:rounded-4xl"

// Gaps
className="gap-4 md:gap-8"
```

### Mobile Considerations

1. Stack columns vertically: `grid-cols-1 md:grid-cols-2`
2. Reduce padding: `p-4 md:p-12`
3. Smaller rounded corners: `rounded-2xl md:rounded-[4rem]`
4. Scrollable tables: wrap in `overflow-x-auto`

---

## Typography Scale

### CRITICAL: Minimum Font Size is 24px

All text in presentations must be at least 24px (text-2xl) for readability on:
- Projector screens from the back of the room
- Mobile devices for participants
- Video recordings at various resolutions

### Headings

| Level | Mobile | Desktop | Weight | Use For |
|-------|--------|---------|--------|---------|
| Title | text-3xl | text-[64px] | font-black | Session titles |
| H2 | text-3xl | text-5xl | font-black | Section headers |
| H3 | text-2xl md:text-4xl | text-4xl | font-black | Subsection headers |
| H4 | text-2xl md:text-3xl | text-3xl | font-black | Card titles |

### Body Text

| Type | Mobile | Desktop | Weight | Use For |
|------|--------|---------|--------|---------|
| Lead | text-2xl | text-3xl | font-light | Opening paragraphs |
| Normal | text-2xl | text-2xl | font-medium | General content |
| Small | text-2xl | text-2xl | font-medium | Secondary info |
| Caption | text-2xl | text-2xl | font-bold | Labels, badges |

### Key Rules

1. **Minimum 24px** - Never use text smaller than text-2xl
2. Always use `tracking-tighter` on large headings
3. Use `leading-tight` or `leading-relaxed` for readability
4. Limit line lengths with `max-w-2xl` or `max-w-4xl`
5. Use `font-black` (900) for impact, `font-bold` (700) for emphasis

---

## SlideTimeline Component

Scroll-linked vertical timeline navigation.

### Features

- **Intersection Observer** - Detects active section
- **Framer Motion animations** - Smooth progress line growth
- **Completed/Active/Upcoming states** - Visual feedback
- **Click-to-scroll** - Navigate to any section
- **Hover labels** - Show section names on hover
- **Accessibility** - Keyboard navigation, ARIA labels

### Usage

```tsx
import { SlideTimeline } from '@/components/academy/SlideTimeline'

<SlideTimeline
  sections={[
    { id: 'intro', label: 'Introduction' },
    { id: 'concept', label: 'Key Concept' },
    { id: 'activity', label: 'Activity' },
  ]}
  position="right"
  alwaysShowLabels={false}
/>
```

### Visual Design

```
Timeline States:
  ● Completed - Filled blue with checkmark
  ◉ Active - Blue with ring pulse
  ○ Upcoming - Gray outline

Progress Line:
  ┃ Gray track (full height)
  ┃ Blue fill (grows with scroll)
```

### Minimal Timeline

For cleaner presentations, use dots-only variant:

```tsx
import { MinimalTimeline } from '@/components/academy/SlideTimeline'

<MinimalTimeline
  sectionIds={['intro', 'concept', 'activity']}
  position="right"
/>
```

---

## Standard UI Layout

```
┌───────────────────────────────────────────────────────────────────┐
│ [MoroAcademy Logo]           [1/15 | 🛡️ M S Slide | 🏠 | ⛶]      │  ← Top: Logo left, Toolbar right
│                                                                   │
│  ●─┐                                                              │
│  ○ │                                                              │
│  ○ │                    [SLIDE CONTENT]                           │  ← Left: Timeline
│  ○ │                                                              │
│  ○─┘                                                              │
│                                                                   │
│ ══════════════════════════════════════                            │  ← Bottom: Progress bar
└───────────────────────────────────────────────────────────────────┘
```

| Position | Element | Description |
|----------|---------|-------------|
| **Top-Left** | MoroAcademy Logo | Links back to /academy |
| **Top-Right** | Toolbar | Page indicator, Facilitator Controls, Home, Fullscreen |
| **Left Side** | Timeline | Minimal dots showing section progress |
| **Bottom** | Progress Bar | Linear scroll progress indicator |
