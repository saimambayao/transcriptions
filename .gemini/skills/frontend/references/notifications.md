# Notification Patterns

Toast notifications with Sonner for CSEA.

## Setup

```tsx
// In layout.tsx or providers
import { Toaster } from "sonner"

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <Toaster position="top-right" richColors />
      </body>
    </html>
  )
}
```

## Basic Toasts

```tsx
import { toast } from "sonner"

// Success
toast.success("Registration approved successfully")

// Error
toast.error("Failed to update cooperative details")

// Warning
toast.warning("Document expires in 30 days")

// Info
toast.info("New compliance requirements available")

// Loading with promise
toast.promise(submitForm(data), {
  loading: "Saving changes...",
  success: "Changes saved successfully",
  error: "Failed to save changes",
})
```

## Action Toast

```tsx
toast("Document submitted", {
  description: "Your registration has been submitted for review.",
  action: {
    label: "View Status",
    onClick: () => router.push("/portal/compliance"),
  },
})
```

## Custom Duration

```tsx
toast.success("Welcome to CSEA Portal", {
  duration: 5000, // 5 seconds
})
```

## Alert Component

```tsx
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { AlertCircle, CheckCircle, Info } from "lucide-react"

// Info Alert
<Alert className="border-negosyo-blue bg-negosyo-blue/5">
  <Info className="h-4 w-4 text-negosyo-blue" />
  <AlertTitle className="text-negosyo-blue">Information</AlertTitle>
  <AlertDescription>New compliance deadline approaching.</AlertDescription>
</Alert>

// Success Alert
<Alert className="border-emerald-500 bg-emerald-50">
  <CheckCircle className="h-4 w-4 text-emerald-600" />
  <AlertTitle className="text-emerald-800">Success</AlertTitle>
  <AlertDescription className="text-emerald-700">Your registration has been approved.</AlertDescription>
</Alert>

// Error Alert
<Alert variant="destructive">
  <AlertCircle className="h-4 w-4" />
  <AlertTitle>Error</AlertTitle>
  <AlertDescription>Failed to submit document. Please try again.</AlertDescription>
</Alert>
```

## Inline Validation Message

```tsx
<div className="space-y-2">
  <Label htmlFor="email">Email</Label>
  <Input id="email" className="border-red-500 focus-visible:ring-red-500" />
  <p className="text-sm text-red-600 flex items-center gap-1">
    <AlertCircle className="h-3 w-3" />
    Please enter a valid email address
  </p>
</div>
```

