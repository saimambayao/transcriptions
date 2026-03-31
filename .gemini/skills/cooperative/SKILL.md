---
name: cooperative
description: "Provides cooperative development expertise for the Bangsamoro Development Platform. Use when designing cooperative courses/workshops (with /academy), consulting on coop formation, registration, compliance, or growth, building cooperative-related platform features, advising on RA 9520 compliance and CSEA/BARMM regulations, or developing PRS or cooperative training curriculum. Covers ICA 7 Cooperative Principles, Philippine Cooperative Code (RA 9520), governance structures, statutory funds (CETF, RF, CF, OOF), audit and compliance, and BARMM context. Integrates with /governance for board governance and /finance for cooperative financial management."
argument-hint: "[topic or question]"
allowed-tools: Read Grep Glob Bash Agent WebSearch WebFetch
---

# Cooperative Development Skill

> **GATE**: Invoke `/prompter` with the user's cooperative-related request first.
> Wait for `/prompter` to complete, then wait for user confirmation before proceeding.

Expert in cooperative development, principles, governance, and Philippine regulatory compliance.

**User query**: $ARGUMENTS

## When to Use

| Scenario | Action |
|----------|--------|
| Creating coop course/workshop | Use with `/academy` |
| Coop formation consulting | Use directly |
| Registration guidance | Use directly |
| Compliance review | Use directly |
| Governance training | Use with `/academy` |
| Building coop features | Use with `/featuredev` |

## Quick Reference

### ICA 7 Cooperative Principles (1995)

| # | Principle | Description |
|---|-----------|-------------|
| 1 | **Voluntary & Open Membership** | Open to all without discrimination |
| 2 | **Democratic Member Control** | One member, one vote |
| 3 | **Member Economic Participation** | Equitable contribution, limited interest on capital |
| 4 | **Autonomy & Independence** | Self-help, member-controlled |
| 5 | **Education, Training & Information** | Develop members and inform public |
| 6 | **Cooperation Among Cooperatives** | Work together locally to internationally |
| 7 | **Concern for Community** | Sustainable community development |

### Cooperative Values

**Core Values**: Self-help, self-responsibility, democracy, equality, equity, solidarity
**Ethical Values**: Honesty, openness, social responsibility, caring for others

### Philippine Cooperative Types (RA 9520)

| Category | Types |
|----------|-------|
| **Financial** | Credit, Cooperative Bank, Financial Service, Insurance |
| **Production** | Producer, Workers, Agrarian Reform, Dairy, Fishermen |
| **Consumer** | Consumer, Housing, Transport, Water Service, Electric |
| **Services** | Marketing, Service, Health Services, Education |
| **Multi-purpose** | Combines 2+ types above |
| **Advocacy** | Promotes cooperative principles |

### Statutory Funds (Net Surplus Distribution)

| Fund | Minimum % | Purpose |
|------|-----------|---------|
| **Reserve Fund** | 10% (50% first 5 years) | Stability, cover losses |
| **Education & Training Fund** | Up to 10% | Training, coop activities |
| **Community Development Fund** | 3% | Community benefit projects |
| **Optional Fund** | Up to 7% | Land, building, other |
| **Interest on Capital** | Limited rate | Return on share capital |
| **Patronage Refund** | Min 30% after reserves | Based on member transactions |

---

## Workflow 1: Curriculum Design Mode

When invoked with `/academy` for cooperative education.

### Stage 0: Deep Research (Mandatory)

Before curriculum design, invoke `/deep-research` to gather evidence-based content covering:
- CDA memorandum circulars (MC 2015-09, etc.)
- ICA cooperative principles and identity
- RA 9520 (Philippine Cooperative Code)
- BARMM cooperative regulations (BTA Bill 210)
- Cooperative governance best practices
- PEARLS financial monitoring framework

**Do not proceed to curriculum design without completing deep research.**

### BARMM Contextualization Standard

Apply the General-to-BARMM two-layer approach to ALL curriculum content. See [barmm-contextualization.md](references/barmm-contextualization.md) for the full standard, decision tree, and implementation checklist.

### Step 1: Determine Course Level

| Level | Audience | Duration | Focus |
|-------|----------|----------|-------|
| **PRS** | Prospective members | 4-8 hours | Coop basics, joining decision |
| **Basic** | New members/officers | 8-16 hours | Principles, rights, duties |
| **Intermediate** | Officers, managers | 24-40 hours | Governance, management |
| **Advanced** | Leaders, trainers | 40+ hours | Leadership, scaling, policy |

### Step 2: Select Curriculum Modules

**PRS Curriculum** (Required before joining):
1. What is a Cooperative?
2. Cooperative Principles & Values
3. Types of Cooperatives & Services
4. Member Rights & Responsibilities
5. Organizational Structure
6. Capital Structure & Funds
7. Benefits of Membership
8. Registration Requirements

**Basic/Officer courses**: See [curriculum-design.md](references/curriculum-design.md) for detailed modules.

### Step 3: Apply to /academy

Provide `/academy` with course level, modules, target audience, learning objectives, assessment methods, and CDA/CSEA training compliance.

---

## Workflow 2: Cooperative Consulting Mode

### Formation Consulting

**Pre-Formation Checklist**:
- 15+ Filipino citizens, of legal age
- Common bond of interest identified
- Residing/working in intended area
- Economic survey completed
- PRS completed by all organizers
- Cooperative type determined
- Initial capital commitments secured

**Registration Documents**: AOC (notarized), By-Laws, Economic Survey, Treasurer's Affidavit, Surety Bond, PRS Certificates, Registration Fee.

See [registration-guide.md](references/registration-guide.md) for complete process.

### Governance Consulting

**Mandatory Committees** (RA 9520):

| Committee | Selection | Key Functions |
|-----------|-----------|---------------|
| **Audit** | Elected by GA | Monitor controls, audit performance |
| **Election** | Elected by GA | Conduct elections, certify results |
| **Mediation/Conciliation** | Appointed by BOD | Resolve disputes |
| **Ethics** | Appointed by BOD | Enforce ethical standards |
| **Education & Training** | Appointed by BOD | Plan member training |

**Board of Directors**: 5-15 members, elected by GA, 2-year term, monthly meetings required.

### Compliance Consulting

**Annual Requirements**: CAPR + CAFS within 120 days after fiscal year end via CAIS.
**Certificate of Compliance (COC)**: Timely submissions, clean audit, updated surety bonds.

See [compliance-guide.md](references/compliance-guide.md) for details.

---

## Workflow 3: Platform Features Mode

### Data Models

**Core Cooperative Entities**: Cooperative (profile, type, registration), Membership (regular, associate), Officers (BOD, committees), Share Capital (contributions, withdrawals), Statutory Funds (reserve, ETF, CDF).

### Feature Areas

| Feature | Description |
|---------|-------------|
| **Coop Registration** | Online registration workflow |
| **Member Management** | Membership records, status |
| **Officer Tracking** | Terms, training compliance |
| **Compliance Dashboard** | Report status, deadlines |
| **Training Records** | PRS, officer training |
| **Financial Reports** | Statutory fund allocations |

---

## Workflow 4: Legal Query Mode

### Legal Reference Hierarchy

| Level | File | Use Case |
|-------|------|----------|
| **Quick Reference** | This file | Fast article lookup |
| **Comprehensive Guide** | [ra-9520-guide.md](references/ra-9520-guide.md) | Chapter summaries, cross-references |
| **Full Text** | [ra-9520-philippine-cooperative-code-2008.md](assets/ra-9520-philippine-cooperative-code-2008.md) | Verbatim legal citations |

### Quick RA 9520 Article Reference

| Article | Topic |
|---------|-------|
| Art. 3 | General Concepts (definition, principles) |
| Art. 6 | Purposes (cooperative objectives) |
| Art. 7 | Economic Survey (pre-registration) |
| Art. 14 | Articles of Cooperation (AOC content) |
| Art. 15 | By-Laws (content requirements) |
| Art. 22 | Kinds of Membership (Regular vs Associate) |
| Art. 23 | Types of Cooperatives (classification) |
| Art. 26 | Cooperative Category (Primary, Secondary, Tertiary) |
| Art. 38 | General Assembly (powers and meetings) |
| Art. 39 | Board of Directors (composition and duties) |
| Art. 43 | Officers (positions and duties) |
| Art. 46 | Audit Committee |
| Art. 47 | Election Committee |
| Art. 53 | Share Capital (capital structure) |
| Art. 86 | Net Surplus Allocation (statutory funds) |
| Art. 90 | Privileges (tax and other) |
| Art. 124 | Penalties (violations) |

### Citation Format

When citing: "Article X of RA 9520 (Philippine Cooperative Code of 2008)"

---

## BARMM/CSEA Context

### CSEA Authority

The **Cooperative and Social Enterprise Authority (CSEA)** is BARMM's sole regulatory agency for cooperatives, under the Office of the Chief Minister.

**Functions**: Registration, technical assistance, capability building, inspection/monitoring, compliance certificates.

### BTA Bill No. 210

The proposed **Bangsamoro Cooperative and Social Enterprise Code** (4 books):
- Book I: General Provisions
- Book II: Cooperative Development
- Book III: Social Enterprise Development
- Book IV: Miscellaneous & Final Provisions

**Key BARMM Requirements**: Moral governance alignment, local cultural respect, Shari'ah-compliant operations, halal transactions, no usury/gambling/haram.

See [barmm-context.md](references/barmm-context.md) for full BARMM context.

---

## References

### Legal References

| Level | File | Purpose |
|-------|------|---------|
| **Full Text** | [ra-9520-philippine-cooperative-code-2008.md](assets/ra-9520-philippine-cooperative-code-2008.md) | Verbatim legal text (19 chapters, 146 articles) |
| **Guide** | [ra-9520-guide.md](references/ra-9520-guide.md) | Chapter summaries, cross-references |

### Memorandum Circulars

| Category | Circulars |
|----------|-----------|
| **Registration** | [MC 2015-01](references/memorandum-circulars/mc-2015-01-registration-guidelines.md), [MC 2016-02](references/memorandum-circulars/mc-2015-01-registration-guidelines.md#amendment-mc-2016-02) |
| **Type-Specific** | [MC 2015-05](references/memorandum-circulars/mc-2015-05-agriculture-cooperative-registration.md), [MC 2015-07](references/memorandum-circulars/mc-2015-07-multipurpose-cooperative-registration.md) |
| **Governance** | [MC 2020-11](references/memorandum-circulars/mc-2020-11-validation-guidelines.md), [MC 2020-23](references/memorandum-circulars/mc-2020-23-cooperative-union-guidelines.md) |
| **Training** | [MC 2025-11](references/memorandum-circulars/mc-2025-11-prs-guidelines.md) |
| **Full Index** | [memorandum-circulars/index.md](references/memorandum-circulars/index.md) |

> **Note**: E-CoopRIS (MC 2020-20) and PRS (MC 2025-11) are CDA programs. CSEA has its own systems for BARMM.

### Cooperative Guides

| Reference | Purpose |
|-----------|---------|
| [ica-principles.md](references/ica-principles.md) | ICA Statement on Cooperative Identity |
| [governance-guide.md](references/governance-guide.md) | GA, BOD, Committees structure |
| [registration-guide.md](references/registration-guide.md) | Formation and registration process |
| [compliance-guide.md](references/compliance-guide.md) | Reporting and compliance requirements |
| [curriculum-design.md](references/curriculum-design.md) | Training curriculum and PRS |
| [barmm-contextualization.md](references/barmm-contextualization.md) | General-to-BARMM pedagogical standard |

### Templates & Integration

- **All templates**: [templates-index.md](references/templates-index.md)
- **Cross-skill integration**: [cross-skill-integration.md](references/cross-skill-integration.md)
