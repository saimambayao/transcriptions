# Bangsamoro Legislative Repository

## Prompt ID
`legislative-repository-001`

## Date Created
2026-01-04

## Original Request
> We have the Bill Registry in the Legislative Tracking module. I want to have a repository of bills and approved bills/BAA just like that in lawphil.net but improved UI. The BAA are approved bills. We have bills also in the reference directory. Put a version control or versioning there that would reflect the filed bill, the committee amended bill, the plenary amended bill, and the finally approved bill and signed into BAA. Call it Bangsamoro Legislative Repository with both bills and resolutions.

---

## Refined Prompt

### Task Intent
Build the **Bangsamoro Legislative Repository** - a comprehensive legal database and public-facing repository for all Bangsamoro legislative items including bills, resolutions, and enacted laws (BAAs), with full-text viewing and legislative lifecycle version tracking.

### Module Context
| Attribute | Value |
|-----------|-------|
| **Module** | Legislative Work |
| **Submodule** | Legislative Tracking |
| **Feature Area** | Legislative Repository (Bills + Resolutions + BAAs) |
| **Route** | `/legislative/tracking?tab=repository` or `/legislative/repository` |
| **User Types** | MP, Committee Staff, Admin, Public (read-only) |

### Tech Context
| Layer | Technologies |
|-------|--------------|
| **Frontend** | React 19, TypeScript 5.8+, Tailwind CSS 4.0+ |
| **Routing** | React Router 7+ |
| **State** | TanStack Query 5+ (server state), Zustand 5+ (client state) |
| **Data Source** | Static TypeScript data files (frontend-first), then DRF API |
| **UI Components** | shadcn/ui patterns, Lucide icons |

---

## Data Sources

### Available Data
| Type | Directory | File Pattern | Count | Description |
|------|-----------|--------------|-------|-------------|
| Bills (Filed) | `docs/reference/bills/` | `BILL{number}.md` | 237 | Original filed bills (Bill 180-424) |
| BAAs (Enacted) | `docs/reference/BAAs/` | `BAA-{number}.md` | 78 | Enacted laws (BAA 1-81) |
| Bill Index | `docs/reference/bills/INDEX.md` | - | 1 | Bill number to title mapping |
| BAA Index | `docs/reference/BAAs/INDEX.md` | - | 1 | BAA number to title mapping |

### Future Data (To Be Added)
| Type | Description |
|------|-------------|
| Resolutions | Parliament resolutions (non-law expressions) |
| Committee Amendments | Bill versions after committee markup |
| Plenary Amendments | Bill versions after floor amendments |

### Data Structure (Markdown Files)

**Bill File Structure (`BILL{n}.md`):**
```markdown
Republic of the Philippines
Bangsamoro Autonomous Region in Muslim Mindanao
**BANGSAMORO TRANSITION AUTHORITY**
Cotabato City

SECOND PARLIAMENT
Second Regular Session

Parliament Bill No. **180**

Introduced by
**MPs [Author Names]**
Co-authored by
**MPs [Co-author Names]**

**AN ACT
[FULL TITLE IN CAPS]**

**EXPLANATORY NOTE**
[Explanation text...]

**BE IT ENACTED** by the Bangsamoro Transition Authority...

**SECTION 1. Short Title.** — [Content]
**SEC. 2. [Section Title].** — [Content]
...
**SEC. N. Effectivity.** — [Content]

Approved,
[Signatures]
```

**BAA File Structure (`BAA-{n}.md`):**
```markdown
BILL NO. [original bill number]

Republic of the Philippines
**BANGSAMORO PARLIAMENT**
Bangsamoro Autonomous Region in Muslim Mindanao
BARMM Compound, Cotabato City

**BANGSAMORO TRANSITION AUTHORITY**
**(FIRST REGULAR SESSION)**

**BANGSAMORO AUTONOMY ACT NO. [number]**

Begun and held in Cotabato City, on [date].

**AN ACT**
**[FULL TITLE IN CAPS]**

Be it enacted by the Bangsamoro Transition Authority Parliament in session assembled:

**SECTION 1. [Title].** - [Content]
...

**APPROVED.**

(Signed)
**[SPEAKER NAME]**
Speaker

This Act was passed by the Bangsamoro Parliament on [date].

(Signed)
**[SECRETARY-GENERAL NAME]**
Secretary-General

**APPROVED:**

(Signed)
**[CHIEF MINISTER NAME]**
Chief Minister
Date: [Approval Date]
```

---

## Legislative Item Types

| Type | Code | Description | Lifecycle | Final Form |
|------|------|-------------|-----------|------------|
| **Bill** | `BILL` | Proposed legislation that creates, amends, or repeals laws | Filed → Committee → Plenary → Enacted | Becomes BAA |
| **Resolution** | `RES` | Expression of parliament sentiment, policy, or action | Filed → Committee → Plenary → Adopted | Adopted Resolution |
| **BAA** | `BAA` | Bangsamoro Autonomy Act - enacted law | N/A (final form) | Law of the Region |

---

## Bill Lifecycle & Version Control

### Legislative Journey Stages
```
┌─────────┐    ┌───────────┐    ┌─────────┐    ┌─────────┐
│  FILED  │───►│ COMMITTEE │───►│ PLENARY │───►│ ENACTED │
│  (v1)   │    │   (v2)    │    │  (v3)   │    │  (v4)   │
└─────────┘    └───────────┘    └─────────┘    └─────────┘
```

### Version Definitions
| Version | Stage | Description | Data Source |
|---------|-------|-------------|-------------|
| **v1 - Filed** | Initial filing | Original bill as submitted by MP author | `bills/BILL{n}.md` |
| **v2 - Committee** | Committee review | Bill with committee amendments/markup | Future: `bills/BILL{n}-committee.md` |
| **v3 - Plenary** | Floor deliberation | Bill with plenary/floor amendments | Future: `bills/BILL{n}-plenary.md` |
| **v4 - Enacted** | Signed into law | Final version signed by Chief Minister | `BAAs/BAA-{n}.md` |

### Bill Status Values
| Status | Badge Color | Description |
|--------|-------------|-------------|
| `FILED` | Gray | Bill submitted, awaiting committee referral |
| `IN_COMMITTEE` | Blue | Under committee deliberation |
| `COMMITTEE_APPROVED` | Teal | Passed committee, awaiting plenary |
| `IN_PLENARY` | Yellow | Under plenary deliberation |
| `PLENARY_APPROVED` | Orange | Passed plenary, awaiting Chief Minister signature |
| `ENACTED` | Green | Signed into law as BAA |
| `VETOED` | Red | Rejected by Chief Minister |
| `ARCHIVED` | Gray | Withdrawn or expired |

---

## Primary Requirements

### 1. Data Layer
- [ ] Create TypeScript interfaces for Bill, Resolution, BAA, LegislativeItem
- [ ] Parse all 237 bill markdown files into structured data
- [ ] Parse all 78 BAA markdown files into structured data
- [ ] Create bill-to-BAA mapping (link bills to their enacted versions)
- [ ] Generate static data file: `frontend/src/data/legislative-repository.ts`

### 2. Repository List View
- [ ] Tab navigation: Bills | Resolutions | Enacted Laws (BAAs)
- [ ] Search across title, number, author
- [ ] Filter by: Session, Year, Status, Committee, Author
- [ ] Sort by: Number, Date Filed, Date Enacted, Title
- [ ] Pagination (25/50/100 per page)
- [ ] Status badges with semantic colors
- [ ] Bill-to-BAA link indicator for enacted bills

### 3. Detail View (Full Text)
- [ ] Legal document layout (similar to LawPhil but modern)
- [ ] Header: Republic, Parliament, Session info
- [ ] Title and number prominently displayed
- [ ] Version tabs: [Filed] [Committee] [Plenary] [Enacted]
- [ ] Timeline visualization of legislative journey
- [ ] Full text with proper section formatting
- [ ] Bold section numbers, italic legal terms
- [ ] Signatories section at bottom
- [ ] Metadata sidebar: Status, Dates, Authors, Committee

### 4. Navigation & Routing
- [ ] Route: `/legislative/repository` (main)
- [ ] Route: `/legislative/repository/bills` (bills tab)
- [ ] Route: `/legislative/repository/resolutions` (resolutions tab)
- [ ] Route: `/legislative/repository/baas` (enacted laws tab)
- [ ] Route: `/legislative/repository/bill/:billNumber` (bill detail)
- [ ] Route: `/legislative/repository/baa/:baaNumber` (BAA detail)

### 5. UI/UX Improvements Over LawPhil
| LawPhil (Current) | BPMP Repository (Target) |
|-------------------|--------------------------|
| Purple background, dated fonts | Clean white/slate, modern Inter font |
| No sidebar navigation | Table of Contents sidebar (sections) |
| Basic HTML formatting | Tailwind-styled legal document |
| No search within document | In-page search + Ctrl+F |
| Static fixed width | Fully responsive design |
| No version history | Version tabs with timeline |
| Plain text links | Card-based related items |

---

## Data Model

### TypeScript Interfaces

```typescript
// Legislative item types
type LegislativeType = 'BILL' | 'RESOLUTION' | 'BAA';

// Bill status in lifecycle
type BillStatus =
  | 'FILED'
  | 'IN_COMMITTEE'
  | 'COMMITTEE_APPROVED'
  | 'IN_PLENARY'
  | 'PLENARY_APPROVED'
  | 'ENACTED'
  | 'VETOED'
  | 'ARCHIVED';

// Parliamentary session
interface ParliamentarySession {
  parliament: number; // 1 = First Parliament (BTA), 2 = Second Parliament
  session: string; // "First Regular Session", "Second Regular Session", etc.
  year: number;
}

// Author/MP information
interface Author {
  name: string;
  title?: string; // "MP", "Atty.", "Engr.", etc.
  role: 'principal' | 'co-author';
}

// Legislative version
interface LegislativeVersion {
  version: 'filed' | 'committee' | 'plenary' | 'enacted';
  date: string; // ISO date
  content: string; // Full markdown content
  changes?: string; // Summary of changes from previous version
}

// Base legislative item
interface LegislativeItem {
  id: string;
  type: LegislativeType;
  number: number;
  title: string;
  shortTitle?: string;
  session: ParliamentarySession;
  authors: Author[];
  dateFiled: string;
  status: BillStatus;
  committee?: string;
  versions: LegislativeVersion[];
  content: string; // Current/latest version content
  metadata: {
    dateCommittee?: string;
    datePlenary?: string;
    dateEnacted?: string;
    speaker?: string;
    secretaryGeneral?: string;
    chiefMinister?: string;
  };
}

// Bill with BAA link
interface Bill extends LegislativeItem {
  type: 'BILL';
  enactedAs?: number; // BAA number if enacted
}

// Resolution
interface Resolution extends LegislativeItem {
  type: 'RESOLUTION';
  resolutionType: 'simple' | 'joint' | 'concurrent';
}

// Enacted law
interface BAA extends LegislativeItem {
  type: 'BAA';
  originalBillNumber: number;
  effectivityDate: string;
}
```

---

## UI Components

### 1. LegislativeRepository (Main Container)
```
/frontend/src/features/legislative/components/LegislativeRepository.tsx
```
- Tab navigation (Bills, Resolutions, Enacted Laws)
- Search bar with filters
- Renders appropriate list component

### 2. BillList / ResolutionList / BAAList
```
/frontend/src/features/legislative/components/BillList.tsx
/frontend/src/features/legislative/components/ResolutionList.tsx
/frontend/src/features/legislative/components/BAAList.tsx
```
- Table/card view of items
- Status badges
- Click to view detail

### 3. LegislativeDetailView
```
/frontend/src/features/legislative/components/LegislativeDetailView.tsx
```
- Full text display
- Version tabs
- Timeline visualization
- Metadata sidebar

### 4. LegislativeDocument
```
/frontend/src/features/legislative/components/LegislativeDocument.tsx
```
- Renders markdown as styled legal document
- Section formatting
- Signatory block

### 5. VersionTimeline
```
/frontend/src/features/legislative/components/VersionTimeline.tsx
```
- Visual timeline of bill journey
- Clickable stages

---

## File Structure

```
frontend/src/
├── data/
│   └── legislative-repository/
│       ├── index.ts              # Main export
│       ├── bills.ts              # Parsed bill data
│       ├── baas.ts               # Parsed BAA data
│       ├── resolutions.ts        # Parsed resolution data (future)
│       └── mappings.ts           # Bill-to-BAA mappings
│
├── features/legislative/
│   ├── components/
│   │   ├── LegislativeRepository.tsx
│   │   ├── BillList.tsx
│   │   ├── BAAList.tsx
│   │   ├── ResolutionList.tsx
│   │   ├── LegislativeDetailView.tsx
│   │   ├── LegislativeDocument.tsx
│   │   ├── VersionTabs.tsx
│   │   ├── VersionTimeline.tsx
│   │   ├── LegislativeSearch.tsx
│   │   └── LegislativeFilters.tsx
│   │
│   ├── hooks/
│   │   ├── useLegislativeRepository.ts
│   │   ├── useBillDetail.ts
│   │   └── useBAADetail.ts
│   │
│   └── types/
│       └── legislative.ts        # TypeScript interfaces
```

---

## Success Criteria

### Functional
- [ ] Repository displays all 237 bills
- [ ] Repository displays all 78 BAAs
- [ ] Tab navigation works (Bills / Resolutions / Enacted Laws)
- [ ] Search filters results correctly
- [ ] Bill detail shows full text with proper formatting
- [ ] BAA detail shows full text with proper formatting
- [ ] Version tabs switch between available versions
- [ ] Bills linked to their BAA show the connection
- [ ] Responsive design works on mobile/tablet/desktop

### UI/UX
- [ ] Clean, modern typography (better than LawPhil)
- [ ] Proper legal document formatting
- [ ] Status badges use semantic colors
- [ ] Timeline visualization is clear and intuitive
- [ ] No purple colors (per project guidelines)
- [ ] Icons used instead of emojis

### Performance
- [ ] Initial load under 2 seconds
- [ ] Search results appear within 300ms
- [ ] Smooth tab transitions

---

## Implementation Phases

### Phase 1: Data Layer (Current)
1. Create TypeScript interfaces
2. Build parser for bill markdown files
3. Build parser for BAA markdown files
4. Create bill-to-BAA mapping logic
5. Generate static data files

### Phase 2: Repository List View
1. Create main repository component
2. Implement tab navigation
3. Build bill/BAA list tables
4. Add search functionality
5. Add filter dropdowns
6. Add pagination

### Phase 3: Detail View
1. Create detail view layout
2. Implement legal document renderer
3. Add version tabs
4. Build timeline visualization
5. Add metadata sidebar

### Phase 4: Polish & Integration
1. Responsive design adjustments
2. Loading states and error handling
3. Integration with existing Legislative Tracking
4. Route configuration

### Phase 5: Future Enhancements
1. Add resolution data
2. Add committee/plenary versions when available
3. Backend API integration
4. Full-text search with highlighting
5. PDF export

---

## Related References
- LawPhil.net (reference for legal document display)
- Current Bill Registry: `/legislative/tracking?tab=registry`
- GEMINI.md project guidelines

---

## Notes
- Frontend-first approach: Build UI with static data, then add API later
- No purple colors per project guidelines
- Use icons instead of emojis
- Files should stay under 1000 lines
- Philippine Peso icon for any monetary references
