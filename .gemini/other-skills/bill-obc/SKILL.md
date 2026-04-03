---
name: bill
description: Bill drafting skill for OBCMS - Other Bangsamoro Communities Management System. Draft legislative bills for OBC communities to be filed in the Bangsamoro Parliament, Philippine Congress, or LGU Sanggunians. Use when advocating for OBC rights, services, or programs through legislation.
argument-hint: "[topic]"
---

# Bill Drafting for OBC Legislative Advocacy

```
+==============================================================================+
|  GATE: INVOKE /prompter IMMEDIATELY                                          |
+==============================================================================+
|                                                                              |
|  DO NOT read further. DO NOT proceed with any workflow.                      |
|                                                                              |
|  ACTION REQUIRED NOW:                                                        |
|  1. INVOKE /prompter with the user's bill drafting request                   |
|  2. WAIT for /prompter to complete its 5-phase workflow                      |
|  3. WAIT for user confirmation ("Yes, proceed")                              |
|  4. ONLY THEN return here and continue below                                 |
|                                                                              |
|  If user says "No" or "Adjust" -> repeat /prompter                           |
|  If user says "Let me rephrase" -> restart with new input                    |
|                                                                              |
+==============================================================================+
```

---

## Purpose

Draft legislative bills advocating for Other Bangsamoro Communities (OBCs) in Regions IX, X, XI, and XII. Bills can be filed in:

| Legislative Body | Jurisdiction | Examples |
|-----------------|--------------|----------|
| **Bangsamoro Parliament (BTA)** | BARMM policies affecting OBCs | OBC inclusion programs, OOBC mandate expansion |
| **Philippine Congress** | National laws benefiting OBCs | National OBC recognition, funding allocations |
| **Provincial Sanggunian** | Provincial ordinances | Provincial OBC coordination offices |
| **Municipal/City Sanggunian** | Municipal ordinances | Local OBC assistance programs |
| **Barangay Council** | Barangay resolutions | Community-level OBC support |

---

## When to Use

| Scenario | Action |
|----------|--------|
| Drafting bills for OBC programs | Use directly |
| Advocating OBC rights in legislation | Use directly |
| Preparing legislative proposals for OOBC | Use directly |
| Creating model ordinances for LGUs | Use directly |
| Building bill drafting features in OBCMS | Use with `/featuredev` |

---

## Quick Reference

### Bill Structure (Philippine Legislative Format)

```
REPUBLIC OF THE PHILIPPINES
[LEGISLATIVE BODY]
[Session Information]

[BILL TYPE] NO. ____

AN ACT [TITLE IN ALL CAPS DESCRIBING THE BILL'S PURPOSE]

Be it enacted by [Legislative Body]:

SECTION 1. Short Title. - This Act shall be known as the "[Short Title]."

SECTION 2. Declaration of Policy. - [Policy statement]

SECTION 3. Definition of Terms. - As used in this Act:
   (a) "[Term]" refers to [definition];
   (b) "[Term]" refers to [definition];

SECTION 4. [Substantive Provisions]

SECTION 5. [Additional Provisions]

SECTION 6. Appropriations. - [Funding provisions if applicable]

SECTION 7. Implementing Rules and Regulations. - [IRR provision]

SECTION 8. Separability Clause. - [Standard separability clause]

SECTION 9. Repealing Clause. - [Repealing provisions]

SECTION 10. Effectivity. - This Act shall take effect [effectivity date].

Approved,
```

---

## Workflow 1: Bill Drafting Mode

### Step 1: Determine Legislative Body

| Body | Use When | Key Considerations |
|------|----------|-------------------|
| **Bangsamoro Parliament** | OBC matters within BARMM jurisdiction | BOL alignment, BARMM context |
| **Philippine Congress** | National-level OBC legislation | Constitutional alignment, nationwide impact |
| **Provincial Sanggunian** | Province-wide OBC programs | Local Government Code, provincial scope |
| **Municipal Sanggunian** | City/municipality OBC programs | Local Government Code, municipal scope |
| **Barangay Council** | Barangay-level OBC support | Barangay powers, community scope |

### Step 2: Define Bill Purpose

Common OBC bill purposes:

| Category | Example Purposes |
|----------|-----------------|
| **Recognition** | Formal recognition of OBC communities |
| **Services** | Establish OBC service centers, assistance programs |
| **Coordination** | Create OBC coordination offices in LGUs |
| **Funding** | Allocate funds for OBC programs |
| **Rights** | Protect OBC community rights |
| **Culture** | Preserve Bangsamoro cultural heritage outside BARMM |
| **Education** | Educational support for OBC students |
| **Livelihood** | Economic development programs for OBCs |

### Step 3: Draft Components

**Required Components:**
1. **Title** - Clear, descriptive title
2. **Declaration of Policy** - Policy rationale
3. **Definition of Terms** - Key terms defined
4. **Substantive Provisions** - Main content
5. **Implementing Mechanism** - How it will be implemented
6. **Funding** - Appropriations if needed
7. **Standard Clauses** - Separability, repealing, effectivity

### Step 4: Review and Validate

```
[ ] Aligned with BOL (RA 11054) if for Parliament
[ ] Constitutional alignment if for Congress
[ ] Local Government Code compliance if for LGU
[ ] Clear policy rationale stated
[ ] Terms properly defined
[ ] Implementable provisions
[ ] Funding source identified
[ ] No conflicting laws
[ ] Proper legal format followed
```

---

## Workflow 2: Model Ordinance Mode

For creating model ordinances that LGUs can adapt:

### Model Ordinance Template

```
ORDINANCE NO. ____
Series of ____

AN ORDINANCE [TITLE]

WHEREAS, [recital 1];
WHEREAS, [recital 2];
WHEREAS, [recital 3];

NOW, THEREFORE, be it ordained by the Sangguniang [Panlalawigan/Panlungsod/Bayan] of [LGU Name]:

SECTION 1. Title. - This Ordinance shall be known as the "[Short Title]."

SECTION 2. Purpose. - [Purpose statement]

SECTION 3. Definition of Terms. - [Definitions]

SECTION 4. [Substantive provisions]

SECTION 5. Funding. - [Funding source]

SECTION 6. Penalties. - [If applicable]

SECTION 7. Effectivity. - This Ordinance shall take effect [effectivity].

ENACTED: [Date]
APPROVED: [Date]

[Signatures]
```

---

## OBC-Specific Bill Topics

### Priority Legislative Areas for OBCs

| Area | Purpose | Target Body |
|------|---------|-------------|
| **OBC Recognition Act** | National recognition of OBC status | Congress |
| **OOBC Strengthening** | Enhance OOBC mandate and resources | Parliament |
| **Regional OBC Offices** | Establish OBC coordination in Regions IX-XII | Provincial Sanggunians |
| **OBC Education Support** | Scholarships and educational programs | Congress, LGUs |
| **Cultural Preservation** | Bangsamoro heritage outside BARMM | Congress, LGUs |
| **Livelihood Programs** | Economic support for OBC communities | LGUs |
| **Anti-Discrimination** | Protect OBCs from discrimination | Congress |
| **Social Services Access** | Ensure OBC access to government services | LGUs |

### Sample Bill Titles for OBC Advocacy

**For Congress:**
- "An Act Recognizing Other Bangsamoro Communities and Providing for Their Welfare"
- "An Act Establishing Regional Coordination Offices for Other Bangsamoro Communities"
- "An Act Providing Educational Scholarships for Other Bangsamoro Communities"

**For Bangsamoro Parliament:**
- "An Act Strengthening the Office for Other Bangsamoro Communities"
- "An Act Expanding OOBC Programs to Reach More OBCs in Regions IX, X, XI, and XII"

**For LGU Sanggunians:**
- "An Ordinance Creating the [Province/City/Municipality] OBC Assistance Center"
- "An Ordinance Providing Livelihood Support to Other Bangsamoro Communities"

---

## Legal References

| Reference | Relevance |
|-----------|-----------|
| **RA 11054 (BOL)** | BARMM governance, OOBC mandate |
| **1987 Constitution** | National legislative framework |
| **RA 7160 (LGC)** | LGU legislative powers |
| **RA 8371 (IPRA)** | Indigenous peoples' rights (some OBCs may qualify) |

---

## Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| `/resolution` | Draft supporting resolutions |
| `/coordination` | Coordinate with legislative advocates |
| `/communities` | Research OBC community needs for bills |
| `/mana` | Use MANA data to support legislative proposals |
| `/governance` | Ensure good governance principles |
| `/deep-research` | Research legal precedents and best practices |

---

## Output Format

When drafting bills, provide:

1. **Complete bill text** in proper legislative format
2. **Explanatory note** summarizing the bill's purpose
3. **Policy brief** explaining the need for the legislation
4. **Stakeholder analysis** identifying supporters and potential opponents
5. **Implementation considerations** for the executive branch

---

*This skill supports OBCMS's mission to advocate for Other Bangsamoro Communities through legislative channels at all levels of government.*
