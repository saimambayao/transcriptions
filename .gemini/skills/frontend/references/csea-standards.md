# CSEA Design Standards

**Official CSEA UI/UX Standards - Negosyo Blue Primary**

This document provides the official design standards for the Cooperative and Social Enterprise Authority (CSEA) Digital Platform.

## Table of Contents

1. [Color Palette](#color-palette)
2. [Component Standards](#component-standards)
3. [Typography](#typography)
4. [Spacing & Layout](#spacing--layout)
5. [Form Components](#form-components)
6. [Data Display](#data-display)

---

## Color Palette

### CSEA Brand Colors

**Official CSEA color palette** - Use Tailwind's custom classes or hex values:

```css
/* CSEA Brand Colors (from globals.css) */
--negosyo-blue: #0056D2;    /* Primary - headers, links, primary buttons */
--negosyo-red: #D30A28;     /* Hero sections, promotional banners, featured areas */
--csea-green: #008000;      /* Secondary - CTAs, marketplace, success actions */
--csea-yellow: #FFD700;     /* Accent - highlights, warnings */
--csea-red: #DC2626;        /* Destructive - errors, delete actions */
```

### Primary: Negosyo Blue `#0056D2`

Use for primary UI elements - navigation, headers, links, active states:

```tsx
// Using Tailwind custom class (recommended)
<div className="bg-negosyo-blue text-white">
<Button className="bg-negosyo-blue hover:bg-negosyo-blue/90">
<span className="text-negosyo-blue">

// Using hex values
<div className="bg-[#0056D2] text-white">
<Button className="bg-[#0056D2] hover:bg-[#0056D2]/90">
```

**When to use Negosyo Blue:**
- Navigation bars and headers
- Primary text links
- Table headers
- Active sidebar items
- Focus rings and borders

### Negosyo Red `#D30A28`

Use for hero sections, promotional content, and featured areas:

```tsx
// Using Tailwind custom class (recommended)
<section className="bg-negosyo-red text-white">
  <h1>Hero Content</h1>
</section>

// Hero section with search box
<div className="bg-negosyo-red text-white py-16">
  <Badge className="bg-white/20 text-white">Featured</Badge>
  <h1 className="text-4xl font-bold">Main Headline</h1>
  <p className="text-red-100">Supporting text</p>
  <Button className="bg-white text-negosyo-red hover:bg-red-50">
    Primary CTA
  </Button>
</div>
```

**When to use Negosyo Red:**
- Homepage hero sections
- Promotional banners
- Featured product highlights
- Special announcements
- Marketing landing pages

### Secondary: CSEA Green `#008000`

Use for call-to-action buttons and marketplace/shop elements:

```tsx
// Using Tailwind custom class (recommended)
<Button className="bg-csea-green hover:bg-green-700 text-white">
  Shop Marketplace
</Button>

// Using hex values
<Button className="bg-[#008000] hover:bg-green-700 text-white">
  Add to Cart
</Button>
```

**When to use CSEA Green:**
- "Shop Marketplace" and CTA buttons
- Add to cart buttons
- Success/confirmation actions
- Marketplace-related elements

### Semantic Colors (Status Indicators Only)

Use **only** for semantic meaning:

```tsx
// Success
<Badge className="bg-emerald-100 text-emerald-800">Active</Badge>

// Warning
<Badge className="bg-orange-100 text-orange-800">Pending</Badge>

// Error
<Badge className="bg-red-100 text-red-800">Inactive</Badge>

// Info
<Badge className="bg-blue-100 text-blue-800">Processing</Badge>
```

### Neutral Colors

```css
/* Gray Scale - Use for text, backgrounds, borders */
--neutral-50: #f9fafb;   /* bg-gray-50 */
--neutral-100: #f3f4f6;  /* bg-gray-100 */
--neutral-200: #e5e7eb;  /* border-gray-200 */
--neutral-500: #6b7280;  /* text-gray-500 */
--neutral-700: #374151;  /* text-gray-700 */
--neutral-900: #111827;  /* text-gray-900 */
```

---

## Component Standards

### Button Hierarchy

```tsx
import { Button } from "@/components/ui/button"

// Primary Button
<Button className="bg-negosyo-blue hover:bg-negosyo-blue/90 text-white">
  Primary Action
</Button>

// Secondary Button
<Button variant="outline" className="border-negosyo-blue text-negosyo-blue hover:bg-negosyo-blue/10">
  Secondary Action
</Button>

// Tertiary Button
<Button variant="ghost" className="text-negosyo-blue hover:bg-negosyo-blue/10">
  Tertiary Action
</Button>

// Destructive Button
<Button variant="destructive">
  Delete
</Button>
```

### Card Components

**Standard Card with CSEA Header:**
```tsx
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

<Card>
  <CardHeader className="bg-negosyo-blue text-white rounded-t-lg">
    <CardTitle>Card Title</CardTitle>
  </CardHeader>
  <CardContent className="p-6">
    <p className="text-gray-600">Card content</p>
  </CardContent>
</Card>
```

**Stat Card:**
```tsx
<Card>
  <CardHeader className="flex flex-row items-center justify-between pb-2">
    <CardTitle className="text-sm font-medium text-gray-500">
      Total Cooperatives
    </CardTitle>
    <Building2 className="h-5 w-5 text-negosyo-blue" />
  </CardHeader>
  <CardContent>
    <div className="text-3xl font-bold text-negosyo-blue">1,234</div>
    <p className="text-sm text-emerald-600 mt-1">+12% from last month</p>
  </CardContent>
</Card>
```

### Form Input Components

**Text Input:**
```tsx
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

<div className="space-y-2">
  <Label htmlFor="name">
    Name <span className="text-red-600">*</span>
  </Label>
  <Input
    id="name"
    placeholder="Enter name"
    className="focus-visible:ring-negosyo-blue"
  />
  <p className="text-sm text-gray-500">Helper text</p>
</div>
```

**Select Dropdown:**
```tsx
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

<div className="space-y-2">
  <Label htmlFor="type">Type *</Label>
  <Select>
    <SelectTrigger className="focus:ring-negosyo-blue">
      <SelectValue placeholder="Select type" />
    </SelectTrigger>
    <SelectContent>
      <SelectItem value="producer">Producer</SelectItem>
      <SelectItem value="consumer">Consumer</SelectItem>
    </SelectContent>
  </Select>
</div>
```

---

## Typography

### Font Stack

```css
font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
```

### Heading Scales

```tsx
<h1 className="text-4xl font-bold text-gray-900">Heading 1</h1>
<h2 className="text-3xl font-bold text-gray-900">Heading 2</h2>
<h3 className="text-2xl font-semibold text-gray-900">Heading 3</h3>
<h4 className="text-xl font-semibold text-gray-900">Heading 4</h4>
<h5 className="text-lg font-medium text-gray-900">Heading 5</h5>
```

### Body Text

```tsx
<p className="text-base text-gray-700">Body text (16px)</p>
<p className="text-sm text-gray-600">Small text (14px)</p>
<p className="text-xs text-gray-500">Extra small (12px)</p>
```

---

## Spacing & Layout

### Standard Spacing Scale

4px, 8px, 16px, 24px, 32px, 48px

Tailwind: `p-1`, `p-2`, `p-4`, `p-6`, `p-8`, `p-12`

### Container Widths

```tsx
<div className="container mx-auto px-4 sm:px-6 lg:px-8">
  {/* Content with responsive padding */}
</div>
```

### Grid Layouts

```tsx
// 3-column grid
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <Card>Column 1</Card>
  <Card>Column 2</Card>
  <Card>Column 3</Card>
</div>

// 4-column stat grid
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
  <StatCard />
  <StatCard />
  <StatCard />
  <StatCard />
</div>
```

---

## Form Components

### Form with React Hook Form + Zod

```tsx
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import { z } from "zod"
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form"

const formSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters"),
  email: z.string().email("Invalid email address"),
})

export function CooperativeForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
  })

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Name *</FormLabel>
              <FormControl>
                <Input {...field} className="focus-visible:ring-negosyo-blue" />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        <div className="flex justify-end gap-3">
          <Button variant="outline">Cancel</Button>
          <Button type="submit" className="bg-negosyo-blue hover:bg-negosyo-blue/90">
            Submit
          </Button>
        </div>
      </form>
    </Form>
  )
}
```

---

## Data Display

### Data Table with CSEA Header

```tsx
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

<div className="rounded-lg border overflow-hidden">
  <Table>
    <TableHeader className="bg-negosyo-blue">
      <TableRow>
        <TableHead className="text-white font-semibold">Name</TableHead>
        <TableHead className="text-white font-semibold">Type</TableHead>
        <TableHead className="text-white font-semibold">Status</TableHead>
        <TableHead className="text-white font-semibold text-right">Actions</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      {data.map((item) => (
        <TableRow key={item.id} className="hover:bg-gray-50">
          <TableCell className="font-medium">{item.name}</TableCell>
          <TableCell>{item.type}</TableCell>
          <TableCell>
            <Badge className="bg-emerald-100 text-emerald-800">
              {item.status}
            </Badge>
          </TableCell>
          <TableCell className="text-right">
            <Button variant="ghost" size="sm">View</Button>
            <Button variant="ghost" size="sm">Edit</Button>
          </TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>
</div>
```

---

## Modal Patterns

### Standard Dialog with CSEA Header

```tsx
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"

<Dialog open={open} onOpenChange={setOpen}>
  <DialogContent className="sm:max-w-[500px]">
    <DialogHeader className="bg-negosyo-blue -m-6 mb-6 p-6 rounded-t-lg">
      <DialogTitle className="text-white">Modal Title</DialogTitle>
      <DialogDescription className="text-white/80">
        Modal description text
      </DialogDescription>
    </DialogHeader>

    <div className="space-y-4">
      {/* Modal content */}
    </div>

    <DialogFooter>
      <Button variant="outline" onClick={() => setOpen(false)}>
        Cancel
      </Button>
      <Button className="bg-negosyo-blue hover:bg-negosyo-blue/90">
        Save
      </Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

---

## Quick Reference

### Component Checklist

When creating any UI component:

- [ ] Uses Negosyo Blue (`#0056D2`) for primary elements
- [ ] Semantic colors only for status indicators
- [ ] Minimum 44x44px touch targets
- [ ] WCAG 2.1 AA contrast ratios
- [ ] Responsive (320px - 1920px)
- [ ] TypeScript types defined
- [ ] Loading states implemented
- [ ] Error states handled

### Color Usage Priority

1. **Negosyo Blue** (`#0056D2`) - Primary for all main UI elements
2. **Negosyo Red** (`#D30A28`) - Hero sections, promotions, featured content
3. **CSEA Green** (`#008000`) - CTAs, marketplace, success actions
4. **Semantic Colors** - Status indicators only
5. **Neutral Grays** - Text, backgrounds, borders
