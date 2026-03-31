# Form Design Patterns

Comprehensive guide for building effective, accessible forms in the Bangsamoro Development Platform.

## Table of Contents
- [Validation Strategy](#validation-strategy)
- [Error Handling](#error-handling)
- [Form Layout](#form-layout)
- [Input Patterns](#input-patterns)
- [Multi-Step Forms](#multi-step-forms)
- [Checkout Forms](#checkout-forms)

## Validation Strategy

### Inline Validation (Preferred)

Validate fields after the user leaves the field (on blur), not while typing:

```tsx
// Good: Validate on blur
<Input
  onBlur={(e) => validateField(e.target.value)}
  {...field}
/>

// Bad: Validate on every keystroke (annoying)
<Input
  onChange={(e) => validateField(e.target.value)}
  {...field}
/>
```

### Validation Timing Rules

| Scenario | When to Validate |
|----------|------------------|
| Required field | On blur (after user leaves) |
| Format validation | On blur |
| Async validation (email exists) | On blur with debounce (300ms) |
| Password strength | While typing (non-blocking) |
| Form submission | On submit (re-validate all) |

### Remove Errors Immediately

Clear error messages as soon as the user starts correcting:

```tsx
// Clear error when user starts typing
<Input
  onChange={(e) => {
    if (errors.email) clearError('email');
    field.onChange(e);
  }}
  onBlur={() => validateField('email')}
/>
```

## Error Handling

### Error Message Placement

Always place error messages directly below the field:

```tsx
<div className="space-y-2">
  <Label htmlFor="email">
    Email <span className="text-destructive">*</span>
  </Label>
  <Input
    id="email"
    aria-invalid={!!errors.email}
    aria-describedby={errors.email ? "email-error" : undefined}
    className={errors.email ? "border-destructive" : ""}
  />
  {errors.email && (
    <p id="email-error" className="text-sm text-destructive flex items-center gap-1">
      <AlertCircle className="h-4 w-4" />
      {errors.email.message}
    </p>
  )}
</div>
```

### Error Message Guidelines

Write error messages that are:

| Principle | Bad | Good |
|-----------|-----|------|
| Specific | "Invalid input" | "Email must include @ symbol" |
| Helpful | "Error" | "Password must be at least 8 characters" |
| Polite | "You failed to..." | "Please enter a valid phone number" |
| Actionable | "Invalid format" | "Use format: 09XX-XXX-XXXX" |

### Visual Error Indicators

```css
/* Error state styling */
.field-error {
  border-color: var(--destructive);
  background-color: hsl(var(--destructive) / 0.05);
}

/* Error message styling */
.error-message {
  color: var(--destructive);
  font-size: 0.875rem;
  margin-top: 0.25rem;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}
```

## Form Layout

### Single Column (Preferred for Mobile)

```tsx
<form className="space-y-4">
  <div className="space-y-2">
    <Label>First Name *</Label>
    <Input />
  </div>
  <div className="space-y-2">
    <Label>Last Name *</Label>
    <Input />
  </div>
  <div className="space-y-2">
    <Label>Email *</Label>
    <Input type="email" />
  </div>
</form>
```

### Two Column (Desktop Only)

```tsx
<form className="space-y-4">
  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div className="space-y-2">
      <Label>First Name *</Label>
      <Input />
    </div>
    <div className="space-y-2">
      <Label>Last Name *</Label>
      <Input />
    </div>
  </div>
  <div className="space-y-2">
    <Label>Email *</Label>
    <Input type="email" />
  </div>
</form>
```

### Required Fields

- Mark required fields with asterisk (*) in the label
- Optionally mark optional fields as "(optional)"
- Be consistent throughout the application

```tsx
<Label>
  Email <span className="text-destructive">*</span>
</Label>

<Label>
  Middle Name <span className="text-muted-foreground">(optional)</span>
</Label>
```

## Input Patterns

### Text Input with Character Count

```tsx
<div className="space-y-2">
  <div className="flex justify-between">
    <Label>Description *</Label>
    <span className="text-sm text-muted-foreground">
      {value.length}/500
    </span>
  </div>
  <Textarea
    value={value}
    maxLength={500}
    onChange={(e) => setValue(e.target.value)}
  />
</div>
```

### Phone Number (Philippines)

```tsx
<div className="space-y-2">
  <Label>Phone Number *</Label>
  <Input
    type="tel"
    placeholder="09XX-XXX-XXXX"
    pattern="09[0-9]{2}-?[0-9]{3}-?[0-9]{4}"
  />
  <p className="text-sm text-muted-foreground">
    Format: 09XX-XXX-XXXX
  </p>
</div>
```

### Currency Input

```tsx
<div className="space-y-2">
  <Label>Price *</Label>
  <div className="relative">
    <span className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground">
      PHP
    </span>
    <Input
      type="number"
      min="0"
      step="0.01"
      className="pl-12"
      placeholder="0.00"
    />
  </div>
</div>
```

### Select with Search (Combobox)

```tsx
<Popover>
  <PopoverTrigger asChild>
    <Button variant="outline" className="w-full justify-between">
      {value || "Select cooperative..."}
      <ChevronsUpDown className="ml-2 h-4 w-4" />
    </Button>
  </PopoverTrigger>
  <PopoverContent className="w-full p-0">
    <Command>
      <CommandInput placeholder="Search cooperatives..." />
      <CommandList>
        <CommandEmpty>No cooperative found.</CommandEmpty>
        <CommandGroup>
          {cooperatives.map((coop) => (
            <CommandItem key={coop.id} onSelect={() => setValue(coop.name)}>
              {coop.name}
            </CommandItem>
          ))}
        </CommandGroup>
      </CommandList>
    </Command>
  </PopoverContent>
</Popover>
```

### File Upload

```tsx
<div className="space-y-2">
  <Label>Business Permit *</Label>
  <div className="border-2 border-dashed rounded-lg p-6 text-center hover:border-primary transition-colors">
    <Upload className="h-8 w-8 mx-auto text-muted-foreground mb-2" />
    <p className="text-sm text-muted-foreground">
      Drag & drop or click to upload
    </p>
    <p className="text-xs text-muted-foreground mt-1">
      PDF, JPG, PNG up to 5MB
    </p>
    <Input
      type="file"
      accept=".pdf,.jpg,.jpeg,.png"
      className="hidden"
      onChange={handleFileChange}
    />
  </div>
</div>
```

## Multi-Step Forms

### Progress Indicator

```tsx
<div className="flex items-center justify-between mb-8">
  {steps.map((step, index) => (
    <div key={step.id} className="flex items-center">
      <div className={cn(
        "w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium",
        index < currentStep && "bg-primary text-primary-foreground",
        index === currentStep && "bg-primary text-primary-foreground",
        index > currentStep && "bg-muted text-muted-foreground"
      )}>
        {index < currentStep ? (
          <Check className="h-4 w-4" />
        ) : (
          index + 1
        )}
      </div>
      <span className={cn(
        "ml-2 text-sm hidden sm:inline",
        index <= currentStep ? "text-foreground" : "text-muted-foreground"
      )}>
        {step.title}
      </span>
      {index < steps.length - 1 && (
        <div className={cn(
          "w-12 h-0.5 mx-4",
          index < currentStep ? "bg-primary" : "bg-muted"
        )} />
      )}
    </div>
  ))}
</div>
```

### Step Navigation

```tsx
<div className="flex justify-between mt-8">
  <Button
    type="button"
    variant="outline"
    onClick={prevStep}
    disabled={currentStep === 0}
  >
    <ChevronLeft className="h-4 w-4 mr-2" />
    Previous
  </Button>

  {currentStep < steps.length - 1 ? (
    <Button type="button" onClick={nextStep}>
      Next
      <ChevronRight className="h-4 w-4 ml-2" />
    </Button>
  ) : (
    <Button type="submit">
      Submit Application
    </Button>
  )}
</div>
```

## Checkout Forms

### Guest Checkout Option

Always allow checkout without account creation:

```tsx
<div className="space-y-4">
  <RadioGroup defaultValue="guest">
    <div className="flex items-center space-x-2 p-4 border rounded-lg">
      <RadioGroupItem value="guest" id="guest" />
      <Label htmlFor="guest" className="flex-1 cursor-pointer">
        <div className="font-medium">Continue as Guest</div>
        <div className="text-sm text-muted-foreground">
          Checkout without creating an account
        </div>
      </Label>
    </div>
    <div className="flex items-center space-x-2 p-4 border rounded-lg">
      <RadioGroupItem value="account" id="account" />
      <Label htmlFor="account" className="flex-1 cursor-pointer">
        <div className="font-medium">Create Account</div>
        <div className="text-sm text-muted-foreground">
          Save your info for faster checkout next time
        </div>
      </Label>
    </div>
  </RadioGroup>
</div>
```

### Address Form (Philippines)

```tsx
<div className="space-y-4">
  <div className="space-y-2">
    <Label>Region *</Label>
    <Select onValueChange={setRegion}>
      <SelectTrigger>
        <SelectValue placeholder="Select region" />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="barmm">BARMM</SelectItem>
        {/* Other regions */}
      </SelectContent>
    </Select>
  </div>

  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div className="space-y-2">
      <Label>Province *</Label>
      <Select disabled={!region}>
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
      <Label>City/Municipality *</Label>
      <Select disabled={!province}>
        <SelectTrigger>
          <SelectValue placeholder="Select city" />
        </SelectTrigger>
        <SelectContent>
          {cities.map(c => (
            <SelectItem key={c.id} value={c.id}>{c.name}</SelectItem>
          ))}
        </SelectContent>
      </Select>
    </div>
  </div>

  <div className="space-y-2">
    <Label>Barangay *</Label>
    <Select disabled={!city}>
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
    <Input placeholder="House/Unit No., Street Name" />
  </div>

  <div className="space-y-2">
    <Label>Postal Code *</Label>
    <Input placeholder="7400" maxLength={4} />
  </div>
</div>
```

### Order Summary (Always Visible)

```tsx
<Card className="sticky top-4">
  <CardHeader>
    <CardTitle>Order Summary</CardTitle>
  </CardHeader>
  <CardContent className="space-y-4">
    {items.map(item => (
      <div key={item.id} className="flex justify-between text-sm">
        <span>{item.name} x {item.quantity}</span>
        <span>PHP {item.total.toFixed(2)}</span>
      </div>
    ))}
    <Separator />
    <div className="flex justify-between text-sm">
      <span>Subtotal</span>
      <span>PHP {subtotal.toFixed(2)}</span>
    </div>
    <div className="flex justify-between text-sm">
      <span>Shipping</span>
      <span>{shipping === 0 ? 'FREE' : `PHP ${shipping.toFixed(2)}`}</span>
    </div>
    <Separator />
    <div className="flex justify-between font-semibold">
      <span>Total</span>
      <span>PHP {total.toFixed(2)}</span>
    </div>
  </CardContent>
</Card>
```

## Button States

### Keep Submit Enabled

Never disable the submit button preemptively:

```tsx
// Good: Always enabled, validate on submit
<Button type="submit">
  {isSubmitting ? (
    <>
      <Loader2 className="h-4 w-4 mr-2 animate-spin" />
      Submitting...
    </>
  ) : (
    'Submit'
  )}
</Button>

// Bad: Disabled until all fields valid
<Button type="submit" disabled={!isValid}>
  Submit
</Button>
```

### Loading State on Submit

```tsx
<Button type="submit" disabled={isSubmitting}>
  {isSubmitting ? (
    <>
      <Loader2 className="h-4 w-4 mr-2 animate-spin" />
      Processing...
    </>
  ) : (
    'Place Order'
  )}
</Button>
```
