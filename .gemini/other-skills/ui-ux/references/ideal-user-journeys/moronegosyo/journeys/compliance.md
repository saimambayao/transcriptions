# Compliance Submission Journey - MoroNegosyo

## Overview

This journey maps the complete compliance submission experience for tenant managers on MoroNegosyo, focusing on STEPS (Social Enterprise) and PESOS (Cooperative) compliance frameworks under CSEA's FRAMES regulatory system. The journey emphasizes clarity in requirements, guided document submission, and transparent review processes.

## Persona

**Name**: Miguel Pangandaman
**Age**: 50
**Role**: Cooperative Treasurer
**Location**: Jolo, Sulu
**Context**: Miguel is the treasurer of the Jolo Farmers Cooperative, responsible for financial reporting and regulatory compliance. He has been with the cooperative for 15 years and handles annual submissions to CSEA. He is detail-oriented but finds digital systems challenging. He works primarily from a desktop computer at the cooperative office.

**Goals**:
- Submit all required compliance documents on time
- Avoid rejection due to missing or incorrect documents
- Maintain the cooperative's good standing with CSEA
- Understand what documents are needed before deadlines
- Get clear feedback on submission status

**Tech Comfort**: Low-moderate - can use basic computer applications
**Connectivity**: Moderate 3G/4G in Jolo town center
**Document Skills**: Good with financial documents, less so with scanning

---

## Journey Map

### Stage 1: Compliance Awareness

**User Goal**: Understand upcoming compliance requirements before deadlines

**Actions**:
1. Miguel logs into the portal dashboard
2. Sees compliance status widget on dashboard
3. Notes upcoming deadline alerts
4. Navigates to Compliance section
5. Reviews FRAMES compliance overview
6. Identifies which submissions are due

**Touchpoints**:
- Dashboard compliance widget
- Deadline alert banners
- Compliance navigation menu
- FRAMES overview page
- Submission calendar
- Document checklist

**Emotions**: Aware, responsible, slightly anxious about deadlines

**Pain Points**:
- Compliance information buried in portal
- Deadlines not visible early enough
- Requirements change without notification
- Unclear which FRAMES category applies

**Opportunities**:
- Prominent compliance status on dashboard
- 30/15/7 day deadline reminders
- Requirements version history
- Clear FRAMES category guidance

**Design Requirements**:
```
Dashboard Compliance Widget:

[FRAMES Compliance Status]
Overall: 85% Compliant

Upcoming:
[!] PESOS Annual Report - Due Jan 31, 2026 (32 days)
[!] Audited Financial Statements - Due Jan 31, 2026

[View Full Compliance Status]

---

Deadline Alert Banner:
[Warning icon] PESOS Annual Report due in 30 days
You have 2 pending document submissions
[Start Submission] [Dismiss]

---

Compliance Calendar View:
January 2026
| Sun | Mon | Tue | Wed | Thu | Fri | Sat |
|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |  1  |  2  |  3  |  4  |
|  5  |  6  |  7  |  8  |  9  | 10  | 11  |
| ... |     |     |     |     |     |     |
| 26  | 27  | 28  | 29  | 30  | 31* |     |

*31 = PESOS Annual Report deadline (highlighted)
```

---

### Stage 2: Requirements Understanding

**User Goal**: Know exactly what documents I need to prepare

**Actions**:
1. Miguel opens the specific compliance submission
2. Reviews the document requirements list
3. Reads descriptions for each required document
4. Downloads templates where available
5. Notes which documents are mandatory vs optional
6. Creates personal checklist for preparation

**Touchpoints**:
- Submission detail page
- Requirements checklist
- Document descriptions with examples
- Template downloads
- Mandatory/optional indicators
- Printable checklist option

**Emotions**: Learning, planning, wanting clarity

**Pain Points**:
- Requirements described in legal jargon
- No examples of acceptable documents
- Templates are outdated or hard to find
- Unclear which are mandatory

**Opportunities**:
- Plain language descriptions
- Sample document gallery
- Current, editable templates
- Clear mandatory markers

**Design Requirements**:
```
PESOS Annual Report Submission:

Due Date: January 31, 2026
Status: Not Started

What you need to submit:

Mandatory Documents:
1. [x] Audited Financial Statements
   Annual financial statements audited by
   CDA-accredited auditor
   [View Sample] [Download Template]

2. [ ] Annual Report Form
   CSEA Form 101 - Annual Cooperative Report
   [View Sample] [Download Form]

3. [ ] Board Resolution
   Resolution authorizing submission
   [View Sample] [Download Template]

4. [ ] Updated Membership List
   Current list of all members with status
   [View Sample] [Download Template]

Optional Documents:
5. [ ] Activity Photos
   Documentation of cooperative activities
   [Guidelines]

6. [ ] Awards/Recognition
   Any awards received during the year
   [Guidelines]

[Print Checklist] [Start Submission]

---

Document Description (expandable):

Audited Financial Statements
What: Annual financial statements including
      Balance Sheet, Income Statement,
      Cash Flow Statement
Who: Must be audited by CDA-accredited auditor
      [View List of Accredited Auditors]
Format: PDF, signed and stamped
Example: [View Sample Document]
```

---

### Stage 3: Document Preparation

**User Goal**: Prepare all documents correctly before the submission

**Actions**:
1. Miguel downloads required templates
2. Fills in templates with cooperative data
3. Gathers existing documents (audited statements)
4. Scans physical documents
5. Converts documents to required format
6. Verifies all documents are ready
7. Organizes files for upload

**Touchpoints**:
- Template downloads
- Template instructions
- Scanning guidance
- Format converter tools
- Document preview
- Preparation checklist

**Emotions**: Focused, methodical, sometimes frustrated with technical issues

**Pain Points**:
- Templates hard to fill on computer
- Scanning creates unclear images
- File size too large for upload
- PDF conversion is complicated

**Opportunities**:
- Fillable PDF templates
- Mobile scanning app integration
- Automatic file compression
- Built-in format conversion

**Design Requirements**:
```
Document Preparation Guide:

[Preparing Your Documents]

Templates Available:
1. Annual Report Form (Word/PDF) [Download]
   - Fill in cooperative information
   - Print and sign
   - Scan back to PDF

2. Board Resolution Template [Download]
   - Customize for your cooperative
   - Get signatures from board
   - Scan to PDF

Scanning Tips:
- Use good lighting
- Keep document flat
- Capture all edges
- Ensure text is readable

Recommended Apps:
- CamScanner (free)
- Microsoft Lens (free)
- Adobe Scan (free)

[View Scanning Tutorial Video]

File Requirements:
- Format: PDF, JPG, PNG
- Max Size: 10MB per file
- Minimum Resolution: 300 DPI

[Check if my files are ready] - opens validation tool
```

---

### Stage 4: Document Upload

**User Goal**: Upload all documents correctly without errors

**Actions**:
1. Miguel starts the submission process
2. Sees list of required documents with upload buttons
3. Clicks to upload first document
4. Selects file from computer
5. Sees upload progress and confirmation
6. Previews uploaded document
7. Repeats for each required document
8. Sees completion status

**Touchpoints**:
- Submission wizard
- Document upload interface
- File browser
- Upload progress indicator
- Document preview
- Validation feedback
- Completion checklist

**Emotions**: Careful, methodical, relieved when successful

**Pain Points**:
- Slow upload on poor connection
- Upload fails without clear error
- Can't see what was uploaded
- Accidentally uploading wrong document

**Opportunities**:
- Resume interrupted uploads
- Clear error messages
- Preview before confirming
- Easy document replacement

**Design Requirements**:
```
Document Upload Interface:

PESOS Annual Report Submission
Step 2 of 4: Upload Documents

Progress: 2 of 4 mandatory documents uploaded

Documents:
[Audited Financial Statements]
Status: Uploaded ✓
[Preview] [Replace]

[Annual Report Form]
Status: Uploading... 45%
[filename.pdf - 3.2 MB]
[Cancel]

[Board Resolution]
Status: Not uploaded
[Choose File] or drag and drop
Accepted: PDF, JPG, PNG (max 10MB)

[Updated Membership List]
Status: Not uploaded
[Choose File] or drag and drop

---

Upload Validation:

[!] File too large (12MB)
Please reduce file size to under 10MB
[Tips to reduce file size]

[✓] File uploaded successfully
Document preview available

[x] File format not accepted
Please upload PDF, JPG, or PNG

---

Preview Modal:
[Document thumbnail/preview]
Filename: audited_statements_2025.pdf
Size: 2.4 MB
Pages: 15

Is this the correct document?
[Replace] [Confirm]
```

---

### Stage 5: Submission Review

**User Goal**: Verify my submission is complete before sending

**Actions**:
1. Miguel sees submission summary
2. Reviews all uploaded documents
3. Checks for any missing items
4. Reads submission declaration
5. Adds any notes for reviewer
6. Confirms identity/authorization
7. Submits the compliance package

**Touchpoints**:
- Submission summary page
- Document thumbnails with preview
- Missing item alerts
- Declaration/certification
- Notes field
- Identity confirmation
- Submit button

**Emotions**: Careful review, slight anxiety, relief upon submission

**Pain Points**:
- Summary too long to review
- Can't edit without losing progress
- Declaration language is confusing
- Uncertain if submission went through

**Opportunities**:
- Collapsible summary sections
- Edit capabilities per section
- Plain language declaration
- Clear submission confirmation

**Design Requirements**:
```
Submission Review:

PESOS Annual Report - 2025
Status: Ready to Submit

Document Summary:
Mandatory Documents (4/4 complete):
1. Audited Financial Statements ✓ [View]
2. Annual Report Form ✓ [View]
3. Board Resolution ✓ [View]
4. Updated Membership List ✓ [View]

Optional Documents (1/2 uploaded):
5. Activity Photos ✓ [View]
6. Awards/Recognition - [Add now]

[Edit Documents]

---

Notes to Reviewer (optional):
[Provide any context or clarification for
the CSEA reviewer]
[_________________________________]
[_________________________________]

---

Certification:
I, Miguel Pangandaman, as Treasurer of
Jolo Farmers Cooperative, certify that:

[x] All information submitted is true and accurate
[x] I am authorized to submit on behalf of
    the cooperative
[x] Documents have been reviewed by
    cooperative leadership

Name: [Miguel Pangandaman] (editable)
Position: [Treasurer] (editable)
Date: December 30, 2025

[Submit for Review]

---

Submission Confirmation:
[Success icon]
Your submission has been received!

Reference #: PESOS-2025-JFC-0123
Submitted: December 30, 2025 at 2:45 PM

What happens next:
1. CSEA will review your submission (5-10 business days)
2. You'll be notified of any issues or approvals
3. Check status anytime in your compliance dashboard

[Download Confirmation] [View Submission Status]
```

---

### Stage 6: Review Tracking

**User Goal**: Monitor my submission status and respond to any requests

**Actions**:
1. Miguel returns to check submission status
2. Sees current review stage
3. Receives notification of reviewer comment
4. Reads request for additional information
5. Uploads additional/corrected document
6. Resubmits and waits for final decision

**Touchpoints**:
- Submission status page
- Review timeline
- Email/SMS notifications
- Reviewer comments section
- Additional upload interface
- Resubmission flow

**Emotions**: Waiting, checking, sometimes anxious, responsive

**Pain Points**:
- No visibility into review progress
- Generic status messages
- Unclear what additional info needed
- Resubmission process unclear

**Opportunities**:
- Detailed review timeline
- Specific action requests
- Guided resubmission
- Estimated completion time

**Design Requirements**:
```
Submission Status Page:

PESOS Annual Report - 2025
Reference #: PESOS-2025-JFC-0123

Status: Under Review - Additional Info Requested

Timeline:
[x] Submitted - Dec 30, 2025 2:45 PM
[x] Received - Dec 30, 2025 2:45 PM
[!] Additional Info Requested - Jan 3, 2026
[ ] Under Review
[ ] Decision

---

[!] Action Required:
Reviewer Comment (Jan 3, 2026):

"The Board Resolution is missing signatures
from 2 required board members (Secretary and
Auditor). Please submit a corrected copy
with all required signatures."

What to do:
1. Get the missing signatures
2. Scan the completed resolution
3. Upload below

[Upload Corrected Document]

Already uploaded: board_resolution_v2.pdf
[View] [Replace]

[Resubmit]

---

After Resubmission:

Status: Under Review
Additional document received Jan 5, 2026

Estimated Decision: Jan 10-12, 2026
```

---

### Stage 7: Approval/Feedback

**User Goal**: Receive final decision and understand next steps

**Actions**:
1. Miguel receives decision notification
2. Opens submission to see result
3. If approved: downloads certificate
4. If rejected: reviews reasons
5. If rejected: understands appeal process
6. Updates compliance status in cooperative records

**Touchpoints**:
- Decision notification (email/SMS)
- Submission result page
- Approval certificate
- Rejection details
- Appeal process information
- Compliance record update

**Emotions**: Anticipating, relieved (if approved), frustrated (if rejected)

**Pain Points**:
- Decision delayed without explanation
- Rejection reasons unclear
- Appeal process complicated
- No certificate for approved submissions

**Opportunities**:
- Timely decision notifications
- Clear rejection explanations
- Straightforward appeal process
- Downloadable approval certificates

**Design Requirements**:
```
Approval Result:

[Success Icon]
PESOS Annual Report - APPROVED

Compliance Status: Active until Dec 31, 2026

Your cooperative has successfully completed
the PESOS Annual Report submission for 2025.

Approval Details:
Reference: PESOS-2025-JFC-0123
Approved: January 10, 2026
Reviewer: CSEA Compliance Unit
Valid Until: December 31, 2026

[Download Certificate] [View Details]

---

Rejection Result:

[Warning Icon]
PESOS Annual Report - REJECTED

Your submission could not be approved due to
the following issues:

Reason for Rejection:
1. Audited Financial Statements
   - Financial statements were not audited by
     a CDA-accredited auditor
   - [View list of accredited auditors]

2. Updated Membership List
   - List does not include required fields
     (member status, share capital)
   - [View required format]

What you can do:
Option 1: Correct and Resubmit (Recommended)
- You have 15 days to submit corrections
- No additional fee required
[Start Corrected Submission]

Option 2: File an Appeal
- If you believe this decision is incorrect
- Must be filed within 30 days
[Learn About Appeals]

Need Help?
[Contact CSEA Compliance Office]
Phone: (064) xxx-xxxx
Email: compliance@csea.bangsamoro.gov.ph
```

---

### Stage 8: Compliance Maintenance

**User Goal**: Stay compliant throughout the year with proactive management

**Actions**:
1. Miguel views overall FRAMES compliance status
2. Sees which documents are expiring
3. Reviews upcoming submission deadlines
4. Sets reminders for renewals
5. Updates documents as they're renewed
6. Maintains good compliance standing

**Touchpoints**:
- FRAMES compliance dashboard
- Document expiry tracker
- Deadline calendar
- Reminder settings
- Document update interface
- Compliance score/status

**Emotions**: Proactive, organized, maintaining status

**Pain Points**:
- Loses track of multiple deadlines
- Documents expire without warning
- No central view of all compliance items
- Renewal process starts from scratch

**Opportunities**:
- Unified compliance dashboard
- Automatic expiry reminders
- Pre-populated renewal forms
- Compliance health score

**Design Requirements**:
```
FRAMES Compliance Dashboard:

Overall Status: 92% Compliant
[Progress bar visualization]

FRAMES Categories:
| Category | Status | Score | Next Due |
|----------|--------|-------|----------|
| Formation | ✓ | 100% | - |
| Registration | ✓ | 100% | Mar 2027 |
| Auditing | ✓ | 95% | Jan 2027 |
| Monitoring | ! | 80% | Jan 2026 |
| Enforcement | ✓ | 100% | - |
| Sustainability | ✓ | 85% | Jun 2026 |

[View Details]

---

Expiring Documents:
| Document | Expires | Days Left |
|----------|---------|-----------|
| Business Permit | Mar 31 | 90 days |
| CSEA Registration | Aug 15 | 228 days |

[Set Reminders]

---

Upcoming Submissions:
| Submission | Due Date | Status |
|------------|----------|--------|
| PESOS Annual | Jan 31 | Complete ✓ |
| Q1 Report | Apr 15 | Not started |
| Audit Prep | May 31 | Not started |

[View Calendar]

---

Reminder Settings:
Notify me:
[x] 30 days before deadline
[x] 15 days before deadline
[x] 7 days before deadline
[ ] 3 days before deadline

Via:
[x] Email
[x] SMS
[x] In-app notification

[Save Preferences]
```

---

### Stage 9: Annual Compliance Cycle

**User Goal**: Complete the full annual compliance cycle efficiently

**Actions**:
1. Miguel completes all annual requirements
2. Receives annual compliance certificate
3. Archives year's documents
4. Prepares for next year's cycle
5. Reviews any changes to requirements
6. Updates templates and processes

**Touchpoints**:
- Annual completion notification
- Compliance certificate
- Document archive
- Next year preparation
- Requirement updates
- Process improvement suggestions

**Emotions**: Accomplished, forward-thinking, wanting continuity

**Pain Points**:
- No annual summary of accomplishments
- Documents scattered across submissions
- Requirements change without training
- No way to improve process

**Opportunities**:
- Annual compliance report
- Document archive organization
- Requirement change notifications
- Process improvement recommendations

**Design Requirements**:
```
Annual Compliance Summary:

Congratulations! 2025 Compliance Complete

Jolo Farmers Cooperative
CSEA ID: JFC-2015-001234

2025 Compliance Achievements:
- PESOS Annual Report ✓
- Quarterly Reports (4/4) ✓
- Audit Compliance ✓
- Registration Current ✓

Overall Score: 95%
Rating: Excellent

[Download Annual Certificate]

---

Document Archive:
All 2025 Submissions

| Submission | Submitted | Status |
|------------|-----------|--------|
| PESOS Annual | Dec 30 | Approved |
| Q4 Report | Nov 15 | Approved |
| Q3 Report | Aug 14 | Approved |
| ... | ... | ... |

[Download All Documents (ZIP)]

---

Prepare for 2026:

Changes for 2026:
- New PESOS form (Form 101-A)
  [Download New Template]
- Additional sustainability reporting required
  [View New Requirements]

First 2026 Deadline:
Q1 Report - Due April 15, 2026

[Set Up 2026 Reminders]

---

Improve Your Process:
Based on your 2025 experience:

Suggestions:
- You submitted Q2 report 2 days before deadline
  Consider: Start submissions 2 weeks earlier

- Document revisions requested 2 times
  Consider: Use our document checklist before upload

[View Best Practices Guide]
```

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| On-Time Submission Rate | > 95% | Deadline tracking |
| First-Time Approval Rate | > 80% | Revision requests |
| Document Rejection Rate | < 10% | Rejection tracking |
| Average Submission Time | < 45 min | Session analytics |
| Revision Turnaround | < 5 days | Resubmission timing |
| Compliance Dashboard Access | Weekly | Page analytics |
| Reminder Engagement | > 70% click-through | Notification tracking |
| Certificate Download Rate | > 90% | Download analytics |
| Appeal Rate | < 5% | Appeal submissions |
| Compliance Score Average | > 85% | Score calculation |

---

## Implementation Status

| Feature | Status | Notes |
|---------|--------|-------|
| Dashboard compliance widget | TBD | FRAMES status display |
| Deadline alert system | TBD | Notification triggers |
| Requirements checklist | TBD | Template downloads |
| Document upload interface | TBD | Multi-file support |
| Upload validation | TBD | File type/size checks |
| Submission review page | TBD | Summary display |
| Review tracking | TBD | Status timeline |
| Reviewer comments | TBD | Communication interface |
| Approval certificate | TBD | PDF generation |
| Compliance dashboard | TBD | FRAMES visualization |
| Reminder system | TBD | Email/SMS/push |
| Document archive | TBD | Historical access |

---

## Recommendations

### Priority 1: Compliance Visibility
1. Create prominent dashboard widget showing FRAMES status
2. Implement 30/15/7 day deadline reminders
3. Send proactive notifications for upcoming requirements
4. Display compliance score with trend indicators

### Priority 2: Document Preparation Support
1. Provide fillable PDF templates for all forms
2. Create document scanning tutorial content
3. Implement file validation before upload
4. Offer auto-compression for large files

### Priority 3: Upload Experience
1. Enable drag-and-drop file upload
2. Show clear progress for each document
3. Provide document preview before confirmation
4. Allow easy replacement of uploaded files

### Priority 4: Transparent Review Process
1. Display detailed review timeline
2. Provide specific action items for revisions
3. Enable direct communication with reviewers
4. Give estimated decision timeframes

### Priority 5: Compliance Continuity
1. Generate downloadable approval certificates
2. Create annual compliance summary reports
3. Archive all submissions for historical access
4. Notify of requirement changes with training materials

---

## Implementation Plan

### Phase 1: Frontend Foundation

**Pages:**
- `frontend/src/app/(tenant)/portal/compliance/page.tsx` - FRAMES dashboard
- `frontend/src/app/(tenant)/portal/compliance/submissions/page.tsx` - Submission history
- `frontend/src/app/(tenant)/portal/compliance/submissions/new/page.tsx` - New submission
- `frontend/src/app/(tenant)/portal/compliance/submissions/[id]/page.tsx` - Submission detail/status
- `frontend/src/app/(tenant)/portal/compliance/documents/page.tsx` - Document archive
- `frontend/src/app/(tenant)/portal/compliance/calendar/page.tsx` - Deadline calendar
- `frontend/src/app/(tenant)/portal/compliance/certificates/page.tsx` - Certificates archive

**Components:**
- `frontend/src/components/compliance/FRAMESDashboard.tsx` - Overall status view
- `frontend/src/components/compliance/ComplianceScore.tsx` - Score with categories
- `frontend/src/components/compliance/CategoryCard.tsx` - FRAMES category status
- `frontend/src/components/compliance/DeadlineAlert.tsx` - Upcoming deadline banner
- `frontend/src/components/compliance/SubmissionWizard.tsx` - Multi-step submission
- `frontend/src/components/compliance/RequirementsChecklist.tsx` - Document list
- `frontend/src/components/compliance/DocumentUploader.tsx` - Upload with validation
- `frontend/src/components/compliance/DocumentPreview.tsx` - Preview modal
- `frontend/src/components/compliance/SubmissionReview.tsx` - Summary before submit
- `frontend/src/components/compliance/SubmissionTimeline.tsx` - Status tracking
- `frontend/src/components/compliance/ReviewerComment.tsx` - CSEA feedback display
- `frontend/src/components/compliance/DocumentResponseForm.tsx` - Respond to request
- `frontend/src/components/compliance/CertificateCard.tsx` - Certificate display
- `frontend/src/components/compliance/ComplianceCalendar.tsx` - Deadline calendar
- `frontend/src/components/compliance/ReminderSettings.tsx` - Notification prefs

**shadcn/ui Components Used:**
- Card, Badge, Progress for dashboard widgets
- Form, Input, Select, Textarea for forms
- Table for submission and document lists
- Dialog for document preview and confirmations
- Alert for deadline warnings and action items
- Calendar for deadline visualization
- Switch for notification toggles
- Skeleton for loading states
- Tabs for submission sections

### Phase 2: State & Services

**Hooks:**
- `frontend/src/lib/hooks/useCompliance.ts` - FRAMES status and score
- `frontend/src/lib/hooks/useSubmissions.ts` - Submission list and history
- `frontend/src/lib/hooks/useSubmission.ts` - Single submission state
- `frontend/src/lib/hooks/useSubmissionWizard.ts` - Wizard step management
- `frontend/src/lib/hooks/useDocumentUpload.ts` - Upload with validation
- `frontend/src/lib/hooks/useComplianceCalendar.ts` - Deadlines and reminders
- `frontend/src/lib/hooks/useCertificates.ts` - Certificate access
- `frontend/src/lib/hooks/useReminderSettings.ts` - Notification preferences

**Services:**
- `frontend/src/lib/services/compliance.ts` - FRAMES status API
- `frontend/src/lib/services/submissions.ts` - Submission CRUD
- `frontend/src/lib/services/compliance-documents.ts` - Document operations
- `frontend/src/lib/services/certificates.ts` - Certificate download
- `frontend/src/lib/services/reminders.ts` - Reminder settings

**Types:**
- `frontend/src/lib/types/compliance.ts` - FRAMESStatus, ComplianceScore
- `frontend/src/lib/types/submission.ts` - Submission, SubmissionStatus
- `frontend/src/lib/types/compliance-document.ts` - RequiredDocument, UploadedDocument
- `frontend/src/lib/types/certificate.ts` - Certificate, CertificateType
- `frontend/src/lib/types/reminder.ts` - Reminder, ReminderPreferences

### Phase 3: Backend Integration

**Endpoints (`backend/apps/compliance/api.py`):**
- `GET /api/tenant/compliance` - FRAMES status overview
- `GET /api/tenant/compliance/score` - Compliance score breakdown
- `GET /api/tenant/compliance/deadlines` - Upcoming deadlines
- `GET /api/tenant/compliance/requirements/{type}` - Requirements for submission type

**Endpoints (`backend/apps/compliance/api.py`):**
- `GET /api/tenant/submissions` - List submissions
- `POST /api/tenant/submissions` - Create submission
- `GET /api/tenant/submissions/{id}` - Submission detail
- `PATCH /api/tenant/submissions/{id}` - Update draft
- `POST /api/tenant/submissions/{id}/submit` - Submit for review
- `POST /api/tenant/submissions/{id}/documents` - Upload document
- `DELETE /api/tenant/submissions/{id}/documents/{doc_id}` - Remove document
- `POST /api/tenant/submissions/{id}/respond` - Respond to reviewer

**Endpoints (`backend/apps/compliance/api.py`):**
- `GET /api/tenant/certificates` - List certificates
- `GET /api/tenant/certificates/{id}/download` - Download PDF
- `GET /api/tenant/documents/archive` - Historical documents
- `GET /api/tenant/documents/templates/{type}` - Download template

**Endpoints (`backend/apps/notifications/api.py`):**
- `GET /api/tenant/reminders` - Get reminder settings
- `PATCH /api/tenant/reminders` - Update settings
- `GET /api/tenant/notifications/compliance` - Compliance notifications

**Schemas (`backend/apps/*/schemas.py`):**
- `FRAMESStatusSchema`, `ComplianceScoreSchema`
- `DeadlineSchema`, `RequirementSchema`
- `SubmissionCreateSchema`, `SubmissionDetailSchema`
- `SubmissionDocumentSchema`, `ReviewerCommentSchema`
- `CertificateSchema`, `TemplateSchema`
- `ReminderSettingsSchema`, `NotificationSchema`

### Phase 4: Polish & UX

**Loading States:**
- Skeleton for FRAMES dashboard
- Skeleton for submission timeline
- Document upload progress indicator
- Certificate generation loading

**Error Handling:**
- Document upload failure with retry
- Submission validation errors
- Review response submission errors
- Certificate download failure

**Animations:**
- Compliance score progress animation
- Document upload success feedback
- Timeline status transitions
- Certificate download confirmation

**Accessibility:**
- Dashboard status announcements
- Form validation error messages
- Document list keyboard navigation
- Calendar navigation support

**Mobile Optimization:**
- Camera capture for document scanning
- Touch-friendly document list
- Responsive calendar view
- Push notifications for deadlines

### Implementation Sequence

**Week 1-2: FRAMES Dashboard**
1. FRAMES dashboard layout
2. Compliance score component
3. Category status cards
4. Deadline alert banners
5. Quick action links

**Week 3-4: Requirements & Preparation**
6. Requirements checklist page
7. Document template downloads
8. Scanning tips and guidelines
9. File validation utility
10. Preparation checklist

**Week 5-6: Submission Wizard**
11. Submission wizard container
12. Document upload interface (depends on #9)
13. Upload progress and validation
14. Document preview modal
15. Document replacement flow

**Week 7-8: Review & Tracking**
16. Submission review page (depends on #15)
17. Declaration and certification
18. Submission confirmation
19. Status tracking timeline
20. Reviewer comment display

**Week 9-10: Certificates & Maintenance**
21. Response to reviewer request
22. Approval/rejection display
23. Certificate download
24. Compliance calendar view
25. Reminder settings and notifications

---

## Implementation Status

*Audited: December 30, 2025*

### Frontend Pages
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Tenant Dashboard | ✅ Exists | `frontend/src/app/(tenant)/dashboard/page.tsx` | Has compliance widget |
| Compliance Overview | ✅ Exists | `frontend/src/app/(tenant)/compliance/page.tsx` | FRAMES status |
| Business Documents | ✅ Exists | `frontend/src/app/(tenant)/business/documents/page.tsx` | Document management |
| FRAMES Dashboard | ❌ Missing | `frontend/src/app/(tenant)/portal/compliance/page.tsx` | Full FRAMES view |
| Submission History | ❌ Missing | `frontend/src/app/(tenant)/portal/compliance/submissions/page.tsx` | Past submissions |
| New Submission | ❌ Missing | `frontend/src/app/(tenant)/portal/compliance/submissions/new/page.tsx` | Submit documents |
| Submission Detail | ❌ Missing | `frontend/src/app/(tenant)/portal/compliance/submissions/[id]/page.tsx` | Track status |
| Document Archive | ❌ Missing | `frontend/src/app/(tenant)/portal/compliance/documents/page.tsx` | Historical docs |
| Deadline Calendar | ❌ Missing | `frontend/src/app/(tenant)/portal/compliance/calendar/page.tsx` | Compliance calendar |
| Certificates | ❌ Missing | `frontend/src/app/(tenant)/portal/compliance/certificates/page.tsx` | Download certs |

### Components
| Component | Status | Path | Notes |
|-----------|--------|------|-------|
| FRAMESDashboard | 🚧 Needs Audit | `frontend/src/components/compliance/` | Overall status |
| ComplianceScore | 🚧 Needs Audit | `frontend/src/components/compliance/` | Score display |
| CategoryCard | 🚧 Needs Audit | `frontend/src/components/compliance/` | FRAMES category |
| DeadlineAlert | ❌ Missing | `frontend/src/components/compliance/` | Upcoming deadline |
| SubmissionWizard | ❌ Missing | `frontend/src/components/compliance/` | Multi-step submit |
| RequirementsChecklist | ❌ Missing | `frontend/src/components/compliance/` | Document list |
| DocumentUploader | 🚧 Needs Audit | `frontend/src/components/compliance/` | Upload with validation |
| DocumentPreview | 🚧 Needs Audit | `frontend/src/components/compliance/` | Preview modal |
| SubmissionReview | ❌ Missing | `frontend/src/components/compliance/` | Summary before submit |
| SubmissionTimeline | ❌ Missing | `frontend/src/components/compliance/` | Status tracking |
| ReviewerComment | ❌ Missing | `frontend/src/components/compliance/` | CSEA feedback |
| DocumentResponseForm | ❌ Missing | `frontend/src/components/compliance/` | Respond to request |
| CertificateCard | ❌ Missing | `frontend/src/components/compliance/` | Certificate display |
| ComplianceCalendar | ❌ Missing | `frontend/src/components/compliance/` | Deadline calendar |
| ReminderSettings | ❌ Missing | `frontend/src/components/compliance/` | Notification prefs |

### Backend APIs
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET /api/core/compliance | ✅ Exists | `backend/apps/core/api.py` | Compliance status |
| GET /api/core/dashboard/metrics | ✅ Exists | `backend/apps/core/api.py` | Dashboard metrics |
| GET /api/tenant/documents | ✅ Exists | `backend/apps/tenant/api.py` | Documents list |
| GET /api/tenant/compliance | ❌ Missing | `backend/apps/compliance/api.py` | FRAMES overview |
| GET /api/tenant/compliance/score | ❌ Missing | `backend/apps/compliance/api.py` | Score breakdown |
| GET /api/tenant/compliance/deadlines | ❌ Missing | `backend/apps/compliance/api.py` | Upcoming deadlines |
| GET /api/tenant/compliance/requirements/{type} | ❌ Missing | `backend/apps/compliance/api.py` | Requirements list |
| GET /api/tenant/submissions | ❌ Missing | `backend/apps/compliance/api.py` | Submission history |
| POST /api/tenant/submissions | ❌ Missing | `backend/apps/compliance/api.py` | Create submission |
| GET /api/tenant/submissions/{id} | ❌ Missing | `backend/apps/compliance/api.py` | Submission detail |
| POST /api/tenant/submissions/{id}/submit | ❌ Missing | `backend/apps/compliance/api.py` | Submit for review |
| POST /api/tenant/submissions/{id}/documents | ❌ Missing | `backend/apps/compliance/api.py` | Upload document |
| POST /api/tenant/submissions/{id}/respond | ❌ Missing | `backend/apps/compliance/api.py` | Respond to reviewer |
| GET /api/tenant/certificates | ❌ Missing | `backend/apps/compliance/api.py` | List certificates |
| GET /api/tenant/certificates/{id}/download | ❌ Missing | `backend/apps/compliance/api.py` | Download PDF |

### Overall Progress
- **Frontend**: 3/10 pages (30%)
- **Components**: 5/15 need audit (33%)
- **Backend**: 3/15 endpoints (20%)
