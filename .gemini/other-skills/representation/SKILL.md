---
name: representation
description: Representation work domain skill for e-Bangsamoro. Covers constituent services, case management, district engagement, and MP representation duties. Use when implementing constituent tracking, case management, or community engagement features.
argument-hint: "[topic]"
---

# Representation Work - e-Bangsamoro

## Purpose
Provides domain expertise for the Representation Work module of e-Bangsamoro, covering MP duties in representing constituents and managing district affairs in the Bangsamoro Autonomous Region in Muslim Mindanao (BARMM).

## When to Use
- Implementing constituent service tracking
- Building case management systems
- Creating district engagement features
- Implementing feedback collection systems
- Designing community outreach tools
- Developing barangay coordination interfaces
- Creating constituent request workflows

## Key Entities

### Core Entities
- **Constituent**: Registered constituents from BARMM districts
- **Case**: Constituent cases/requests requiring MP intervention
- **District**: Parliamentary districts within BARMM
- **Barangay**: Local community units within districts
- **Engagement**: Community engagement records and events
- **Feedback**: Constituent feedback and satisfaction records
- **ServiceRequest**: Formal requests for assistance

### Supporting Entities
- **CaseNote**: Notes and updates on case progress
- **CaseAssignment**: Staff assigned to handle cases
- **EngagementAttendee**: Participants in community events
- **ReferralAgency**: Government agencies for case referrals

## Case Lifecycle

```
1. Received     - Initial submission of case/request
2. Acknowledged - Confirmation sent to constituent
3. Assessed     - Case evaluated and categorized
4. Assigned     - Staff member assigned to handle
5. In Progress  - Active work on resolution
6. Pending      - Awaiting external input/agency response
7. Resolved     - Solution implemented
8. Closed       - Case formally closed with feedback
```

## Service Types

### Assistance Categories
- **Financial Assistance** - Emergency aid, educational support, medical assistance
- **Livelihood Support** - Skills training, business assistance, employment referrals
- **Health Services** - Medical referrals, PHILHEALTH assistance, hospital coordination
- **Educational Support** - Scholarship referrals, school enrollment, TESDA coordination
- **Legal Assistance** - Legal aid referrals, document assistance, dispute mediation
- **Infrastructure Requests** - Road repairs, water systems, community facilities

### Administrative Services
- **Document Assistance** - Certification, endorsement letters, recommendations
- **Information Requests** - Government program inquiries, process guidance
- **Complaint Resolution** - Service delivery complaints, agency coordination
- **Referrals to Agencies** - DSWD, DOLE, DTI, and other national/regional agencies

### Community Projects
- **Barangay Development** - Small infrastructure, community facilities
- **Peace and Order** - Security concerns, conflict resolution referrals
- **Disaster Response** - Emergency coordination, relief operations

## Priority Levels

| Priority | Response Time | Description |
|----------|---------------|-------------|
| Critical | 24 hours | Life-threatening, emergency situations |
| High | 3 days | Urgent needs, time-sensitive matters |
| Medium | 7 days | Standard requests, routine assistance |
| Low | 14 days | Information requests, non-urgent matters |

## District Structure (BARMM)

### Parliamentary Districts
- Lanao del Sur 1st District
- Lanao del Sur 2nd District
- Maguindanao 1st District
- Maguindanao 2nd District
- Basilan District (including Isabela City)
- Sulu District
- Tawi-Tawi District
- Cotabato City District

### Geographic Hierarchy
```
Region (BARMM)
  +-- Province/City
      +-- Municipality
          +-- Barangay
              +-- Purok/Sitio
```

## Constituent Data Model

### Required Fields
- Full Name (First, Middle, Last, Suffix)
- Date of Birth
- Gender
- Contact Information (Phone, Email if available)
- Complete Address (Barangay, Municipality, Province)
- District Assignment

### Optional Fields
- Voter Registration Status
- Occupation
- Household Information
- Previous Cases/Interactions
- Special Categories (PWD, Senior, Solo Parent, IP)

## Integration Points

### Internal Systems
- **Legislative Work** - Bills affecting constituents
- **Oversight Work** - Agency performance monitoring
- **Budget Management** - Allocation for constituent services
- **Office Management** - Staff assignment and scheduling

### External Systems
- DSWD Systems - Social welfare referrals
- PHILHEALTH - Health insurance verification
- DOLE - Employment assistance
- DTI - Business registration and support
- TESDA - Skills training programs
- LGU Systems - Local government coordination

## Reporting Requirements

### Regular Reports
- Weekly Case Summary
- Monthly Constituent Services Report
- Quarterly District Engagement Report
- Annual Representation Performance Report

### Key Metrics
- Cases received vs resolved
- Average resolution time
- Constituent satisfaction rate
- Service type distribution
- Geographic distribution of cases
- Response time compliance

## Reference Files
- [constituent-services.md](references/constituent-services.md) - Service delivery procedures
- [case-management.md](references/case-management.md) - Case handling workflows
- [district-engagement.md](references/district-engagement.md) - Community engagement practices

## UI/UX Considerations

### Dashboard Elements
- Case status overview (pie/bar chart)
- Recent cases list
- Pending actions queue
- District map with case distribution
- Quick action buttons for common tasks

### Form Design
- Progressive disclosure for constituent registration
- Smart address selection (Province > Municipality > Barangay)
- Document upload for supporting files
- Mobile-responsive for field staff

### Accessibility
- Support for Tagalog/Filipino language
- Offline capability for remote areas
- SMS notification integration
- Simple interface for non-technical staff
