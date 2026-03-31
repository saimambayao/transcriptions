# Compliance & FRAMES User Journeys

Cross-cutting compliance journeys for Cooperatives, Social Enterprises, and CSEA staff implementing the FRAMES regulatory framework.

## Table of Contents
- [Overview](#overview)
- [Coop/SE Registration Journey](#coopse-registration-journey)
- [Document Submission Journey](#document-submission-journey)
- [FRAMES Compliance Journey](#frames-compliance-journey)
- [Renewal & Maintenance Journey](#renewal--maintenance-journey)

## Overview

### FRAMES Framework
FRAMES is CSEA's comprehensive regulatory framework for cooperatives and social enterprises:
- **F**ormation - Initial organization setup and documentation
- **R**egistration - Official registration and certification
- **A**uditing - Financial and operational audits
- **M**onitoring & Evaluation - Ongoing performance tracking
- **E**nforcement - Compliance enforcement actions
- **S**ustainability - Long-term viability assessment

### Key User Flows
| User | Journey | Goal |
|------|---------|------|
| Coop/SE Manager | Registration | Get approved to sell on platform |
| Coop/SE Manager | Document Submission | Upload required compliance documents |
| Coop/SE Manager | Renewal | Maintain active status |
| CSEA Reviewer | Application Review | Verify and approve registrations |
| CSEA Auditor | Compliance Monitoring | Ensure ongoing compliance |

---

## Coop/SE Registration Journey

### Registration Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Start      │───▶│  Basic      │───▶│  Document   │───▶│  Review     │───▶│  Approved   │
│  Application│    │  Information│    │  Upload     │    │  Period     │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                            │                  │
                                            ▼                  ▼
                                      Required docs:      CSEA reviews
                                      - CDA Registration  (3-5 days)
                                      - Business Permit
                                      - BIR Registration
```

### Step 1: Application Start

```tsx
// Registration Type Selection
<div className="container max-w-2xl py-12">
  <div className="text-center mb-8">
    <h1 className="text-2xl font-bold">Register Your Organization</h1>
    <p className="text-muted-foreground mt-2">
      Join the Negosyo platform and reach customers across Bangsamoro
    </p>
  </div>

  <div className="grid md:grid-cols-2 gap-6">
    {/* Cooperative */}
    <Card
      className={cn(
        "cursor-pointer transition-all hover:border-primary",
        selectedType === 'cooperative' && "border-primary ring-2 ring-primary/20"
      )}
      onClick={() => setSelectedType('cooperative')}
    >
      <CardContent className="p-6 text-center">
        <div className="h-16 w-16 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
          <Users className="h-8 w-8 text-primary" />
        </div>
        <h3 className="font-semibold text-lg">Cooperative</h3>
        <p className="text-sm text-muted-foreground mt-2">
          A member-owned organization registered with CDA
        </p>
        <ul className="text-sm text-left mt-4 space-y-2">
          <li className="flex items-center gap-2">
            <Check className="h-4 w-4 text-green-600" />
            CDA Registration required
          </li>
          <li className="flex items-center gap-2">
            <Check className="h-4 w-4 text-green-600" />
            Member-owned structure
          </li>
          <li className="flex items-center gap-2">
            <Check className="h-4 w-4 text-green-600" />
            Democratic governance
          </li>
        </ul>
      </CardContent>
    </Card>

    {/* Social Enterprise */}
    <Card
      className={cn(
        "cursor-pointer transition-all hover:border-primary",
        selectedType === 'social-enterprise' && "border-primary ring-2 ring-primary/20"
      )}
      onClick={() => setSelectedType('social-enterprise')}
    >
      <CardContent className="p-6 text-center">
        <div className="h-16 w-16 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
          <Building className="h-8 w-8 text-primary" />
        </div>
        <h3 className="font-semibold text-lg">Social Enterprise</h3>
        <p className="text-sm text-muted-foreground mt-2">
          A business with a social or environmental mission
        </p>
        <ul className="text-sm text-left mt-4 space-y-2">
          <li className="flex items-center gap-2">
            <Check className="h-4 w-4 text-green-600" />
            DTI/SEC Registration required
          </li>
          <li className="flex items-center gap-2">
            <Check className="h-4 w-4 text-green-600" />
            Social impact focus
          </li>
          <li className="flex items-center gap-2">
            <Check className="h-4 w-4 text-green-600" />
            Profit with purpose
          </li>
        </ul>
      </CardContent>
    </Card>
  </div>

  <div className="mt-8 text-center">
    <Button size="lg" disabled={!selectedType}>
      Continue
      <ChevronRight className="h-4 w-4 ml-2" />
    </Button>
  </div>

  {/* Help Section */}
  <Card className="mt-8 bg-muted/50">
    <CardContent className="p-4 flex items-start gap-4">
      <HelpCircle className="h-5 w-5 text-muted-foreground shrink-0 mt-0.5" />
      <div>
        <p className="font-medium text-sm">Not sure which to choose?</p>
        <p className="text-sm text-muted-foreground">
          If you're registered with CDA as a cooperative, choose Cooperative.
          Otherwise, if you have a business with social impact goals, choose Social Enterprise.
        </p>
        <Button variant="link" className="p-0 h-auto mt-2" asChild>
          <Link href="/help/registration-types">Learn more</Link>
        </Button>
      </div>
    </CardContent>
  </Card>
</div>
```

### Step 2: Organization Information

```tsx
// Multi-step Registration Form
<div className="container max-w-2xl py-8">
  {/* Progress Steps */}
  <div className="mb-8">
    <div className="flex items-center justify-between">
      {steps.map((step, i) => (
        <div key={step.id} className="flex items-center">
          <div className={cn(
            "flex items-center justify-center w-10 h-10 rounded-full text-sm font-medium",
            i < currentStep && "bg-green-600 text-white",
            i === currentStep && "bg-primary text-white",
            i > currentStep && "bg-muted text-muted-foreground"
          )}>
            {i < currentStep ? <Check className="h-5 w-5" /> : i + 1}
          </div>
          <div className="ml-3 hidden sm:block">
            <p className={cn(
              "text-sm font-medium",
              i <= currentStep ? "text-foreground" : "text-muted-foreground"
            )}>
              {step.title}
            </p>
          </div>
          {i < steps.length - 1 && (
            <div className={cn(
              "w-12 md:w-24 h-0.5 mx-4",
              i < currentStep ? "bg-green-600" : "bg-muted"
            )} />
          )}
        </div>
      ))}
    </div>
  </div>

  {/* Form Content */}
  <Card>
    <CardHeader>
      <CardTitle>{steps[currentStep].title}</CardTitle>
      <CardDescription>{steps[currentStep].description}</CardDescription>
    </CardHeader>
    <CardContent>
      {currentStep === 0 && (
        <div className="space-y-4">
          <div className="space-y-2">
            <Label>Organization Name *</Label>
            <Input placeholder="Official registered name" />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label>Registration Number *</Label>
              <Input placeholder="CDA/SEC/DTI Number" />
            </div>
            <div className="space-y-2">
              <Label>Date of Registration *</Label>
              <DatePicker />
            </div>
          </div>

          <div className="space-y-2">
            <Label>Primary Sector *</Label>
            <Select>
              <SelectTrigger>
                <SelectValue placeholder="Select sector" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="agriculture">Agriculture & Fisheries</SelectItem>
                <SelectItem value="handicrafts">Handicrafts & Weaving</SelectItem>
                <SelectItem value="food">Food Processing</SelectItem>
                <SelectItem value="services">Services</SelectItem>
                <SelectItem value="retail">Retail & Trading</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <div className="space-y-2">
            <Label>Number of Members/Employees *</Label>
            <Input type="number" placeholder="0" />
          </div>

          <div className="space-y-2">
            <Label>Brief Description *</Label>
            <Textarea
              placeholder="Describe your organization's activities, products, and social impact..."
              rows={4}
            />
          </div>
        </div>
      )}

      {currentStep === 1 && (
        <div className="space-y-4">
          {/* Address fields */}
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label>Province *</Label>
              <Select onValueChange={setProvince}>
                <SelectTrigger>
                  <SelectValue placeholder="Select province" />
                </SelectTrigger>
                <SelectContent>
                  {provinces.map(p => (
                    <SelectItem key={p.id} value={p.id}>{p.name}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label>Municipality *</Label>
              <Select disabled={!province}>
                <SelectTrigger>
                  <SelectValue placeholder="Select municipality" />
                </SelectTrigger>
                <SelectContent>
                  {municipalities.map(m => (
                    <SelectItem key={m.id} value={m.id}>{m.name}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
          </div>

          <div className="space-y-2">
            <Label>Barangay *</Label>
            <Select disabled={!municipality}>
              <SelectTrigger>
                <SelectValue placeholder="Select barangay" />
              </SelectTrigger>
              <SelectContent>
                {barangays.map(b => (
                  <SelectItem key={b.id} value={b.id}>{b.name}</SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>

          <div className="space-y-2">
            <Label>Street Address *</Label>
            <Input placeholder="Building, street name, landmarks" />
          </div>

          <Separator className="my-6" />

          <h4 className="font-medium">Contact Person</h4>

          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label>Full Name *</Label>
              <Input placeholder="Juan Dela Cruz" />
            </div>
            <div className="space-y-2">
              <Label>Position *</Label>
              <Input placeholder="Manager, President, etc." />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label>Email *</Label>
              <Input type="email" placeholder="contact@organization.org" />
            </div>
            <div className="space-y-2">
              <Label>Phone Number *</Label>
              <Input type="tel" placeholder="09XX-XXX-XXXX" />
            </div>
          </div>
        </div>
      )}
    </CardContent>
    <CardFooter className="flex justify-between">
      <Button
        variant="outline"
        onClick={prevStep}
        disabled={currentStep === 0}
      >
        <ChevronLeft className="h-4 w-4 mr-2" />
        Previous
      </Button>
      <Button onClick={nextStep}>
        {currentStep === steps.length - 1 ? 'Submit' : 'Next'}
        <ChevronRight className="h-4 w-4 ml-2" />
      </Button>
    </CardFooter>
  </Card>
</div>
```

---

## Document Submission Journey

### Document Upload Interface

```tsx
// Document Upload Section
<Card>
  <CardHeader>
    <CardTitle>Required Documents</CardTitle>
    <CardDescription>
      Upload the following documents to complete your registration.
      All documents must be valid and clearly readable.
    </CardDescription>
  </CardHeader>
  <CardContent className="space-y-6">
    {requiredDocuments.map((doc) => (
      <div
        key={doc.id}
        className={cn(
          "p-4 rounded-lg border-2 border-dashed transition-colors",
          doc.uploaded ? "border-green-500 bg-green-50" : "border-muted hover:border-primary"
        )}
      >
        <div className="flex items-start gap-4">
          <div className={cn(
            "h-10 w-10 rounded-full flex items-center justify-center",
            doc.uploaded ? "bg-green-100 text-green-600" : "bg-muted text-muted-foreground"
          )}>
            {doc.uploaded ? (
              <CheckCircle className="h-5 w-5" />
            ) : (
              <FileText className="h-5 w-5" />
            )}
          </div>

          <div className="flex-1">
            <div className="flex items-center gap-2">
              <h4 className="font-medium">{doc.name}</h4>
              <Badge variant={doc.required ? 'destructive' : 'secondary'}>
                {doc.required ? 'Required' : 'Optional'}
              </Badge>
            </div>
            <p className="text-sm text-muted-foreground mt-1">
              {doc.description}
            </p>

            {doc.uploaded ? (
              <div className="flex items-center gap-4 mt-3">
                <div className="flex items-center gap-2 text-sm">
                  <FileText className="h-4 w-4" />
                  <span>{doc.uploadedFile.name}</span>
                  <span className="text-muted-foreground">
                    ({formatFileSize(doc.uploadedFile.size)})
                  </span>
                </div>
                <Button variant="ghost" size="sm" onClick={() => removeDocument(doc.id)}>
                  <X className="h-4 w-4 mr-1" />
                  Remove
                </Button>
                <Button variant="ghost" size="sm" onClick={() => viewDocument(doc.id)}>
                  <Eye className="h-4 w-4 mr-1" />
                  View
                </Button>
              </div>
            ) : (
              <div className="mt-3">
                <input
                  type="file"
                  id={`upload-${doc.id}`}
                  className="hidden"
                  accept={doc.acceptedTypes.join(',')}
                  onChange={(e) => handleUpload(doc.id, e.target.files?.[0])}
                />
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => document.getElementById(`upload-${doc.id}`)?.click()}
                >
                  <Upload className="h-4 w-4 mr-2" />
                  Upload {doc.name}
                </Button>
                <p className="text-xs text-muted-foreground mt-2">
                  Accepted: {doc.acceptedTypes.join(', ')} (max {doc.maxSize}MB)
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    ))}
  </CardContent>
</Card>

// Required Documents List
const requiredDocuments = [
  {
    id: 'cda-registration',
    name: 'CDA Certificate of Registration',
    description: 'Certificate of Registration from the Cooperative Development Authority',
    required: true,
    acceptedTypes: ['.pdf', '.jpg', '.png'],
    maxSize: 5,
  },
  {
    id: 'business-permit',
    name: 'Business Permit',
    description: 'Current business permit from your LGU',
    required: true,
    acceptedTypes: ['.pdf', '.jpg', '.png'],
    maxSize: 5,
  },
  {
    id: 'bir-registration',
    name: 'BIR Certificate of Registration',
    description: 'Certificate of Registration (Form 2303) from BIR',
    required: true,
    acceptedTypes: ['.pdf', '.jpg', '.png'],
    maxSize: 5,
  },
  {
    id: 'articles',
    name: 'Articles of Cooperation',
    description: 'Filed articles with CDA/SEC',
    required: false,
    acceptedTypes: ['.pdf'],
    maxSize: 10,
  },
  {
    id: 'bylaws',
    name: 'By-Laws',
    description: 'Approved by-laws of the organization',
    required: false,
    acceptedTypes: ['.pdf'],
    maxSize: 10,
  },
];
```

---

## FRAMES Compliance Journey

### FRAMES Dashboard (For Coop/SE)

```tsx
// FRAMES Compliance Dashboard
<div className="space-y-6">
  <div className="flex items-center justify-between">
    <div>
      <h1 className="text-2xl font-bold">FRAMES Compliance</h1>
      <p className="text-muted-foreground">
        Track your organization's compliance with CSEA requirements
      </p>
    </div>
    <Badge variant={overallStatus === 'compliant' ? 'success' : 'warning'} className="text-sm">
      {overallStatus === 'compliant' ? 'Fully Compliant' : 'Action Required'}
    </Badge>
  </div>

  {/* FRAMES Categories */}
  <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
    {framesCategories.map((category) => (
      <Card key={category.id} className={cn(
        "cursor-pointer hover:border-primary transition-colors",
        category.status === 'non-compliant' && "border-destructive"
      )}>
        <CardContent className="p-4">
          <div className="flex items-start justify-between">
            <div className="flex items-center gap-3">
              <div className={cn(
                "h-10 w-10 rounded-full flex items-center justify-center",
                category.status === 'compliant' && "bg-green-100 text-green-600",
                category.status === 'pending' && "bg-yellow-100 text-yellow-600",
                category.status === 'non-compliant' && "bg-red-100 text-red-600"
              )}>
                <category.icon className="h-5 w-5" />
              </div>
              <div>
                <h3 className="font-medium">{category.name}</h3>
                <p className="text-xs text-muted-foreground">{category.fullName}</p>
              </div>
            </div>
            <ComplianceStatusIcon status={category.status} />
          </div>

          {/* Progress */}
          <div className="mt-4 space-y-2">
            <div className="flex justify-between text-sm">
              <span className="text-muted-foreground">Compliance</span>
              <span className="font-medium">{category.compliance}%</span>
            </div>
            <Progress value={category.compliance} className="h-2" />
          </div>

          {/* Requirements Summary */}
          <div className="mt-3 flex items-center gap-4 text-sm">
            <span className="flex items-center gap-1 text-green-600">
              <CheckCircle className="h-3 w-3" />
              {category.completedRequirements}
            </span>
            <span className="flex items-center gap-1 text-yellow-600">
              <Clock className="h-3 w-3" />
              {category.pendingRequirements}
            </span>
            <span className="flex items-center gap-1 text-red-600">
              <AlertCircle className="h-3 w-3" />
              {category.missingRequirements}
            </span>
          </div>
        </CardContent>
      </Card>
    ))}
  </div>

  {/* Detailed Requirements */}
  <Card>
    <CardHeader>
      <CardTitle>Compliance Requirements</CardTitle>
    </CardHeader>
    <CardContent>
      <Accordion type="multiple" className="w-full">
        {framesCategories.map((category) => (
          <AccordionItem key={category.id} value={category.id}>
            <AccordionTrigger className="hover:no-underline">
              <div className="flex items-center gap-3">
                <category.icon className="h-5 w-5 text-muted-foreground" />
                <span>{category.fullName}</span>
                <Badge variant="outline" className="ml-auto mr-2">
                  {category.completedRequirements}/{category.totalRequirements}
                </Badge>
              </div>
            </AccordionTrigger>
            <AccordionContent>
              <div className="space-y-3 pl-8">
                {category.requirements.map((req) => (
                  <div
                    key={req.id}
                    className="flex items-center justify-between p-3 rounded-lg bg-muted/50"
                  >
                    <div className="flex items-center gap-3">
                      <RequirementStatusIcon status={req.status} />
                      <div>
                        <p className="font-medium text-sm">{req.name}</p>
                        {req.expiryDate && (
                          <p className="text-xs text-muted-foreground">
                            {req.status === 'expiring'
                              ? `Expires ${formatDate(req.expiryDate)}`
                              : req.status === 'expired'
                              ? `Expired ${formatDate(req.expiryDate)}`
                              : `Valid until ${formatDate(req.expiryDate)}`
                            }
                          </p>
                        )}
                      </div>
                    </div>
                    {req.status !== 'compliant' && (
                      <Button size="sm" variant="outline">
                        {req.status === 'missing' ? 'Upload' : 'Update'}
                      </Button>
                    )}
                  </div>
                ))}
              </div>
            </AccordionContent>
          </AccordionItem>
        ))}
      </Accordion>
    </CardContent>
  </Card>
</div>

// FRAMES Categories - Formation, Registration, Auditing, Monitoring, Enforcement, Sustainability
const framesCategories = [
  { id: 'F', name: 'Formation', fullName: 'Formation & Setup', icon: FileText, color: 'text-negosyo-blue' },
  { id: 'R', name: 'Registration', fullName: 'Registration & Certification', icon: ClipboardCheck, color: 'text-negosyo-blue' },
  { id: 'A', name: 'Auditing', fullName: 'Financial & Operational Audits', icon: Search, color: 'text-negosyo-blue' },
  { id: 'M', name: 'Monitoring', fullName: 'Monitoring & Evaluation', icon: Activity, color: 'text-negosyo-blue' },
  { id: 'E', name: 'Enforcement', fullName: 'Compliance Enforcement', icon: Shield, color: 'text-negosyo-blue' },
  { id: 'S', name: 'Sustainability', fullName: 'Long-term Sustainability', icon: Leaf, color: 'text-negosyo-blue' },
];
```

### CSEA FRAMES Review Interface

```tsx
// CSEA FRAMES Review
<div className="grid lg:grid-cols-3 gap-6">
  {/* Organization Info */}
  <div className="lg:col-span-2 space-y-6">
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div>
            <CardTitle>{organization.name}</CardTitle>
            <CardDescription>
              {organization.type} • {organization.location}
            </CardDescription>
          </div>
          <OverallComplianceBadge score={organization.complianceScore} />
        </div>
      </CardHeader>
      <CardContent>
        {/* FRAMES Scores */}
        <div className="grid grid-cols-6 gap-4">
          {framesScores.map((frame) => (
            <div key={frame.id} className="text-center">
              <div className={cn(
                "h-16 w-16 rounded-full mx-auto flex items-center justify-center text-lg font-bold",
                frame.score >= 80 && "bg-green-100 text-green-600",
                frame.score >= 50 && frame.score < 80 && "bg-yellow-100 text-yellow-600",
                frame.score < 50 && "bg-red-100 text-red-600"
              )}>
                {frame.score}%
              </div>
              <p className="text-sm font-medium mt-2">{frame.id}</p>
              <p className="text-xs text-muted-foreground">{frame.name}</p>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>

    {/* Documents Review */}
    <Card>
      <CardHeader>
        <CardTitle>Submitted Documents</CardTitle>
      </CardHeader>
      <CardContent>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Document</TableHead>
              <TableHead>FRAMES</TableHead>
              <TableHead>Submitted</TableHead>
              <TableHead>Expiry</TableHead>
              <TableHead>Status</TableHead>
              <TableHead></TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {documents.map((doc) => (
              <TableRow key={doc.id}>
                <TableCell className="font-medium">{doc.name}</TableCell>
                <TableCell>
                  <Badge variant="outline">{doc.framesCategory}</Badge>
                </TableCell>
                <TableCell>{formatDate(doc.submittedAt)}</TableCell>
                <TableCell>
                  <ExpiryBadge date={doc.expiryDate} />
                </TableCell>
                <TableCell>
                  <DocumentStatusBadge status={doc.verificationStatus} />
                </TableCell>
                <TableCell>
                  <div className="flex gap-2">
                    <Button variant="ghost" size="sm" onClick={() => viewDocument(doc)}>
                      <Eye className="h-4 w-4" />
                    </Button>
                    <DropdownMenu>
                      <DropdownMenuTrigger asChild>
                        <Button variant="ghost" size="sm">
                          <MoreHorizontal className="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>
                      <DropdownMenuContent align="end">
                        <DropdownMenuItem onClick={() => approveDocument(doc.id)}>
                          <CheckCircle className="h-4 w-4 mr-2" />
                          Approve
                        </DropdownMenuItem>
                        <DropdownMenuItem onClick={() => requestRevision(doc.id)}>
                          <AlertCircle className="h-4 w-4 mr-2" />
                          Request Revision
                        </DropdownMenuItem>
                        <DropdownMenuItem
                          className="text-destructive"
                          onClick={() => rejectDocument(doc.id)}
                        >
                          <X className="h-4 w-4 mr-2" />
                          Reject
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </div>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  </div>

  {/* Sidebar - Review Actions */}
  <div className="space-y-6">
    <Card>
      <CardHeader>
        <CardTitle>Review Actions</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <Button className="w-full" onClick={approveAll}>
          <CheckCircle className="h-4 w-4 mr-2" />
          Approve Compliance
        </Button>
        <Button variant="outline" className="w-full" onClick={requestChanges}>
          <MessageSquare className="h-4 w-4 mr-2" />
          Request Changes
        </Button>
        <Button variant="destructive" className="w-full" onClick={flagNonCompliant}>
          <AlertTriangle className="h-4 w-4 mr-2" />
          Flag Non-Compliant
        </Button>
      </CardContent>
    </Card>

    <Card>
      <CardHeader>
        <CardTitle>Review Notes</CardTitle>
      </CardHeader>
      <CardContent>
        <Textarea
          placeholder="Add internal review notes..."
          rows={4}
          value={notes}
          onChange={(e) => setNotes(e.target.value)}
        />
        <Button className="mt-2" size="sm">Save Notes</Button>
      </CardContent>
    </Card>

    <Card>
      <CardHeader>
        <CardTitle>Activity Log</CardTitle>
      </CardHeader>
      <CardContent className="space-y-3">
        {activityLog.map((activity) => (
          <div key={activity.id} className="flex gap-3 text-sm">
            <div className="h-2 w-2 rounded-full bg-muted-foreground mt-2" />
            <div>
              <p>{activity.action}</p>
              <p className="text-xs text-muted-foreground">
                {activity.user} • {formatRelativeTime(activity.timestamp)}
              </p>
            </div>
          </div>
        ))}
      </CardContent>
    </Card>
  </div>
</div>
```

---

## Renewal & Maintenance Journey

### Expiry Notifications

```tsx
// Renewal Alerts Dashboard
<div className="space-y-4">
  {/* Urgent Alert */}
  {urgentRenewals.length > 0 && (
    <Alert variant="destructive">
      <AlertTriangle className="h-4 w-4" />
      <AlertTitle>Urgent: Documents Expiring Soon</AlertTitle>
      <AlertDescription>
        {urgentRenewals.length} document(s) will expire within 30 days.
        Renew now to maintain your compliance status.
      </AlertDescription>
    </Alert>
  )}

  {/* Renewal Timeline */}
  <Card>
    <CardHeader>
      <CardTitle>Upcoming Renewals</CardTitle>
    </CardHeader>
    <CardContent>
      <div className="space-y-4">
        {upcomingRenewals.map((item) => (
          <div
            key={item.id}
            className="flex items-center justify-between p-4 rounded-lg border"
          >
            <div className="flex items-center gap-4">
              <div className={cn(
                "h-12 w-12 rounded-full flex items-center justify-center",
                item.daysUntilExpiry <= 7 && "bg-red-100 text-red-600",
                item.daysUntilExpiry > 7 && item.daysUntilExpiry <= 30 && "bg-yellow-100 text-yellow-600",
                item.daysUntilExpiry > 30 && "bg-green-100 text-green-600"
              )}>
                <Calendar className="h-6 w-6" />
              </div>
              <div>
                <p className="font-medium">{item.documentName}</p>
                <p className="text-sm text-muted-foreground">
                  Expires: {formatDate(item.expiryDate)}
                </p>
              </div>
            </div>
            <div className="flex items-center gap-4">
              <Badge variant={
                item.daysUntilExpiry <= 7 ? 'destructive' :
                item.daysUntilExpiry <= 30 ? 'warning' : 'secondary'
              }>
                {item.daysUntilExpiry} days left
              </Badge>
              <Button size="sm">
                <Upload className="h-4 w-4 mr-2" />
                Renew
              </Button>
            </div>
          </div>
        ))}
      </div>
    </CardContent>
  </Card>
</div>
```

---

## Key UX Principles for Compliance

### 1. Reduce Anxiety
- Clear status indicators
- Progress visibility
- Helpful error messages

### 2. Guide Don't Punish
- Checklists over requirements
- Proactive reminders before expiry
- Easy renewal process

### 3. Mobile Document Upload
- Camera integration for scanning
- Preview before submit
- Multiple file formats supported

### 4. Transparency
- Show review status
- Provide reasons for rejection
- Clear next steps

### 5. Communication
- Email notifications for status changes
- In-app messaging with reviewers
- Clear escalation paths
