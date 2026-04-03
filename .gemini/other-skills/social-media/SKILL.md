---
name: social-media
description: "Provides social media strategy and management expertise for cooperatives, social enterprises, and government agencies in BARMM. Use when designing social media courses (with /academy), consulting on social media strategy, planning Social Marketing behavior change campaigns on social platforms, or implementing platform social media features. Covers FIERCE framework, content creation, community management, analytics, and sector-specific approaches."
argument-hint: "[topic]"
---

# Social Media

Domain expertise for social media strategy, content creation, community management, and analytics. Tailored for cooperatives, social enterprises, and government agencies in BARMM.

## When to Use

| Scenario | Invocation |
|----------|------------|
| Design social media courses | `/social-media` + `/academy` |
| Consulting for coops/SEs | `/social-media` (standalone) |
| Brand social strategy | `/social-media` + `/branding` |
| Marketing integration | `/social-media` + `/marketer` |
| **Behavior change campaigns** | `/social-media` + `/marketer` (Social Marketing) |
| Platform feature specs | `/social-media` + `/featuredev` |

## Workflow Modes

### Mode 1: Curriculum Design (with /academy)

For social media training courses and workshops:

1. Determine learning level (Foundational, Practitioner, Advanced)
2. Select modules from `references/curriculum-design.md`
3. Adapt for sector context (Cooperative, SE, Government)
4. Design assessments and outcomes
5. Use templates from `assets/` for course materials

See [references/curriculum-design.md](references/curriculum-design.md) for complete curriculum guide.

### Mode 2: Consulting

For social media strategy development:

1. **Audit** - Use `assets/social-media-audit-template.md`
2. **Strategy** - Use `assets/social-media-strategy-template.md`
3. **Content Planning** - Use `assets/content-calendar-template.md`
4. Apply sector-specific adaptations from `references/sector-contexts.md`

### Mode 3: Platform Features

For Negosyo Portal social media features:

1. Define feature requirements using strategy frameworks
2. Spec UI/UX with `/featuredev`
3. Integrate with storefront social sharing
4. Connect to analytics dashboards

---

## Core Frameworks

### FIERCE Framework

| Phase | Focus |
|-------|-------|
| **F**ocus | Define goals, SMART objectives |
| **I**nsight | Audit current state, research audience |
| **E**ngage | Content pillars, community strategy |
| **R**espond | Engagement, crisis protocols |
| **C**reate | Content creation, scheduling |
| **E**valuate | Analytics, optimization |

### Content Distribution (70/20/10)

| Type | % | Description |
|------|---|-------------|
| Value | 70% | Educational, entertaining, helpful |
| Shared | 20% | Curated, partner, UGC content |
| Promotional | 10% | Products, services, offers |

### Philippines Social Media Context

| Insight | Implication |
|---------|-------------|
| 92.1% use Facebook | Must-have platform |
| Mobile-first users | Optimize for mobile |
| High Reels consumption | Prioritize short video |
| Messenger for business | Customer service channel |

---

## Sector Adaptations

### Cooperatives

Focus on ICA Cooperative Principles in social media:
- Member stories and testimonials
- Cooperative education content
- Facebook Groups for member community
- Democratic values in voice and tone

See [references/sector-contexts.md](references/sector-contexts.md) for details.

### Social Enterprises

Balance commercial and social mission:
- Impact stories (40% of content)
- Product features (30%)
- Community engagement (20%)
- Promotions (10%)

### Government

Build citizen trust and service delivery:
- Program announcements
- Citizen service information
- Accessibility compliance
- Crisis communication protocols

---

## BARMM Context

| Factor | Adaptation |
|--------|------------|
| **Languages** | Filipino, Arabic, local languages |
| **Cultural sensitivity** | Islamic values, traditions |
| **Timing** | Avoid prayer times, Ramadan adjustments |
| **Celebrations** | Eid greetings, local events |

---

## Key Performance Indicators

| KPI | Formula | Benchmark |
|-----|---------|-----------|
| Engagement Rate | (Likes+Comments+Shares)/Followers × 100 | 1-3% Instagram |
| Reach | Platform-reported | - |
| Click-Through Rate | Clicks/Impressions × 100 | - |
| Follower Growth | New/Total × 100 | - |

See [references/analytics-measurement.md](references/analytics-measurement.md) for complete metrics.

---

## Social Marketing on Social Platforms

**Social Marketing ≠ Social Media Marketing.** Social Marketing uses marketing principles to influence behavior for social good. When applied to social platforms, it leverages reach, targeting, and social proof for behavior change campaigns.

### When to Use Social Marketing

| Use Case | Example |
|----------|---------|
| Public health | Vaccination, nutrition campaigns |
| Civic engagement | Program registration, participation |
| Environmental | Recycling, conservation behaviors |
| Cooperative adoption | Member participation, principle adherence |
| SE impact | Conscious purchasing, stakeholder engagement |

### Behavior Change Content Pillars

| Pillar | Purpose | % of Content |
|--------|---------|--------------|
| **Awareness** | Educate about issue/behavior | 25% |
| **Motivation** | Inspire and encourage | 25% |
| **Enablement** | Provide tools and how-tos | 25% |
| **Community** | Social proof and support | 25% |

### Social Norms Messaging

Use descriptive norms ("92% of members participate") and dynamic norms ("More people are joining every day") to show desired behavior is common and approved.

### Digital Nudges on Social Platforms

| Nudge | Platform Application |
|-------|---------------------|
| Commitment | "I commit to..." campaigns |
| Social Proof | Testimonial videos, UGC |
| Simplification | One-click sign-up links |
| Timing | Reminder posts at decision points |

See [references/social-marketing.md](references/social-marketing.md) for complete guide.

---

## Skill Integrations

| Skill | Integration |
|-------|-------------|
| `/academy` | Social media curriculum, workshops |
| `/marketer` | Campaign integration, funnel alignment; **Social Marketing campaign planning** |
| `/branding` | Visual identity, brand voice; **Cause branding, impact messaging** |
| `/featuredev` | Platform social features |

---

## References

| Reference | Purpose |
|-----------|---------|
| [social-media-strategy.md](references/social-media-strategy.md) | Strategy frameworks, SMART goals |
| [content-creation.md](references/content-creation.md) | Content types, formats, scheduling |
| [community-management.md](references/community-management.md) | Engagement, moderation, crisis |
| [analytics-measurement.md](references/analytics-measurement.md) | KPIs, reporting, optimization |
| [social-marketing.md](references/social-marketing.md) | **Behavior change campaigns, social norms, digital nudges** |
| [sector-contexts.md](references/sector-contexts.md) | Coop, SE, government adaptations |
| [curriculum-design.md](references/curriculum-design.md) | Course modules, workshop formats |

---

## Cooperative Integration

When this skill encounters cooperative-related contexts, invoke `/cooperative` for specialized knowledge.

### Cooperative Triggers

Invoke `/cooperative` when you detect:
- Keywords: "cooperative", "coop", "RA 9520", "CDA", "primary cooperative", "secondary cooperative", "CSEA"
- Topics: Cooperative social media content, member engagement posts, GA event promotion, coop news announcements, member recruitment campaigns, cooperative education content, patronage refund announcements
- Entities: Cooperative members, officers, BOD, GA, committees, statutory funds

### Integration Pattern

```
/social-media + /cooperative Integration
|
+-- Detect cooperative context in user request
+-- Invoke /cooperative for domain knowledge
|   +-- RA 9520 provisions (member communication requirements)
|   +-- ICA Cooperative Principles (content themes)
|   +-- CDA memorandum circulars (social media guidelines)
+-- Apply social media methodology with cooperative context
|   +-- Member-centric content (not customer-centric)
|   +-- Cooperative values in messaging
|   +-- Facebook Groups for member community
|   +-- Democratic engagement in social channels
+-- Reference /cooperative assets as needed
```

### Key /cooperative Assets

| Asset | Path | Use When |
|-------|------|----------|
| RA 9520 Full Text | `../../cooperative/assets/ra-9520-philippine-cooperative-code-2008.md` | Verbatim legal citations for posts |
| RA 9520 Guide | `../../cooperative/references/ra-9520-guide.md` | Understanding cooperative principles for content |
| Templates Index | `../../cooperative/assets/templates/index.md` | Social media post templates |
| Memorandum Circulars | `../../cooperative/references/memorandum-circulars/index.md` | Communication compliance guidelines |

---

## Assets

| Asset | Purpose |
|-------|---------|
| [social-media-strategy-template.md](assets/social-media-strategy-template.md) | Strategy document template |
| [content-calendar-template.md](assets/content-calendar-template.md) | Monthly content calendar |
| [social-media-audit-template.md](assets/social-media-audit-template.md) | Audit/assessment template |
