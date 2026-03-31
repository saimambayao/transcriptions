# BARMM UI/UX Context Reference
## Based on 2nd Bangsamoro Development Plan 2023-2028

---

## Quick Reference: BARMM Digital Context

**Region:** Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)
**Population:** 4.4M+ (42% ages 15-39, highly trainable workforce)
**Primary Languages:** Filipino, Bangsamoro Maranao, Tausug, Maguindanaoan
**Regional Vision:** "A Bangsamoro that is united, enlightened, self-governing, peaceful, just, morally upright, and progressive."
**Digital Maturity:** Emerging (high mobile-first, limited broadband, offline-first essential)

---

## BDP 2023-2028 Strategic Goals

### Six Development Goals (All Require Digital Enablement)

1. **Stable, Just, and Accountable Government** - Digital governance, e-services, compliance tracking
2. **Equitable, Competitive, Robust Economy** - MSME support, cooperatives, market access (36,000+ registered coops)
3. **Peaceful, Safe, Resilient Communities** - Digital inclusion, economic opportunity
4. **Inclusive, Responsive Quality Services** - Equitable digital access for all sectors
5. **Rich, Diverse Culture & Identity Preserved** - Local language support, cultural representation
6. **Strategic Climate-Resilient Infrastructure** - Digital resilience, offline capability

### Macroeconomic Targets 2023-2028

| Indicator | Target | UI/UX Implication |
|-----------|--------|-------------------|
| GRDP Growth | 8-9% annually | Must support growing MSME & coop participation |
| Industry/Services Growth | 10-12% double-digit | Mobile commerce, digital marketplace essential |
| Poverty Reduction | 20-25% (from 29.8%) | Accessibility critical for lower-income users |
| Unemployment | 3-5% | Skills training platforms crucial |

---

## Target User Personas & Digital Context

### 1. Cooperative Members & Social Entrepreneurs

**Population:** 12,214 registered cooperatives (BARMM), only 11.66% compliant

**Digital Characteristics:**
- Limited formal business education
- Mobile-primary access (smartphones primary device)
- Low digital literacy, non-English speakers
- Often from agricultural/fishing sectors
- Offline periods common due to connectivity gaps

**UI/UX Considerations:**
- Large, accessible buttons and touch targets (minimum 48px)
- Single-language UI first (Bangsamoro), English secondary
- Simple, task-focused workflows (avoid complexity)
- Offline-first functionality for form entry
- Voice/audio support for literacy variations
- Progress indication for multi-step processes
- Local payment methods integration

**Cooperatives Sectors:**
- Producer: 37.58% (agricultural products)
- Marketing: 27.54% (product distribution)
- Agricultural: 12.82% (farming operations)

### 2. MSME Owners & Operators

**Population:** 8,427 new BNRs in 2021 (161% increase), aiming for formalization

**Digital Characteristics:**
- Informal sector dominant (low compliance)
- Ages 25-55 (42% of population is 15-39, potential growth)
- Limited access to credit/banking (only 0.92% national BNR share)
- High out-migration (highest in country, looking for income)
- Value barter trade alongside formal commerce

**UI/UX Considerations:**
- Minimal data entry requirements (respect time poverty)
- Mobile payment/cash options
- Offline product catalog and order placement
- Business registration simplified to 3-4 steps
- Financial literacy support within interface
- Informal seller verification pathways

### 3. Farmers & Fisherfolks

**Population:** 252,758 registered fisherfolks, significant agricultural base

**Digital Characteristics:**
- Predominantly male, older (average age 57, needs mentoring)
- Agricultural productivity yields below national average
- High post-harvest losses due to poor infrastructure
- Limited extension services access
- Tawi-Tawi seaweed production (48.4% national share)

**UI/UX Considerations:**
- Weather/seasonal information prioritized
- Market price information (real-time critical)
- Multilingual crop/commodity names
- Visual-heavy interface (reduce text dependency)
- Offline availability for production guides
- Simple data recording (yield, input costs)

### 4. Government Staff (CSEA, BARMM Agencies)

**Population:** BARMM ministries, local government units (75 municipalities)

**Digital Characteristics:**
- Varying technical skill levels
- Need compliance/audit trail systems
- Works with cooperatives and MSME registrations
- Database/reporting requirements

**UI/UX Considerations:**
- Administrative dashboards with export capability
- Audit trail and data integrity critical
- Role-based access control
- Bulk operation support (multiple registrations)
- Integration with government systems

### 5. Young Population (Digital Native Growth Opportunity)

**Population:** 42% of region ages 15-39 (1.85M+)

**Digital Characteristics:**
- Mobile-first expectations
- Social media native
- Higher digital literacy
- Seeking employment and entrepreneurship
- Some internet access anxiety in rural areas

**UI/UX Considerations:**
- Modern, app-like experience
- Social sharing features
- Gamification for engagement
- Career pathway visualization
- Peer-to-peer learning tools

---

## Digital Context: BARMM Connectivity Challenges

### Connectivity Reality (BDP 2023-2028 Data)

| Challenge | Impact | Design Response |
|-----------|--------|-----------------|
| **Poor Internet in BaSulTa** | Mobile signal absent in many areas | Aggressive offline-first approach |
| **Mobile-dependent urban** | Cotabato City, Marawi rely on mobile networks | Optimize for mobile data limits |
| **Island provinces (Tawi-Tawi, Sulu)** | Intermittent connectivity, slower speeds | Large asset pre-caching, smaller payloads |
| **Rural areas** | No broadband, unreliable electricity | Minimal data, battery-conscious design |
| **High data costs** | Data expensive relative to income | Minimize data usage (text > images) |

### Offline-First Architecture Requirements

```
Priority 1 (Always Available):
- Core forms and data entry
- Product catalogs
- Essential reference data
- Transaction history

Priority 2 (Sync When Connected):
- Supporting documents
- User guides
- Market data
- Government announcements

Priority 3 (Cloud-Only):
- Complex analytics
- Multi-user collaboration
- Large file uploads
```

---

## Cultural & Islamic Design Considerations

### Bangsamoro Identity & Values

1. **Islamic Foundation**
   - Design respects Islamic calendar (Ramadan, Islamic holidays)
   - Halal industry dominant (strategic focus of BDP)
   - Prayer time awareness and observance
   - Modesty in imagery and representation

2. **Cultural Diversity**
   - Bangsamoro Maranao, Tausug, Maguindanaoan languages
   - Local cultural symbols and aesthetics
   - Traditional leadership structures (barangay, clan systems)
   - Respect for local customs in workflows

3. **Peace & Reconciliation**
   - Design promotes unity, not division
   - Inclusive representation (gender, age, minority groups)
   - Transparent government processes build trust
   - Fair marketplace for all backgrounds

### Language & Localization Strategy

**Tier 1 (Essential):**
- Bangsamoro interface language options
- English as secondary
- Local commodity names (seaweed, cassava varieties)

**Tier 2 (Expansion):**
- Tausug (Sulu province)
- Maranao (Lanao del Sur)
- Maguindanaoan (Maguindanao)

**Tier 3 (Support):**
- Filipino as fallback
- Visual/icon-based alternatives

### Visual Design Principles

**Color Palette Modifications:**
- No purple (explicit instruction from project)
- Blue (Negosyo Blue #0056D2) is primary, accessible
- Green for approval/success (agricultural connotation)
- Orange/amber for warnings (harvest/caution concept)
- Red for errors (respect cultural meaning)

**Imagery Guidelines:**
- Islamic aesthetic: geometric patterns, calligraphy
- Diverse representation: multiple ethnicities, ages, family structures
- Agricultural imagery: crops, fishing, cooperatives
- Modern Bangsamoro: development, technology, infrastructure

**Typography:**
- Clear, readable sans-serif for low-bandwidth environments
- Support local character sets (Jawi, Baybayin)
- Maintain text hierarchy despite small screens

---

## User Literacy & Education Levels

### BARMM Education Statistics

| Metric | Data | Design Impact |
|--------|------|----------------|
| **Low Scientific Literacy** | 3.2% (national avg), lower in region | Avoid technical jargon, explain systems |
| **High School Enrollment Gaps** | Teacher-student ratio constraints | Basic digital literacy can't be assumed |
| **Madrasah Education** | 1,196+ accredited, 2,121+ traditional | Religious/cultural context sensitive |
| **Out-of-school youth** | High, seeking alternative learning | Accessible education platforms essential |

### Digital Literacy Levels

**Level 1 (Basic - 40% of target):**
- Smartphone app navigation
- Text/voice input, minimal typing
- Simple purchase/payment flows
- Icon recognition (no text needed)

**Level 2 (Intermediate - 40% of target):**
- Mobile web browsing
- Form completion
- Account management
- Basic data entry
- Photo/document upload

**Level 3 (Advanced - 20% of target):**
- Full dashboard usage
- Data analysis/reports
- Complex workflows
- Export/integration

### Accessibility for Literacy Variation

1. **Visual Alternatives**
   - Icons paired with color and text
   - Photos/illustrations for instructions
   - Step-by-step visual guides
   - Video tutorials with captions

2. **Oral Support**
   - Audio labels for buttons
   - Voice input for forms
   - Text-to-speech for content
   - Hotline support (human fallback)

3. **Cognitive Load Reduction**
   - One task per screen
   - Clear, simple language
   - Progress indicators
   - Confirmation before actions

---

## Cooperative & MSME User Journeys

### Cooperative Registration & Compliance Flow

**User:** Cooperative leader (rural, 50+ years old, limited English)

**Pain Points:**
- 12,214 registered but only 11.66% compliant
- Complex requirements documentation
- Limited support for compliance process
- Offline areas can't access resources

**Design Imperatives:**
- Phased checklist approach (don't show all requirements at once)
- Document upload with photo guidance (phone camera)
- Offline progress saving and sync-on-connect
- WhatsApp/SMS notification support
- Local language checklist with symbols
- Connect to CSEA staff via in-app chat

### MSME Business Registration (BNR) Flow

**User:** Small business owner (25-40 years old, wants to formalize)

**Pain Points:**
- Fear of taxation
- Complex paperwork
- Limited time (works other jobs)
- Only 0.92% of national BNR from BARMM

**Design Imperatives:**
- Wizard-based registration (5 steps max)
- Mobile photo of documents (no scanning)
- Offline-capable form entry
- Instant registration confirmation
- Printed/QR code receipt for record
- Direct link to credit access information

### Farmer/Fisherfolk Market Information

**User:** Cassava farmer (Lanao del Sur) or seaweed farmer (Tawi-Tawi)

**Pain Points:**
- No market price transparency (vulnerable to middlemen)
- Productivity below national average
- Post-harvest losses critical
- High out-migration due to low income

**Design Imperatives:**
- Current commodity prices (update daily/weekly)
- Simple price entry for farmers to contribute
- Weather forecasts specific to province
- Pest/disease alerts (push notifications)
- Pre-harvest/post-harvest guidance
- Local market buyer directory
- Export opportunity alerts (halal certification)

---

## Accessibility Requirements (WCAG 2.2 Level AA+)

### BARMM-Specific Accessibility

1. **Low Vision Support**
   - Minimum text size 16px (older users prevalent)
   - High contrast (4.5:1 minimum)
   - Zoom to 200% without loss of functionality
   - Dark mode option (reduces battery drain in low-power situations)

2. **Motor/Dexterity Challenges**
   - Minimum touch target 48px x 48px
   - Large form inputs, buttons
   - Slow network tolerance (no aggressive timeouts)
   - Voice input alternative to typing

3. **Cognitive Accessibility**
   - Clear heading hierarchy
   - Consistent navigation
   - Predictable behavior
   - Progressive disclosure (show only necessary info)

4. **Sensory Accessibility**
   - Captions/transcripts for video content
   - Text alternative to images
   - Don't rely on color alone
   - Meaningful alt text (not "image1.jpg")

---

## Performance & Technical Constraints

### Expected Device Profile

**Primary Device:** Android smartphone (5-8 inch screen)
**Secondary Device:** Feature phone with basic browser
**Connection:** 2G/3G (LTE where available)
**Data Plan:** Limited (expensive for users)
**Battery:** Limited (frequent charging not available)

### Performance Targets

| Metric | Target | Strategy |
|--------|--------|----------|
| **First Contentful Paint** | < 3s on 3G | Defer non-critical JS |
| **Page Bundle Size** | < 150KB | Code splitting, lazy loading |
| **Images** | < 50KB per image | WebP, compression, lazy load |
| **Offline Functionality** | 100% for core features | Service Workers, IndexedDB |
| **Battery Drain** | Minimal | Reduce animations, background sync |

### Data Usage Optimization

```
Target: < 1MB per session for core user

- Remove auto-playing videos
- Compress images to WebP (50% size reduction)
- Minimal animations
- Smart sync (batch requests, off-peak timing)
- Offline-first reduces requests by 70%
```

---

## Hallal Industry Integration (Strategic BDP Focus)

### BARMM Halal Context

- Only Muslim-majority region in Philippines
- Growing export market opportunity
- Bangsamoro Halal Board policy-making
- MOST Halal Testing Laboratory operational

### UI/UX for Halal Commerce

1. **Halal Certification Display**
   - Clear certification status
   - Valid dates and issuing body
   - Certification document access
   - QR code linking to registry

2. **Halal Supply Chain Transparency**
   - Producer profile with prayer times
   - Ingredient sourcing (Islamic requirements)
   - Processing facility details
   - Traceability from production to market

3. **Halal Producer Support**
   - Certification checklist
   - Requirements by commodity type
   - Cost transparency
   - Training resources access

---

## Design System Tokens for BARMM

### Color Palette

```css
/* Primary */
--color-primary: #0056D2 (Negosyo Blue)

/* Status */
--color-success: #16a34a (Agricultural green)
--color-warning: #ea580c (Harvest orange)
--color-error: #dc2626 (Alert red)
--color-info: #0284c7 (Water blue)

/* Semantic */
--color-compliant: #16a34a
--color-pending: #ea580c
--color-warning: #f97316
--color-offline: #6b7280

/* Accessibility: Maintain 4.5:1 contrast on white background */
```

### Typography for Mobile & Low Literacy

```css
/* Mobile-first, readable at small sizes */
--font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui
--font-size-body: 16px (16px minimum for readability)
--font-size-heading: 24px (strong hierarchy)
--line-height: 1.6 (accessibility standard)
--letter-spacing: 0.5px (improve distinction)
```

### Spacing & Touch Targets

```css
/* Mobile-touch optimized */
--space-xs: 4px
--space-sm: 8px
--space-md: 16px (standard spacing)
--space-lg: 24px
--space-xl: 32px

/* Minimum touch target: 48px x 48px */
--button-height: 48px
--input-height: 48px
--icon-target: 48px
```

---

## Development Priorities

### Phase 1: Core BARMM Features (Q1-Q2)
1. Offline-first architecture with service workers
2. Cooperative registration & compliance
3. MSME business directory
4. Mobile-optimized marketplace
5. Local language support (Bangsamoro)

### Phase 2: BARMM Economic Tools (Q3-Q4)
1. Commodity price tracker (farmer/fisher)
2. Halal certification tracker
3. Cooperative performance dashboard
4. Market linkage features
5. Export opportunity alerts

### Phase 3: BARMM Community Features (Year 2)
1. Cultural content preservation
2. Peace-building community features
3. Youth employment/skills platform
4. Microfinance & credit access
5. Supply chain transparency

---

## Measurement & Success Metrics

### BARMM-Specific KPIs

| KPI | Target | Owner |
|-----|--------|-------|
| **Cooperative Compliance Rate** | 50% (up from 11.66%) | CSEA |
| **MSME Formalization Rate** | 5,000+ annual registrations | MTIT |
| **Farmer/Fisher Market Access** | 10,000+ users by end 2024 | MAFAR |
| **Digital Literacy Growth** | 80% can complete core task | Training |
| **Offline Functionality** | 99% availability in 2G zones | Platform |
| **Language Coverage** | 3+ languages supported | Product |

### User Satisfaction (BARMM Context)

- Net Promoter Score (NPS) > 50 among cooperative members
- Task completion rate > 80% for Level 1 literacy users
- Mobile app rating > 4.2 stars (IOS/Android)
- Support ticket satisfaction > 90% (WhatsApp/SMS primary)
- Return usage rate > 60% within 30 days

---

## Reference Resources

**Key BDP 2023-2028 Chapters:**
- Chapter 4: Development Framework (6 goals, 12 principles)
- Chapter 7: Economy (cooperatives, MSMEs, agriculture, fisheries, tourism)
- Chapter 8: Technology & Innovation (STI, digital ecosystem, connectivity)

**BARMM Government Websites:**
- BPDA: bpda.bangsamoro.gov.ph
- CSEA: csea.bangsamoro.gov.ph
- BARMM Parliament: parliament.bangsamoro.gov.ph

**Relevant Laws:**
- BOL (Bangsamoro Organic Law) - RA 11054
- BAA No. 6 - BEDC establishment
- BAA No. 11 - Administrative Code

**Design Inspiration Sources:**
- Shopee, Lazada (mobile commerce in Southeast Asia)
- Paytm, Phonepe (offline-first fintech)
- mPharma (low-bandwidth healthcare)
- Zuri (African MSME platform)

---

**Last Updated:** 2024
**Based on:** 2nd Bangsamoro Development Plan 2023-2028
**Compliance:** WCAG 2.2 Level AA, BDP Strategic Goals
