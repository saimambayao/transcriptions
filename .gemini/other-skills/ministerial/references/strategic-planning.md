# Strategic Plan Workflow & Data Lifecycle Pattern

**Version**: 1.0  |  **Date**: 2026-01-12  |  **Status**: Approved Pattern

---

## Purpose

This document defines the standard workflow and data lifecycle pattern for all Strategic Planning submodules (Points 1-10) in the Ministerial Planning module. All submodule architecture documents should reference this pattern for consistency.

---

## Table of Contents

1. [Pattern Overview](#1-pattern-overview)
2. [Workflow States](#2-workflow-states)
3. [Edit Permissions by Status](#3-edit-permissions-by-status)
4. [Submission Process](#4-submission-process)
5. [Amendment Process](#5-amendment-process)
6. [Planning Cycle](#6-planning-cycle)
7. [Data Models](#7-data-models)
8. [Integration with Submodules](#8-integration-with-submodules)
9. [Implementation Checklist](#9-implementation-checklist)

---

## 1. Pattern Overview

### 1.1 Key Principles

| Principle | Description |
|-----------|-------------|
| **Strategic Plan Level** | All 10 planning points are submitted together as a cohesive package |
| **Ministerial Certification** | Submission requires certification by Minister/Director General/Executive Director |
| **Same Approval Path** | Amendments follow the same approval process as original submissions |
| **Per Planning Cycle** | New alignments each year/BDP period, not one-time entries |
| **Version History** | All versions preserved for audit and reference |

### 1.2 Applicable Submodules

This pattern applies to all 10 points of the Strategic Planning Framework:

| Point | Submodule | Architecture Doc |
|-------|-----------|------------------|
| 1 | Legal Alignment | `arch-subm-planning-01-legal-alignment.md` |
| 2 | BDP Alignment | `arch-subm-planning-02-bdp-alignment.md` |
| 3 | Priority Agenda Alignment | `arch-subm-planning-03-priority-agenda.md` |
| 4 | Stakeholder Analysis | `arch-subm-planning-04-stakeholder.md` |
| 5 | Strategic Direction | `arch-subm-planning-05-strategy.md` |
| 6 | Theory of Change | `arch-subm-planning-06-toc.md` |
| 7 | PPA Design | `arch-subm-planning-07-ppa.md` |
| 8 | Resource Planning | `arch-subm-planning-08-resources.md` |
| 9 | Risk Management | `arch-subm-planning-09-risk.md` |
| 10 | M&E Framework | `arch-subm-planning-10-monitoring.md` |

---

## 2. Workflow States

### 2.1 State Diagram

```
+---------------------------------------------------------------------+
|                    STRATEGIC PLAN WORKFLOW                            |
+---------------------------------------------------------------------+
|                                                                       |
|  [DRAFT]                                                              |
|    |                                                                  |
|    | Planning Officer creates/edits all 10 points                     |
|    | All AI-assisted features available                               |
|    | Full edit capability                                             |
|    |                                                                  |
|    v (Submit with certification)                                      |
|                                                                       |
|  [SUBMITTED]                                                          |
|    |                                                                  |
|    | Certified by Minister/Director General/Executive Director        |
|    | No edits allowed                                                 |
|    | Awaiting BPDA/OCM review                                         |
|    |                                                                  |
|    v                                                                  |
|                                                                       |
|  [UNDER REVIEW]                                                       |
|    |                                                                  |
|    | BPDA/OCM reviewing strategic plan                                |
|    | No edits allowed by MOA                                          |
|    | Reviewer can add feedback/comments                               |
|    |                                                                  |
|    +------+------+                                                    |
|    |             |                                                    |
|    v             v                                                    |
|                                                                       |
|  [RETURNED]   [APPROVED]                                              |
|    |             |                                                    |
|    | Feedback    | Final approval by BPDA/OCM                         |
|    | provided    | Read-only (no edits)                               |
|    | Edit        | Can request amendment for changes                   |
|    | enabled     |                                                    |
|    |             |                                                    |
|    v             |                                                    |
|  (Resubmit)     |                                                    |
|    |             |                                                    |
|    +-------------+                                                    |
|                                                                       |
+---------------------------------------------------------------------+
```

### 2.2 State Definitions

| Status | Description | Who Can Change | Edit Capability |
|--------|-------------|----------------|-----------------|
| **Draft** | Working state for MOA planning team | Planning Officer | Full edit |
| **Submitted** | Sent to BPDA/OCM with ministerial certification | None | Read-only |
| **Under Review** | Being reviewed by BPDA/OCM | Reviewer (comments only) | Read-only |
| **Returned** | Sent back for revisions with feedback | Planning Officer | Full edit |
| **Approved** | Final approved version | None (requires amendment) | Read-only |

### 2.3 State Transitions

| From | To | Action | Required Role |
|------|-----|--------|---------------|
| Draft | Submitted | Submit | Planning Officer + Director certification |
| Submitted | Under Review | Start Review | BPDA/OCM Reviewer |
| Under Review | Approved | Approve | BPDA/OCM Reviewer |
| Under Review | Returned | Return | BPDA/OCM Reviewer |
| Returned | Submitted | Resubmit | Planning Officer |
| Approved | Draft (new version) | Create Amendment | Planning Officer |

---

## 3. Edit Permissions by Status

### 3.1 Permission Matrix

| Status | Planning Officer | Director | BPDA/OCM Reviewer |
|--------|------------------|----------|-------------------|
| **Draft** | Create, Edit, Delete | View, Approve for submission | - |
| **Submitted** | View only | View only | View, Start Review |
| **Under Review** | View only | View only | Add comments, Approve/Return |
| **Returned** | Edit, Resubmit | View, Re-approve | View feedback history |
| **Approved** | View only | View only | View only, Receive amendment requests |

### 3.2 Field-Level Permissions

All submodule fields follow the same permission rules:

| Permission | Draft | Submitted | Under Review | Returned | Approved |
|------------|-------|-----------|--------------|----------|----------|
| **Read** | All roles | All roles | All roles | All roles | All roles |
| **Create** | Planning Officer | - | - | Planning Officer | - |
| **Update** | Planning Officer | - | - | Planning Officer | - |
| **Delete** | Planning Officer | - | - | Planning Officer | - |
| **Comment** | All roles | All roles | BPDA/OCM | All roles | All roles |

---

## 4. Submission Process

### 4.1 Submission Flow

```
+---------------------------------------------------------------------+
|                       SUBMISSION PROCESS                              |
+---------------------------------------------------------------------+
|                                                                       |
|  1. COMPLETION CHECK                                                  |
|     +---------------------------------------------------------------+ |
|     | System validates all 10 points are complete:                   | |
|     | - Point 1: Legal Alignment (required fields filled)            | |
|     | - Point 2: BDP Alignment (goals mapped)                        | |
|     | - Point 3: Priority Agenda (at least 1 alignment)              | |
|     | - Point 4: Stakeholder Analysis (stakeholders identified)      | |
|     | - Point 5: Strategic Direction (objectives defined)            | |
|     | - Point 6: Theory of Change (pathways mapped)                  | |
|     | - Point 7: PPA Design (programs/activities created)            | |
|     | - Point 8: Resource Planning (budget allocated)                | |
|     | - Point 9: Risk Management (risks identified)                  | |
|     | - Point 10: M&E Framework (indicators defined)                 | |
|     +---------------------------------------------------------------+ |
|                                                                       |
|  2. DIRECTOR REVIEW                                                   |
|     +---------------------------------------------------------------+ |
|     | Director reviews all 10 points:                                | |
|     | - Validates completeness and accuracy                          | |
|     | - Reviews alignment with MOA mandate                            | |
|     | - Checks consistency across points                              | |
|     | - May use AI Validate for quality check                        | |
|     +---------------------------------------------------------------+ |
|                                                                       |
|  3. MINISTERIAL CERTIFICATION                                         |
|     +---------------------------------------------------------------+ |
|     | Minister/Director General/Executive Director certifies:        | |
|     | - Confirms strategic plan accuracy                              | |
|     | - Certifies alignment with MOA mandate                          | |
|     | - Digital signature/confirmation recorded                       | |
|     | - Timestamp and certifier identity logged                       | |
|     +---------------------------------------------------------------+ |
|                                                                       |
|  4. SUBMIT TO BPDA/OCM                                                |
|     +---------------------------------------------------------------+ |
|     | Strategic Plan (all 10 points) submitted:                      | |
|     | - Status changes to "Submitted"                                 | |
|     | - Notification sent to BPDA/OCM                                 | |
|     | - All fields become read-only                                   | |
|     | - Submission timestamp recorded                                 | |
|     +---------------------------------------------------------------+ |
|                                                                       |
+---------------------------------------------------------------------+
```

### 4.2 Certification Requirements

| Certifier Role | MOA Type | Authority Level |
|----------------|----------|-----------------|
| **Minister** | Ministry | Highest authority for Ministry strategic plans |
| **Director General** | Bureau, Commission | Highest authority for attached office plans |
| **Executive Director** | Office, Agency | Highest authority for smaller office plans |

### 4.3 Completion Validation Rules

Each submodule defines its own completion requirements:

| Point | Minimum Requirements for Completion |
|-------|-------------------------------------|
| 1 | At least one legal basis citation |
| 2 | At least one BDP goal mapping |
| 3 | At least one priority alignment with description |
| 4 | At least one stakeholder identified |
| 5 | Vision, mission, and at least one strategic objective |
| 6 | At least one ToC pathway defined |
| 7 | At least one PPA defined |
| 8 | Budget summary completed |
| 9 | At least one risk identified with mitigation |
| 10 | At least one KPI/indicator defined |

---

## 5. Amendment Process

### 5.1 Amendment Flow

```
+---------------------------------------------------------------------+
|                       AMENDMENT PROCESS                               |
+---------------------------------------------------------------------+
|                                                                       |
|  1. AMENDMENT REQUEST                                                 |
|     +---------------------------------------------------------------+ |
|     | Planning Officer initiates amendment:                          | |
|     | - Creates new version (draft) from approved version            | |
|     | - Original approved version preserved as reference             | |
|     | - Amendment justification required                              | |
|     | - Change summary auto-generated                                 | |
|     +---------------------------------------------------------------+ |
|                                                                       |
|  2. AMENDMENT EDITING                                                 |
|     +---------------------------------------------------------------+ |
|     | Planning Officer edits amendment:                               | |
|     | - All AI-assisted features available                            | |
|     | - Track changes visible (what changed from original)            | |
|     | - Amendment reason documented                                   | |
|     +---------------------------------------------------------------+ |
|                                                                       |
|  3. SAME APPROVAL PATH                                                |
|     +---------------------------------------------------------------+ |
|     | Amendment follows same approval process:                        | |
|     | - Director review                                               | |
|     | - Ministerial certification                                     | |
|     | - Submit to BPDA/OCM                                            | |
|     | - BPDA/OCM review and approve/return                           | |
|     +---------------------------------------------------------------+ |
|                                                                       |
|  4. VERSION HISTORY                                                   |
|     +---------------------------------------------------------------+ |
|     | System maintains version history:                               | |
|     | - Version 1.0: Original approved                                | |
|     | - Version 1.1: First amendment                                  | |
|     | - Version 1.2: Second amendment                                 | |
|     | - Each version linked to planning cycle                         | |
|     +---------------------------------------------------------------+ |
|                                                                       |
+---------------------------------------------------------------------+
```

### 5.2 Amendment Approval Authority

| Amendment Type | Approval Authority | Same as Original |
|----------------|-------------------|------------------|
| **Any submodule changes** | BPDA/OCM | Yes |
| **Minor corrections** | BPDA/OCM | Yes |
| **Major restructuring** | BPDA/OCM | Yes |

### 5.3 Version Numbering

| Version | Description |
|---------|-------------|
| **1.0** | Original approved version |
| **1.1** | First amendment to version 1.0 |
| **1.2** | Second amendment to version 1.0 |
| **2.0** | New planning year (fresh start) |
| **2.1** | First amendment to version 2.0 |

---

## 6. Planning Cycle

### 6.1 Cycle Structure

```
+---------------------------------------------------------------------+
|                        PLANNING CYCLE                                 |
+---------------------------------------------------------------------+
|                                                                       |
|  BDP PERIOD: 2023-2028 (Bangsamoro Development Plan)                  |
|                                                                       |
|  +---------------------------------------------------------------+   |
|  | Year 1 (2023) - Version 1.x                                    |   |
|  | - Create new Strategic Plan for 2023                           |   |
|  | - Complete all 10 points                                        |   |
|  | - Submit, review, approve                                       |   |
|  | - Amendments as needed (1.1, 1.2, etc.)                         |   |
|  +---------------------------------------------------------------+   |
|                                                                       |
|  +---------------------------------------------------------------+   |
|  | Year 2 (2024) - Version 2.x                                    |   |
|  | - Create new Strategic Plan for 2024                           |   |
|  | - Can copy from previous year as starting point                |   |
|  | - Update based on progress/changes                              |   |
|  | - Submit, review, approve                                       |   |
|  +---------------------------------------------------------------+   |
|                                                                       |
|  +---------------------------------------------------------------+   |
|  | Year 3 (2025) - Version 3.x                                    |   |
|  | - Create new Strategic Plan for 2025                           |   |
|  | - Reflect mid-BDP adjustments                                   |   |
|  | - Submit, review, approve                                       |   |
|  +---------------------------------------------------------------+   |
|                                                                       |
|  ... Years 4-6 follow same pattern                                    |
|                                                                       |
|  NEXT BDP PERIOD: 2029-2034                                           |
|  - Fresh strategic planning cycle begins                              |
|  - New alignments to updated frameworks                               |
|                                                                       |
+---------------------------------------------------------------------+
```

### 6.2 Planning Cycle Rules

| Rule | Description |
|------|-------------|
| **Annual Submission** | Each year requires a new strategic plan submission |
| **Copy Forward** | Can use previous year as template (optional) |
| **Historical Access** | All previous years remain accessible (read-only) |
| **Cross-Year Analysis** | AI can analyze trends across planning cycles |
| **BDP Alignment** | All plans must align with current BDP period |

### 6.3 Timeline (Typical)

| Phase | Timing | Activities |
|-------|--------|------------|
| **Planning** | Q4 of previous year | MOA creates draft, completes 10 points |
| **Review** | Q4-Q1 | Director review, ministerial certification |
| **Submission** | Q1 | Submit to BPDA/OCM |
| **Approval** | Q1-Q2 | BPDA/OCM review and approve |
| **Implementation** | Q2-Q4 | Execute approved strategic plan |
| **Amendment** | As needed | Submit amendments if changes required |

---

## 7. Data Models

### 7.1 Django Models

```python
# backend/apps/ministerial/models/workflow.py

from django.db import models
from apps.core.models import TenantScopedModel


class StrategicPlanStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    SUBMITTED = 'submitted', 'Submitted'
    UNDER_REVIEW = 'under_review', 'Under Review'
    RETURNED = 'returned', 'Returned'
    APPROVED = 'approved', 'Approved'


class StrategicPlan(TenantScopedModel):
    """
    Strategic Plan with workflow status tracking.

    Contains all 10 planning points as related models.
    Workflow applies at this level (not individual points).
    """

    # Basic info
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # Workflow status
    status = models.CharField(
        max_length=20,
        choices=StrategicPlanStatus.choices,
        default=StrategicPlanStatus.DRAFT
    )

    # Submission tracking
    submitted_at = models.DateTimeField(null=True, blank=True)
    submitted_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='submitted_plans'
    )

    # Certification tracking (Minister/DG/ED)
    certified_at = models.DateTimeField(null=True, blank=True)
    certified_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='certified_plans',
        help_text='Minister/Director General/Executive Director'
    )
    certification_title = models.CharField(
        max_length=100,
        blank=True,
        help_text='Title of certifier (e.g., Minister, Director General)'
    )

    # Review tracking (BPDA/OCM)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_plans'
    )
    reviewer_feedback = models.TextField(
        blank=True,
        help_text='Feedback from BPDA/OCM reviewer'
    )

    # Approval tracking
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_plans'
    )

    # Version tracking
    version = models.CharField(
        max_length=10,
        default='1.0',
        help_text='Version number (e.g., 1.0, 1.1, 2.0)'
    )
    previous_version = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='amendments',
        help_text='Link to previous version (for amendments)'
    )
    is_amendment = models.BooleanField(
        default=False,
        help_text='True if this is an amendment to an approved plan'
    )
    amendment_justification = models.TextField(
        blank=True,
        help_text='Reason for amendment (required for amendments)'
    )

    # Planning cycle
    planning_year = models.PositiveIntegerField(
        help_text='Year this plan covers (e.g., 2024)'
    )
    bdp_period = models.CharField(
        max_length=20,
        default='2023-2028',
        help_text='BDP period (e.g., 2023-2028)'
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ministerial_strategic_plans'
        unique_together = ['tenant', 'planning_year', 'version']
        ordering = ['-planning_year', '-version']

    def __str__(self):
        return f"{self.title} ({self.planning_year} v{self.version})"

    # Permission check methods
    def can_edit(self, user) -> bool:
        """Check if user can edit this plan based on status."""
        if self.status in [StrategicPlanStatus.DRAFT, StrategicPlanStatus.RETURNED]:
            return user.has_role('planning_officer', self.tenant)
        return False

    def can_submit(self, user) -> bool:
        """Check if user can submit this plan."""
        return (
            self.status == StrategicPlanStatus.DRAFT and
            user.has_role('planning_officer', self.tenant)
        )

    def can_certify(self, user) -> bool:
        """Check if user can certify this plan."""
        return (
            self.status == StrategicPlanStatus.DRAFT and
            user.has_role('director', self.tenant)
        )

    def can_review(self, user) -> bool:
        """Check if user can review this plan."""
        return (
            self.status == StrategicPlanStatus.SUBMITTED and
            user.has_role(['bpda_reviewer', 'ocm_staff'])
        )

    def can_approve(self, user) -> bool:
        """Check if user can approve this plan."""
        return (
            self.status == StrategicPlanStatus.UNDER_REVIEW and
            user.has_role(['bpda_reviewer', 'ocm_staff'])
        )

    def can_return(self, user) -> bool:
        """Check if user can return this plan for revisions."""
        return (
            self.status == StrategicPlanStatus.UNDER_REVIEW and
            user.has_role(['bpda_reviewer', 'ocm_staff'])
        )

    def can_create_amendment(self, user) -> bool:
        """Check if user can create an amendment."""
        return (
            self.status == StrategicPlanStatus.APPROVED and
            user.has_role('planning_officer', self.tenant)
        )

    # Workflow action methods
    def submit(self, user, certifier, certification_title):
        """Submit plan for review."""
        if not self.can_submit(user):
            raise PermissionError('Cannot submit this plan')

        from django.utils import timezone
        self.status = StrategicPlanStatus.SUBMITTED
        self.submitted_at = timezone.now()
        self.submitted_by = user
        self.certified_at = timezone.now()
        self.certified_by = certifier
        self.certification_title = certification_title
        self.save()

        # Log status change
        StrategicPlanStatusHistory.objects.create(
            tenant=self.tenant,
            strategic_plan=self,
            from_status=StrategicPlanStatus.DRAFT,
            to_status=StrategicPlanStatus.SUBMITTED,
            changed_by=user,
            comment=f'Certified by {certification_title}'
        )

    def start_review(self, user):
        """Start review process."""
        if not self.can_review(user):
            raise PermissionError('Cannot review this plan')

        self.status = StrategicPlanStatus.UNDER_REVIEW
        self.save()

        StrategicPlanStatusHistory.objects.create(
            tenant=self.tenant,
            strategic_plan=self,
            from_status=StrategicPlanStatus.SUBMITTED,
            to_status=StrategicPlanStatus.UNDER_REVIEW,
            changed_by=user
        )

    def approve(self, user):
        """Approve the plan."""
        if not self.can_approve(user):
            raise PermissionError('Cannot approve this plan')

        from django.utils import timezone
        self.status = StrategicPlanStatus.APPROVED
        self.approved_at = timezone.now()
        self.approved_by = user
        self.reviewed_at = timezone.now()
        self.reviewed_by = user
        self.save()

        StrategicPlanStatusHistory.objects.create(
            tenant=self.tenant,
            strategic_plan=self,
            from_status=StrategicPlanStatus.UNDER_REVIEW,
            to_status=StrategicPlanStatus.APPROVED,
            changed_by=user
        )

    def return_for_revision(self, user, feedback):
        """Return plan for revisions."""
        if not self.can_return(user):
            raise PermissionError('Cannot return this plan')

        from django.utils import timezone
        self.status = StrategicPlanStatus.RETURNED
        self.reviewed_at = timezone.now()
        self.reviewed_by = user
        self.reviewer_feedback = feedback
        self.save()

        StrategicPlanStatusHistory.objects.create(
            tenant=self.tenant,
            strategic_plan=self,
            from_status=StrategicPlanStatus.UNDER_REVIEW,
            to_status=StrategicPlanStatus.RETURNED,
            changed_by=user,
            comment=feedback
        )

    def create_amendment(self, user, justification) -> 'StrategicPlan':
        """Create amendment version from approved plan."""
        if not self.can_create_amendment(user):
            raise PermissionError('Cannot create amendment')

        # Parse version and increment
        major, minor = self.version.split('.')
        new_version = f"{major}.{int(minor) + 1}"

        # Create new plan as amendment
        amendment = StrategicPlan.objects.create(
            tenant=self.tenant,
            title=self.title,
            description=self.description,
            status=StrategicPlanStatus.DRAFT,
            version=new_version,
            previous_version=self,
            is_amendment=True,
            amendment_justification=justification,
            planning_year=self.planning_year,
            bdp_period=self.bdp_period,
        )

        # Copy all related submodule data
        self._copy_submodules_to(amendment)

        return amendment

    def _copy_submodules_to(self, target):
        """Copy all 10 planning points to target plan."""
        # Point 1: Legal Alignments
        for item in self.legal_alignments.all():
            item.pk = None
            item.strategic_plan = target
            item.save()

        # Point 2: BDP Alignments
        for item in self.bdp_alignments.all():
            item.pk = None
            item.strategic_plan = target
            item.save()

        # Point 3: Priority Alignments
        for item in self.priority_alignments.all():
            item.pk = None
            item.strategic_plan = target
            item.save()

        # Point 4-10: Similar pattern for other submodules
        # ... (implement for each submodule)


class StrategicPlanStatusHistory(TenantScopedModel):
    """Audit trail for strategic plan status changes."""

    strategic_plan = models.ForeignKey(
        StrategicPlan,
        on_delete=models.CASCADE,
        related_name='status_history'
    )
    from_status = models.CharField(
        max_length=20,
        choices=StrategicPlanStatus.choices,
        null=True,
        blank=True
    )
    to_status = models.CharField(
        max_length=20,
        choices=StrategicPlanStatus.choices
    )
    changed_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ministerial_plan_status_history'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.strategic_plan} - {self.from_status} -> {self.to_status}"
```

### 7.2 TypeScript Types

```typescript
// types/strategic-plan-workflow.ts

export type StrategicPlanStatus =
  | 'draft'
  | 'submitted'
  | 'under_review'
  | 'returned'
  | 'approved';

export interface StrategicPlan {
  id: string;
  title: string;
  description: string;

  // Status
  status: StrategicPlanStatus;

  // Submission
  submittedAt: string | null;
  submittedBy: string | null;

  // Certification
  certifiedAt: string | null;
  certifiedBy: string | null;
  certificationTitle: string;

  // Review
  reviewedAt: string | null;
  reviewedBy: string | null;
  reviewerFeedback: string;

  // Approval
  approvedAt: string | null;
  approvedBy: string | null;

  // Version
  version: string;
  previousVersionId: string | null;
  isAmendment: boolean;
  amendmentJustification: string;

  // Planning cycle
  planningYear: number;
  bdpPeriod: string;

  // Timestamps
  createdAt: string;
  updatedAt: string;
}

export interface StatusTransition {
  action: 'submit' | 'start_review' | 'approve' | 'return' | 'create_amendment';
  fromStatus: StrategicPlanStatus;
  toStatus: StrategicPlanStatus;
  requiredRole: string[];
}

export const STATUS_TRANSITIONS: StatusTransition[] = [
  { action: 'submit', fromStatus: 'draft', toStatus: 'submitted', requiredRole: ['planning_officer'] },
  { action: 'start_review', fromStatus: 'submitted', toStatus: 'under_review', requiredRole: ['bpda_reviewer', 'ocm_staff'] },
  { action: 'approve', fromStatus: 'under_review', toStatus: 'approved', requiredRole: ['bpda_reviewer', 'ocm_staff'] },
  { action: 'return', fromStatus: 'under_review', toStatus: 'returned', requiredRole: ['bpda_reviewer', 'ocm_staff'] },
  { action: 'submit', fromStatus: 'returned', toStatus: 'submitted', requiredRole: ['planning_officer'] },
];

// Permission check helpers
export function canEdit(plan: StrategicPlan, userRole: string): boolean {
  return (
    ['draft', 'returned'].includes(plan.status) &&
    userRole === 'planning_officer'
  );
}

export function canSubmit(plan: StrategicPlan, userRole: string): boolean {
  return plan.status === 'draft' && userRole === 'planning_officer';
}

export function canCertify(plan: StrategicPlan, userRole: string): boolean {
  return plan.status === 'draft' && userRole === 'director';
}

export function canReview(plan: StrategicPlan, userRole: string): boolean {
  return (
    plan.status === 'submitted' &&
    ['bpda_reviewer', 'ocm_staff'].includes(userRole)
  );
}

export function canApprove(plan: StrategicPlan, userRole: string): boolean {
  return (
    plan.status === 'under_review' &&
    ['bpda_reviewer', 'ocm_staff'].includes(userRole)
  );
}

export function canCreateAmendment(plan: StrategicPlan, userRole: string): boolean {
  return plan.status === 'approved' && userRole === 'planning_officer';
}
```

### 7.3 API Endpoints

```typescript
// Workflow action endpoints
POST /api/v1/strategic-plans/{id}/submit/
POST /api/v1/strategic-plans/{id}/start-review/
POST /api/v1/strategic-plans/{id}/approve/
POST /api/v1/strategic-plans/{id}/return/
POST /api/v1/strategic-plans/{id}/create-amendment/

// Status history
GET /api/v1/strategic-plans/{id}/status-history/

// Version history
GET /api/v1/strategic-plans/{id}/versions/
```

---

## 8. Integration with Submodules

### 8.1 Submodule Architecture Reference

Each submodule architecture document should include this reference:

```markdown
## Data Lifecycle & Workflow

This submodule follows the standard Strategic Plan Workflow pattern.

**Reference**: `arch-pattern-workflow-lifecycle.md`

### Key Points:

1. **Workflow Level**: Strategic Plan (not individual submodule items)
2. **Edit Permissions**: Based on plan status (Draft/Returned = editable)
3. **Submission**: All 10 points submitted together with ministerial certification
4. **Amendment**: Same approval path as original (BPDA/OCM)
5. **Planning Cycle**: New submission each year/BDP period

### Submodule-Specific Completion Requirements:

| Requirement | Description |
|-------------|-------------|
| [Define minimum requirements for this submodule to be "complete"] |
```

### 8.2 Submodule Completion Check

Each submodule must implement a completion check:

```python
# Example for Priority Agenda submodule
def is_complete(self) -> bool:
    """Check if this submodule meets minimum completion requirements."""
    return (
        self.priority_alignments.exists() and
        self.priority_alignments.filter(contribution_description__isnull=False).exists()
    )
```

---

## 9. Implementation Checklist

Use this checklist when implementing the workflow pattern in a submodule:

### 9.1 Backend Implementation

- [ ] Submodule model inherits from `TenantScopedModel`
- [ ] Submodule model has FK to `StrategicPlan`
- [ ] `is_complete()` method implemented
- [ ] ViewSet respects `plan.can_edit(user)` for create/update/delete
- [ ] ViewSet respects `plan.status` for read-only enforcement

### 9.2 Frontend Implementation

- [ ] Form disabled when `plan.status` not in ['draft', 'returned']
- [ ] Status badge displayed showing current workflow state
- [ ] "Read-only" indicator when editing is disabled
- [ ] Reviewer feedback displayed when status is 'returned'
- [ ] Version history accessible

### 9.3 UI Components

- [ ] `WorkflowStatusBadge` - Shows current status
- [ ] `WorkflowTimeline` - Shows status history
- [ ] `CertificationPanel` - For ministerial certification
- [ ] `ReviewerFeedbackPanel` - Shows/adds reviewer comments
- [ ] `AmendmentDialog` - For creating amendments

### 9.4 Testing

- [ ] Unit tests for permission check methods
- [ ] Integration tests for workflow transitions
- [ ] E2E tests for complete submission flow

---

## References

| Document | Description |
|----------|-------------|
| `arch-mod-planning.md` | Parent module architecture |
| `arch-subm-planning-03-priority-agenda.md` | Example submodule with workflow integrated |
| BARMM Strategic Planning Guidelines | Official planning guidelines |

---

**Document End**

*This pattern ensures consistent workflow behavior across all 10 planning points while maintaining proper approval chains and audit trails.*
