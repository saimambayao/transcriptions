# CSEA Admin Portal User Journeys

User journey maps and UX patterns for CSEA staff managing cooperatives and social enterprises.

## Table of Contents
- [User Personas](#user-personas)
- [Registration Review Journey](#registration-review-journey)
- [Compliance Monitoring Journey](#compliance-monitoring-journey)
- [Analytics & Reporting Journey](#analytics--reporting-journey)
- [User Management Journey](#user-management-journey)

## BARMM Governance Context (BDP 2023-2028)

The Bangsamoro Development Plan 2023-2028 establishes the governance framework for CSEA operations within the Bangsamoro Autonomous Region.

### Overall Goal
An **empowered, cohesive, and progressive Bangsamoro**:
- **Empowered**: Improved capacity through better access to services and economic opportunities
- **Cohesive**: Improved relationships between stakeholders, reduced conflict, forged partnerships
- **Progressive**: Sustained ability to optimize resources for development needs

### Goal 1: Stable, Just, and Accountable Government
CSEA operates within this goal framework:
- **Stable**: Continuity of service delivery during political events or emergencies
- **Just**: Government as primary agent of economic and social justice
- **Accountable**: Frameworks to recognize good performance and stop bad practices

### Pillars of Moral Governance (CSEA Operations)
CSEA staff must embody these principles from BDP 2023-2028:
1. **Integrity** - No financial influence on official duties
2. **Accountability** - Open and transparent decisions, documented
3. **Transparency and Honesty** - Declare interests, resolve conflicts
4. **Justice** - Serve without prejudice regardless of family or political alliances
5. **Inclusivity** - Foster environment free from discrimination based on religion, ethnicity, culture
6. **Objectivity** - Merit-based decisions in public appointments and approvals
7. **Dialogue and Meaningful Engagement** - Consult with community on what needs to be addressed

### Geographic Service Coverage
CSEA serves cooperatives and social enterprises across:
- **5 Provinces**: Maguindanao (split into 2 divisions), Lanao del Sur (split into 2 divisions), Basilan, Sulu, Tawi-Tawi
- **3 Cities**: Marawi City, Lamitan City, Cotabato City
- **Special Geographic Area**: 63 barangays in North Cotabato
- **2,590 Total Barangays** across the region

### Regulatory Context
- Cooperatives registered under CDA with BARMM oversight
- Social enterprises under CSEA regulatory framework
- FRAMES compliance monitoring for sustainability standards
- Integration with national programs (4Ps, SLP, Social Pension)

---

## User Personas

### Registration Officer
- **Goal**: Process new cooperative/SE registrations efficiently with fairness and transparency
- **Behavior**: Reviews applications daily, verifies documents, ensures compliance
- **Pain Points**: Incomplete submissions, back-and-forth communication, geographic barriers
- **Needs**: Checklist-driven workflow, communication templates, batch processing
- **BARMM Context**: Must handle applications from remote island provinces (BaSulTa) and GIDA areas; ensures objectivity regardless of applicant's tribal or political affiliation

### Compliance Auditor (FRAMES Monitor)
- **Goal**: Ensure all registered entities meet FRAMES regulatory requirements
- **Behavior**: Reviews compliance status, schedules inspections, tracks sustainability indicators
- **Pain Points**: Tracking multiple deadlines, inconsistent data, travel to far-flung areas
- **Needs**: Dashboard with alerts, calendar integration, document management, offline capability
- **BARMM Context**: Must coordinate with 2,590 barangays across island and mainland provinces; respects local governance structures

### CSEA Administrator
- **Goal**: Oversee platform operations and access control with accountability
- **Behavior**: Manages users, reviews reports, configures settings, maintains audit trails
- **Pain Points**: Audit trail visibility, permission management, ensuring staff accountability
- **Needs**: User management tools, activity logs, analytics, role-based access control
- **BARMM Context**: Implements moral governance principles; ensures system supports stable, just administration

### Policy Analyst
- **Goal**: Generate insights for BDP-aligned policy decisions
- **Behavior**: Analyzes sector data, creates reports aligned with development goals
- **Pain Points**: Data extraction, manual report generation, aligning metrics with BDP targets
- **Needs**: Export tools, visualization dashboards, automated reports, BDP indicator tracking
- **BARMM Context**: Reports on cooperative/SE contribution to Goal 2 (equitable economy), poverty reduction targets

### Provincial Coordinator
- **Goal**: Oversee cooperative/SE development within specific province
- **Behavior**: Reviews provincial statistics, coordinates with LGUs, manages field staff
- **Pain Points**: Coordination across municipalities, varying LGU engagement levels
- **Needs**: Provincial dashboard, LGU communication tools, field monitoring reports
- **BARMM Context**: Different provinces have different challenges (island vs. mainland, peace & order, connectivity)

---

## Registration Review Journey

### Application Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Submitted  │───▶│  Under      │───▶│  Approved/  │───▶│  Active     │
│             │    │  Review     │    │  Rejected   │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │
      ▼                  ▼                  ▼
  Auto-assign       Checklist          Notification
  to reviewer       verification       to applicant
```

### Registration Queue

**Prioritize and distribute workload**:
```tsx
// Registration Queue
<div className="space-y-6">
  {/* Queue Stats */}
  <div className="grid grid-cols-4 gap-4">
    <StatCard
      title="Pending Review"
      value={stats.pending}
      icon={Inbox}
      highlight={stats.pending > 10}
    />
    <StatCard
      title="Under Review"
      value={stats.inReview}
      icon={Eye}
    />
    <StatCard
      title="Approved Today"
      value={stats.approvedToday}
      icon={CheckCircle}
      className="text-green-600"
    />
    <StatCard
      title="Avg. Processing Time"
      value={`${stats.avgDays} days`}
      icon={Clock}
    />
  </div>

  {/* Filters & Actions */}
  <div className="flex items-center justify-between">
    <div className="flex items-center gap-4">
      <Select defaultValue="pending">
        <SelectTrigger className="w-40">
          <SelectValue />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Applications</SelectItem>
          <SelectItem value="pending">Pending</SelectItem>
          <SelectItem value="in-review">Under Review</SelectItem>
          <SelectItem value="needs-info">Needs Information</SelectItem>
        </SelectContent>
      </Select>
      <Select defaultValue="all">
        <SelectTrigger className="w-40">
          <SelectValue />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Types</SelectItem>
          <SelectItem value="cooperative">Cooperatives</SelectItem>
          <SelectItem value="social-enterprise">Social Enterprises</SelectItem>
        </SelectContent>
      </Select>
      <Input placeholder="Search by name or reference..." className="w-64" />
    </div>
    <div className="flex gap-2">
      <Button variant="outline">
        <Download className="h-4 w-4 mr-2" />
        Export
      </Button>
      <Button>
        <UserPlus className="h-4 w-4 mr-2" />
        Assign Reviewer
      </Button>
    </div>
  </div>

  {/* Application Table */}
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead className="w-12">
          <Checkbox />
        </TableHead>
        <TableHead>Reference</TableHead>
        <TableHead>Organization</TableHead>
        <TableHead>Type</TableHead>
        <TableHead>Submitted</TableHead>
        <TableHead>Status</TableHead>
        <TableHead>Reviewer</TableHead>
        <TableHead className="w-12"></TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      {applications.map((app) => (
        <TableRow key={app.id}>
          <TableCell>
            <Checkbox />
          </TableCell>
          <TableCell className="font-mono text-sm">{app.reference}</TableCell>
          <TableCell>
            <div>
              <p className="font-medium">{app.organizationName}</p>
              <p className="text-sm text-muted-foreground">{app.municipality}</p>
            </div>
          </TableCell>
          <TableCell>
            <Badge variant="outline">{app.type}</Badge>
          </TableCell>
          <TableCell>
            <div>
              <p className="text-sm">{formatDate(app.submittedAt)}</p>
              <p className="text-xs text-muted-foreground">
                {formatRelativeTime(app.submittedAt)}
              </p>
            </div>
          </TableCell>
          <TableCell>
            <ApplicationStatusBadge status={app.status} />
          </TableCell>
          <TableCell>
            {app.reviewer ? (
              <div className="flex items-center gap-2">
                <Avatar className="h-6 w-6">
                  <AvatarImage src={app.reviewer.avatar} />
                  <AvatarFallback>{app.reviewer.initials}</AvatarFallback>
                </Avatar>
                <span className="text-sm">{app.reviewer.name}</span>
              </div>
            ) : (
              <span className="text-sm text-muted-foreground">Unassigned</span>
            )}
          </TableCell>
          <TableCell>
            <Button variant="ghost" size="sm" asChild>
              <Link href={`/csea/registrations/${app.id}`}>
                Review
              </Link>
            </Button>
          </TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>
</div>
```

### Application Review Page

**Checklist-driven verification**:
```tsx
// Application Review
<div className="grid lg:grid-cols-3 gap-6">
  {/* Main Content */}
  <div className="lg:col-span-2 space-y-6">
    {/* Header */}
    <div className="flex items-start justify-between">
      <div>
        <div className="flex items-center gap-2">
          <h1 className="text-2xl font-bold">{application.organizationName}</h1>
          <ApplicationStatusBadge status={application.status} />
        </div>
        <p className="text-muted-foreground">
          Reference: {application.reference} • Submitted {formatDate(application.submittedAt)}
        </p>
      </div>
      <div className="flex gap-2">
        <Button variant="outline" onClick={requestMoreInfo}>
          <MessageSquare className="h-4 w-4 mr-2" />
          Request Info
        </Button>
        <Button variant="destructive" onClick={openRejectDialog}>
          <X className="h-4 w-4 mr-2" />
          Reject
        </Button>
        <Button onClick={openApproveDialog}>
          <Check className="h-4 w-4 mr-2" />
          Approve
        </Button>
      </div>
    </div>

    {/* Organization Details */}
    <Card>
      <CardHeader>
        <CardTitle>Organization Information</CardTitle>
      </CardHeader>
      <CardContent>
        <dl className="grid grid-cols-2 gap-4">
          <div>
            <dt className="text-sm text-muted-foreground">Type</dt>
            <dd className="font-medium">{application.type}</dd>
          </div>
          <div>
            <dt className="text-sm text-muted-foreground">Registration Date</dt>
            <dd className="font-medium">{formatDate(application.registrationDate)}</dd>
          </div>
          <div>
            <dt className="text-sm text-muted-foreground">Province</dt>
            <dd className="font-medium">{application.province}</dd>
          </div>
          <div>
            <dt className="text-sm text-muted-foreground">Municipality</dt>
            <dd className="font-medium">{application.municipality}</dd>
          </div>
          <div>
            <dt className="text-sm text-muted-foreground">Number of Members</dt>
            <dd className="font-medium">{application.memberCount}</dd>
          </div>
          <div>
            <dt className="text-sm text-muted-foreground">Primary Sector</dt>
            <dd className="font-medium">{application.sector}</dd>
          </div>
        </dl>
      </CardContent>
    </Card>

    {/* Documents */}
    <Card>
      <CardHeader>
        <CardTitle>Submitted Documents</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          {application.documents.map((doc) => (
            <div
              key={doc.id}
              className="flex items-center justify-between p-3 border rounded-lg"
            >
              <div className="flex items-center gap-3">
                <FileText className="h-5 w-5 text-muted-foreground" />
                <div>
                  <p className="font-medium">{doc.name}</p>
                  <p className="text-sm text-muted-foreground">
                    {doc.type} • {formatFileSize(doc.size)}
                  </p>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <DocumentStatusBadge status={doc.verificationStatus} />
                <Button variant="ghost" size="sm">
                  <Eye className="h-4 w-4 mr-2" />
                  View
                </Button>
              </div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>

    {/* Contact Information */}
    <Card>
      <CardHeader>
        <CardTitle>Contact Person</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex items-center gap-4">
          <Avatar className="h-12 w-12">
            <AvatarFallback>{application.contact.initials}</AvatarFallback>
          </Avatar>
          <div>
            <p className="font-medium">{application.contact.name}</p>
            <p className="text-sm text-muted-foreground">{application.contact.position}</p>
            <div className="flex gap-4 mt-2 text-sm">
              <span className="flex items-center gap-1">
                <Mail className="h-4 w-4" />
                {application.contact.email}
              </span>
              <span className="flex items-center gap-1">
                <Phone className="h-4 w-4" />
                {application.contact.phone}
              </span>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  </div>

  {/* Sidebar - Verification Checklist */}
  <div className="space-y-6">
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center justify-between">
          Verification Checklist
          <Badge variant="outline">
            {checklist.filter(c => c.verified).length}/{checklist.length}
          </Badge>
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-3">
        {checklist.map((item) => (
          <div
            key={item.id}
            className="flex items-start gap-3 p-2 rounded-lg hover:bg-muted/50"
          >
            <Checkbox
              checked={item.verified}
              onCheckedChange={(checked) => updateChecklistItem(item.id, checked)}
            />
            <div className="flex-1">
              <p className={cn(
                "text-sm font-medium",
                item.verified && "line-through text-muted-foreground"
              )}>
                {item.label}
              </p>
              {item.note && (
                <p className="text-xs text-muted-foreground mt-1">{item.note}</p>
              )}
            </div>
          </div>
        ))}
      </CardContent>
    </Card>

    {/* Activity Log */}
    <Card>
      <CardHeader>
        <CardTitle>Activity Log</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {activities.map((activity) => (
          <div key={activity.id} className="flex gap-3 text-sm">
            <div className="h-2 w-2 rounded-full bg-muted-foreground mt-2 shrink-0" />
            <div>
              <p>{activity.description}</p>
              <p className="text-xs text-muted-foreground">
                {activity.user} • {formatRelativeTime(activity.timestamp)}
              </p>
            </div>
          </div>
        ))}
      </CardContent>
    </Card>

    {/* Internal Notes */}
    <Card>
      <CardHeader>
        <CardTitle>Internal Notes</CardTitle>
      </CardHeader>
      <CardContent>
        <Textarea
          placeholder="Add notes visible only to CSEA staff..."
          value={notes}
          onChange={(e) => setNotes(e.target.value)}
          rows={4}
        />
        <Button className="mt-2" size="sm" variant="outline">
          Save Note
        </Button>
      </CardContent>
    </Card>
  </div>
</div>
```

---

## Compliance Monitoring Journey

### Compliance Dashboard

```tsx
// Compliance Overview
<div className="space-y-6">
  {/* Alert Banner */}
  {expiringSoon.length > 0 && (
    <Alert>
      <AlertTriangle className="h-4 w-4" />
      <AlertTitle>Compliance Alerts</AlertTitle>
      <AlertDescription>
        {expiringSoon.length} organizations have documents expiring within 30 days
      </AlertDescription>
    </Alert>
  )}

  {/* Compliance Stats */}
  <div className="grid grid-cols-4 gap-4">
    <StatCard
      title="Fully Compliant"
      value={stats.compliant}
      total={stats.total}
      icon={ShieldCheck}
      color="green"
    />
    <StatCard
      title="Pending Review"
      value={stats.pendingReview}
      icon={Clock}
      color="yellow"
    />
    <StatCard
      title="Non-Compliant"
      value={stats.nonCompliant}
      icon={AlertCircle}
      color="red"
      highlight
    />
    <StatCard
      title="Expiring Soon"
      value={stats.expiringSoon}
      icon={Calendar}
      color="orange"
    />
  </div>

  {/* Compliance Table */}
  <Card>
    <CardHeader>
      <div className="flex items-center justify-between">
        <CardTitle>Organization Compliance</CardTitle>
        <div className="flex gap-2">
          <Input placeholder="Search..." className="w-64" />
          <Select defaultValue="all">
            <SelectTrigger className="w-40">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Status</SelectItem>
              <SelectItem value="compliant">Compliant</SelectItem>
              <SelectItem value="expiring">Expiring Soon</SelectItem>
              <SelectItem value="non-compliant">Non-Compliant</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>
    </CardHeader>
    <CardContent>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Organization</TableHead>
            <TableHead>Type</TableHead>
            <TableHead>CDA Registration</TableHead>
            <TableHead>Business Permit</TableHead>
            <TableHead>BIR</TableHead>
            <TableHead>Overall Status</TableHead>
            <TableHead className="w-12"></TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {organizations.map((org) => (
            <TableRow key={org.id}>
              <TableCell>
                <div>
                  <p className="font-medium">{org.name}</p>
                  <p className="text-sm text-muted-foreground">{org.location}</p>
                </div>
              </TableCell>
              <TableCell>
                <Badge variant="outline">{org.type}</Badge>
              </TableCell>
              <TableCell>
                <DocumentExpiryBadge
                  status={org.cdaRegistration.status}
                  expiryDate={org.cdaRegistration.expiryDate}
                />
              </TableCell>
              <TableCell>
                <DocumentExpiryBadge
                  status={org.businessPermit.status}
                  expiryDate={org.businessPermit.expiryDate}
                />
              </TableCell>
              <TableCell>
                <DocumentExpiryBadge
                  status={org.birRegistration.status}
                  expiryDate={org.birRegistration.expiryDate}
                />
              </TableCell>
              <TableCell>
                <ComplianceStatusBadge status={org.overallStatus} />
              </TableCell>
              <TableCell>
                <Button variant="ghost" size="sm" asChild>
                  <Link href={`/csea/organizations/${org.id}/compliance`}>
                    View
                  </Link>
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </CardContent>
  </Card>
</div>
```

### Document Expiry Badge Component

```tsx
// Document Expiry Badge
function DocumentExpiryBadge({ status, expiryDate }: { status: string; expiryDate?: Date }) {
  if (status === 'missing') {
    return (
      <Badge variant="destructive" className="gap-1">
        <X className="h-3 w-3" />
        Missing
      </Badge>
    );
  }

  if (!expiryDate) {
    return (
      <Badge variant="secondary" className="gap-1">
        <HelpCircle className="h-3 w-3" />
        Unknown
      </Badge>
    );
  }

  const daysUntilExpiry = differenceInDays(expiryDate, new Date());

  if (daysUntilExpiry < 0) {
    return (
      <Badge variant="destructive" className="gap-1">
        <AlertCircle className="h-3 w-3" />
        Expired
      </Badge>
    );
  }

  if (daysUntilExpiry < 30) {
    return (
      <Badge variant="warning" className="gap-1">
        <Clock className="h-3 w-3" />
        {daysUntilExpiry}d left
      </Badge>
    );
  }

  return (
    <Badge variant="success" className="gap-1">
      <CheckCircle className="h-3 w-3" />
      Valid
    </Badge>
  );
}
```

---

## Analytics & Reporting Journey

### Analytics Dashboard

```tsx
// CSEA Analytics
<div className="space-y-6">
  {/* Period Selector */}
  <div className="flex items-center justify-between">
    <h1 className="text-2xl font-bold">Platform Analytics</h1>
    <div className="flex gap-2">
      <Select defaultValue="30d">
        <SelectTrigger className="w-40">
          <SelectValue />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="7d">Last 7 days</SelectItem>
          <SelectItem value="30d">Last 30 days</SelectItem>
          <SelectItem value="90d">Last 90 days</SelectItem>
          <SelectItem value="1y">Last year</SelectItem>
        </SelectContent>
      </Select>
      <Button variant="outline">
        <Download className="h-4 w-4 mr-2" />
        Export Report
      </Button>
    </div>
  </div>

  {/* Key Metrics */}
  <div className="grid grid-cols-4 gap-4">
    <StatCard
      title="Total Cooperatives"
      value={metrics.totalCoops}
      change={{ value: metrics.coopsGrowth, trend: 'up' }}
      icon={Building}
    />
    <StatCard
      title="Social Enterprises"
      value={metrics.totalSEs}
      change={{ value: metrics.seGrowth, trend: 'up' }}
      icon={Store}
    />
    <StatCard
      title="Total Products"
      value={metrics.totalProducts}
      change={{ value: metrics.productsGrowth, trend: 'up' }}
      icon={Package}
    />
    <StatCard
      title="Platform GMV"
      value={`PHP ${formatCurrency(metrics.gmv)}`}
      change={{ value: metrics.gmvGrowth, trend: 'up' }}
      icon={TrendingUp}
    />
  </div>

  {/* Charts Row */}
  <div className="grid lg:grid-cols-2 gap-6">
    {/* Registration Trend */}
    <Card>
      <CardHeader>
        <CardTitle>Registration Trend</CardTitle>
      </CardHeader>
      <CardContent>
        <RegistrationChart data={registrationData} />
      </CardContent>
    </Card>

    {/* Sector Distribution */}
    <Card>
      <CardHeader>
        <CardTitle>Sector Distribution</CardTitle>
      </CardHeader>
      <CardContent>
        <SectorPieChart data={sectorData} />
      </CardContent>
    </Card>
  </div>

  {/* Geographic Distribution */}
  <Card>
    <CardHeader>
      <CardTitle>Geographic Distribution</CardTitle>
    </CardHeader>
    <CardContent>
      <div className="grid lg:grid-cols-2 gap-6">
        {/* Map */}
        <div className="h-[400px] rounded-lg bg-muted">
          <BARMMMap data={geographicData} />
        </div>

        {/* Province Breakdown */}
        <div className="space-y-4">
          {provinces.map((province) => (
            <div key={province.name} className="space-y-2">
              <div className="flex justify-between text-sm">
                <span>{province.name}</span>
                <span className="font-medium">{province.count}</span>
              </div>
              <Progress value={(province.count / maxCount) * 100} />
            </div>
          ))}
        </div>
      </div>
    </CardContent>
  </Card>
</div>
```

---

## User Management Journey

### User List with Roles

```tsx
// User Management
<div className="space-y-6">
  <div className="flex items-center justify-between">
    <div>
      <h1 className="text-2xl font-bold">User Management</h1>
      <p className="text-muted-foreground">
        Manage CSEA staff access and permissions
      </p>
    </div>
    <Button>
      <UserPlus className="h-4 w-4 mr-2" />
      Invite User
    </Button>
  </div>

  {/* Role Filter Tabs */}
  <Tabs defaultValue="all">
    <TabsList>
      <TabsTrigger value="all">
        All Users ({users.length})
      </TabsTrigger>
      <TabsTrigger value="admin">
        Administrators ({users.filter(u => u.role === 'admin').length})
      </TabsTrigger>
      <TabsTrigger value="reviewer">
        Reviewers ({users.filter(u => u.role === 'reviewer').length})
      </TabsTrigger>
      <TabsTrigger value="auditor">
        Auditors ({users.filter(u => u.role === 'auditor').length})
      </TabsTrigger>
    </TabsList>

    <TabsContent value="all" className="mt-4">
      <Card>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>User</TableHead>
              <TableHead>Role</TableHead>
              <TableHead>Status</TableHead>
              <TableHead>Last Active</TableHead>
              <TableHead className="w-12"></TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {users.map((user) => (
              <TableRow key={user.id}>
                <TableCell>
                  <div className="flex items-center gap-3">
                    <Avatar>
                      <AvatarImage src={user.avatar} />
                      <AvatarFallback>{user.initials}</AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="font-medium">{user.name}</p>
                      <p className="text-sm text-muted-foreground">{user.email}</p>
                    </div>
                  </div>
                </TableCell>
                <TableCell>
                  <RoleBadge role={user.role} />
                </TableCell>
                <TableCell>
                  <Badge variant={user.status === 'active' ? 'success' : 'secondary'}>
                    {user.status}
                  </Badge>
                </TableCell>
                <TableCell className="text-muted-foreground">
                  {formatRelativeTime(user.lastActive)}
                </TableCell>
                <TableCell>
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button variant="ghost" size="icon">
                        <MoreHorizontal className="h-4 w-4" />
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                      <DropdownMenuItem>
                        <Eye className="h-4 w-4 mr-2" />
                        View Profile
                      </DropdownMenuItem>
                      <DropdownMenuItem>
                        <Pencil className="h-4 w-4 mr-2" />
                        Edit Permissions
                      </DropdownMenuItem>
                      <DropdownMenuSeparator />
                      <DropdownMenuItem className="text-destructive">
                        <UserX className="h-4 w-4 mr-2" />
                        Deactivate
                      </DropdownMenuItem>
                    </DropdownMenuContent>
                  </DropdownMenu>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Card>
    </TabsContent>
  </Tabs>
</div>
```

---

## Key UX Principles for Admin Portals

### 1. Efficiency Over Beauty
- Keyboard shortcuts for common actions
- Bulk operations support
- Quick filters and saved views

### 2. Complete Audit Trail
- Log all actions with timestamps
- Show who did what and when
- Support compliance reporting

### 3. Role-Based Views
- Show only relevant information
- Hide actions user can't perform
- Adapt dashboard to role

### 4. Data Export
- Export to Excel/CSV
- Generate PDF reports
- Schedule automated reports

### 5. Clear Status Hierarchy
- Visual distinction between status levels
- Consistent color coding
- Prominent alerts for urgent items

---

## BARMM-Specific Analytics Context (BDP 2023-2028)

### Key Performance Indicators for CSEA
Based on BDP 2023-2028 development goals, CSEA dashboards should track:

#### Economic Indicators (Goal 2)
| Indicator | Baseline (2021) | Target (2028) | CSEA Contribution |
|-----------|-----------------|---------------|-------------------|
| Poverty Incidence | 29.8% | 20-25% | Jobs created via coops/SEs |
| Underemployment | 9.9% | 4-7% | Quality employment through coops |
| GRDP Growth | -- | 5-7% annually | SE/Coop economic contribution |

#### Cooperative/SE Development Metrics
- Number of registered cooperatives by province
- Number of registered social enterprises by sector
- FRAMES compliance rate
- Active vs inactive organizations
- Employment generated (members + workers)
- Gross sales/revenue of registered entities
- Products listed on marketplace

#### Geographic Distribution
CSEA must monitor coverage across:
- 5 provinces (with Maguindanao and Lanao del Sur split into divisions)
- 3 cities
- 116 municipalities
- 2,590 barangays
- Special Geographic Area (63 barangays in North Cotabato)

### Vulnerable Sector Tracking
Per BDP Chapter 9, monitor cooperative/SE support for:

| Sector | Key Metrics |
|--------|-------------|
| **Women's Organizations** | Coops led by women, women membership % |
| **Youth Organizations** | Youth cooperatives, young entrepreneur SEs |
| **Indigenous Peoples** | IP-led coops, traditional product enterprises |
| **PWD Organizations** | PWD-inclusive coops, accessibility compliance |
| **Farmer Cooperatives** | Agricultural coops, MAFAR linkages |
| **Fisher Cooperatives** | Fishery sector, island province focus |

### Inter-Agency Coordination
CSEA analytics should support coordination with:
- **MAFAR**: Agricultural cooperative registration linkages
- **MTIT**: Trade facilitation for cooperative products
- **MSSD**: Social protection beneficiary tracking
- **MBHTE**: Training and capacity building partnerships
- **BDA**: Special development projects for cooperatives

### Report Generation Requirements
Standard reports for BDP monitoring:
1. **Monthly Registration Report** - New registrations by type, province
2. **Quarterly Compliance Report** - FRAMES status summary
3. **Semi-Annual Impact Report** - Jobs created, revenue generated
4. **Annual BDP Contribution Report** - Alignment with development goals
5. **Ad-Hoc Reports** - For policy decisions, development partner requests

### Moral Governance Dashboard
Per BDP Chapter 4 principles, track staff performance on:
- Application processing time (accountability)
- Rejection rate transparency (justice)
- User feedback scores (dialogue and engagement)
- Conflict of interest declarations (integrity)
- Equal treatment across provinces/groups (inclusivity)
