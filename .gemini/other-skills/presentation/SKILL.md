---
name: presentation
description: Web-based presentation UI builder for MoroAcademy. Creates PowerPoint-like slide presentations as Next.js pages for live workshops, video recording, and facilitated training. Use when building presentation slides, session pages, facilitator-controlled content, or projector-ready web interfaces. Covers PresentationMode layout, SlideTimeline navigation, FullPageSection slides, ContentBlock variants, Framer Motion animations, typography scale, responsive design, and video recording optimization. Invoke when /academy needs to build presentation pages in STAGE 4 (IMPLEMENT).
argument-hint: "[topic]"
---

# Presentation - Web-Based Slide UI Builder

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's presentation request                     ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

## Overview

Build PowerPoint-like presentation UIs as web pages for MoroAcademy. Presentations display on projectors, work on mobile devices, support facilitator-controlled locking, and can be recorded for video courses.

**Reference Implementation**: `/frontend/src/app/(academy)/academy/model-presentation/`

---

## When to Use This Skill

Invoke Presentation when:
- **Building Session Pages**: "Create slides for Module 3 Session 2"
- **Presentation Layout**: "Set up PresentationMode for this workshop"
- **Slide Components**: "Add a takeaway slide with animation"
- **Facilitator Control**: "Enable content locking for live workshop"
- **Video Recording**: "Optimize slides for HD recording"
- **Timeline Navigation**: "Add scroll-linked timeline to presentation"
- **Animation Design**: "Add Framer Motion animations to slides"

**Keywords**: "presentation", "slides", "PowerPoint", "session page", "projector", "fullscreen", "PresentationMode", "SlideTimeline", "FullPageSection", "ContentBlock", "Takeaway", "facilitator control", "content locking", "Framer Motion", "animation", "video recording"

---

## Quick Start

### Minimal Presentation Page

```tsx
import { PresentationMode } from '@/components/academy/PresentationMode'
import { FullPageSection, SessionHeader, ContentBlock, Takeaway } from '@/components/academy'

export default function SessionPage() {
  const sections = [
    { id: 'intro', label: 'Introduction' },
    { id: 'concept', label: 'Key Concept' },
    { id: 'takeaway', label: 'Key Takeaway' },
  ]

  return (
    <PresentationMode
      sections={sections}
      exitUrl="/academy/course-name"
      showProgress={true}
      progressPosition="bottom"
    >
      <FullPageSection id="intro" title="Introduction">
        <SessionHeader
          module="Module 1"
          session="Session 1.1"
          title="Topic Title"
          duration="30 Minutes"
          objectives={["Objective 1", "Objective 2"]}
        />
      </FullPageSection>

      <FullPageSection id="concept" title="Key Concept">
        <ContentBlock title="Definition" variant="info">
          <p>Content here...</p>
        </ContentBlock>
      </FullPageSection>

      <FullPageSection id="takeaway" title="Key Takeaway">
        <Takeaway content="The main message to remember." />
      </FullPageSection>
    </PresentationMode>
  )
}
```

---

## Branding Requirements

**MoroAcademy logo MUST appear on every slide.**

| Asset | Path | Use Case |
|-------|------|----------|
| Full Logo | `/images/brand/moroacademy-logo.svg` | Top corner branding |
| Icon Only | `/images/brand/moroacademy-icon.svg` | Smaller displays |

Logo placement: Top-left (default). The `PresentationMode` component handles this automatically.

---

## Font Standard

### Official Font: Inter Only

**All MoroAcademy presentations MUST use Inter as the sole font family.**

```tsx
// Apply Inter to all presentation content
<div className="font-[family-name:var(--font-inter)]">
  {/* All presentation slides */}
</div>
```

**Reference Implementation**: `/frontend/src/app/(academy)/academy/model-presentation/`

### Font Weights

| Weight | Class | Use For |
|--------|-------|---------|
| 900 (Black) | `font-black` | Main titles, key messages |
| 700 (Bold) | `font-bold` | Subheadings, emphasis |
| 600 (Semibold) | `font-semibold` | Card titles, labels |
| 500 (Medium) | `font-medium` | Body text, descriptions |

### Prohibited Fonts

Do NOT use these in presentations:
- Outfit (previously used, now deprecated)
- Playfair Display
- DM Serif Display
- Poppins
- Any decorative or display fonts

**Full typography standards**: See [../academy/references/presentation-ui-standards.md](../academy/references/presentation-ui-standards.md)

---

## Core Components

### PresentationMode (Layout Wrapper)

Fullscreen presentation layout with branding and navigation.

```tsx
<PresentationMode
  sections={[{ id: 'intro', label: 'Introduction' }]}
  showProgress={true}
  progressPosition="bottom"
  showTimeline={false}
  exitUrl="/academy"
>
  {children}
</PresentationMode>
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `sections` | TimelineSection[] | required | Sections for navigation |
| `showLogo` | boolean | true | Show MoroAcademy logo |
| `logoPosition` | string | 'top-left' | Logo position |
| `showProgress` | boolean | true | Show scroll progress bar |
| `progressPosition` | 'top' \| 'bottom' | 'bottom' | Progress bar position |
| `showTimeline` | boolean | false | Show side timeline |
| `showControls` | boolean | true | Show toolbar controls |
| `exitUrl` | string | '/academy' | Exit navigation URL |

### FullPageSection (Slide Container)

Each slide is a full-viewport section.

```tsx
<FullPageSection id="unique-id" title="Slide Title">
  {/* Slide content */}
</FullPageSection>
```

Features: Full viewport height, scroll-snap, auto-registers in navigation, supports content locking.

### SessionHeader (Title Slide)

Opening slide with session info and objectives.

```tsx
<SessionHeader
  module="Module 1"
  session="Session 1.1"
  title="Understanding Entrepreneurship"
  duration="30 Minutes"
  objectives={["Objective 1", "Objective 2"]}
/>
```

### ContentBlock (Styled Content)

Colored side-border blocks for different content types.

```tsx
<ContentBlock title="Key Concept" variant="info" icon={Lightbulb}>
  <p>Content goes here...</p>
</ContentBlock>
```

| Variant | Border | Use For |
|---------|--------|---------|
| `default` | Gray | General content |
| `info` | Blue | Definitions, explanations |
| `activity` | Green | Exercises, activities |
| `takeaway` | Amber | Key points, summaries |
| `caution` | Red | Warnings, important notes |

### TableWrapper (Data Tables)

Presentation-ready tables.

```tsx
<TableWrapper
  title="Comparison"
  headers={['Aspect', 'Option A', 'Option B']}
  rows={[['Cost', '₱1,000', '₱2,000']]}
/>
```

### Takeaway (Key Message)

Large box for critical takeaways.

```tsx
<Takeaway content="Strong businesses create shared prosperity." />
```

### NextSession (Navigation)

Link to next session.

```tsx
<NextSession title="1.2 Opportunity Recognition" path="/academy/edp/module1/session2" />
```

---

## Typography Scale

**CRITICAL: Minimum font size is 24px (text-2xl).**

| Level | Mobile | Desktop | Use For |
|-------|--------|---------|---------|
| Title | text-3xl | text-[64px] | Session titles |
| H2 | text-3xl | text-5xl | Section headers |
| Body | text-2xl | text-2xl | General content |
| Lead | text-2xl | text-3xl | Opening paragraphs |

Never use text-sm, text-base, text-lg, or text-xl for slide content.

---

## Content Width

| Screen Size | Width | Padding |
|-------------|-------|---------|
| Mobile (<768px) | 100% | px-4 |
| Desktop (≥768px) | 85% centered | px-12 |

---

## Text Formatting in JSX

**Markdown does NOT work in JSX. Use HTML tags:**

| Want | DON'T Use | DO Use |
|------|-----------|--------|
| **Bold** | `**text**` | `<strong>text</strong>` |
| *Italic* | `*text*` | `<em>text</em>` |
| Links | `[text](url)` | `<a href="url">text</a>` |

---

## Keyboard Navigation

| Action | Keys |
|--------|------|
| Next slide | `↓` `→` `PageDown` `Space` |
| Previous slide | `↑` `←` `PageUp` |
| First slide | `Home` |
| Last slide | `End` |
| Exit fullscreen | `Escape` |

---

## Facilitator Control (Content Locking)

For live workshops, facilitators can lock content to control pace.

### Lock Levels

| Level | Scope | Use Case |
|-------|-------|----------|
| Module | All sessions in module | "We'll cover this tomorrow" |
| Session | All sections in session | "Focus on this first" |
| Section | Individual slide | "Don't scroll ahead" |

Facilitator controls appear in toolbar for users with `admin`, `content_manager`, or `superuser` roles.

---

## Additional References

For detailed documentation, see:
- [references/animations.md](references/animations.md) - Framer Motion animation patterns
- [references/layout-patterns.md](references/layout-patterns.md) - Layout patterns and responsive design
- [references/slide-types.md](references/slide-types.md) - Slide type reference with examples

---

## Skill Integration

| When | Invoke | Purpose |
|------|--------|---------|
| Building session pages | This skill | Create presentation UI |
| Course/workshop design | `/academy` | Curriculum structure |
| API endpoints | `/backend` | Data integration |
| Full-stack features | `/featuredev` | Complete implementation |

**Called by**: `/academy` during STAGE 4 (IMPLEMENT) for building presentation pages.
