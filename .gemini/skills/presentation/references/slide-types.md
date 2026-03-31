# Slide Types Reference

Reference for different slide types with examples.

---

## 1. Title Slide

Session header with objectives. Sets expectations for the session.

```tsx
<FullPageSection id="intro" title="Introduction">
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
</FullPageSection>
```

**Animation**: fadeIn + stagger objectives (0.8s)

---

## 2. Concept Slide

Large heading + explanation. Use ContentBlock for definitions.

```tsx
<FullPageSection id="concept" title="Key Concept">
  <h2 className="text-3xl md:text-5xl font-black mb-8 tracking-tighter">
    Key Concept Title
  </h2>
  <ContentBlock title="Definition" variant="info" icon={Info}>
    <p className="text-2xl">
      Detailed explanation of the concept...
    </p>
  </ContentBlock>
</FullPageSection>
```

**Animation**: slideUp for heading, stagger for body (0.6s)

---

## 3. Data Slide

Tables, charts, statistics. Use TableWrapper for structured data.

```tsx
<FullPageSection id="comparison" title="Comparison">
  <TableWrapper
    title="Business Entity Comparison"
    headers={['Aspect', 'Sole Proprietor', 'Partnership', 'Corporation']}
    rows={[
      ['Ownership', 'Single owner', '2+ partners', 'Shareholders'],
      ['Liability', 'Unlimited', 'Unlimited', 'Limited'],
      ['Taxation', 'Personal', 'Pass-through', 'Corporate + Personal']
    ]}
  />
</FullPageSection>
```

**Animation**: scaleIn for table (0.5s)

---

## 4. Visual Slide

Diagrams, flowcharts, images. Use grid layouts and colored cards.

```tsx
<FullPageSection id="flow" title="Money Flow">
  <div className="flex flex-col items-center space-y-4">
    <div className="p-8 bg-gray-900 text-white rounded-3xl text-center">
      <p className="text-4xl font-black">MARKET</p>
    </div>
    <div className="h-16 w-1 bg-gray-300"></div>
    <div className="p-8 bg-blue-600 text-white rounded-3xl text-center">
      <p className="text-4xl font-black">COOPERATIVE</p>
    </div>
    <div className="h-16 w-1 bg-gray-300"></div>
    <div className="p-8 bg-green-600 text-white rounded-3xl text-center">
      <p className="text-4xl font-black">MEMBERS</p>
    </div>
  </div>
</FullPageSection>
```

**Animation**: staggerContainer for sequential reveal

---

## 5. Grid Cards Slide

Multiple items displayed as cards.

```tsx
<FullPageSection id="traits" title="Key Traits">
  <h2 className="text-3xl md:text-5xl font-black mb-8 tracking-tighter">
    Entrepreneurial Traits
  </h2>
  <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
    {traits.map(trait => (
      <div className="p-6 bg-white rounded-3xl border-2 shadow-sm">
        <trait.icon className="w-12 h-12 text-blue-600 mb-4" />
        <h4 className="text-2xl font-black mb-2">{trait.title}</h4>
        <p className="text-xl text-gray-600">{trait.description}</p>
      </div>
    ))}
  </div>
</FullPageSection>
```

**Animation**: staggerContainer + staggerItem (0.1s stagger)

---

## 6. Quote Slide

Large italic text, centered or with attribution.

```tsx
<FullPageSection id="quote" title="Inspiration">
  <div className="text-center max-w-4xl mx-auto">
    <p className="text-3xl md:text-5xl font-light italic leading-relaxed text-gray-700">
      "The best way to predict the future is to create it."
    </p>
    <p className="text-2xl font-bold text-gray-500 mt-8">
      — Peter Drucker
    </p>
  </div>
</FullPageSection>
```

**Animation**: fadeIn with slight scale (0.8s)

---

## 7. Activity Slide

Green ContentBlock with clear instructions and deliverables.

```tsx
<FullPageSection id="activity" title="Activity">
  <ContentBlock title="Group Activity: Business Model Canvas" variant="activity" icon={Users}>
    <div className="space-y-4">
      <p className="text-2xl font-bold">Instructions:</p>
      <ol className="text-2xl space-y-2 list-decimal list-inside">
        <li>Form groups of 4-5 members</li>
        <li>Choose a business idea from your cooperative</li>
        <li>Complete the Business Model Canvas template</li>
        <li>Prepare a 3-minute presentation</li>
      </ol>
      <p className="text-2xl font-bold mt-6">Time: 30 minutes</p>
      <p className="text-2xl font-bold">Deliverable: Completed BMC poster</p>
    </div>
  </ContentBlock>
</FullPageSection>
```

**Animation**: slideFromLeft (0.5s)

---

## 8. Takeaway Slide

Amber Takeaway component with single memorable message.

```tsx
<FullPageSection id="takeaway" title="Key Takeaway">
  <Takeaway
    content="Strong individual businesses create shared prosperity for the entire community."
  />
</FullPageSection>
```

**Animation**: popIn with spring (0.5s)

---

## 9. Navigation Slide

NextSession component to continue journey.

```tsx
<FullPageSection id="next" title="Up Next">
  <NextSession
    title="1.2 Opportunity Recognition"
    path="/academy/edp/module1/session2"
  />
</FullPageSection>
```

**Animation**: fadeIn (0.5s)

---

## Complete Session Page Template

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
import { fadeIn, slideUp, scaleIn, staggerContainer, staggerItem } from '@/lib/presentation-animations'

export default function ModuleXSessionY() {
  return (
    <div className="pb-20">
      {/* 1. Title Slide */}
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
            objectives={["Objective 1", "Objective 2"]}
          />
        </motion.div>
      </FullPageSection>

      {/* 2. Content Slide */}
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

      {/* 3. Data Slide */}
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

      {/* 4. Activity Slide */}
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

      {/* 5. Takeaway Slide */}
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

      {/* 6. Navigation Slide */}
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
