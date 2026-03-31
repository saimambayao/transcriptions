# Framer Motion Animations

Animation patterns for presentation slides using Framer Motion (Motion for React).

---

## Setup

```tsx
'use client'

import { motion, AnimatePresence, useReducedMotion } from 'framer-motion'
import { useInView } from 'framer-motion'
```

---

## Animation Variants Library

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

## Scroll-Triggered Reveal

Animate elements when they enter the viewport:

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
| `once` | boolean | Only animate once (recommended) |
| `margin` | string | Trigger offset (e.g., "-100px") |
| `amount` | number | Percentage visible before trigger (0-1) |

---

## Staggered Content Animation

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

## Text Reveal Animation

Word-by-word text reveal:

```tsx
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
```

---

## Slide Transitions with AnimatePresence

Direction-aware animations for slide navigation:

```tsx
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

  return (
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
  )
}
```

---

## Parallax Scroll Effects

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

  const y = useTransform(scrollYProgress, [0, 1], [100, -100])
  const opacity = useTransform(scrollYProgress, [0, 0.3, 0.7, 1], [0, 1, 1, 0])

  return (
    <motion.div ref={ref} style={{ y, opacity }}>
      {children}
    </motion.div>
  )
}
```

---

## Progress Indicator

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

## Micro-Interactions

Hover and tap effects:

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

## Accessibility: Reduced Motion

Always respect user preferences:

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
```

**Reduced Motion Alternatives:**

| Animation Type | With Motion | Reduced Motion |
|----------------|-------------|----------------|
| Slide/transform | x, y movement | Opacity fade only |
| Scale | scale: 0.8 → 1 | Opacity fade only |
| Parallax | Scroll-linked position | Static position |
| Stagger | Sequential delays | Instant appearance |

---

## Animation Presets by Slide Type

| Slide Type | Animation | Duration |
|------------|-----------|----------|
| Title Slide | fadeIn + stagger objectives | 0.8s |
| Content Slide | slideUp heading, stagger body | 0.6s |
| Data/Table | scaleIn | 0.5s |
| Cards/Grid | staggerContainer + staggerItem | 0.1s stagger |
| Quote | fadeIn with slight scale | 0.8s |
| Takeaway | popIn with spring | 0.5s |
| Activity | slideFromLeft | 0.5s |

---

## Reusable Animated Components

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
