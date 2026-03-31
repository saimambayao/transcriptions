---
name: resolution
description: Resolution drafting skill for OBCMS - Other Bangsamoro Communities Management System. Draft legislative resolutions for OBC communities to be filed in the Bangsamoro Parliament, Philippine Congress, or LGU Sanggunians. Use for expressing positions, commendations, requests, or investigations related to OBCs.
argument-hint: "[topic]"
---

# Resolution Drafting for OBC Legislative Advocacy

```
+==============================================================================+
|  GATE: INVOKE /prompter IMMEDIATELY                                          |
+==============================================================================+
|                                                                              |
|  DO NOT read further. DO NOT proceed with any workflow.                      |
|                                                                              |
|  ACTION REQUIRED NOW:                                                        |
|  1. INVOKE /prompter with the user's resolution drafting request             |
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

Draft legislative resolutions advocating for Other Bangsamoro Communities (OBCs) in Regions IX, X, XI, and XII. Resolutions can be filed in:

| Legislative Body | Jurisdiction | Examples |
|-----------------|--------------|----------|
| **Bangsamoro Parliament (BTA)** | BARMM positions on OBC matters | Urging executive action on OBC programs |
| **Philippine Congress** | National positions on OBCs | Recognizing OBC contributions, requesting investigations |
| **Provincial Sanggunian** | Provincial positions | Endorsing OBC programs, expressing support |
| **Municipal/City Sanggunian** | Municipal positions | Local OBC recognition, commendations |
| **Barangay Council** | Barangay positions | Community-level support for OBCs |

---

## Resolution Types

| Type | Purpose | Example Use |
|------|---------|-------------|
| **Simple Resolution** | Express position of one chamber | Parliament position on OBC welfare |
| **Joint Resolution** | Express position of both chambers | Bicameral support for OBC legislation |
| **Concurrent Resolution** | Internal rules, non-binding | Creating joint OBC committees |
| **Commendation Resolution** | Recognize achievements | Honor OBC community leaders |
| **Request Resolution** | Request executive action | Urge OOBC funding increase |
| **Investigation Resolution** | Call for inquiry | Investigate OBC service gaps |

---

## When to Use

| Scenario | Action |
|----------|--------|
| Expressing legislative support for OBCs | Use directly |
| Commending OBC community achievements | Use directly |
| Requesting executive action on OBC matters | Use directly |
| Calling for investigations on OBC issues | Use directly |
| Endorsing OBC programs and initiatives | Use directly |
| Building resolution features in OBCMS | Use with `/featuredev` |

---

## Quick Reference

### Resolution Structure (Philippine Legislative Format)

```
REPUBLIC OF THE PHILIPPINES
[LEGISLATIVE BODY]
[Session Information]

[RESOLUTION TYPE] NO. ____

[TITLE - e.g., "A RESOLUTION EXPRESSING SUPPORT FOR..."]

WHEREAS, [recital 1 - background/context];

WHEREAS, [recital 2 - facts/circumstances];

WHEREAS, [recital 3 - rationale/justification];

WHEREAS, [recital 4 - additional considerations];

NOW, THEREFORE, BE IT RESOLVED, AS IT IS HEREBY RESOLVED, [operative clause - main action];

RESOLVED FURTHER, [additional operative clauses if needed];

RESOLVED FINALLY, That copies of this Resolution be furnished to [recipients].

Adopted,

[Date]
[Signatures]
```

---

## Workflow 1: Resolution Drafting Mode

### Step 1: Determine Resolution Type

| Type | Use When | Key Elements |
|------|----------|--------------|
| **Commendation** | Recognizing OBC achievements | Achievements, contributions, impact |
| **Support/Endorsement** | Backing OBC initiatives | Program details, benefits, alignment |
| **Request** | Urging executive action | Current situation, desired action, rationale |
| **Investigation** | Calling for inquiry | Issues, concerns, scope of inquiry |
| **Position** | Expressing stance on OBC matters | Issue, position, reasoning |

### Step 2: Gather Information

**For Commendation Resolutions:**
```
[ ] Full name and title of honoree(s)
[ ] Specific achievements being recognized
[ ] Impact on OBC communities
[ ] Dates and locations of achievements
[ ] Supporting facts and figures
```

**For Request Resolutions:**
```
[ ] Current situation description
[ ] Specific action being requested
[ ] Responsible agency/official
[ ] Timeline if applicable
[ ] Expected outcomes
```

**For Investigation Resolutions:**
```
[ ] Issue or problem to investigate
[ ] Scope of investigation
[ ] Committee to conduct inquiry
[ ] Expected deliverables
[ ] Timeline for completion
```

### Step 3: Draft Components

**WHEREAS Clauses (Recitals):**
- Establish context and background
- Present facts and circumstances
- Build logical case for resolution
- Reference legal basis if applicable

**RESOLVED Clauses (Operative):**
- State the main action or position
- Be clear and specific
- Include all necessary details
- Specify recipients for copies

### Step 4: Review and Validate

```
[ ] Purpose clearly stated
[ ] Recitals build logical case
[ ] Operative clauses are specific
[ ] Proper legislative format
[ ] Names and titles accurate
[ ] Dates and facts verified
[ ] Recipients for copies identified
```

---

## OBC-Specific Resolution Topics

### Priority Resolution Areas for OBCs

| Area | Purpose | Example Resolutions |
|------|---------|-------------------|
| **Recognition** | Recognize OBC communities and leaders | Commending OBC community leaders |
| **Support** | Express support for OBC programs | Endorsing OOBC initiatives |
| **Funding** | Request funding for OBC services | Urging budget allocation for OOBC |
| **Services** | Call for improved OBC services | Requesting LGU OBC assistance centers |
| **Investigation** | Investigate OBC issues | Inquiry into OBC service gaps |
| **Cultural** | Celebrate OBC heritage | Recognizing Bangsamoro cultural events |
| **Education** | Support OBC education | Endorsing OBC scholarship programs |
| **Coordination** | Improve OBC coordination | Urging inter-agency OBC collaboration |

### Sample Resolution Titles for OBC Advocacy

**For Bangsamoro Parliament:**
- "A Resolution Urging the Chief Minister to Increase Funding for the Office for Other Bangsamoro Communities"
- "A Resolution Commending the OOBC for Its Outstanding Service to OBCs in Regions IX, X, XI, and XII"
- "A Resolution Requesting an Investigation into the Needs of Other Bangsamoro Communities"

**For Philippine Congress:**
- "A Resolution Expressing Support for the Recognition of Other Bangsamoro Communities Nationwide"
- "A Resolution Commending Bangsamoro Communities Outside BARMM for Their Contributions to National Development"

**For LGU Sanggunians:**
- "A Resolution Endorsing the Establishment of an OBC Assistance Center in [Province/City/Municipality]"
- "A Resolution Commending [Name] for Outstanding Leadership in the OBC Community"
- "A Resolution Requesting the Municipal Mayor to Allocate Funds for OBC Livelihood Programs"

---

## Workflow 2: Commendation Resolution Mode

For recognizing OBC community achievements:

### Commendation Resolution Template

```
REPUBLIC OF THE PHILIPPINES
[LEGISLATIVE BODY]
[Session]

RESOLUTION NO. ____

A RESOLUTION COMMENDING [NAME/ORGANIZATION] FOR [ACHIEVEMENT]

WHEREAS, [background on the honoree];

WHEREAS, [specific achievements being recognized];

WHEREAS, [impact on OBC communities];

WHEREAS, [the legislative body] recognizes the importance of honoring individuals/organizations who contribute to the welfare of Other Bangsamoro Communities;

NOW, THEREFORE, BE IT RESOLVED, AS IT IS HEREBY RESOLVED, That [Legislative Body] hereby commends [Name/Organization] for [achievement];

RESOLVED FURTHER, That [Name/Organization] is hereby recognized for [specific contributions];

RESOLVED FINALLY, That copies of this Resolution be furnished to [honoree], the Office for Other Bangsamoro Communities, and other concerned agencies.

Adopted,

[Date]
```

---

## Workflow 3: Request Resolution Mode

For urging executive action on OBC matters:

### Request Resolution Template

```
REPUBLIC OF THE PHILIPPINES
[LEGISLATIVE BODY]
[Session]

RESOLUTION NO. ____

A RESOLUTION URGING [OFFICIAL/AGENCY] TO [ACTION] FOR THE BENEFIT OF OTHER BANGSAMORO COMMUNITIES

WHEREAS, Other Bangsamoro Communities (OBCs) in Regions IX, X, XI, and XII [current situation];

WHEREAS, [specific issue or need];

WHEREAS, [rationale for requested action];

WHEREAS, [legal/policy basis if applicable];

NOW, THEREFORE, BE IT RESOLVED, AS IT IS HEREBY RESOLVED, That [Legislative Body] hereby urges [Official/Agency] to [specific action requested];

RESOLVED FURTHER, That [additional actions if needed];

RESOLVED FINALLY, That copies of this Resolution be furnished to [Official/Agency], the Office for Other Bangsamoro Communities, and other concerned parties.

Adopted,

[Date]
```

---

## Legal References

| Reference | Relevance |
|-----------|-----------|
| **RA 11054 (BOL)** | BARMM governance, OOBC mandate |
| **1987 Constitution** | Legislative powers |
| **RA 7160 (LGC)** | LGU legislative authority |
| **Parliamentary Rules** | Resolution procedures for BTA |
| **Congress Rules** | House and Senate procedures |

---

## Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| `/bill` | Draft accompanying legislation |
| `/coordination` | Coordinate with legislative sponsors |
| `/communities` | Research OBC community data |
| `/mana` | Use MANA findings to support resolutions |
| `/governance` | Ensure good governance principles |
| `/deep-research` | Research precedents and best practices |

---

## Output Format

When drafting resolutions, provide:

1. **Complete resolution text** in proper legislative format
2. **Explanatory note** if needed
3. **Background brief** explaining the context
4. **Stakeholder list** for furnishing copies
5. **Suggested sponsors** in the legislative body

---

*This skill supports OBCMS's mission to advocate for Other Bangsamoro Communities through legislative resolutions at all levels of government.*
