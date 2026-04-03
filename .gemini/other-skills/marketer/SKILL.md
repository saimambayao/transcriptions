---
name: marketer
description: "Provides marketing management expertise for the Bangsamoro Development Platform. Use when designing marketing courses/workshops (with /academy), consulting on marketing strategy, branding, or campaigns, building marketing-related platform features, researching marketing frameworks or digital marketing best practices, applying marketing to cooperative, SE, or government contexts, or planning Social Marketing campaigns for behavior change. Covers marketing fundamentals (4Ps, 7Ps, STP, AIDA), digital marketing, Social Marketing (behavior change for social good -- distinct from social media marketing), branding strategy, and sector-specific marketing for cooperatives, social enterprises, and public sector in BARMM. Integrates with /branding for brand strategy, /social-media for social platform execution, and /enterprise-dev for Phase 4 marketing."
argument-hint: "[topic]"
---

# Marketing Management Skill

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's marketing request                        ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

Expert guidance for marketing strategy and execution in the Bangsamoro context.

## When to Use

| Trigger | Action |
|---------|--------|
| Marketing course/workshop design | Invoke with `/academy` for curriculum expertise |
| Marketing strategy consulting | Use directly with marketing frameworks |
| Brand development | Apply branding and positioning frameworks |
| Digital marketing execution | Use digital marketing strategies |
| Campaign planning | Apply campaign planning templates |

## Core Concepts

### What is Marketing?

"Marketing is the activity, set of institutions, and processes for creating, communicating, delivering, and exchanging offerings that have value for customers, clients, partners, and society at large." — American Marketing Association

### The Marketing Mix

| Model | Elements | Best For |
|-------|----------|----------|
| **4Ps** | Product, Price, Place, Promotion | Physical products |
| **7Ps** | + People, Process, Physical Evidence | Services (coops, SEs) |

### STP Framework

| Step | Description | Key Question |
|------|-------------|--------------|
| **Segmentation** | Divide market into groups | Who are the different buyers? |
| **Targeting** | Select segments to serve | Which segments should we focus on? |
| **Positioning** | Create distinct place in mind | How should we be perceived? |

### MVaP-Informed Product Differentiation

When positioning products, apply the **Minimum Valuable Product (MVaP)** framework:

| Kano Category | Marketing Focus | Positioning Strategy |
|---------------|-----------------|---------------------|
| **Delighters** | Lead with this | Build UVP around ONE Delighter - this is your competitive moat |
| **Performance** | Meet threshold | Define Minimum Performance Metrics (MPM) to be competitive, not more |
| **Must-Haves** | Don't over-invest | Table stakes - mention but don't differentiate on these |
| **Zone of Indifference** | Avoid | Don't market features customers are lukewarm about |

**Key Insight**: Avoid creating a "Maximally Undifferentiated Product" (MUP) by trying to compete on every dimension. Focus marketing on ONE clear differentiator.

See [../shared/references/mvap-framework.md](../shared/references/mvap-framework.md) for complete framework.

### AIDA Model

```
AWARENESS → INTEREST → DESIRE → ACTION
    ↓           ↓          ↓         ↓
  Know       Learn      Want       Buy
```

## Workflow Modes

### Mode 1: Curriculum Design (with /academy)

When designing marketing courses or workshops:

#### STAGE 0: Deep Research (Recommended)

For comprehensive curriculum, invoke `/deep-research` first:

```
STAGE 0: DEEP RESEARCH → Output: Validated Research Brief
│
├── Research latest marketing trends and case studies
├── Gather sector-specific examples (coop, SE, government)
├── Validate with authoritative sources (Kotler, AMA, CIM)
└── OUTPUT: Research Brief for curriculum design
```

#### Curriculum Design Steps

1. **Identify learning level**: Foundational / Practitioner / Advanced
2. **Select course format**: Half-day / Full-day / Multi-day / Online
3. **Choose modules**: See [curriculum-design.md](references/curriculum-design.md)
4. **Design assessments**: Marketing audit, campaign plan, portfolio

**Standard Marketing Course Modules:**
1. Introduction to Marketing
2. Understanding Your Market (STP)
3. The Marketing Mix (4Ps/7Ps)
4. Digital Marketing Fundamentals
5. Branding and Positioning
6. Marketing Communication
7. Marketing Planning
8. Marketing Measurement

### Mode 2: Marketing Consulting

For marketing strategy consulting:

1. **Assess current state**: Marketing audit, SWOT analysis
2. **Identify objectives**: What does the organization want to achieve?
3. **Select frameworks**: Based on need (positioning, digital, campaign)
4. **Consider sector context**: Coop, SE, or government application

**Framework Selection Guide:**

| Need | Framework |
|------|-----------|
| Market entry | STP + 4Ps/7Ps |
| Idea validation | Mom Test + 5 Validation Methods |
| Customer acquisition | AIDA + Customer Journey |
| Brand development | Positioning + Brand Identity |
| Digital presence | Digital Marketing Strategy |
| Campaign execution | Campaign Planning |
| **Behavior change** | **Social Marketing (Kotler-Lee 10-Step)** |

**Templates available:**
- [Marketing Plan Template](assets/marketing-plan-template.md)
- [Brand Positioning Template](assets/brand-positioning-template.md)
- [Campaign Planning Template](assets/campaign-planning-template.md)

### Mode 3: Platform Feature Development

When building marketing-related features for the platform:

1. Read [sector-contexts.md](references/sector-contexts.md) for sector considerations
2. Apply marketing principles to feature design
3. Consider user journey and touchpoints
4. Integrate with existing portal architecture

## Quick Reference

### Marketing Framework Selection

| Situation | Framework |
|-----------|-----------|
| New product/service launch | STP + 4Ps/7Ps + AIDA |
| Business idea validation | Mom Test + Risk Scoring + 5 Validation Methods |
| Brand refresh | Brand Positioning + Identity |
| Digital marketing start | Digital Marketing Strategy |
| Campaign planning | Campaign Framework |
| Member engagement (coops) | Cooperative Marketing |
| Impact communication (SEs) | SE Marketing + Storytelling |
| **Behavior change campaigns** | **Social Marketing (see below)** |

### Social Marketing (Behavior Change)

Social Marketing uses marketing principles to influence behavior for social good. **Distinct from social media marketing.**

| Element | Commercial Marketing | Social Marketing |
|---------|---------------------|------------------|
| **Goal** | Profit, sales | Behavior change, social good |
| **Product** | Goods/services | Desired behavior |
| **Price** | Monetary cost | Barriers to change |
| **Competition** | Other brands | Existing behaviors |

**When to Use Social Marketing:**
- Public health campaigns (vaccination, nutrition)
- Environmental behaviors (recycling, conservation)
- Civic engagement (program registration, participation)
- Cooperative adoption (member participation, principles)
- SE impact (conscious purchasing, stakeholder engagement)

**Key Frameworks:**
- Kotler-Lee 10-Step Planning Model
- Andreasen's 6 Benchmark Criteria
- Stages of Change (Transtheoretical Model)
- NSMC 8 Benchmark Criteria

See [social-marketing.md](references/social-marketing.md) for complete guide.

### Key Marketing Metrics

| Category | Metrics |
|----------|---------|
| **Awareness** | Reach, impressions, brand recall |
| **Engagement** | Likes, comments, shares, time on page |
| **Conversion** | Leads, sales, sign-ups |
| **Retention** | Repeat purchase, loyalty, NPS |
| **ROI** | CAC, CLV, marketing ROI |

### Digital Marketing Channels

| Channel | Best For |
|---------|----------|
| **Facebook** | Community building, local reach |
| **Instagram** | Visual products, lifestyle brands |
| **TikTok** | Youth engagement, viral content |
| **Website** | Credibility, information hub |
| **Email** | Nurturing, retention |
| **Google** | Search visibility, local discovery |

### Positioning Statement Formula

```
For [target segment], [brand] is the [category]
that [key benefit] because [reason to believe].
```

## Reference Files

| File | Use When |
|------|----------|
| [marketing-fundamentals.md](references/marketing-fundamentals.md) | Need 4Ps, 7Ps, STP, AIDA, Kotler details |
| [market-research.md](references/market-research.md) | Need validation methods, Mom Test, assumption testing |
| [digital-marketing.md](references/digital-marketing.md) | Need social media, content, SEO, analytics |
| [social-marketing.md](references/social-marketing.md) | **Behavior change campaigns, social good marketing** |
| [sector-contexts.md](references/sector-contexts.md) | Applying marketing to coops, SEs, government |
| [curriculum-design.md](references/curriculum-design.md) | Designing marketing courses with /academy |

## Integration with Other Skills

| Skill | Integration Pattern |
|-------|---------------------|
| `/academy` | Provides marketing subject matter expertise for course design |
| `/branding` | Social marketing brand positioning, cause branding |
| `/social-media` | Social marketing campaigns on social platforms |
| `/cooperative` | Applies marketing to member engagement |
| `/social-enterprise` | Applies marketing to impact communication |
| `/featuredev` | Guides marketing-related feature requirements |
| `/deep-research` | Sources for marketing research |

## BARMM Application Examples

### Cooperative Example
**Challenge**: Low member engagement in cooperative activities

**Strategy**:
- Segment members by activity level and needs
- Position coop as community partner, not just service provider
- Use Facebook groups for community building
- Create member success stories for social proof
- Implement referral program for member recruitment

### Social Enterprise Example
**Challenge**: Products not communicating social impact to buyers

**Strategy**:
- Develop impact storytelling framework
- Create "From Maker to Market" content series
- Add impact labels to products
- Use Instagram for behind-the-scenes stories
- Partner with influencers who share mission

### Government (CSEA) Example
**Challenge**: Low awareness of CSEA programs among target beneficiaries

**Strategy**:
- Segment by cooperative type and location
- Use local radio for rural reach
- Partner with barangay officials as messengers
- Create simple infographics for social media
- Host community information sessions

## Constraints

- Use authoritative sources (Kotler, AMA, CIM, HubSpot)
- Adapt strategies for BARMM cultural context
- Support CSEA's mandate for cooperative and SE development
- Consider budget constraints of small organizations
- Avoid purple colors in any UI recommendations
- Mobile-first approach for digital marketing

---

## Workflow: Marketing in Cooperatives

See [cooperative-marketing.md](references/cooperative-marketing.md) for cooperative marketing types, marketing cooperatives (RA 9520 Art. 23), member recruitment, cooperative identity marketing, and practical scenarios.
