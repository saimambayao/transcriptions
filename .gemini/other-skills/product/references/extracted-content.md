# Product - Extracted Detailed Content

## Table of Contents

- [Workflow: Cooperative Platform Features](#workflow-cooperative-platform-features)
- [SE Development Journey Integration](#se-development-journey-integration)

---

## Workflow: Cooperative Platform Features

This section provides practical guidance for designing and developing features for cooperative platforms within the Negosyo Bangsamoro Digital Platform. All business rules and compliance requirements reference RA 9520 (Philippine Cooperative Code of 2008) and CSEA regulations.

### Cooperative User Types in Platform

Understanding user types is essential for feature design and access control:

| User Type | Description | Portal Access | Key Permissions |
|-----------|-------------|---------------|-----------------|
| **Member** | Regular cooperative member | Coop/SE Portal | View patronage, vote in GA, access training |
| **Officer** | BOD, Committee members | Coop/SE Portal | Governance tools, approve transactions, view reports |
| **Manager/Staff** | Employed by cooperative | Coop/SE Portal | Day-to-day operations, member management, reporting |
| **CSEA Staff** | Regulator oversight | CSEA Portal | Compliance review, registration approval, auditing |
| **Public** | Potential members, customers | Public Portal | View products, storefront, apply for membership |

**User Journey Mapping:**

```text
PUBLIC USER JOURNEY:
Browse Marketplace → View Cooperative Storefront → Express Membership Interest
                                                          ↓
MEMBER ONBOARDING:
Application → Common Bond Verification → Share Capital Payment → Member Activation
                                                                        ↓
MEMBER ENGAGEMENT:
Patronize Products → Accumulate Patronage → Attend GA → Vote → Receive Dividend
                                                                        ↓
MEMBER ADVANCEMENT:
Training Completion → Officer Nomination → Election → Governance Participation
```

### Cooperative-Specific Feature Categories

#### 1. Membership Management Features

| Feature | Description | RA 9520 Reference |
|---------|-------------|-------------------|
| **Member Registry** | Complete member database with status tracking | Art. 26 (Membership Book) |
| **Share Capital Tracking** | Individual and aggregate share capital records | Art. 39 (Share Capital) |
| **Common Bond Verification** | Validate membership eligibility criteria | Art. 4 (Common Bond) |
| **Membership Application** | Online application with document upload | Art. 25 (Membership Qualifications) |
| **Member Withdrawal** | Process voluntary withdrawal, compute refund | Art. 30 (Termination of Membership) |

**Key Data Points per Member:**
- Personal information (name, address, contact)
- Common bond proof (residence, occupation, association)
- Share capital (subscribed, paid-up, unpaid)
- Patronage history (transactions, accumulated points)
- Training records (ETF-funded courses, certifications)
- Voting eligibility status
- Dividend/patronage refund history

#### 2. Governance Features

| Feature | Description | RA 9520 Reference |
|---------|-------------|-------------------|
| **GA Management** | Schedule, announce, and conduct General Assembly | Art. 45 (General Assembly) |
| **Voting System** | One member, one vote electronic voting | Art. 46 (Voting Rights) |
| **Resolution Tracking** | Record and monitor GA/BOD resolutions | Art. 47 (Powers of General Assembly) |
| **Election Module** | Officer nomination, election, term tracking | Art. 43 (Board of Directors) |
| **Committee Management** | Create committees, assign members, track activities | Art. 44 (Committees) |

**Quorum Requirements (Art. 45):**

```text
QUORUM CALCULATION:
├── Regular GA: Majority of members (50% + 1)
├── Special GA: Majority of members (50% + 1)
├── Amendment of By-Laws: 2/3 of all members
└── Dissolution: 2/3 of all members
```

#### 3. Compliance Features (FRAMES)

| FRAMES Category | Features | Key Metrics |
|-----------------|----------|-------------|
| **Financial** | Financial statements, audit reports, ratios | Liquidity, solvency, profitability |
| **Regulatory** | Registration validity, permit tracking | License expiry, renewal status |
| **Administrative** | Record-keeping, minutes, resolutions | Document completeness, timeliness |
| **Membership** | Member count, growth, retention | Net member growth rate |
| **Economic** | Business volume, patronage, services | Member transaction value |
| **Social** | Training, community projects, CTF utilization | Training hours, beneficiaries |

**Compliance Dashboard Components:**

```text
FRAMES COMPLIANCE DASHBOARD:
│
├── Overall Compliance Score: [0-100%]
│
├── Financial (F)
│   ├── AFS Submission Status: [Submitted/Pending/Overdue]
│   ├── Financial Ratios: [Within Range/Warning/Critical]
│   └── Audit Findings: [Clean/Minor/Major]
│
├── Regulatory (R)
│   ├── COR Validity: [Valid/Expiring/Expired]
│   ├── Accreditation Status: [Active/Pending/Lapsed]
│   └── Required Permits: [Complete/Incomplete]
│
├── Administrative (A)
│   ├── GA Minutes: [Complete/Incomplete]
│   ├── BOD Resolutions: [Updated/Outdated]
│   └── Records Management: [Good/Fair/Poor]
│
├── Membership (M)
│   ├── Member Count Trend: [Growing/Stable/Declining]
│   ├── Common Bond Compliance: [Verified/Unverified]
│   └── Member Participation Rate: [High/Medium/Low]
│
├── Economic (E)
│   ├── Business Volume: [Target Met/Below/Above]
│   ├── Patronage Distribution: [Completed/Pending]
│   └── Service Utilization: [Active/Moderate/Low]
│
└── Social (S)
    ├── Training Hours: [Target Met/Below]
    ├── ETF Utilization: [Optimal/Underutilized]
    └── Community Projects: [Active/None]
```

#### 4. Financial Features

| Feature | Description | RA 9520 Reference |
|---------|-------------|-------------------|
| **Patronage Tracking** | Record member transactions for refund calculation | Art. 3 (Patronage Refund) |
| **Net Surplus Allocation** | Distribute surplus per statutory requirements | Art. 86 (Net Surplus Allocation) |
| **Statutory Fund Management** | Track RF, ETF, CDF, OF balances and utilization | Art. 86 (Statutory Funds) |
| **Share Capital Ledger** | Individual member share capital accounts | Art. 39 (Share Capital) |
| **Dividend Computation** | Calculate and distribute interest on share capital | Art. 86 (Interest on Capital) |

**Statutory Fund Allocation (Art. 86):**

```text
NET SURPLUS ALLOCATION:
│
├── Reserve Fund (RF): At least 10%
│   └── Purpose: Cover losses, business expansion
│
├── Education and Training Fund (ETF): At least 10%
│   └── Purpose: Member/officer training, scholarship
│
├── Community Development Fund (CDF): At least 3%
│   └── Purpose: Community projects, social responsibility
│
├── Optional Fund (OF): Per by-laws
│   └── Purpose: Land and building, contingency, etc.
│
└── DISTRIBUTABLE SURPLUS (Remainder):
    ├── Interest on Share Capital: Max 1% over savings rate
    └── Patronage Refund: Based on patronage volume
```

#### 5. Training Features

| Feature | Description | RA 9520 Reference |
|---------|-------------|-------------------|
| **Officer Training Tracking** | Monitor mandatory training compliance | Art. 44 (Officer Qualifications) |
| **ETF Utilization** | Plan and track education fund usage | Art. 86 (ETF) |
| **Certification Management** | Issue and verify training certificates | MC on Training Requirements |
| **Training Calendar** | Schedule and announce training programs | ETF Planning |
| **Learning Records** | Member training history and achievements | Member Development |

**Mandatory Training Requirements:**

```text
OFFICER TRAINING REQUIREMENTS:
│
├── Pre-Membership Education Seminar (PMES)
│   └── Required: All members before joining
│
├── Basic Cooperative Management Training
│   └── Required: All officers within first year
│
├── Specialized Training by Role:
│   ├── BOD: Governance and Policy
│   ├── Treasurer: Financial Management
│   ├── Secretary: Records and Documentation
│   ├── Audit Committee: Internal Audit
│   └── Manager: Operations Management
│
└── Continuing Education:
    └── Annual refresher for all officers
```

### Cooperative Data Models

**Core Data Entities for Platform Development:**

```text
COOPERATIVE DATA MODEL:
│
├── COOPERATIVE
│   ├── coop_id (primary key)
│   ├── registration_number
│   ├── name, address, contact
│   ├── type (primary, secondary, tertiary)
│   ├── category (credit, consumer, producer, etc.)
│   ├── common_bond (type, description)
│   ├── registration_date
│   ├── fiscal_year_end
│   ├── compliance_status
│   └── accreditation_status
│
├── MEMBER
│   ├── member_id (primary key)
│   ├── coop_id (foreign key)
│   ├── personal_info (name, address, contact, birthdate)
│   ├── common_bond_proof
│   ├── membership_date
│   ├── membership_status (active, inactive, withdrawn)
│   ├── share_capital_subscribed
│   ├── share_capital_paid
│   ├── voting_eligibility
│   └── officer_history[]
│
├── SHARE_CAPITAL_LEDGER
│   ├── ledger_id (primary key)
│   ├── member_id (foreign key)
│   ├── transaction_date
│   ├── transaction_type (subscription, payment, withdrawal)
│   ├── amount
│   ├── running_balance
│   └── reference_number
│
├── PATRONAGE_TRANSACTION
│   ├── transaction_id (primary key)
│   ├── member_id (foreign key)
│   ├── transaction_date
│   ├── transaction_type (purchase, service, loan interest)
│   ├── amount
│   ├── patronage_points
│   └── fiscal_year
│
├── STATUTORY_FUND
│   ├── fund_id (primary key)
│   ├── coop_id (foreign key)
│   ├── fund_type (RF, ETF, CDF, OF)
│   ├── fiscal_year
│   ├── beginning_balance
│   ├── allocations
│   ├── utilizations
│   └── ending_balance
│
├── GOVERNANCE_ENTITY
│   ├── entity_id (primary key)
│   ├── coop_id (foreign key)
│   ├── entity_type (GA, BOD, Committee)
│   ├── meeting_date
│   ├── attendees[]
│   ├── quorum_present
│   ├── resolutions[]
│   └── minutes_document
│
└── RESOLUTION
    ├── resolution_id (primary key)
    ├── governance_entity_id (foreign key)
    ├── resolution_number
    ├── resolution_date
    ├── subject
    ├── content
    ├── vote_result (for, against, abstain)
    └── implementation_status
```

### Cooperative Business Rules

**These rules must be enforced in platform features:**

#### 1. Democratic Voting (Art. 46)

```text
VOTING RULE: One Member, One Vote
│
├── Regardless of share capital amount
├── Proxy voting allowed only if specified in by-laws
├── Voting eligibility requires:
│   ├── Active membership status
│   ├── No delinquent obligations
│   └── Attended required trainings
└── Electronic voting must ensure:
    ├── Member identity verification
    ├── Vote secrecy
    ├── Vote immutability
    └── Audit trail
```

#### 2. Patronage-Based Surplus Distribution (Art. 86)

```text
PATRONAGE REFUND CALCULATION:
│
├── Total Patronage = Sum of all member patronage transactions
├── Member Patronage = Individual member's patronage transactions
├── Distributable Surplus = Net Surplus - Statutory Funds - Interest on Capital
│
├── Member Refund = (Member Patronage / Total Patronage) x Distributable Surplus
│
└── Platform Requirements:
    ├── Track all patronage-eligible transactions
    ├── Calculate proportional share automatically
    ├── Generate individual refund statements
    └── Process distribution or credit to share capital
```

#### 3. Statutory Fund Allocation (Art. 86)

```text
MANDATORY ALLOCATIONS (Before distribution):
│
├── Reserve Fund (RF): Minimum 10% of net surplus
│   └── Cannot be distributed until dissolution
│
├── Education and Training Fund (ETF): Minimum 10%
│   └── Used only for education and training
│
├── Community Development Fund (CDF): Minimum 3%
│   └── Used for community projects
│
└── Platform Validation:
    ├── Block surplus distribution if minimums not met
    ├── Track fund utilization against proper purposes
    └── Generate compliance reports per fund
```

#### 4. Officer Term Limits and Qualifications (Art. 43-44)

```text
OFFICER REQUIREMENTS:
│
├── Term: Maximum 2 years, re-election allowed
├── Qualifications:
│   ├── Member in good standing
│   ├── Completed mandatory training
│   ├── No delinquent obligations
│   └── Not convicted of cooperative-related offense
│
├── Disqualifications:
│   ├── Government employee with regulatory function
│   ├── Elected government official
│   └── Employed by cooperative (for BOD)
│
└── Platform Enforcement:
    ├── Validate eligibility during nomination
    ├── Track term expiry dates
    ├── Block re-nomination if disqualified
    └── Maintain officer history
```

#### 5. Quorum Requirements (Art. 45)

```text
MEETING QUORUM VALIDATION:
│
├── Regular/Special GA: 50% + 1 of total members
├── By-Law Amendment: 2/3 of total members
├── Dissolution: 2/3 of total members
│
└── Platform Features:
    ├── Calculate required quorum before meeting
    ├── Real-time attendance tracking
    ├── Alert when quorum not met
    └── Block voting if quorum insufficient
```

### Practical Scenarios

#### Scenario 1: Designing Member Dashboard for a Credit Cooperative

**Context:** Design a dashboard for members of Bangsamoro Credit Cooperative (1,200 members) to view their account and participate in cooperative activities.

**User Story:** As a member, I want to see my share capital, loan status, and patronage so that I can track my engagement with the cooperative.

**Dashboard Components:**

```text
MEMBER DASHBOARD LAYOUT:
┌─────────────────────────────────────────────────────────────────────┐
│ MEMBER DASHBOARD - [Member Name]                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                │
│ │ Share Capital│  │ Loan Balance │  │  Patronage   │                │
│ │   ₱15,000    │  │    ₱8,500    │  │  ₱45,200     │                │
│ │  Paid-up     │  │   Current    │  │  This Year   │                │
│ └──────────────┘  └──────────────┘  └──────────────┘                │
│                                                                      │
│ ┌─────────────────────────────────────────────────────────────────┐ │
│ │ UPCOMING EVENTS                                                  │ │
│ ├─────────────────────────────────────────────────────────────────┤ │
│ │ • Annual GA - March 15, 2025 [Register to Attend]               │ │
│ │ • Financial Literacy Training - Feb 20, 2025 [Enroll]           │ │
│ └─────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│ ┌─────────────────────────────────────────────────────────────────┐ │
│ │ RECENT TRANSACTIONS                                              │ │
│ ├─────────────────────────────────────────────────────────────────┤ │
│ │ Jan 15 | Loan Payment         | ₱2,000 | Patronage: ₱200        │ │
│ │ Jan 10 | Share Capital        | ₱1,000 | N/A                    │ │
│ │ Dec 28 | Loan Payment         | ₱2,000 | Patronage: ₱200        │ │
│ └─────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│ [View Full History] [Apply for Loan] [Pay Share Capital]            │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Feature Prioritization (RICE):**

| Feature | Reach | Impact | Confidence | Mission | Effort | Score | Priority |
|---------|-------|--------|------------|---------|--------|-------|----------|
| Share capital view | 10 | 2 | 1.0 | 1.0 | 1 | 20.0 | Must |
| Patronage tracking | 10 | 3 | 0.8 | 1.5 | 2 | 18.0 | Must |
| GA registration | 8 | 2 | 1.0 | 1.5 | 2 | 12.0 | Should |
| Training enrollment | 6 | 2 | 0.8 | 1.0 | 2 | 4.8 | Should |
| Loan application | 8 | 3 | 0.8 | 1.0 | 4 | 4.8 | Next |

#### Scenario 2: Building Patronage Refund Calculation Feature

**Context:** Build a feature for Mindanao Farmers Cooperative (800 members) to calculate and distribute patronage refunds at fiscal year end.

**Business Rules (from RA 9520 Art. 86):**

1. Calculate total net surplus for fiscal year
2. Deduct statutory fund allocations (RF 10%, ETF 10%, CDF 3%)
3. Deduct interest on share capital (max 1% above savings rate)
4. Remaining is distributable surplus
5. Distribute based on each member's patronage ratio

**Feature Flow:**

```text
PATRONAGE REFUND WORKFLOW:
│
├── STEP 1: Close Fiscal Year
│   ├── Input: Audited financial statements
│   ├── Validate: Net surplus amount
│   └── Output: Confirmed net surplus
│
├── STEP 2: Compute Statutory Allocations
│   ├── RF = Net Surplus x 10%
│   ├── ETF = Net Surplus x 10%
│   ├── CDF = Net Surplus x 3%
│   ├── OF = Per by-laws (if any)
│   └── Remaining = Net Surplus - All Allocations
│
├── STEP 3: Compute Interest on Capital
│   ├── For each member: Share Capital x Interest Rate
│   ├── Interest Rate = Savings Rate + 1% (max)
│   └── Total Interest = Sum of all member interest
│
├── STEP 4: Compute Distributable Surplus
│   └── Distributable = Remaining - Total Interest
│
├── STEP 5: Compute Individual Refunds
│   ├── Total Patronage = Sum of all member patronage
│   ├── For each member:
│   │   └── Refund = (Member Patronage / Total Patronage) x Distributable
│   └── Generate member statements
│
├── STEP 6: Distribution Options
│   ├── Option A: Credit to share capital
│   ├── Option B: Cash payout
│   └── Option C: Combination
│
└── STEP 7: Record and Report
    ├── Update member ledgers
    ├── Generate distribution report
    └── Submit to CSEA (CAPR)
```

**UI Mockup - Patronage Computation Screen:**

```text
┌─────────────────────────────────────────────────────────────────────┐
│ PATRONAGE REFUND COMPUTATION - FY 2024                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ NET SURPLUS (Audited):                              ₱2,500,000.00   │
│                                                                      │
│ STATUTORY ALLOCATIONS:                                               │
│   Reserve Fund (10%):                               ₱  250,000.00   │
│   Education and Training Fund (10%):                ₱  250,000.00   │
│   Community Development Fund (3%):                  ₱   75,000.00   │
│   Optional Fund (5%):                               ₱  125,000.00   │
│   ─────────────────────────────────────────────────────────────     │
│   Total Allocations:                                ₱  700,000.00   │
│                                                                      │
│ AFTER ALLOCATIONS:                                  ₱1,800,000.00   │
│                                                                      │
│ INTEREST ON SHARE CAPITAL:                                           │
│   Total Share Capital:                              ₱5,000,000.00   │
│   Interest Rate:                                    8%              │
│   Total Interest:                                   ₱  400,000.00   │
│                                                                      │
│ DISTRIBUTABLE SURPLUS:                              ₱1,400,000.00   │
│                                                                      │
│ PATRONAGE SUMMARY:                                                   │
│   Total Members:                                    800             │
│   Total Patronage Volume:                           ₱28,000,000.00  │
│   Average Refund per Member:                        ₱    1,750.00   │
│                                                                      │
│ [Preview Member Statements] [Approve Distribution] [Export Report]  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

#### Scenario 3: Creating FRAMES Compliance Tracking Dashboard

**Context:** Build a FRAMES compliance dashboard for CSEA staff to monitor 150 cooperatives in BARMM.

**Dashboard Requirements:**

1. Overview of all cooperatives' compliance status
2. Drill-down to individual cooperative details
3. Alert system for expiring documents and overdue submissions
4. Trend analysis for compliance improvement

**Dashboard Layout:**

```text
┌─────────────────────────────────────────────────────────────────────┐
│ CSEA COMPLIANCE DASHBOARD - FRAMES Overview                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ COMPLIANCE SUMMARY                                                   │
│ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐                             │
│ │  45   │ │  78   │ │  20   │ │   7   │                             │
│ │ Full  │ │Partial│ │  Low  │ │ Non-  │                             │
│ │Comply │ │Comply │ │Comply │ │Comply │                             │
│ └───────┘ └───────┘ └───────┘ └───────┘                             │
│                                                                      │
│ FRAMES BREAKDOWN (150 Coops)                                         │
│ ┌────────────────────────────────────────────────────────────────┐  │
│ │ F - Financial:    ████████████░░░░░░░░  62% compliant          │  │
│ │ R - Regulatory:   ████████████████░░░░  82% compliant          │  │
│ │ A - Admin:        ██████████░░░░░░░░░░  55% compliant          │  │
│ │ M - Membership:   ████████████████████  95% compliant          │  │
│ │ E - Economic:     ████████████████░░░░  78% compliant          │  │
│ │ S - Social:       ████████░░░░░░░░░░░░  45% compliant          │  │
│ └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│ URGENT ATTENTION (Expires within 30 days)                            │
│ ┌────────────────────────────────────────────────────────────────┐  │
│ │ • Bangsamoro MPC - COR expires Jan 31, 2025                    │  │
│ │ • Lanao Farmers Coop - AFS overdue by 15 days                  │  │
│ │ • Maguindanao Credit Coop - GA Minutes pending                 │  │
│ └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│ [View All Cooperatives] [Generate Report] [Send Reminders]          │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Feature Prioritization for CSEA Portal:**

| Feature | Priority | Rationale |
|---------|----------|-----------|
| Compliance score calculation | Must | Core CSEA mandate |
| Document expiry alerts | Must | Prevent regulatory gaps |
| CAPR submission tracking | Must | Annual compliance requirement |
| Cooperative detail view | Must | Case management |
| Bulk reminder sending | Should | Efficiency for staff |
| Trend analysis charts | Should | Strategic planning |
| Export to Excel/PDF | Should | Reporting needs |
| Predictive compliance risk | Could | Future enhancement |

### RA 9520 Quick Reference for Platform Features

| Article | Topic | Platform Relevance |
|---------|-------|-------------------|
| Art. 3 | Definitions | Patronage refund, net surplus terminology |
| Art. 4 | Common Bond | Membership eligibility validation |
| Art. 25 | Membership Qualifications | Application requirements |
| Art. 26 | Membership Book | Member registry requirements |
| Art. 30 | Termination | Withdrawal/expulsion workflow |
| Art. 39 | Share Capital | Capital structure, ledger requirements |
| Art. 43 | Board of Directors | Officer management features |
| Art. 44 | Officers and Committees | Committee tracking, qualifications |
| Art. 45 | General Assembly | GA management, quorum validation |
| Art. 46 | Voting Rights | One member, one vote enforcement |
| Art. 47 | GA Powers | Resolution types and requirements |
| Art. 86 | Net Surplus | Fund allocation, distribution logic |
| Art. 51 | Books and Records | Document management requirements |
| Art. 52 | Reports | CAPR submission features |

---


## SE Development Journey Integration

This skill serves as **Product Management** within Phase 4: DELIVER & DRIVE, orchestrated by `/enterprise-dev`.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PHASE 4: DELIVER & DRIVE                                  │
│                                                                              │
│        /enterprise-dev orchestrates three sub-skills                         │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         THREE PILLARS                                        │
│                                                                              │
│   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐                      │
│   │  MARKETING  │   │   PRODUCT   │   │   FINANCE   │                      │
│   │ MANAGEMENT  │   │ MANAGEMENT  │   │ MANAGEMENT  │                      │
│   │             │   │             │   │             │                      │
│   │ /marketer   │   │ /product    │   │ /finance    │                      │
│   │             │   │  ◄── HERE   │   │             │                      │
│   └─────────────┘   └─────────────┘   └─────────────┘                      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### When Invoked by /enterprise-dev

**Context**: You are helping someone develop a social enterprise. `/enterprise-dev` has invoked you for Product Management.

**Inputs from /design-thinking, /lean-canvas, and /toc:**

| Input | Source | Maps To |
|-------|--------|---------|
| User Personas | `/design-thinking` | Target user profiles |
| Journey Maps | `/design-thinking` | User touchpoints |
| Empathy Insights | `/design-thinking` | Pain points to address |
| Prototypes | `/design-thinking` | Feature validation |
| Solution | `/lean-canvas` | Product features |
| Key Metrics | `/lean-canvas` | Product success metrics |
| Problem | `/lean-canvas` | Jobs to be done |
| Theory of Change | `/toc` | Impact-driven features |
| Indicators | `/toc` | Success measurement |

**Your Outputs Must Include:**

| Output | Description | Used By |
|--------|-------------|---------|
| **Product Roadmap** | Now/Next/Later plan | Development team |
| **Feature Backlog** | Prioritized features | Sprint planning |
| **MVP Specification** | Minimum viable product | Initial launch |
| **Quality Standards** | Delivery processes | QA team |

**Workflow:**

```text
PRODUCT MANAGEMENT WORKFLOW:
│
├── 1. Receive Inputs
│   ├── Personas from /design-thinking → Target users
│   ├── Journey Maps → User touchpoints
│   ├── Solution from /lean-canvas → Product scope
│   ├── Key Metrics → Success metrics
│   ├── Problem → Jobs to be done
│   └── ToC from /toc → Impact features
│
├── 2. Define Product Vision
│   ├── Align with SE mission
│   ├── Define target outcomes
│   └── Set success criteria
│
├── 3. Prioritize Features
│   ├── Apply RICE/MoSCoW/Kano
│   ├── Balance impact vs effort
│   └── Identify MVP scope
│
├── 4. Create Roadmap
│   ├── Now: MVP features
│   ├── Next: Growth features
│   └── Later: Scale features
│
├── 5. Define Quality Standards
│   ├── Acceptance criteria
│   ├── Testing approach
│   └── Delivery process
│
└── OUTPUTS:
    ├── Product Roadmap
    ├── Feature Backlog
    ├── MVP Specification
    └── Quality Standards
```

---


