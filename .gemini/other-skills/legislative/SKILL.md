---
name: legislative
description: Legislative work domain skill for e-Bangsamoro. Covers bill drafting, resolution management, committee work, voting procedures, and parliamentary processes. Use when implementing legislative features, bill tracking, committee management, or voting systems.
argument-hint: "[topic]"
---

# Legislative Work - e-Bangsamoro

## Purpose
Provides domain expertise for the Legislative Work module of e-Bangsamoro, covering bills, resolutions, committee work, and parliamentary procedures for the Bangsamoro Parliament.

## When to Use
- Implementing bill drafting and tracking features
- Building resolution management systems
- Creating committee work interfaces
- Implementing voting and deliberation features
- Designing legislative document workflows

## Key Entities
- **Bill**: Proposed legislation with lifecycle stages
- **Resolution**: Non-binding legislative actions
- **Committee**: Groups handling specific legislative areas
- **Session**: Parliamentary session records
- **Vote**: Voting records on bills/resolutions
- **Amendment**: Proposed changes to bills

## Bill Lifecycle
1. Draft -> Filed -> First Reading -> Committee Referral -> Second Reading -> Deliberation -> Third Reading -> Approval -> Transmittal

## Reference Files
- [bill-lifecycle.md](references/bill-lifecycle.md) - Detailed bill stages and transitions
- [resolution-types.md](references/resolution-types.md) - Types of resolutions and procedures
- [committee-procedures.md](references/committee-procedures.md) - Committee organization and work

## Bangsamoro Parliament Context

### Legal Framework
The Bangsamoro Parliament operates under the Bangsamoro Organic Law (BOL), Republic Act No. 11054, which established the Bangsamoro Autonomous Region in Muslim Mindanao (BARMM).

### Parliament Composition
- 80 Members of Parliament (MPs)
- Speaker of the Parliament (presiding officer)
- Deputy Speakers
- Majority and Minority Floor Leaders

### Types of Legislation
1. **Bills (Bangsamoro Parliamentary Acts)** - Proposed laws requiring passage through readings
2. **Resolutions** - Expressions of parliament sentiment or internal rules
3. **Ordinances** - Local regulatory measures

## Data Models Overview

### Bill Model
```python
class Bill(BaseModel):
    """Legislative bill in the Bangsamoro Parliament."""
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)
    number = models.CharField(max_length=50)  # e.g., "BPA-001-2024"
    title = models.CharField(max_length=500)
    summary = models.TextField(blank=True)
    full_text = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=BILL_STATUS_CHOICES)

    # Authorship
    principal_author = models.ForeignKey('accounts.User', related_name='authored_bills')
    co_authors = models.ManyToManyField('accounts.User', related_name='coauthored_bills')

    # Tracking
    filed_date = models.DateField(null=True)
    committee = models.ForeignKey('Committee', null=True)
    session = models.ForeignKey('Session', null=True)

    # Workflow
    current_reading = models.IntegerField(default=0)  # 0=not yet, 1-3=reading number
    approved_date = models.DateField(null=True)
    transmitted_date = models.DateField(null=True)
```

### Resolution Model
```python
class Resolution(BaseModel):
    """Parliamentary resolution."""
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)
    number = models.CharField(max_length=50)  # e.g., "PR-001-2024"
    title = models.CharField(max_length=500)
    type = models.CharField(max_length=30, choices=RESOLUTION_TYPE_CHOICES)
    content = models.TextField()

    author = models.ForeignKey('accounts.User', related_name='authored_resolutions')
    status = models.CharField(max_length=20, choices=RESOLUTION_STATUS_CHOICES)
    adopted_date = models.DateField(null=True)
```

### Committee Model
```python
class Committee(BaseModel):
    """Standing or special committee."""
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)  # e.g., "APPROP", "RULES"
    type = models.CharField(max_length=20, choices=COMMITTEE_TYPE_CHOICES)
    description = models.TextField(blank=True)

    chairperson = models.ForeignKey('accounts.User', related_name='chaired_committees')
    vice_chairperson = models.ForeignKey('accounts.User', related_name='vice_chaired_committees')
    members = models.ManyToManyField('accounts.User', through='CommitteeMembership')
```

### Session Model
```python
class Session(BaseModel):
    """Parliamentary session."""
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g., "1st Regular Session"
    session_number = models.IntegerField()
    session_type = models.CharField(max_length=20)  # regular, special

    start_date = models.DateField()
    end_date = models.DateField(null=True)
    is_current = models.BooleanField(default=False)
```

### Vote Model
```python
class Vote(BaseModel):
    """Voting record on bills/resolutions."""
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)

    # Can vote on bill or resolution
    bill = models.ForeignKey('Bill', null=True, on_delete=models.CASCADE)
    resolution = models.ForeignKey('Resolution', null=True, on_delete=models.CASCADE)

    vote_type = models.CharField(max_length=20)  # voice, division, nominal
    vote_date = models.DateTimeField()

    # Results
    ayes = models.IntegerField(default=0)
    nays = models.IntegerField(default=0)
    abstentions = models.IntegerField(default=0)
    result = models.CharField(max_length=20)  # passed, failed, deferred
```

## API Endpoints

### Bills API
```
GET    /api/v1/bills/              # List bills (filterable)
POST   /api/v1/bills/              # Create new bill
GET    /api/v1/bills/{id}/         # Get bill details
PUT    /api/v1/bills/{id}/         # Update bill
DELETE /api/v1/bills/{id}/         # Soft delete bill

# Custom actions
POST   /api/v1/bills/{id}/file/              # File bill (draft -> filed)
POST   /api/v1/bills/{id}/advance-reading/   # Advance to next reading
POST   /api/v1/bills/{id}/refer-committee/   # Refer to committee
POST   /api/v1/bills/{id}/approve/           # Approve bill
POST   /api/v1/bills/{id}/transmit/          # Transmit to Chief Minister
```

### Resolutions API
```
GET    /api/v1/resolutions/        # List resolutions
POST   /api/v1/resolutions/        # Create resolution
GET    /api/v1/resolutions/{id}/   # Get resolution details
PUT    /api/v1/resolutions/{id}/   # Update resolution
POST   /api/v1/resolutions/{id}/adopt/  # Adopt resolution
```

### Committees API
```
GET    /api/v1/committees/         # List committees
GET    /api/v1/committees/{id}/    # Get committee details
GET    /api/v1/committees/{id}/bills/  # Bills referred to committee
GET    /api/v1/committees/{id}/members/  # Committee members
```

### Sessions API
```
GET    /api/v1/sessions/           # List sessions
GET    /api/v1/sessions/current/   # Get current session
GET    /api/v1/sessions/{id}/agenda/  # Session agenda
```

### Votes API
```
GET    /api/v1/votes/              # List votes
POST   /api/v1/votes/              # Record vote
GET    /api/v1/votes/{id}/         # Vote details
```

## Frontend Components

### Bill Management
- `BillList` - Paginated list with filters (status, committee, session)
- `BillDetail` - Full bill view with timeline
- `BillForm` - Create/edit bill form
- `BillTimeline` - Visual lifecycle progress
- `BillActions` - Workflow action buttons

### Resolution Management
- `ResolutionList` - Resolution listing
- `ResolutionDetail` - Resolution view
- `ResolutionForm` - Create/edit form

### Committee Work
- `CommitteeList` - Committee directory
- `CommitteeDetail` - Committee info and members
- `CommitteeAgenda` - Meeting agenda
- `CommitteeReport` - Committee reports on bills

### Session Management
- `SessionList` - Sessions overview
- `SessionAgenda` - Current session agenda
- `SessionCalendar` - Session calendar view

### Voting
- `VotingPanel` - Real-time voting interface
- `VoteResults` - Vote outcome display
- `VoteHistory` - Historical voting records

## Business Rules

### Bill Filing Requirements
- Must have a title and summary
- Must have at least one author
- Number auto-generated based on session and sequence
- Author must be an MP

### Reading Advancement Rules
1. **First Reading** - Automatic after filing
2. **Second Reading** - Requires committee report
3. **Third Reading** - Requires approval in Second Reading deliberation

### Voting Thresholds
- Simple majority (50%+1) for regular bills
- Supermajority (2/3) for constitutional matters
- Quorum required: Majority of MPs present

### Committee Rules
- Each bill referred to at least one committee
- Committee must submit report within 60 days
- Chairperson can request extension

## Integration Points

### With Budget Module
- Appropriation bills linked to budget allocations
- Budget review committee coordination

### With Ministerial Module
- Bills implementing 10-point agenda
- Ministry consultation on technical bills

### With Office Module
- MP staff access to bill drafting
- Committee secretary assignments

## Permission Levels

| Role | Permissions |
|------|-------------|
| Public | View enacted bills, resolutions |
| MP | Author, vote, amend bills |
| Committee Chair | Manage committee agenda, reports |
| Speaker | Advance readings, call votes |
| Admin | Full access to legislative data |
