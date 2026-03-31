# MoroNegosyo Design Thinking Document

**Platform**: Negosyo Bangsamoro Digital Platform
**URL**: https://negosyo.bangsamoro.site
**Framework**: Stanford d.school 5-Phase Design Thinking
**Date**: December 2024

---

## Executive Summary

MoroNegosyo is a multi-agency e-commerce and business management platform connecting Bangsamoro cooperatives, social enterprises, government agencies, and consumers. This Design Thinking document captures user insights, problem definitions, and opportunity areas to guide platform development.

---

## Table of Contents

1. [Platform Overview](#platform-overview)
2. [Phase 1: Empathize](#phase-1-empathize)
3. [Phase 2: Define](#phase-2-define)
4. [Phase 3: Ideate](#phase-3-ideate)
5. [Phase 4: Prototype](#phase-4-prototype)
6. [Phase 5: Test](#phase-5-test)
7. [Implementation Roadmap](#implementation-roadmap)

---

## Platform Overview

### Vision

To create a thriving digital economy for Bangsamoro by connecting cooperatives and social enterprises with consumers, while enabling government oversight and support.

### Portal Architecture

| Portal | Route | Primary Users | Purpose |
|--------|-------|---------------|---------|
| **Public Marketplace** | `/` | Consumers, General Public | Discover and purchase products |
| **Coop/SE Portal** | `/portal` | Cooperative & SE Managers | Manage business operations |
| **CSEA Admin** | `/csea` | CSEA Staff, Auditors | Oversight and compliance |
| **Coop Storefront** | `/coop/[slug]` | Public | Individual cooperative shops |
| **SE Storefront** | `/se/[slug]` | Public | Individual SE shops |

### Stakeholder Ecosystem

```
                    ┌─────────────────────────────────────┐
                    │         CSEA (Regulator)            │
                    │   Oversight, Compliance, Support    │
                    └─────────────────┬───────────────────┘
                                      │
           ┌──────────────────────────┼──────────────────────────┐
           │                          │                          │
           ▼                          ▼                          ▼
┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────────┐
│    Cooperatives     │   │  Social Enterprises │   │  Training Service   │
│  - Primary Coops    │   │  - Community-based  │   │     Providers       │
│  - Secondary Coops  │   │  - Impact-focused   │   │  - Capacity building│
└──────────┬──────────┘   └──────────┬──────────┘   └─────────────────────┘
           │                          │
           └────────────┬─────────────┘
                        │
                        ▼
              ┌─────────────────────┐
              │     Consumers       │
              │  - Local buyers     │
              │  - Conscious buyers │
              │  - Institutional    │
              └─────────────────────┘
```

---

## Phase 1: Empathize

### User Personas

#### Persona 1: Maria - Cooperative Manager

```
┌─────────────────────────────────────────────────────────────────────────┐
│  MARIA - COOPERATIVE MANAGER                                            │
├─────────────────────────────────────────────────────────────────────────┤
│  Demographics:                                                          │
│  - Age: 42, Female                                                      │
│  - Location: Cotabato City                                              │
│  - Role: General Manager, Cotabato Weavers Primary Cooperative          │
│  - Tech Comfort: Moderate (uses smartphone, basic computer)             │
│  - Education: College graduate (Business Administration)                │
├─────────────────────────────────────────────────────────────────────────┤
│  Goals:                                                                 │
│  - Increase coop sales and member livelihood                            │
│  - Maintain compliance with CDA/CSEA requirements                       │
│  - Expand market beyond local barangay                                  │
│  - Build coop's reputation for quality products                         │
├─────────────────────────────────────────────────────────────────────────┤
│  Pain Points:                                                           │
│  - Limited market access beyond local community                         │
│  - Complex compliance paperwork (FRAMES reporting)                      │
│  - Difficulty managing inventory and orders manually                    │
│  - Lack of digital marketing skills                                     │
│  - Slow payment collection from buyers                                  │
├─────────────────────────────────────────────────────────────────────────┤
│  Quote:                                                                 │
│  "We make beautiful products, but only our neighbors know about us.     │
│   We need to reach buyers who appreciate our craft."                    │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Persona 2: Ahmad - Social Enterprise Founder

```
┌─────────────────────────────────────────────────────────────────────────┐
│  AHMAD - SOCIAL ENTERPRISE FOUNDER                                      │
├─────────────────────────────────────────────────────────────────────────┤
│  Demographics:                                                          │
│  - Age: 28, Male                                                        │
│  - Location: Marawi City                                                │
│  - Role: Founder, Marawi Coffee Collective (Social Enterprise)          │
│  - Tech Comfort: High (uses multiple apps, active on social media)      │
│  - Education: College graduate (Agricultural Science)                   │
├─────────────────────────────────────────────────────────────────────────┤
│  Goals:                                                                 │
│  - Scale impact to more coffee farming families                         │
│  - Build a sustainable business model                                   │
│  - Tell the story of Marawi's rehabilitation through coffee             │
│  - Secure partnerships with conscious buyers                            │
├─────────────────────────────────────────────────────────────────────────┤
│  Pain Points:                                                           │
│  - Difficulty communicating social impact to buyers                     │
│  - Competition with commercial brands on price                          │
│  - Inconsistent order volume makes planning difficult                   │
│  - Limited access to business development support                       │
│  - No platform to showcase impact metrics                               │
├─────────────────────────────────────────────────────────────────────────┤
│  Quote:                                                                 │
│  "Every bag of coffee is a story of resilience. Buyers should see       │
│   the families behind the product, not just the price."                 │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Persona 3: Fatima - Conscious Consumer

```
┌─────────────────────────────────────────────────────────────────────────┐
│  FATIMA - CONSCIOUS CONSUMER                                            │
├─────────────────────────────────────────────────────────────────────────┤
│  Demographics:                                                          │
│  - Age: 35, Female                                                      │
│  - Location: Davao City (originally from Maguindanao)                   │
│  - Occupation: Marketing Professional                                   │
│  - Tech Comfort: Very high                                              │
│  - Income: Middle class                                                 │
├─────────────────────────────────────────────────────────────────────────┤
│  Goals:                                                                 │
│  - Support Bangsamoro businesses and communities                        │
│  - Find authentic, quality products from home region                    │
│  - Know the story and impact behind purchases                           │
│  - Convenient shopping with reliable delivery                           │
├─────────────────────────────────────────────────────────────────────────┤
│  Pain Points:                                                           │
│  - Hard to find authentic Bangsamoro products online                    │
│  - Can't verify if products truly benefit communities                   │
│  - Concerns about product quality and delivery reliability              │
│  - No trusted platform for regional products                            │
│  - Scattered sellers across social media (hard to compare)              │
├─────────────────────────────────────────────────────────────────────────┤
│  Quote:                                                                 │
│  "I want to buy from home, but I need to trust that my money            │
│   actually helps our kababayan, not just middlemen."                    │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Persona 4: Director Aisha - CSEA Staff

```
┌─────────────────────────────────────────────────────────────────────────┐
│  DIRECTOR AISHA - CSEA STAFF                                            │
├─────────────────────────────────────────────────────────────────────────┤
│  Demographics:                                                          │
│  - Age: 48, Female                                                      │
│  - Location: Cotabato City (BARMM Government Center)                    │
│  - Role: Division Chief, Cooperative Development Division               │
│  - Tech Comfort: Moderate                                               │
│  - Education: Master's in Public Administration                         │
├─────────────────────────────────────────────────────────────────────────┤
│  Goals:                                                                 │
│  - Grow number of compliant coops and SEs in BARMM                      │
│  - Improve FRAMES compliance rates                                      │
│  - Demonstrate sector impact to BARMM leadership                        │
│  - Streamline registration and monitoring processes                     │
├─────────────────────────────────────────────────────────────────────────┤
│  Pain Points:                                                           │
│  - Manual tracking of coop/SE compliance is time-consuming              │
│  - Difficulty reaching coops in remote areas                            │
│  - Limited real-time visibility into sector performance                 │
│  - Reports are manually compiled (error-prone, delayed)                 │
│  - Hard to identify coops needing intervention                          │
├─────────────────────────────────────────────────────────────────────────┤
│  Quote:                                                                 │
│  "I need to see the health of our cooperative sector at a glance,       │
│   not dig through spreadsheets for weeks."                              │
└─────────────────────────────────────────────────────────────────────────┘
```

### Empathy Maps

#### Cooperative Manager Empathy Map

| Quadrant | Insights |
|----------|----------|
| **SAYS** | "We need more buyers" / "Compliance is too complicated" / "We can't afford marketing" |
| **THINKS** | Worried about member livelihoods / Overwhelmed by paperwork / Hopes for digital tools |
| **DOES** | Sells at local markets / Files manual reports / Uses Facebook for promotion |
| **FEELS** | Frustrated by limited reach / Proud of products / Anxious about compliance deadlines |

#### Consumer Empathy Map

| Quadrant | Insights |
|----------|----------|
| **SAYS** | "I want to support local" / "How do I know it's authentic?" / "Is delivery reliable?" |
| **THINKS** | Skeptical of online sellers / Wants to make a difference / Compares with commercial options |
| **DOES** | Searches on Facebook/Instagram / Asks friends for recommendations / Hesitates before purchase |
| **FEELS** | Disconnected from home region / Desire to help community / Uncertain about quality |

### User Journey Maps

#### Current State: Cooperative Selling Journey

```
STAGE           AWARENESS        LISTING          SELLING          FULFILLMENT      COMPLIANCE

Actions         Word of mouth    Manual catalog   Respond to       Pack & ship      Prepare reports
                Facebook posts   Price lists      inquiries        Manual tracking  Submit to CSEA
                Local markets    No online store  Negotiate price  Local delivery   Annual audit

Touchpoints     Social media     Paper/Excel      Messenger/SMS    Physical store   Manual forms
                Barangay events  Local flyers     Phone calls      Partner couriers Paper documents

Emotions        😊 Hopeful       😰 Overwhelmed   😐 Uncertain     😓 Stressed      😤 Frustrated

Pain Points     Limited reach    No central       Time-consuming   Logistics gaps   Complex process
                No visibility    platform         No payment       Tracking issues  Deadline pressure
                                 Manual updates   integration      Quality control  Limited guidance
```

#### Current State: Consumer Buying Journey

```
STAGE           DISCOVERY        EVALUATION       PURCHASE         DELIVERY         POST-PURCHASE

Actions         See FB post      Ask questions    Send payment     Wait for item    Share/review
                Friend referral  Compare options  Confirm order    Track status     Reorder?
                Search online    Check seller     Negotiate        Receive product  Recommend

Touchpoints     Social media     Messenger        GCash/bank       Courier/pickup   Messenger
                Google search    Phone call       Direct transfer  SMS updates      Word of mouth

Emotions        😊 Curious       😐 Skeptical     😰 Uncertain     😤 Anxious       😊/😞 Variable

Pain Points     Hard to find     No reviews       No protection    No tracking      No feedback loop
                Scattered info   Trust issues     Manual process   Delays common    Can't verify impact
```

---

## Phase 2: Define

### Problem Statements

#### Problem 1: Market Access Gap

```
COOPERATIVE AND SE MANAGERS need EXPANDED MARKET ACCESS
beyond their local communities because GEOGRAPHIC ISOLATION
and LACK OF DIGITAL PRESENCE limit their customer base to
neighbors and occasional local market visitors.

Impact: Limited sales, underutilized production capacity,
        reduced member/beneficiary income
```

#### Problem 2: Trust and Verification Gap

```
CONSCIOUS CONSUMERS need TRUSTED VERIFICATION of product
authenticity and social impact because SCATTERED ONLINE SELLING
and LACK OF CERTIFICATIONS make it impossible to distinguish
genuine community products from commercial resellers.

Impact: Lost sales to coops/SEs, consumer hesitation,
        inability to command premium prices
```

#### Problem 3: Operational Efficiency Gap

```
COOPERATIVE MANAGERS need INTEGRATED BUSINESS TOOLS
for inventory, orders, and compliance because MANUAL PROCESSES
and DISCONNECTED SYSTEMS consume time that should be spent
on member services and product quality.

Impact: Errors, delays, compliance failures, operational stress
```

#### Problem 4: Sector Visibility Gap

```
CSEA STAFF need REAL-TIME SECTOR VISIBILITY
and performance analytics because MANUAL REPORTING
delays intervention and makes impact demonstration
to leadership difficult.

Impact: Reactive (not proactive) support, difficulty
        justifying budget, compliance gaps undetected
```

### How Might We (HMW) Statements

#### HMW - Market Access

| HMW Statement | Opportunity Area |
|---------------|------------------|
| HMW help coops/SEs reach buyers beyond their barangay without requiring digital marketing expertise? | Marketplace Discovery |
| HMW make it easy for a coop with no website to have a professional online presence? | Storefront Creation |
| HMW connect Bangsamoro products with diaspora consumers who want to support home? | Diaspora Market |
| HMW enable institutional buyers (hotels, restaurants) to easily source from coops? | B2B Channel |

#### HMW - Trust & Verification

| HMW Statement | Opportunity Area |
|---------------|------------------|
| HMW help buyers see and feel the social impact of their purchase? | Impact Storytelling |
| HMW create trust signals that distinguish verified coops/SEs from resellers? | Verification Badges |
| HMW enable buyers to trace products back to the community that made them? | Traceability |
| HMW build confidence in product quality before purchase? | Quality Assurance |

#### HMW - Operational Efficiency

| HMW Statement | Opportunity Area |
|---------------|------------------|
| HMW simplify order management so managers spend less time on admin? | Order Management |
| HMW make FRAMES compliance feel like a natural part of operations, not extra work? | Integrated Compliance |
| HMW help coops manage inventory without spreadsheets? | Inventory System |
| HMW enable secure, trackable payments that build buyer confidence? | Payment Integration |

#### HMW - Sector Visibility

| HMW Statement | Opportunity Area |
|---------------|------------------|
| HMW give CSEA real-time visibility into sector health without waiting for reports? | Analytics Dashboard |
| HMW help CSEA identify struggling coops before they become non-compliant? | Early Warning |
| HMW demonstrate sector impact to BARMM leadership with compelling data? | Impact Reporting |
| HMW enable proactive support instead of reactive compliance enforcement? | Support Triggers |

### Insight Synthesis

```
KEY INSIGHT 1: THE TRUST TRIANGLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Buyers, sellers, and regulators form a trust triangle.
When CSEA verifies a coop, buyers trust it.
When buyers purchase, sellers are motivated.
When sellers comply, CSEA can verify.
The platform must strengthen all three sides.

KEY INSIGHT 2: IMPACT IS THE DIFFERENTIATOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Coops and SEs cannot compete on price with commercial sellers.
Their competitive advantage is IMPACT - the story, the community,
the change that happens when someone buys from them.
The platform must make impact visible and compelling.

KEY INSIGHT 3: DIGITAL DIVIDE IS REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Many coops have limited digital literacy.
Complex tools will be abandoned.
The platform must be simpler than Facebook Marketplace
while providing more value than manual processes.

KEY INSIGHT 4: COMPLIANCE AS SERVICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Coops see compliance as burden, not benefit.
When compliance data is generated through normal operations
(sales, inventory, finances), it becomes invisible.
Make compliance a byproduct, not extra work.
```

---

## Phase 3: Ideate

### Opportunity Areas

#### Area 1: Unified Marketplace with Trust Signals

**Concept**: A single marketplace where all verified BARMM coops and SEs can list products, with clear trust indicators showing registration status, compliance level, and impact metrics.

**Features**:
- CSEA Verified badge for registered entities
- FRAMES Compliant badge for those meeting standards
- Impact score showing community benefit
- Product traceability to source community
- Reviews and ratings from verified buyers

**User Value**:
- Buyers: Confidence in authenticity
- Sellers: Credibility through verification
- CSEA: Visible sector activity

#### Area 2: Zero-Setup Storefronts

**Concept**: Auto-generated professional storefronts for every registered coop/SE, requiring only basic information to create a complete online shop.

**Features**:
- Auto-generated from registration data
- Template-based design (no design skills needed)
- Built-in product catalog management
- Integrated order management
- Impact story section

**User Value**:
- Sellers: Professional presence without expertise
- Buyers: Consistent, trustworthy shopping experience
- CSEA: Digital presence for all registered entities

#### Area 3: Impact Storytelling Engine

**Concept**: Tools and templates that help coops/SEs tell their story - who they are, who benefits, what changes when someone buys.

**Features**:
- Story templates for different SE types
- Photo/video integration for products
- Beneficiary profiles (with consent)
- Impact metrics dashboard
- Buyer-to-beneficiary connection

**User Value**:
- Sellers: Differentiate from commercial competitors
- Buyers: Emotional connection to purchases
- CSEA: Demonstrate sector impact

#### Area 4: Integrated Operations Hub

**Concept**: Simple, mobile-friendly tools for managing inventory, orders, and compliance in one place - making operations easier while generating compliance data automatically.

**Features**:
- Simple inventory tracking
- Order management with status updates
- Automatic FRAMES data generation
- Financial summary for reporting
- Member/beneficiary registry

**User Value**:
- Sellers: Less admin, more focus on products
- CSEA: Real-time compliance visibility
- Buyers: Order tracking and updates

#### Area 5: Sector Intelligence Dashboard

**Concept**: Real-time analytics for CSEA showing sector health, compliance status, and impact metrics - enabling proactive support.

**Features**:
- Live sector statistics
- Compliance heat map
- Alert system for at-risk entities
- Impact visualization
- Report generation

**User Value**:
- CSEA: Data-driven decision making
- Leadership: Clear impact demonstration
- Coops/SEs: Targeted support

### Concept Prioritization

| Concept | Impact | Feasibility | Priority |
|---------|--------|-------------|----------|
| Unified Marketplace with Trust Signals | High | Medium | P1 |
| Zero-Setup Storefronts | High | High | P1 |
| Impact Storytelling Engine | High | Medium | P2 |
| Integrated Operations Hub | High | Medium | P2 |
| Sector Intelligence Dashboard | Medium | High | P1 |

---

## Phase 4: Prototype

### MVP Feature Set

#### Phase 1 MVP: Foundation (Months 1-3)

| Feature | Description | User Benefit |
|---------|-------------|--------------|
| **Public Marketplace** | Browse and search products | Buyers discover products |
| **Basic Storefronts** | Auto-generated shop pages | Sellers have online presence |
| **Registration Integration** | CSEA-verified entities only | Trust through verification |
| **Product Catalog** | Add/edit products with photos | Sellers list offerings |
| **Inquiry System** | Contact seller for orders | Buyers initiate purchase |

#### Phase 2: Transactions (Months 4-6)

| Feature | Description | User Benefit |
|---------|-------------|--------------|
| **Order Management** | Create, track, fulfill orders | Streamlined operations |
| **Payment Integration** | GCash, bank transfer tracking | Secure transactions |
| **Buyer Accounts** | Order history, favorites | Repeat purchasing |
| **Seller Dashboard** | Sales overview, analytics | Business insights |
| **Basic Compliance** | FRAMES data generation | Automatic reporting |

#### Phase 3: Scale (Months 7-12)

| Feature | Description | User Benefit |
|---------|-------------|--------------|
| **Impact Stories** | Beneficiary profiles, metrics | Differentiation |
| **CSEA Dashboard** | Sector analytics, alerts | Proactive oversight |
| **Inventory Management** | Stock tracking, alerts | Operational efficiency |
| **B2B Features** | Bulk orders, invoicing | Institutional buyers |
| **Mobile App** | Native mobile experience | Convenience |

### Prototype Testing Plan

#### Test 1: Storefront Usability

**Participants**: 5 cooperative managers (varying digital literacy)

**Scenario**: Create a storefront and list 3 products

**Success Metrics**:
- Task completion rate > 80%
- Time to complete < 30 minutes
- Satisfaction score > 4/5

**Questions to Answer**:
- Can managers complete setup without assistance?
- Where do they get confused?
- What's missing that they expect?

#### Test 2: Buyer Discovery

**Participants**: 10 consumers (diaspora and local)

**Scenario**: Find and inquire about a specific product type

**Success Metrics**:
- Task completion rate > 90%
- Time to find product < 5 minutes
- Trust score for verified sellers > 4/5

**Questions to Answer**:
- Do trust signals influence preference?
- Is search/browse effective?
- What information do they need before purchase?

#### Test 3: CSEA Dashboard

**Participants**: 3 CSEA staff members

**Scenario**: Identify non-compliant coops and sector trends

**Success Metrics**:
- Can find non-compliant entities < 2 minutes
- Data accuracy confirmed
- Usefulness score > 4/5

**Questions to Answer**:
- Does dashboard meet oversight needs?
- What additional data is needed?
- How does this change their workflow?

---

## Phase 5: Test

### Validation Framework

#### Desirability Testing

| Question | Method | Success Indicator |
|----------|--------|-------------------|
| Do coops want to list products? | Sign-up rate | >50 coops in 3 months |
| Do buyers trust verified sellers? | A/B testing | Higher conversion with badges |
| Do managers use the dashboard? | Usage analytics | >3 logins/week |
| Do buyers complete purchases? | Conversion rate | >5% browse-to-inquiry |

#### Feasibility Testing

| Question | Method | Success Indicator |
|----------|--------|-------------------|
| Can coops create storefronts? | Task success rate | >80% complete independently |
| Does compliance data generate? | Data validation | >95% accuracy |
| Does platform handle load? | Performance testing | <3s page load |
| Is mobile experience adequate? | Mobile usability | >4/5 satisfaction |

#### Viability Testing

| Question | Method | Success Indicator |
|----------|--------|-------------------|
| Will platform drive sales? | GMV tracking | Growth month-over-month |
| Does it reduce CSEA workload? | Time tracking | >20% time savings |
| Is it sustainable without subsidy? | Cost analysis | Path to sustainability |
| Does it scale to all BARMM? | Capacity testing | Handles 500+ entities |

### Feedback Loops

```
CONTINUOUS FEEDBACK SYSTEM
│
├── In-App Feedback
│   ├── Quick rating after key actions
│   ├── "Report a problem" button
│   └── Feature request submission
│
├── Regular Check-ins
│   ├── Monthly coop manager calls (sample)
│   ├── Quarterly buyer surveys
│   └── Bi-weekly CSEA feedback sessions
│
├── Analytics Monitoring
│   ├── Drop-off points in user flows
│   ├── Feature usage patterns
│   └── Error and support ticket analysis
│
└── Community Input
    ├── Coop assembly feedback collection
    ├── CSEA field visit observations
    └── Partner organization input
```

### Iteration Cycles

| Cycle | Duration | Focus |
|-------|----------|-------|
| Sprint | 2 weeks | Bug fixes, minor improvements |
| Release | Monthly | New features, major improvements |
| Review | Quarterly | Strategic direction, major pivots |

---

## Implementation Roadmap

### Year 1: Foundation

```
Q1 (Months 1-3): MVP Launch
├── Public marketplace live
├── 50 cooperatives onboarded
├── Basic storefronts functional
└── CSEA admin portal active

Q2 (Months 4-6): Transactions
├── Order management system
├── Payment tracking
├── Buyer accounts
└── 100 cooperatives, 20 SEs

Q3 (Months 7-9): Operations
├── Seller dashboard
├── Basic inventory
├── FRAMES integration started
└── First B2B transactions

Q4 (Months 10-12): Scale
├── Impact stories feature
├── CSEA analytics dashboard
├── Mobile optimization
└── 200 entities, measurable GMV
```

### Success Metrics

| Metric | Year 1 Target | Measurement |
|--------|---------------|-------------|
| Registered Entities | 200 | Platform count |
| Active Sellers | 100 | >1 product listed, >1 order/month |
| Gross Merchandise Value | PHP 5M | Total transaction value |
| Buyer Accounts | 1,000 | Registered consumers |
| FRAMES Compliance | 80% | Registered entities compliant |
| CSEA Time Savings | 20% | Staff survey |
| Seller Satisfaction | 4/5 | Quarterly survey |
| Buyer Trust Score | 4/5 | Post-purchase survey |

---

## Appendix: BARMM Context Considerations

### Cultural Adaptations

| Factor | Platform Adaptation |
|--------|---------------------|
| **Community Focus** | Highlight community/coop identity over individual sellers |
| **Relationship-Based** | Enable seller-buyer communication before purchase |
| **Halal Considerations** | Clear product labeling for halal/non-food items |
| **Local Languages** | Support for key terms in Maguindanaon, Maranao, Tausug |
| **Respect for Authority** | CSEA verification as trust signal respected |

### Inclusion Principles

| Principle | Implementation |
|-----------|----------------|
| **Digital Literacy** | Minimal clicks, guided flows, phone support |
| **Connectivity** | Lightweight pages, offline capability for orders |
| **Gender Inclusion** | Women-led coop/SE highlighting, safety features |
| **Geographic Reach** | Logistics partnerships beyond urban centers |

---

## Works Cited

[1] Stanford d.school. "Design Thinking Bootleg." https://dschool.stanford.edu/resources/design-thinking-bootleg

[2] IDEO. "The Field Guide to Human-Centered Design." https://www.designkit.org/resources/1

[3] CSEA-BARMM. Internal research on cooperative sector challenges.

[4] RA 9520. Philippine Cooperative Code of 2008.

[5] RA 11232. Revised Corporation Code (Social Enterprise provisions).
