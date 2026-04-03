# Presentation UI Standards

Standards for creating PowerPoint-like presentation UIs for live workshops and video content in MoroAcademy.

---

## Overview

Instead of creating PowerPoint slides, build web-based presentation pages that:
- Display beautifully on projectors and screens
- Work on mobile devices for participants
- Support facilitator-controlled content locking
- Enable keyboard navigation (Arrow keys)
- Can be recorded for video courses

**Reference Implementation**: `/frontend/src/app/(academy)/academy/edp/`

---

## Branding Requirements

### MoroAcademy Logo

**Every presentation slide MUST include the MoroAcademy logo** for consistent branding.

**Logo Files:**
- Full logo: `/public/images/brand/moroacademy-logo.svg`
- Icon only: `/public/images/brand/moroacademy-icon.svg`

**Placement:**
- Default position: **Top-left corner**
- Alternative: Top-right (if timeline is on left)
- Size: 32px height (md: 40px)
- Padding from edge: 16px (1rem)

```tsx
import Image from 'next/image'

// Standard logo placement
<Image
  src="/images/brand/moroacademy-logo.svg"
  alt="MoroAcademy"
  width={160}
  height={32}
  className="fixed top-4 left-4 z-50"
  priority
/>
```

**Logo Guidelines:**
- Always use SVG for crisp rendering
- Do not alter colors or proportions
- Ensure sufficient contrast with background
- Link logo to `/academy` for navigation

---

## Font Standard

### Official Font: Inter Only

**All MoroAcademy presentations MUST use Inter as the sole font family.**

This ensures:
- Visual consistency across all courses and workshops
- Professional, clean, and highly readable typography
- Excellent screen rendering at all sizes
- Wide character support for Bangsamoro content

**Reference Implementation**: `/frontend/src/app/(academy)/academy/model-presentation/`

### CSS Implementation

```tsx
// Apply Inter to all presentation content
<div className="font-[family-name:var(--font-inter)]">
  {/* All presentation slides */}
</div>
```

The `--font-inter` CSS variable is defined in the root layout and loaded via `next/font/google`.

### Font Weights

Use these weight variations for visual hierarchy:

| Weight | Class | Use For |
|--------|-------|---------|
| 900 (Black) | `font-black` | Main titles, key messages, impact text |
| 800 (Extra Bold) | `font-extrabold` | Section headers |
| 700 (Bold) | `font-bold` | Subheadings, emphasis |
| 600 (Semibold) | `font-semibold` | Card titles, labels |
| 500 (Medium) | `font-medium` | Body text, descriptions |
| 400 (Normal) | `font-normal` | Secondary text |

### Typography Examples

```tsx
// Title slide
<h1 className="text-5xl md:text-7xl lg:text-8xl font-black tracking-tight">
  Understanding Entrepreneurship
</h1>

// Section header
<h2 className="text-4xl md:text-5xl lg:text-6xl font-black tracking-tight">
  What is an Entrepreneur?
</h2>

// Body text
<p className="text-xl md:text-2xl font-medium leading-relaxed">
  An entrepreneur is someone who identifies opportunities...
</p>

// Quote text
<blockquote className="text-3xl md:text-4xl lg:text-5xl font-bold leading-relaxed">
  The entrepreneur always searches for change...
</blockquote>

// Table text
<td className="text-xl md:text-2xl font-medium">Table content</td>
```

### Why Inter?

Inter was selected as the official MoroAcademy presentation font because:

1. **Highly Legible** - Designed for screens, optimized for UI
2. **Versatile Weight Range** - 100 to 900 weights for full hierarchy
3. **Open Source** - Free to use, no licensing concerns
4. **Modern & Professional** - Clean, contemporary appearance
5. **Multi-script Support** - Good character coverage for Filipino/Bangsamoro text
6. **Performance** - Well-optimized as a variable font

### Prohibited Fonts

Do NOT use these in presentations:
- Outfit (previously used, now deprecated)
- Playfair Display
- DM Serif Display
- Poppins
- Any decorative or display fonts

---

## Presentation Mode (Slide Mode)

For fullscreen presentations, use the **PresentationMode** component which provides:

1. **No top navbar** - Full screen immersion
2. **MoroAcademy logo** - Always visible branding
3. **Bottom progress bar** - Linear scroll progress at bottom of screen
4. **Keyboard navigation** - Arrow keys, Page Up/Down
5. **Fullscreen support** - F11 or button toggle
6. **Minimum 24px font** - All text readable on projectors

### Usage

```tsx
import { PresentationMode } from '@/components/academy/PresentationMode'

export default function SessionPage() {
  return (
    <PresentationMode
      sections={[
        { id: 'intro', label: 'Introduction' },
        { id: 'concept', label: 'Key Concept' },
        { id: 'activity', label: 'Activity' },
        { id: 'takeaway', label: 'Takeaway' },
      ]}
      showProgress={true}
      progressPosition="bottom"
      showTimeline={false}
    >
      <section id="intro">...</section>
      <section id="concept">...</section>
      <section id="activity">...</section>
      <section id="takeaway">...</section>
    </PresentationMode>
  )
}
```

### Recommended Configuration

| Prop | Recommended Value | Reason |
|------|-------------------|--------|
| `showProgress` | `true` | Shows scroll progress to participants |
| `progressPosition` | `"bottom"` | Less obtrusive, doesn't compete with logo |
| `showTimeline` | `false` | Cleaner presentation, use progress bar instead |

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `sections` | TimelineSection[] | required | Sections for timeline navigation |
| `showLogo` | boolean | true | Show MoroAcademy logo |
| `logoPosition` | string | 'top-left' | Logo position on screen |
| `timelinePosition` | 'left' \| 'right' | 'right' | Timeline placement |
| `showProgress` | boolean | true | Show scroll progress bar |
| `progressPosition` | 'top' \| 'bottom' | 'bottom' | Progress bar position (bottom recommended) |
| `showTimeline` | boolean | false | Show side timeline navigation (disabled by default) |
| `minimalTimeline` | boolean | false | Dots only, no labels |
| `alwaysShowLabels` | boolean | false | Always show timeline labels |
| `keyboardNav` | boolean | true | Enable keyboard navigation |
| `showControls` | boolean | true | Show navigation controls |
| `exitUrl` | string | '/academy' | Where to go when exiting |

---

## SlideTimeline Component

The **SlideTimeline** is a scroll-linked vertical timeline navigation that replaces the traditional sidebar in presentation mode.

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

For cleaner presentations, use the minimal dots-only variant:

```tsx
import { MinimalTimeline } from '@/components/academy/SlideTimeline'

<MinimalTimeline
  sectionIds={['intro', 'concept', 'activity']}
  position="right"
/>
```

---

## Core Components

### 1. FullPageSection (Slide Container)

Each "slide" is a full-screen section with scroll-snap behavior.

```tsx
import { FullPageSection } from '../_components/EDPContent'

<FullPageSection id="unique-id" title="Slide Title">
  {/* Slide content */}
</FullPageSection>
```

**Features:**
- Full viewport height (`min-h-[100dvh]` mobile, `min-h-[calc(100vh-64px)]` desktop)
- Scroll-snap for slide-like navigation
- Auto-registers in sidebar navigation
- Supports content locking (facilitator control)
- Intersection observer for active state tracking

**Props:**
| Prop | Type | Description |
|------|------|-------------|
| `id` | string | Unique identifier for navigation |
| `title` | string | Display title in sidebar |
| `className` | string | Additional container styles |
| `contentClassName` | string | Content wrapper styles |

---

### 2. SessionHeader (Title Slide)

Opening slide for each session with objectives.

```tsx
<SessionHeader
  module="Module 1"
  session="Session 1.1"
  title="Understanding Entrepreneurship"
  duration="30 Minutes"
  objectives={[
    "Explain key entrepreneurial traits",
    "Understand cooperative principles",
    "Analyze business entities"
  ]}
/>
```

**Styling:**
- Module/Session: `text-lg md:text-2xl font-black uppercase tracking-[0.2em]`
- Title: `text-3xl md:text-[64px] font-black tracking-tighter`
- Objectives: Blue gradient card with bullet points

---

### 3. ContentBlock (Styled Content)

Colored side-border blocks for different content types.

```tsx
<ContentBlock
  title="Key Concept"
  variant="info"
  icon={Lightbulb}
>
  <p>Content goes here...</p>
</ContentBlock>
```

**Variants:**

| Variant | Border | Background | Use For |
|---------|--------|------------|---------|
| `default` | Gray | None | General content |
| `info` | Blue | Light blue | Definitions, explanations |
| `activity` | Green | Light green | Exercises, activities |
| `takeaway` | Amber | Light amber | Key points, summaries |
| `caution` | Red | Light red | Warnings, important notes |

---

### 4. TableWrapper (Data Tables)

Presentation-ready tables with responsive design.

```tsx
<TableWrapper
  title="Comparison Table"
  headers={['Aspect', 'Option A', 'Option B']}
  rows={[
    ['Cost', 'P1,000', 'P2,000'],
    ['Time', '1 hour', '2 hours']
  ]}
  textSize="xl"
/>
```

**Props:**
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | string | — | Optional table title |
| `headers` | string[] | — | Column headers |
| `rows` | (string\|ReactNode)[][] | — | Table data |
| `textSize` | string | "2xl" | Text size class |

---

### 5. Takeaway (Key Message)

Large, prominent box for critical takeaways.

```tsx
<Takeaway
  content="Strong individual businesses create shared prosperity for the entire community."
/>
```

**Styling:**
- Container: `bg-amber-50 rounded-[4rem] p-20`
- Title: `text-4xl font-black uppercase`
- Content: `text-6xl font-black tracking-tight`

---

### 6. NextSession (Navigation)

Link to proceed to next session.

```tsx
<NextSession
  title="1.2 Opportunity Recognition"
  path="/academy/edp/module1/session2"
/>
```

---

## Typography Scale

Use presentation-friendly sizes for readability on projectors.

### CRITICAL: Minimum Font Size

**ALL text in presentations must be at least 24px (text-2xl in Tailwind).**

This ensures readability on:
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

**Note**: All text sizes are now 24px minimum. The previous smaller sizes (text-sm, text-base, text-lg, text-xl) should NOT be used for slide content.

### Key Rules

1. **Minimum 24px** - Never use text smaller than text-2xl (24px)
2. Always use `tracking-tighter` on large headings
3. Use `leading-tight` or `leading-relaxed` for readability
4. Limit line lengths with `max-w-2xl` or `max-w-4xl`
5. Use `font-black` (900) for impact, `font-bold` (700) for emphasis

---

## Content Width Standards

**CRITICAL: Use 85% screen width on desktop, full width on mobile.**

### Width Rules

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
    // Mobile: full width, Desktop: 85% when no sidebar
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

## Layout Patterns

### Full-Width Slide

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

### Two-Column Layout

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

### Grid Cards

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

### Flow Diagram

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

### Team/Entity Colors

For simulations with multiple teams:

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

## Navigation & Interaction

### Keyboard Navigation

The layout automatically supports:
- **Arrow Down**: Next slide
- **Arrow Up**: Previous slide

### Sidebar Integration

Each `FullPageSection` with `id` and `title` auto-registers in the sidebar for:
- Click navigation to sections
- Visual indication of current section
- Progress tracking

### Content Locking

Facilitators can lock:
- Entire modules
- Individual sessions
- Specific slides/sections

Locked content appears blurred with a lock overlay.

---

## Animations with Framer Motion

Use Framer Motion (Motion for React) to add professional slide transitions, reveal effects, and micro-interactions.

### Setup

```tsx
'use client'

import { motion, AnimatePresence, useReducedMotion } from 'framer-motion'
import { useInView } from 'framer-motion'
```

### Animation Variants Library

Create a shared variants file for consistent animations:

```tsx
// lib/presentation-animations.ts

// Fade animations
export const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { duration: 0.6 } }
}

// Slide animations
export const slideUp = {
  hidden: { opacity: 0, y: 60 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.6, ease: 'easeOut' } }
}

export const slideFromLeft = {
  hidden: { opacity: 0, x: -60 },
  visible: { opacity: 1, x: 0, transition: { duration: 0.5, ease: 'easeOut' } }
}

export const slideFromRight = {
  hidden: { opacity: 0, x: 60 },
  visible: { opacity: 1, x: 0, transition: { duration: 0.5, ease: 'easeOut' } }
}

// Scale animations
export const scaleIn = {
  hidden: { opacity: 0, scale: 0.8 },
  visible: { opacity: 1, scale: 1, transition: { duration: 0.5, ease: 'easeOut' } }
}

export const popIn = {
  hidden: { opacity: 0, scale: 0.5 },
  visible: {
    opacity: 1,
    scale: 1,
    transition: { type: 'spring', stiffness: 300, damping: 20 }
  }
}

// Stagger container
export const staggerContainer = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.2
    }
  }
}

// Stagger items
export const staggerItem = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.4 } }
}
```

---

### Scroll-Triggered Reveal

Animate elements when they enter the viewport using `whileInView`:

```tsx
// Basic reveal on scroll
<motion.div
  initial={{ opacity: 0, y: 50 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-100px" }}
  transition={{ duration: 0.6, ease: "easeOut" }}
>
  <h2>This reveals on scroll</h2>
</motion.div>

// With variants
<motion.div
  variants={slideUp}
  initial="hidden"
  whileInView="visible"
  viewport={{ once: true }}
>
  <ContentBlock title="Key Concept" variant="info">
    Content appears with slide-up animation
  </ContentBlock>
</motion.div>
```

**Viewport Options:**

| Option | Type | Description |
|--------|------|-------------|
| `once` | boolean | Only animate once (recommended for slides) |
| `margin` | string | Trigger offset (e.g., "-100px" triggers earlier) |
| `amount` | number | Percentage visible before trigger (0-1) |

---

### Staggered Content Animation

Animate list items, cards, or bullet points sequentially:

```tsx
// Staggered list items
<motion.ul
  variants={staggerContainer}
  initial="hidden"
  whileInView="visible"
  viewport={{ once: true }}
  className="space-y-4"
>
  {items.map((item, index) => (
    <motion.li key={index} variants={staggerItem}>
      {item}
    </motion.li>
  ))}
</motion.ul>

// Staggered cards
<motion.div
  variants={staggerContainer}
  initial="hidden"
  whileInView="visible"
  viewport={{ once: true }}
  className="grid grid-cols-3 gap-6"
>
  {cards.map((card, index) => (
    <motion.div
      key={index}
      variants={staggerItem}
      className="p-6 bg-white rounded-3xl shadow-sm"
    >
      <h4>{card.title}</h4>
      <p>{card.description}</p>
    </motion.div>
  ))}
</motion.div>
```

**Stagger Timing:**

| Content Type | staggerChildren | delayChildren |
|--------------|-----------------|---------------|
| Bullet points | 0.08s | 0.1s |
| Cards | 0.1s | 0.2s |
| Large sections | 0.15s | 0.3s |

---

### Text Reveal Animation

Character-by-character or word-by-word text reveal:

```tsx
// Word-by-word reveal
const words = "Your inspiring message here".split(" ")

<motion.h2
  className="text-5xl font-black"
  variants={staggerContainer}
  initial="hidden"
  whileInView="visible"
  viewport={{ once: true }}
>
  {words.map((word, index) => (
    <motion.span
      key={index}
      variants={staggerItem}
      className="inline-block mr-4"
    >
      {word}
    </motion.span>
  ))}
</motion.h2>

// Fade-up headline
<motion.h2
  initial={{ opacity: 0, y: 30 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true }}
  transition={{ duration: 0.8, ease: "easeOut" }}
  className="text-5xl font-black tracking-tighter"
>
  Key Takeaway Message
</motion.h2>
```

---

### Slide Transitions with AnimatePresence

For navigating between slides with direction-aware animations:

```tsx
import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'

const slideVariants = {
  enter: (direction: number) => ({
    x: direction > 0 ? 300 : -300,
    opacity: 0
  }),
  center: {
    x: 0,
    opacity: 1
  },
  exit: (direction: number) => ({
    x: direction < 0 ? 300 : -300,
    opacity: 0
  })
}

export function SlideCarousel({ slides }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [direction, setDirection] = useState(0)

  const navigate = (newDirection: number) => {
    setDirection(newDirection)
    setCurrentIndex(prev => prev + newDirection)
  }

  return (
    <div className="relative overflow-hidden">
      <AnimatePresence initial={false} custom={direction} mode="wait">
        <motion.div
          key={currentIndex}
          custom={direction}
          variants={slideVariants}
          initial="enter"
          animate="center"
          exit="exit"
          transition={{ duration: 0.5, ease: "easeInOut" }}
        >
          {slides[currentIndex]}
        </motion.div>
      </AnimatePresence>

      <button onClick={() => navigate(-1)}>Previous</button>
      <button onClick={() => navigate(1)}>Next</button>
    </div>
  )
}
```

---

### Parallax Scroll Effects

Create depth with scroll-linked animations:

```tsx
import { motion, useScroll, useTransform } from 'framer-motion'
import { useRef } from 'react'

export function ParallaxSection({ children }) {
  const ref = useRef(null)
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"]
  })

  // Move slower than scroll (parallax effect)
  const y = useTransform(scrollYProgress, [0, 1], [100, -100])
  const opacity = useTransform(scrollYProgress, [0, 0.3, 0.7, 1], [0, 1, 1, 0])

  return (
    <motion.div ref={ref} style={{ y, opacity }}>
      {children}
    </motion.div>
  )
}

// Background parallax
export function ParallaxBackground({ imageUrl }) {
  const { scrollYProgress } = useScroll()
  const y = useTransform(scrollYProgress, [0, 1], ['0%', '30%'])

  return (
    <motion.div
      className="absolute inset-0 -z-10"
      style={{ y }}
    >
      <img src={imageUrl} className="w-full h-full object-cover" />
    </motion.div>
  )
}
```

---

### Progress Indicator

Scroll-linked progress bar:

```tsx
import { motion, useScroll, useSpring } from 'framer-motion'

export function ScrollProgress() {
  const { scrollYProgress } = useScroll()
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
    restDelta: 0.001
  })

  return (
    <motion.div
      className="fixed top-0 left-0 right-0 h-1 bg-blue-600 origin-left z-50"
      style={{ scaleX }}
    />
  )
}
```

---

### Micro-Interactions

Hover and tap effects for interactive elements:

```tsx
// Card hover effect
<motion.div
  whileHover={{ scale: 1.02, y: -4 }}
  whileTap={{ scale: 0.98 }}
  transition={{ type: "spring", stiffness: 400, damping: 17 }}
  className="p-6 bg-white rounded-3xl shadow-sm cursor-pointer"
>
  <h4>Interactive Card</h4>
</motion.div>

// Button with feedback
<motion.button
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  className="px-8 py-4 bg-blue-600 text-white rounded-2xl font-bold"
>
  Next Slide
</motion.button>

// Icon rotation on hover
<motion.div whileHover={{ rotate: 15 }} transition={{ duration: 0.2 }}>
  <ArrowRight className="w-8 h-8" />
</motion.div>
```

---

### Accessibility: Reduced Motion

Always respect user preferences for reduced motion:

```tsx
import { useReducedMotion, MotionConfig } from 'framer-motion'

// Option 1: Global config (recommended)
export function PresentationLayout({ children }) {
  return (
    <MotionConfig reducedMotion="user">
      {children}
    </MotionConfig>
  )
}

// Option 2: Conditional animations
export function AnimatedContent({ children }) {
  const shouldReduceMotion = useReducedMotion()

  return (
    <motion.div
      initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: shouldReduceMotion ? 0.1 : 0.6 }}
    >
      {children}
    </motion.div>
  )
}

// Option 3: CSS fallback
// In your global CSS:
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Reduced Motion Guidelines:**

| Animation Type | With Motion | Reduced Motion Alternative |
|----------------|-------------|---------------------------|
| Slide/transform | x, y movement | Opacity fade only |
| Scale | scale: 0.8 → 1 | Opacity fade only |
| Parallax | Scroll-linked position | Static position |
| Stagger | Sequential delays | Instant appearance |
| Auto-play video | Playing | Paused with play button |

---

### Animation Presets by Slide Type

| Slide Type | Recommended Animation | Duration |
|------------|----------------------|----------|
| Title Slide | fadeIn + stagger objectives | 0.8s |
| Content Slide | slideUp for heading, stagger for body | 0.6s |
| Data/Table | scaleIn for table | 0.5s |
| Cards/Grid | staggerContainer + staggerItem | 0.1s stagger |
| Quote | fadeIn with slight scale | 0.8s |
| Takeaway | popIn with spring | 0.5s |
| Activity | slideFromLeft | 0.5s |

---

### Animated Components Reference

```tsx
// AnimatedSection - Base animated slide wrapper
export function AnimatedSection({ children, className }) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      whileInView={{ opacity: 1 }}
      viewport={{ once: true, margin: "-50px" }}
      transition={{ duration: 0.5 }}
      className={className}
    >
      {children}
    </motion.div>
  )
}

// AnimatedHeading - Slide-up heading
export function AnimatedHeading({ children, className }) {
  return (
    <motion.h2
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.6, ease: "easeOut" }}
      className={className}
    >
      {children}
    </motion.h2>
  )
}

// AnimatedList - Staggered list
export function AnimatedList({ items, className }) {
  return (
    <motion.ul
      variants={staggerContainer}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true }}
      className={className}
    >
      {items.map((item, i) => (
        <motion.li key={i} variants={staggerItem}>
          {item}
        </motion.li>
      ))}
    </motion.ul>
  )
}
```

---

## Building a Session Page

### Template Structure (With Animations)

```tsx
'use client'

import { motion } from 'framer-motion'
import {
  SessionHeader,
  ContentBlock,
  TableWrapper,
  Takeaway,
  NextSession,
  FullPageSection
} from '../../_components/EDPContent'
import { Info, Users, Lightbulb } from 'lucide-react'
import {
  fadeIn,
  slideUp,
  scaleIn,
  staggerContainer,
  staggerItem
} from '@/lib/presentation-animations'

export default function ModuleXSessionY() {
  return (
    <div className="pb-20">
      {/* 1. Title Slide - Fade in with staggered objectives */}
      <FullPageSection id="intro" title="Introduction">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <SessionHeader
            module="Module X"
            session="Session X.Y"
            title="Session Title"
            duration="30 Minutes"
            objectives={[
              "Objective 1",
              "Objective 2"
            ]}
          />
        </motion.div>
      </FullPageSection>

      {/* 2. Content Slides - Slide up heading, fade content */}
      <FullPageSection id="concept" title="Key Concept">
        <motion.h2
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-3xl md:text-5xl font-black mb-8 tracking-tighter"
        >
          Key Concept
        </motion.h2>
        <motion.div
          variants={slideUp}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
        >
          <ContentBlock title="Definition" variant="info" icon={Info}>
            <p>Explanation content...</p>
          </ContentBlock>
        </motion.div>
      </FullPageSection>

      {/* 3. Data Slide - Scale in table */}
      <FullPageSection id="comparison" title="Comparison">
        <motion.div
          variants={scaleIn}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
        >
          <TableWrapper
            title="Comparison Table"
            headers={['Aspect', 'Option A', 'Option B']}
            rows={[
              ['Row 1', 'Value', 'Value'],
              ['Row 2', 'Value', 'Value']
            ]}
          />
        </motion.div>
      </FullPageSection>

      {/* 4. Activity Slide - Slide from left */}
      <FullPageSection id="activity" title="Activity">
        <motion.div
          initial={{ opacity: 0, x: -60 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
        >
          <ContentBlock title="Activity: Practice" variant="activity" icon={Users}>
            <p>Instructions for the activity...</p>
          </ContentBlock>
        </motion.div>
      </FullPageSection>

      {/* 5. Takeaway Slide - Pop in with spring */}
      <FullPageSection id="takeaway" title="Key Takeaway">
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ type: "spring", stiffness: 300, damping: 20 }}
        >
          <Takeaway content="The main message participants should remember." />
        </motion.div>
      </FullPageSection>

      {/* 6. Navigation Slide - Fade in */}
      <FullPageSection id="next" title="Up Next">
        <motion.div
          variants={fadeIn}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
        >
          <NextSession
            title="X.Z Next Session Title"
            path="/academy/edp/moduleX/sessionZ"
          />
        </motion.div>
      </FullPageSection>
    </div>
  )
}
```

### Template Structure (Static - No Animations)

For simpler implementations or when animations aren't needed:

```tsx
'use client'

import {
  SessionHeader,
  ContentBlock,
  TableWrapper,
  Takeaway,
  NextSession,
  FullPageSection
} from '../../_components/EDPContent'
import { Info, Users } from 'lucide-react'

export default function ModuleXSessionY() {
  return (
    <div className="pb-20">
      <FullPageSection id="intro" title="Introduction">
        <SessionHeader
          module="Module X"
          session="Session X.Y"
          title="Session Title"
          duration="30 Minutes"
          objectives={["Objective 1", "Objective 2"]}
        />
      </FullPageSection>

      <FullPageSection id="concept" title="Key Concept">
        <h2 className="text-3xl md:text-5xl font-black mb-8 tracking-tighter">
          Key Concept
        </h2>
        <ContentBlock title="Definition" variant="info" icon={Info}>
          <p>Explanation content...</p>
        </ContentBlock>
      </FullPageSection>

      <FullPageSection id="takeaway" title="Key Takeaway">
        <Takeaway content="The main message." />
      </FullPageSection>

      <FullPageSection id="next" title="Up Next">
        <NextSession title="Next Session" path="/academy/edp/moduleX/sessionZ" />
      </FullPageSection>
    </div>
  )
}
```

---

## Slide Types Reference

### 1. Title Slide
- Session header with objectives
- Sets expectations for the session

### 2. Concept Slide
- Large heading + explanation
- Use ContentBlock for definitions

### 3. Data Slide
- Tables, charts, statistics
- Use TableWrapper for structured data

### 4. Visual Slide
- Diagrams, flowcharts, images
- Use grid layouts and colored cards

### 5. Quote Slide
- Large italic text
- Centered or with attribution

### 6. Activity Slide
- Green ContentBlock
- Clear instructions and deliverables

### 7. Takeaway Slide
- Amber Takeaway component
- Single memorable message

### 8. Navigation Slide
- NextSession component
- Links to continue journey

---

## Best Practices

### Content Guidelines

1. **One concept per slide** - Keep focus clear
2. **Large text** - Readable from back of room
3. **Visual hierarchy** - Headers > Body > Details
4. **White space** - Don't overcrowd slides
5. **Consistent styling** - Use established patterns

### Technical Guidelines

1. **Unique IDs** - Every FullPageSection needs unique id
2. **Descriptive titles** - Titles appear in navigation
3. **Mobile-first** - Test on phone screens
4. **Accessibility** - Use semantic HTML, proper contrast

### Performance Guidelines

1. **Lazy load images** - Use Next.js Image component
2. **Minimize animations** - Keep simple for recording
3. **Test on projector** - Verify colors and contrast
4. **Offline support** - Consider service worker for workshops

---

## Video Recording Tips

When recording sessions for video courses:

1. **Set viewport** - 1920x1080 for HD recording
2. **Hide browser UI** - Use fullscreen mode
3. **Slow navigation** - Pause between slides for editing
4. **Capture audio separately** - Better quality
5. **Record in sections** - One topic per recording

---

## Creating New Presentations

### Step 1: Plan Slides
List all slides with IDs and types

### Step 2: Create Page
Create new page file in appropriate location

### Step 3: Import Components
Import from EDPContent or create custom

### Step 4: Build Structure
Follow template structure

### Step 5: Style Content
Apply typography and color standards

### Step 6: Test Navigation
Verify keyboard nav and sidebar

### Step 7: Mobile Test
Check responsive behavior

### Step 8: Facilitator Test
Verify locking works if needed
