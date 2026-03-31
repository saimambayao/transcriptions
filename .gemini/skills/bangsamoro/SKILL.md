---
name: bangsamoro
description: |
  Domain expert in Bangsamoro affairs, history, culture, governance, development, and legislation.
  Provides authoritative knowledge on: (1) History and peace process (ARMM to BARMM, BOL, peace
  agreements), (2) Governance (BTA, parliamentary system, 12-point agenda, moral governance),
  (3) Development framework (6 goals, 8 strategies, macroeconomic targets from BDP 2023-2028),
  (4) Legislative archive (89+ enacted BAAs by category, 570+ adopted resolutions by theme),
  (5) Cultural diversity (13 ethnolinguistic groups, traditions, heritage),
  (6) Economy (agriculture, fisheries, trade, tourism, fiscal autonomy),
  (7) Peace and security (normalization, rido, law enforcement),
  (8) Social services (education, health, social welfare),
  (9) Geography (5 provinces per SC ruling, Cotabato City, SGA),
  (10) BOL provisions (RA 11054 — powers, territory, fiscal autonomy, Shari'ah, transition).
  Use this skill whenever the user needs Bangsamoro context for policy research, legislative
  drafting, speech writing, development planning, governance analysis, legislative lookup,
  BAA research, resolution search, BDP targets, or any work involving BARMM affairs.
  Also trigger on: "bangsamoro", "BARMM", "BTA", "BOL", "bangsamoro organic law",
  "Moro", "Mindanao peace process", "MILF", "MNLF", "bangsamoro development plan", "BDP",
  "moral governance", "12-point agenda", "rido", "sultanate", "Cotabato", "Marawi",
  "Maguindanao", "Lanao del Sur", "Sulu", "Tawi-Tawi", "Basilan", "BAA", "bangsamoro autonomy act",
  "which BAA", "what resolution", "BDP goal", "BDP target", "BDP chapter", "development goal",
  "BARMM legislation", "enacted law", "adopted resolution", "parliamentary resolution",
  "bangsamoro law", "BAA number", "resolution number", "legislative archive".
  Primary sources: 2nd Bangsamoro Development Plan 2023-2028, Bangsamoro Organic Law (RA 11054),
  89+ Bangsamoro Autonomy Acts, 570+ adopted resolutions, Bangsamoro Administrative Code (BAA No. 13).
allowed-tools:
  - Read
  - Glob
  - Grep
  - WebSearch
  - Agent
argument-hint: "[topic, BAA number, resolution number, BDP goal, or question about Bangsamoro]"
---

# Bangsamoro Domain Expert

Authoritative domain knowledge on Bangsamoro affairs — governance, development, culture, history,
economy, peace, social services, and **legislation**. This is a global skill usable across all
projects. It serves as the knowledge foundation for all parliamentarian skills: `/bill-drafter`,
`/resolution-drafter`, `/legislative-briefer`, `/speech-writer`, `/policy-recommendation`.

---

## Phase 1: Query Classification

When invoked, classify the query into one of these types to determine depth and sources:

| Query Type | Signal Words | Approach |
|-----------|-------------|----------|
| **Simple fact** | "how many", "what is", "who is", "list the" | Answer from Quick Reference inline |
| **BAA lookup** | "which BAA", "BAA number", "what law", "enacted legislation" | Use BAA Index → full text if needed |
| **Resolution lookup** | "which resolution", "resolution number", "what resolution" | Use Resolution Index → full text if needed |
| **BDP reference** | "BDP goal", "BDP target", "development plan", "chapter" | Use BDP Summaries → full chapter if needed |
| **Cross-reference** | "what legislation supports", "BAAs related to", "laws for BDP goal" | Use Cross-Reference Map → drill into sources |
| **Domain research** | "explain", "analyze", "describe", "context for" | Read reference file(s) from Knowledge Domains |
| **Multi-domain** | "draft a bill", "write a briefer", "policy on" | Compose from multiple sources → hand off to downstream skill |

## Phase 2: Source Selection

Based on query type, select sources in this priority order:

### Source Hierarchy (most authoritative first)
1. **BOL (RA 11054)** — constitutional-level authority → `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (5 files)
2. **Enacted BAAs** — regional legislation → full text at `~/Vault/bangsamoro/bangsamoro-laws/BAA-{N}.md` (89 files). Backup: `~/Vault/bangsamoro/bangsamoro-laws/BAA-{N}.md`
3. **Adopted Resolutions** — parliamentary will → full text at `~/Vault/bangsamoro/bangsamoro-resolutions/resolution{N}.md` (556 files). Backup: `~/Vault/bangsamoro/bangsamoro-resolutions/resolution{N}.md`
4. **2nd BDP 2023-2028** — planning authority → chapters at `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/`. Backup: `docs/bdp/bdp-2023-2028/`
5. **Reference files** — curated summaries → `references/*.md` (13 files)
6. **Quick Reference** — inline data in this skill file
7. **WebSearch** — for post-2022 data or verification

### Source Selection by Query Type

| Query Type | First Read | If More Detail Needed | Full Text Source |
|-----------|-----------|----------------------|-----------------|
| BAA lookup | Vault: `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md` | `~/Vault/bangsamoro/bangsamoro-laws/INDEX.md` | `~/Vault/bangsamoro/bangsamoro-laws/BAA-{N}.md` |
| Resolution lookup | Vault: `~/Vault/bangsamoro/bangsamoro-resolutions/resolution-classification.md` | `~/Vault/bangsamoro/bangsamoro-resolutions/INDEX.md` | `~/Vault/bangsamoro/bangsamoro-resolutions/resolution{N}.md` |
| BDP reference | Vault: `~/Vault/bangsamoro/bangsamoro-development/bdp-chapter-summaries.md` | Quick Reference below | `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/{chapter}.md` |
| BOL provision | `references/bol-key-provisions.md` | — | `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` |
| Domain research | Relevant `references/*.md` file | — | See Knowledge Domains table |
| Cross-reference | Cross-Reference Map below | BAA Index + BDP Summaries | Full text of identified sources |

**Rule: Check local sources BEFORE web searching.** Always read vault/reference files first.

## Phase 3: Compose Answer

1. **Gather** — Read the selected sources
2. **Cite** — Every fact must include source: `[BAA 35]`, `[BDP Ch. 9]`, `[BOL Art. XII, Sec. 9]`, `[Resolution 78]`, or `[Source: moa-structure.md]`
3. **Compose** — Structure the answer for the downstream consumer (skill or user)
4. **Caveat** — Flag data vintage, Sulu status, or conflicts per Error Handling section
5. **Hand off** — If the query requires action (drafting, writing), compose context and hand to the appropriate downstream skill

---

## Knowledge Domains

| Domain | Reference File | Key Topics |
|--------|----------------|------------|
| History & Peace | [history-peace-process.md](references/history-peace-process.md) | Sultanates, colonial resistance, FAB/CAB, BOL, ARMM to BARMM transition |
| Governance | [governance-framework.md](references/governance-framework.md) | BTA, parliamentary system, 12-point agenda, moral governance pillars |
| MOA Structure | [moa-structure.md](references/moa-structure.md) | 16 ministries/OCM, attached agencies, commissions, councils, boards |
| Development | [development-framework.md](references/development-framework.md) | Vision/mission, 6 goals, 8 strategies, macroeconomic targets |
| Culture | [cultural-diversity.md](references/cultural-diversity.md) | 13 ethnolinguistic groups, sultanates, traditions, heritage |
| Economy | [economy.md](references/economy.md) | Agriculture, fisheries, trade, investment, tourism, fiscal autonomy |
| Peace & Security | [peace-security.md](references/peace-security.md) | Normalization, rido settlement, terrorism, law enforcement |
| Social Services | [social-services.md](references/social-services.md) | Education, health, social welfare, WASH |
| Geography | [geography.md](references/geography.md) | 6 provinces, Cotabato City, SGA, demographics, spatial strategy |
| BOL | [bol-key-provisions.md](references/bol-key-provisions.md) | RA 11054 — powers, territory, fiscal autonomy, Shari'ah, transition |
| Officials | [barmm-officials-2025-2026.md](references/barmm-officials-2025-2026.md) | Current BTA leadership, ministers, MPs |
| Legislative Patterns | ~/Vault/bangsamoro/bangsamoro-laws/baa-legislative-patterns.md | Header evolution, enacting clause variants, section numbering patterns, standard clause templates, templated bill types |
| Resolution Patterns | ~/Vault/bangsamoro/bangsamoro-resolutions/resolution-drafting-patterns.md | WHEREAS conventions, operative clause patterns, Hijri dates, header format evolution, type-specific patterns |

---

## BAA Quick-Reference (89 Enacted Laws)

**Full categorized index:** `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md`
**Full text source:** `~/Vault/bangsamoro/bangsamoro-laws/BAA-{N}.md` | **Index:** `~/Vault/bangsamoro/bangsamoro-laws/INDEX.md`

### BAAs by Category

#### Governance & Administration
| BAA | Short Title |
|-----|------------|
| 4 | Bangsamoro Human Rights Commission |
| 5 | Bangsamoro Attorney-General's Office |
| 6 | Bangsamoro Socio-Economic Development Planning System |
| 8 | Bangsamoro Women Commission |
| 10 | Bangsamoro Youth Commission |
| 11 | Power of Appointment in BARMM |
| 12 | Bangsamoro Sports Commission |
| 13 | **Bangsamoro Administrative Code** (establishes all MOAs) |
| 17 | **Bangsamoro Civil Service Code** |
| 31 | Bangsamoro Sustainable Development Board |
| 49 | **Bangsamoro Local Governance Code** |
| 81 | Salamat Excellence Award for Leadership |

#### Budget & Appropriations
| BAA | Short Title |
|-----|------------|
| 3 | GAA FY 2020 |
| 14 | Extension of 2020 Appropriations |
| 15 | GAA FY 2021 |
| 22 | Special Development Fund (PHP 10B from 2020-2021 SDF) |
| 23 | GAA FY 2022 |
| 24 | Extension of 2020-2021 GAA |
| 32 | GAA FY 2023 |
| 33 | Extension of 2022 GAA |
| 34 | Extension of 2020-2021 SDF |
| 36 | Revolving Fund for Nationally-Funded Personnel |
| 38 | Continued Use of FY 2020-2022 Funds |
| 51 | Extension of 2020-2023 SDF |
| 52 | Extension of FY 2023 GAA |
| 63 | Supplemental Appropriations |
| 65 | GAA FY 2025 |
| 75 | Supplemental Appropriations (FY 2025) |

#### Health
| BAA | Short Title |
|-----|------------|
| 21 | COVID Oxygen Tanks (PHP 50M) |
| 25 | Upgrade Datu Blah Sinsuat Hospital to Level II (Maguindanao) |
| 26 | Upgrade Wao District Hospital (Lanao del Sur) |
| 27 | Level II Hospital in Maimbung (Sulu) |
| 28 | Upgrade Sulu Provincial Hospital to Level II |
| 29 | Upgrade Buluan District Hospital to Level II (Maguindanao) |
| 30 | Upgrade Unayan Hospital to District Hospital (Binidayan, Lanao del Sur) |
| 73 | Convert Iranon District Hospital to Provincial Hospital (Parang) |
| 74 | Upgrade Maguindanao Provincial Hospital to Level III Regional Hospital |
| 76 | Upgrade Sibutu Hospital to Level I (Tawi-Tawi) |
| 78 | Level I Hospital in Tipo-Tipo (Basilan) |
| 79 | Level I Hospital in Maluso (Basilan) |
| 80 | Upgrade Dr. Montañer Memorial Hospital |

#### Education & Culture
| BAA | Short Title |
|-----|------------|
| 18 | **Bangsamoro Education Code** (integrated quality education system) |
| 40 | Bangsamoro Science High School System |
| 50 | Bangsamoro Kulliyyah for Islamic Studies |
| 59 | Bangsamoro Agriculture and Fisheries Training Institute |

#### Economy & Labor
| BAA | Short Title |
|-----|------------|
| 9 | Regulation of Recruitment Agencies |
| 19 | Bangsamoro Overseas Employment Policies |
| 72 | 7-Day Bereavement Leave (public and private sector) |

#### Peace & Security / Memorials
| BAA | Short Title |
|-----|------------|
| 57 | Financial Assistance to Bangsamoro Mujahideen |
| 60 | Sheikh Salamat Hashim & Mimbantas Memorial Site |
| 61 | Bangsamoro Memorial Marker and Eco-Park, Camp Abubakar |

#### Local Government / Municipality Creation
| BAA | Short Title |
|-----|------------|
| 37 | **Seat of Government in Parang, Maguindanao del Norte** |
| 41 | Create Municipality of Pahamuddin |
| 42 | Create Municipality of Kadayangan |
| 43 | Create Municipality of Nabalawag |
| 44 | Create Municipality of Old Kaabakan |
| 45 | Create Municipality of Kapalawan |
| 46 | Create Municipality of Malidegao |
| 47 | Create Municipality of Tugunan |
| 48 | Create Municipality of Ligawasan |
| 53 | Create Municipality of Nuling (Maguindanao del Norte) |
| 54 | Create Municipality of Datu Sinsuat Balabaran |
| 55 | Create Municipality of Sheik Abas Hamza |
| 70 | Amend BAA 54 (Datu Sinsuat Balabaran boundary) |
| 71 | Amend BAA 55 (Sheik Abas Hamza boundary) |

#### Electoral & Districts
| BAA | Short Title |
|-----|------------|
| 35 | **Bangsamoro Electoral Code** |
| 58 | Parliamentary Districts (original — declared unconstitutional) |
| 77 | Reconstituted Parliamentary Districts (amends BAA 58 — declared unconstitutional) |

#### Social Welfare & Human Rights
| BAA | Short Title |
|-----|------------|
| 62 | IDP Protection and Rights |
| 64 | Indigenous Peoples' Rights (strengthens MIPA) |

#### Symbols & Identity
| BAA | Short Title |
|-----|------------|
| 1 | Official Flag |
| 2 | Official Emblem |
| 7 | Official Hymn |
| 16 | Official Parliament Seal |
| 20 | Dual Hijri-Gregorian Calendar |
| 39 | Regional Holidays |

#### Environment & Development
| BAA | Short Title |
|-----|------------|
| 31 | Bangsamoro Sustainable Development Board |

#### Recent Legislation (Jan-Feb 2026)
| BAA | Short Title | Category |
|-----|------------|----------|
| 82 | **Bangsamoro Labor and Employment Code** | Economy & Labor |
| 83 | Bangsamoro Nutrition Commission | Social Welfare |
| 84 | **Bangsamoro Budget System Act of 2025** | Budget |
| 85 | **GAA FY 2026** | Budget |
| 86 | **Parliamentary District Act** (32 districts, post-Sulu exclusion) | Electoral |
| 87 | Amends BAA 35 — removes "None of the Above" from ballots | Electoral |
| 88 | Amends BAA 35 (Electoral Code amendment) | Electoral |
| 89 | **Bangsamoro Transitional Justice and Reconciliation Program** | Human Rights |

**Archive currency note:** The vault (`~/Vault/bangsamoro/bangsamoro-laws/`) contains all 89 enacted BAAs (complete, verified). BAAs 82-89 were enacted Jan-Feb 2026. Backup copies in `docs/BAAs/`. For any BAAs enacted after Feb 2026, use WebSearch against the [BARMM Official Gazette](https://officialgazette.bangsamoro.gov.ph/bangsamoro-autonomy-acts-irrs/).

---

## Resolution Quick-Reference (570+ Adopted)

**Full classified index:** `~/Vault/bangsamoro/bangsamoro-resolutions/resolution-classification.md`
**Full text source:** `~/Vault/bangsamoro/bangsamoro-resolutions/resolution{N}.md` | **Index:** `~/Vault/bangsamoro/bangsamoro-resolutions/INDEX.md`

### Key Landmark Resolutions

| Res. No. | Subject | Significance |
|----------|---------|-------------|
| 6 | Parliamentary Rules, Procedures, and Practices | Foundational rules of the BTA Parliament |
| 12 | Approve BTA Transition Plan | Blueprint for ARMM-to-BARMM transition |
| 50 | Create Committee on Bangsamoro Justice System | Expanded statutory committees |
| 55 | Enhanced Transition Plan 2019-2022 | Refined transition roadmap |
| 56 | Call for Transitional Justice and Reconciliation Commission | National-level TJ mechanism |
| 70 | Enhanced Parliamentary Rules | Updated rules of procedure |
| 73 | Allow Virtual Sessions (COVID) | Teleconference/video plenary and committee meetings |
| 78 | **Approve 1st BDP 2020-2022** | First Bangsamoro Development Plan |
| 90 | Approve Recruitment/Selection Boards for all MOAs | Standardized hiring |
| 93 | Urge Congress to Extend BTA to June 2025 | Transition period extension |
| 96 | Approve BTA Parliament Organizational Structure | Institutional framework |

### Resolution Categories (count estimates)

| Category | Example Resolutions | Notes |
|----------|-------------------|-------|
| **Parliamentary rules & org** | 6, 15, 16, 25, 27, 29, 31, 32, 50, 65, 70, 72, 73, 96 | Foundational institutional resolutions |
| **Budget & finance** | 9, 10, 28, 34, 45, 53, 76 | Expenditure programs, fund realignment |
| **Governance & transition** | 3, 4, 7, 12, 26, 54, 55, 90, 93, 95 | Transition plans, BTA operations |
| **Peace & security** | 18, 52, 56, 58, 88, 89, 91, 94 | Violence condemnation, peace process |
| **Marawi rehabilitation** | 33, 41, 52, 84, 85 | Marawi siege response |
| **Health & social welfare** | 35, 42, 47, 48, 51, 60, 61, 74, 76, 79, 81, 82 | Health emergencies, COVID, OFW |
| **Education & culture** | 62, 66, 97 | Cultural recognition, schools |
| **Development planning** | 78 | BDP approval |
| **External relations** | 17, 23, 24, 30, 37, 63, 64, 67 | Appeals to Congress, IGR |
| **Human rights & justice** | 38, 56, 58, 68, 80, 91 | Transitional justice, discrimination |
| **Commendations & condolences** | 2, 11, 21, 46, 59, 71, 74, 86-87, 92, etc. | ~200+ routine resolutions |

---

## BDP 2023-2028 Chapter Guide

**Full chapter summaries with targets:** `~/Vault/bangsamoro/bangsamoro-development/bdp-chapter-summaries.md`
**Full chapter text:** `docs/bdp/bdp-2023-2028/{chapter-file}.md`

| Ch. | Title | BDP Goal | Key Focus Areas |
|-----|-------|----------|-----------------|
| 1 | BARMM Extended Transition | — | History, peace process, ARMM→BARMM, transition timeline |
| 2 | Regional Trends | — | Demographics, population (4.9M), growth rate (3.26%) |
| 3 | Spatial Strategy | 6 | Settlement hierarchy, urban-rural, infrastructure mapping |
| 4 | **Development Framework** | All | Vision, 6 goals, 8 strategies, macro targets, moral governance |
| 5 | **Governance** | 1 | Bureaucracy reform, legislation, fiscal management, civil service |
| 6 | Cultural Diversity | 5 | 13 ethnolinguistic groups, heritage, identity preservation |
| 7 | **Economy** | 2 | Agriculture, fisheries, trade, investment, halal industry |
| 8 | Technology & Innovation | 2, 3 | ICT, digital governance, innovation ecosystem |
| 9 | **Social Services** | 4 | Education, health, social welfare, WASH targets |
| 10 | Peace & Security | 3 | Normalization, DDR, rido, law enforcement, human rights |
| 11 | Infrastructure | 6 | Roads, bridges, ports, airports, water, energy |
| 12 | Environment | 3, 6 | Climate resilience, forest cover, marine protection |
| 13 | Plan Financing | 1 | Revenue, expenditure, block grant, SDF, IRA |
| 14 | Communication Strategy | 1 | Public awareness, stakeholder engagement |

---

## Cross-Reference Map: BDP Goals ↔ BAAs ↔ BDP Chapters

| BDP Goal | Supporting BAAs | BDP Chapters | Key Resolutions |
|----------|----------------|-------------|-----------------|
| **Goal 1: Stable, just, accountable government** | 4, 5, 8, 10, 11, 12, 13, 17, 31, 35, 49, 81 | Ch. 5 (Governance), Ch. 13 (Financing), Ch. 14 (Communication) | 6, 12, 55, 70, 90, 93, 96 |
| **Goal 2: Equitable, competitive, robust economy** | 9, 19, 59, 72 | Ch. 7 (Economy), Ch. 8 (Technology) | 82 |
| **Goal 3: Peaceful, safe, resilient communities** | 57, 60, 61, 62 | Ch. 10 (Peace & Security), Ch. 12 (Environment) | 33, 41, 52, 56, 58, 88, 89 |
| **Goal 4: Inclusive, responsive social services** | 18, 21, 25-30, 40, 50, 64, 73, 74, 76, 78-80 | Ch. 9 (Social Services) | 35, 42, 47, 51, 60, 74, 79, 81 |
| **Goal 5: Culture and identity preserved** | 1, 2, 7, 16, 20, 39 | Ch. 6 (Cultural Diversity) | 62, 66, 97 |
| **Goal 6: Strategic, climate-resilient infrastructure** | 37 | Ch. 3 (Spatial Strategy), Ch. 11 (Infrastructure) | 30, 67 |
| **Budget (cross-cutting)** | 3, 14, 15, 22-24, 32-34, 36, 38, 51, 52, 63, 65, 75 | Ch. 13 (Financing) | 9, 10, 28, 34, 45, 53, 76 |
| **Local government (cross-cutting)** | 41-48, 53-55, 70, 71 | Ch. 3 (Spatial Strategy) | 49 (SGA turnover) |
| **Electoral (cross-cutting)** | 35, 58, 77 | Ch. 5 (Governance) | 93 (BTA extension) |

---

## Primary Sources

### Bangsamoro Organic Law (RA 11054)
The foundational law establishing BARMM. Signed July 27, 2018; ratified by plebiscite January-February 2019. Defines territory, powers, parliamentary system, fiscal autonomy, and transition framework. Read `references/bol-key-provisions.md` for key provisions. For the full verbatim text, read `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (5 chapter files). Fallback: `~/apps/transcriptions/PDFs/RA 11054.pdf`. Check locally BEFORE web searching for BOL provisions.

### Bangsamoro Development Plan 2023-2028
The 2nd BDP covering the extended transition period. Read the full text at `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` (15 chapters) or `docs/bdp/bdp-2023-2028/`. For quick lookups, read `~/Vault/bangsamoro/bangsamoro-development/bdp-chapter-summaries.md` first. Check locally BEFORE web searching for BDP goals, strategies, or targets.

### Bangsamoro Administrative Code (BAA No. 13)
The administrative framework establishing all ministries, offices, and agencies. Read `references/moa-structure.md` for the complete organizational hierarchy. Source text at `~/Vault/bangsamoro/bangsamoro-laws/BAA-13.md`.

### Legislative Archive
- **89 enacted BAAs**: `~/Vault/bangsamoro/bangsamoro-laws/` (89 verified .md files + INDEX.md) — categorized index at `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md`
- **556 adopted resolutions**: `~/Vault/bangsamoro/bangsamoro-resolutions/` (556 verified .md files + INDEX.md) — classified index at `~/Vault/bangsamoro/bangsamoro-resolutions/resolution-classification.md`
- **416 filed bills**: `docs/Bills/` (INDEX.md) — working repo only
- **676 proposed resolutions**: `docs/Proposed-Resolutions/` — working repo only

---

## Quick Reference

### BARMM Vision

> "A Bangsamoro that is united, enlightened, self-governing, peaceful, just, morally upright, and progressive."

### Six Development Goals

1. **Stable, just, and accountable government**
2. **Equitable, competitive, and robust economy**
3. **Peaceful, safe, and resilient communities**
4. **Inclusive, responsive, and quality social services**
5. **Rich and diverse culture and identity preserved**
6. **Strategic, adequate, and climate-resilient infrastructure**

### Eight Development Strategies

1. Improve and strengthen governance mechanisms
2. Create an enabling environment for an equitable, competitive, and robust economy
3. Harness technology and innovations for socioeconomic opportunities
4. Improve ecological integrity and community resilience
5. Enhance peace, public order, safety, security, and human rights
6. Ensure inclusive and equitable access to quality services
7. Mainstream Bangsamoro cultural diversity, beliefs, heritage, and identity
8. Scale up functional, strategic, climate-resilient infrastructure

### Macroeconomic Targets (2023-2028)

| Indicator | Baseline (2021) | Target |
|-----------|----------------|--------|
| GRDP Growth | 7.5% | 8-9% |
| Industry/Services Growth | 7.9% / 6.6% | 10-12% |
| Gross Capital Formation (% of GRDP) | 16.91% | 18-20% |
| Inflation Rate | 2.40% | 2-4% |
| Unemployment Rate | 3.80% | 3-5% |
| Underemployment Rate | 9.0% | 4-7% |
| Poverty Incidence | 29.80% | 20-25% |

### Twelve Pillars of Moral Governance

1. Integrity
2. Accountability
3. Transparency and Honesty
4. Sense of Patriotism
5. Striving for Excellence
6. Cultural Understanding and Tolerance
7. Unwavering Loyalty to God
8. Justice
9. Inclusivity
10. Objectivity
11. Dialogue and Meaningful Engagement
12. Balance Between Practical Life and Moral Side

### Enhanced 12-Point Priority Agenda

1. Strengthen bureaucracy
2. Enact priority codes
3. Increase revenue generation
4. Improve social services
5. Develop infrastructure
6. Foster economic development
7. Protect environment
8. Build disaster resilience
9. Implement peace and normalization
10. Rehabilitate Marawi City
11. Sustain peace and security
12. Preserve cultural heritage

### Territory

| Component | Details |
|-----------|---------|
| Provinces | 5: Basilan (excl. Isabela City), Lanao del Sur, Maguindanao del Norte, Maguindanao del Sur, Tawi-Tawi |
| Cities | 3: Cotabato City (independent component), Marawi City, Lamitan City |
| Municipalities | 116 (pre-SC ruling; subject to adjustment) |
| SGA | 63 barangays from North Cotabato |
| Total Barangays | 2,590 (pre-SC ruling) |
| Land Area | 32,953.01 sq.km per 2nd BDP (includes Sulu; subject to adjustment) |

**Sulu Status (SC Ruling, September 2024):** The Supreme Court declared Sulu is not part of BARMM, respecting the province's rejection of the BOL during the January 2019 plebiscite. BARMM filed a motion for reconsideration. The 2nd BDP (2023-2028) and most statistical references predate this ruling and include Sulu data. When citing BARMM statistics, note whether the data includes or excludes Sulu — this affects population (~900,000), land area, barangay count, and economic indicators.

### Key Statistics (2020-2021)

| Indicator | Value | Source |
|-----------|-------|--------|
| Population (2020 Census) | 4,944,800 (4.54% of national) | PSA |
| Population Growth Rate | 3.26% (2010-2020) | PSA |
| GRDP Growth (2021) | 7.5% (2nd highest nationally) | PSA |
| Poverty Incidence (2021) | 29.80% (down from 54.20% in 2018) | PSA |
| National Economic Share | 1.4% (lowest nationally) | PSA |
| Functional Literacy Rate | 71.6% (lowest nationally; national: 91.6%) | PSA 2019 |

### BARMM Government Structure (BAA No. 13)

**16 Executive Units:** Office of the Chief Minister (OCM) + 15 line ministries

**Ministries:** MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MIPA, MILG, MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC

**OCM Attached Agencies:** BPDA, BBOI, BIO, BICTO, OSC, OOBC, BPA, DAB, BDI, CSEA

**Commissions:** BWC, BYC, BSC, BCPCH

**Independent Bodies:** BHRC, BIAB

**Other:** BEZA (attached to MTIT), Bangsamoro Halal Board (MTIT), Office of the Wali

Read `references/moa-structure.md` for the complete hierarchy with full names.

### Ethnolinguistic Groups

**Islamized groups:** Maguindanaon, Meranao, Iranun, Tausug, Sama, Yakan, Sangil, Molbog, Jama Mapun, Kalagan, Kalibugan

**Non-Moro IPs:** Teduray, Lambangian, Dulangan Manobo, B'laan

---

## Legislative Lookup Workflows

### Workflow A: Find a BAA by Topic

1. Scan the **BAAs by Category** section above for the domain
2. If found → note the BAA number and short title
3. If more detail needed → read `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md`
4. For full text → read `~/Vault/bangsamoro/bangsamoro-laws/BAA-{N}.md`
5. Cite as: `[BAA {N} — {short title}]`

**Example:** "Which BAA covers elections?"
→ Electoral & Districts category → BAA 35 (Electoral Code) [BAA 35]

### Workflow B: Find a Resolution by Theme

1. Scan the **Key Landmark Resolutions** table above
2. If not found → read `~/Vault/bangsamoro/bangsamoro-resolutions/resolution-classification.md`
3. If still not found → Grep `docs/Resolutions/INDEX.md` for keywords
4. For full text → read `~/Vault/bangsamoro/bangsamoro-resolutions/resolution{N}.md`
5. Cite as: `[Resolution {N}]`

**Example:** "What resolution approved the first BDP?"
→ Key Landmark Resolutions → Resolution 78 (Approve 1st BDP 2020-2022) [Resolution 78]

### Workflow C: Find BDP Targets for a Sector

1. Check the **BDP Chapter Guide** table above for the relevant chapter
2. Read `~/Vault/bangsamoro/bangsamoro-development/bdp-chapter-summaries.md` for targets
3. For full data → read `docs/bdp/bdp-2023-2028/{chapter-file}.md`
4. Cite as: `[BDP Ch. {N} — {title}]`

**Example:** "What are the BDP education targets?"
→ BDP Chapter Guide → Ch. 9 (Social Services) → read summaries for education targets [BDP Ch. 9]

### Workflow D: Cross-Reference (BAAs Supporting a BDP Goal)

1. Look up the goal in the **Cross-Reference Map** above
2. Identify supporting BAAs and chapters
3. Read specific BAA texts or BDP chapters as needed
4. Compose the mapping with citations

**Example:** "What legislation supports BDP Goal 4 (social services)?"
→ Cross-Reference Map → BAAs 18, 21, 25-30, 40, 50, 64, 73, 74, 76, 78-80 → BDP Ch. 9
→ Key laws: BAA 18 (Education Code), BAA 40 (Science High Schools), BAA 64 (IP Rights), plus 13 hospital upgrade BAAs

---

## Usage Examples

**Q:** "What are the BARMM development goals?"
**A:** Answer from Quick Reference — the 6 goals are listed inline. No file read needed. [Quick Reference]

**Q:** "I need the complete BARMM agency hierarchy for a bill's implementing agency section."
**A:** Read `references/moa-structure.md` for the full organizational chart. The 16 executive units are: OCM + 15 line ministries. [Source: moa-structure.md, from BAA No. 13]

**Q:** "What does the BOL say about fiscal autonomy for a budget resolution?"
**A:** Read `references/bol-key-provisions.md`, Article XII section. Key facts: Annual Block Grant = 5% of net national internal revenue; Special Development Fund = PHP 5B/year for 10 years; 75% of national taxes collected within BARMM. Then compose with /resolution-drafter. [BOL Art. XII]

**Q:** "Which BAA established the civil service system?"
**A:** BAA 17 — Bangsamoro Civil Service Code. For full provisions, read `docs/BAAs/BAA-17.md`. [BAA 17]

**Q:** "What BAAs created new municipalities in the SGA?"
**A:** BAAs 41-48 created 8 municipalities: Pahamuddin, Kadayangan, Nabalawag, Old Kaabakan, Kapalawan, Malidegao, Tugunan, Ligawasan. BAAs 53-55 created 3 more in Maguindanao del Norte. BAAs 70-71 amended BAAs 54-55 boundaries. [BAAs 41-48, 53-55, 70-71]

**Q:** "What resolution relates to Marawi rehabilitation?"
**A:** Multiple resolutions: 33 (support for compensation bill), 41 (special committee on Marawi recovery), 52 (appeal against additional military camp), 84 (prohibit treating ground zero as tourist spot), 85 (tax relief for Marawi taxpayers). [Resolutions 33, 41, 52, 84, 85]

**Q:** "What are the BDP targets for poverty reduction?"
**A:** Poverty Incidence target: 20-25% by 2028 (from 29.80% baseline in 2021). Underemployment: 4-7% (from 9.0%). See BDP Ch. 4 (Development Framework) for macro targets and Ch. 9 (Social Services) for sector programs. [BDP Ch. 4, Quick Reference: Macroeconomic Targets]

**Q:** "What legislation supports BDP Goal 2 (economy)?"
**A:** Supporting BAAs: 9 (recruitment agency regulation), 19 (overseas employment), 59 (agriculture training institute), 72 (bereavement leave). BDP Ch. 7 (Economy) and Ch. 8 (Technology) detail sector strategies. [Cross-Reference Map]

**Q:** "Give me cultural context for a speech about Bangsamoro identity."
**A:** Read `references/cultural-diversity.md` for the 13 ethnolinguistic groups, sultanate history, and traditional governance systems. Supporting legislation: BAAs 1, 2, 7 (symbols), BAA 20 (Hijri calendar), BAA 39 (regional holidays). BDP Goal 5 and Ch. 6 cover cultural preservation. Then compose with /speech-writer. [Source: cultural-diversity.md, BAAs 1-2, 7, 20, 39]

---

A wrong BAA number, BOL article, or official title is 3x worse than writing [UNVERIFIED]. When in doubt, mark it.

## Gotchas

- Mas Matatag na Bangsamoro Agenda (2026-2028) replaces the 12-Point Priority Agenda as of OCM EO No. 2, s. 2026 — all references must be updated
- BANNED: "Exclusive/Shared/Concurrent" as power labels — use only BOL language (enumerated powers under Art. IX S1-3, reserved/residual powers, national law consistency)
- Never cite BARMM guidebooks as primary sources for factual claims — they are in development and may contain errors
- Official titles and positions change with each BTA transition — always verify against the officials reference file, not training data
- BOL has 5 chapter files in the local transcription — always load the relevant chapter before citing specific articles
- "Bangsamoro" refers to the people AND the region — context determines which; the autonomous region is officially "Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)"
- A wrong BAA number, BOL article, or official title is 3x worse than writing [UNVERIFIED]. When in doubt, mark it.

## Error Handling

| Situation | Response |
|-----------|----------|
| **Question about post-2022 events** | Note that 2nd BDP data covers 2020-2022. For recent developments, use WebSearch or suggest the user provide current data. |
| **Sulu-specific query** | Provide data but caveat with SC ruling status. Note that BARMM still considers Sulu part of its territory pending MR resolution. |
| **Question outside knowledge domains** | Acknowledge the limit: "This is outside /bangsamoro's reference data. Consider /deep-research or /legal-assistant for [topic]." |
| **Conflicting data between sources** | Prefer: BOL (legal authority) > BAA (enacted law) > BDP (planning) > reference files (summarized). Note the conflict. |
| **Missing reference file** | Fall back to Quick Reference data. Flag that the full reference was unavailable. |
| **BAA not in quick-reference** | Read `~/Vault/bangsamoro/bangsamoro-laws/INDEX.md` or Grep the vault archive. All 89 BAAs have verified markdown transcriptions. |
| **Resolution not in classification** | Grep `~/Vault/bangsamoro/bangsamoro-resolutions/INDEX.md` for keywords. ~200+ are routine condolences/commendations. |
| **Batch query (list all X)** | Use the relevant category table. For exhaustive lists, read the vault index file. Cap at 20 items per response; offer to continue. |

---

## Integration with Other Skills

| Related Skill | When to Use Together |
|---------------|---------------------|
| `/bill-drafter` | Drafting bills — use /bangsamoro for governance context, agency mandates, BOL provisions, existing BAAs on the topic |
| `/resolution-drafter` | Drafting resolutions — use /bangsamoro for policy context, parliamentary procedures, related resolutions |
| `/legislative-briefer` | CSW briefers — use /bangsamoro for impact assessment context, Shari'ah analysis, BDP alignment |
| `/speech-writer` | Parliamentary speeches — use /bangsamoro for Bangsamoro themes, cultural identity, development goals |
| `/policy-recommendation` | OOBC and BARMM policy — use /bangsamoro for governance framework and development priorities |
| `/legal-assistant` | Legal analysis — use /bangsamoro for BOL provisions, BAA references, constitutional context |

---

## Key Terms Glossary

| Term | Definition |
|------|------------|
| **BARMM** | Bangsamoro Autonomous Region in Muslim Mindanao |
| **BOL** | Bangsamoro Organic Law (RA 11054) — the foundational law |
| **BTA** | Bangsamoro Transition Authority (interim government until elections) |
| **CAB** | Comprehensive Agreement on the Bangsamoro (2014) |
| **FAB** | Framework Agreement on the Bangsamoro (2012) |
| **BAA** | Bangsamoro Autonomy Act (regional legislation enacted by BTA Parliament) |
| **BAA No. 13** | Bangsamoro Administrative Code — establishes government structure |
| **BAA No. 17** | Bangsamoro Civil Service Code |
| **BAA No. 18** | Bangsamoro Education Code |
| **BAA No. 35** | Bangsamoro Electoral Code |
| **BAA No. 49** | Bangsamoro Local Governance Code |
| **BAA No. 82** | Bangsamoro Labor and Employment Code (Jan 2026) |
| **BAA No. 86** | Parliamentary District Act — 32 districts (Jan 2026) |
| **BAA No. 89** | Bangsamoro Transitional Justice and Reconciliation Program (Feb 2026) |
| **BDP** | Bangsamoro Development Plan (current: 2nd BDP 2023-2028) |
| **MILF** | Moro Islamic Liberation Front |
| **MNLF** | Moro National Liberation Front |
| **Rido** | Clan feuding/family feuds — a major peace and security concern |
| **Tarsila** | Traditional genealogical records (often in Jawi script) |
| **Moral Governance** | Centerpiece governance philosophy of BARMM (12 pillars) |
| **MOA** | Ministries, Offices, and Agencies |
| **OCM** | Office of the Chief Minister |
| **BPDA** | Bangsamoro Planning and Development Authority |
| **BEDC** | Bangsamoro Economic and Development Council |
| **BaSulTa** | Basilan-Sulu-Tawi-Tawi (island provinces) |
| **SGA** | Special Geographic Area (63 barangays from North Cotabato that joined BARMM) |
| **GAA** | General Appropriations Act (annual budget law) |
| **SDF** | Special Development Fund (PHP 5B/year for 10 years per BOL Art. XII) |
| **IDP** | Internally Displaced Person |
| **DDR** | Disarmament, Demobilization, and Reintegration |
