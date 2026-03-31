---
name: branding
description: "Provides brand strategy and identity expertise for cooperatives, social enterprises, and government agencies in BARMM. Use when designing branding courses (with /academy), consulting on brand strategy or positioning, building storefront branding features, or developing cause branding. Covers Aaker brand equity, Keller CBBE pyramid, Kapferer identity prism, brand architecture, ICA cooperative marque, Social Marketing brand positioning, and sector-specific branding."
argument-hint: "[topic]"
---

# Branding Skill

## Phase 0: Prompt Refinement (Mandatory)

**Before executing this skill's workflow, invoke `/prompter` first:**

1. Invoke `/prompter` with the user's branding request
2. Present the refined prompt to the user
3. Wait for user confirmation:
   - "Yes, proceed" → Continue to appropriate workflow mode
   - "No, adjust X" → Refine and re-confirm
   - "Let me rephrase" → Restart with new input

**Do not proceed without user confirmation.**

---

Expert guidance for brand strategy and identity development in the Bangsamoro context.

## When to Use

| Trigger | Action |
|---------|--------|
| Branding course/workshop design | Invoke with `/academy` for curriculum expertise |
| Brand strategy consulting | Use directly with strategy frameworks |
| Brand identity development | Apply identity frameworks and templates |
| Platform branding features | Combine with `/featuredev` for implementation |
| Branding + marketing synergy | Coordinate with `/marketer` |

## Core Concepts

### What is a Brand?

A brand is the sum of all experiences, perceptions, and associations that stakeholders have with an organization, product, or service. It goes beyond visual elements to encompass purpose, promise, and personality.

### Brand vs Logo vs Identity

| Term | Definition |
|------|------------|
| **Brand** | Total perception and experience |
| **Brand Identity** | Visual and verbal expression system |
| **Logo** | Primary visual mark/symbol |

### Brand Equity Components (Aaker)

| Component | Description |
|-----------|-------------|
| **Brand Loyalty** | Strength of customer attachment |
| **Brand Awareness** | Recognition and recall |
| **Perceived Quality** | Customer perception of quality |
| **Brand Associations** | Mental connections to brand |
| **Proprietary Assets** | Patents, trademarks, channels |

## Workflow Modes

### Mode 1: Curriculum Design (with /academy)

When designing branding courses or workshops:

#### STAGE 0: Deep Research (Recommended)

For comprehensive curriculum, invoke `/deep-research` first:

```
STAGE 0: DEEP RESEARCH → Output: Validated Research Brief
│
├── Research latest branding trends and case studies
├── Gather sector-specific examples (coop, SE, government)
├── Validate with authoritative sources (Aaker, Keller, Kapferer)
└── OUTPUT: Research Brief for curriculum design
```

#### Curriculum Design Steps

1. **Identify learning level**: Foundational / Practitioner / Advanced
2. **Select course format**: Half-day / Full-day / Multi-day / Online
3. **Choose modules**: See [curriculum-design.md](references/curriculum-design.md)
4. **Design assessments**: Brand audit, identity brief, portfolio

**Standard Branding Course Modules:**
1. Introduction to Branding
2. Brand Foundation (Mission, Vision, Values)
3. Target Audience and Positioning
4. Visual Identity Development
5. Verbal Identity and Messaging
6. Brand Guidelines
7. Brand Touchpoints
8. Brand Measurement

### Mode 2: Brand Consulting

For brand strategy and identity consulting:

1. **Assess current state**: Brand audit using [brand-audit-template.md](assets/brand-audit-template.md)
2. **Define strategy**: Apply frameworks based on need
3. **Develop identity**: Visual and verbal identity system
4. **Consider sector context**: Coop, SE, or government application

**Framework Selection Guide:**

| Need | Framework |
|------|-----------|
| Brand equity building | Aaker Brand Equity Model |
| Customer-based brand building | Keller CBBE Pyramid |
| Identity development | Kapferer Brand Identity Prism |
| Market positioning | Positioning Statement + POP/POD |
| Multi-brand management | Brand Architecture |
| **Behavior change branding** | **Social Marketing + Cause Branding** |

**Templates available:**
- [Brand Strategy Template](assets/brand-strategy-template.md)
- [Brand Identity Brief](assets/brand-identity-brief.md)
- [Brand Audit Template](assets/brand-audit-template.md)

### Mode 3: Platform Feature Development

When building branding features for the platform:

1. Read [sector-contexts.md](references/sector-contexts.md) for sector considerations
2. Apply branding principles to storefront and profile features
3. Ensure visual consistency with Negosyo Blue (#0056D2)
4. Integrate with existing portal architecture

## Quick Reference

### Keller CBBE Pyramid (4 Levels)

| Level | Question | Building Blocks |
|-------|----------|-----------------|
| **1. Identity** | Who are you? | Salience (awareness) |
| **2. Meaning** | What are you? | Performance + Imagery |
| **3. Response** | What about you? | Judgments + Feelings |
| **4. Relationships** | What about you and me? | Resonance (loyalty) |

### Kapferer Identity Prism (6 Facets)

| Facet | Question |
|-------|----------|
| **Physique** | What does it look like? |
| **Personality** | What character does it have? |
| **Culture** | What values does it embody? |
| **Relationship** | What connection does it create? |
| **Reflection** | Who is the typical user? |
| **Self-Image** | How does using it make people feel? |

### Positioning Statement Formula

```
For [target segment], [brand] is the [category]
that [key benefit] because [reason to believe].
```

### Brand Architecture Types

| Type | Description | Best For |
|------|-------------|----------|
| **Branded House** | Master brand dominates | Coops, agencies |
| **Endorsed Brands** | Sub-brands with parent | Multi-product SEs |
| **House of Brands** | Individual brands | Diverse portfolios |

### Social Marketing Branding

Social Marketing uses marketing principles to influence behavior for social good. For branding, this means building brand identity around positive behavior change.

**Cause Branding Spectrum:**

| Level | Description | Example |
|-------|-------------|---------|
| **Cause-Related Marketing** | Temporary campaign tie-in | "Buy one, donate one" |
| **Cause Branding** | Cause integrated into brand | TOMS, Patagonia |
| **Social Purpose Brand** | Brand exists for the cause | Charity: water |

**Social Proof Elements for Impact Brands:**
- Member/beneficiary testimonials
- Impact numbers and outcomes
- Community endorsements
- Trust marks and certifications
- User-generated content

**Impact Messaging Framework:**
```
THE PROBLEM: "Before, families had no access to..."
THE SOLUTION: "Through [brand], they now..."
THE IMPACT: "Today, 500 families..."
THE INVITATION: "Join us to..."
```

See [social-marketing.md](references/social-marketing.md) for complete guide.

## Reference Files

| File | Use When |
|------|----------|
| [brand-strategy.md](references/brand-strategy.md) | Need Aaker, Keller, positioning, architecture details |
| [brand-identity.md](references/brand-identity.md) | Need Kapferer prism, visual/verbal identity systems |
| [social-marketing.md](references/social-marketing.md) | **Cause branding, impact messaging, behavior change branding** |
| [sector-contexts.md](references/sector-contexts.md) | Applying branding to coops, SEs, government |
| [curriculum-design.md](references/curriculum-design.md) | Designing branding courses with /academy |

## Integration with Other Skills

| Skill | Integration Pattern |
|-------|---------------------|
| `/academy` | Provides branding subject matter expertise for course design |
| `/marketer` | Coordinates brand positioning with marketing strategy; **Social Marketing campaign planning** |
| `/social-media` | **Social norms messaging, behavior change content, impact storytelling** |
| `/social-enterprise` | Applies branding to SE impact communication |
| `/cooperative` | Applies branding to cooperative identity |
| `/featuredev` | Guides branding-related feature requirements |
| `/deep-research` | Sources for branding research questions |

## BARMM Application Examples

### Cooperative Example
**Challenge**: Low brand recognition beyond immediate community

**Strategy**:
- Apply ICA Marque and .coop domain for credibility
- Position on cooperative difference (member-owned, values-driven)
- Develop consistent visual identity across all touchpoints
- Create member success stories for social proof
- Build branded house architecture for multiple services

### Social Enterprise Example
**Challenge**: Products not communicating impact story to buyers

**Strategy**:
- Develop impact-first brand positioning
- Create Kapferer identity prism emphasizing Culture and Relationship
- Build visual identity that tells maker stories
- Use impact labels and certifications as trust signals
- Design packaging that communicates purpose

### Government (CSEA) Example
**Challenge**: Need unified brand for multi-program agency

**Strategy**:
- Apply branded house architecture with program sub-brands
- Build trust through Capability, Reliability, Transparency, Humanity
- Create consistent visual system (Negosyo Blue #0056D2)
- Develop accessible, citizen-centered brand voice
- Ensure platform presence reflects institutional credibility

---

## Workflow: Cooperative Branding

See [cooperative-branding.md](references/cooperative-branding.md) for cooperative brand identity, ICA Marque usage, brand elements, messaging, stakeholder branding, and practical scenarios.

## Constraints

- Use authoritative sources (Aaker, Keller, Kapferer, Wheeler)
- Adapt strategies for BARMM cultural context
- Support CSEA's mandate for cooperative and SE development
- Consider budget constraints of small organizations
- Avoid purple colors in any UI recommendations
- Primary color: Negosyo Blue (#0056D2)
- Mobile-first approach for digital branding
