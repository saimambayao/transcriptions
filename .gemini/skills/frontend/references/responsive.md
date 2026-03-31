# Responsive Design Patterns

Mobile-first responsive patterns for CSEA with Next.js and Tailwind.

## Breakpoints

```tsx
// Tailwind v4 breakpoints
// sm: 640px   - Small tablets
// md: 768px   - Tablets
// lg: 1024px  - Laptops
// xl: 1280px  - Desktops
// 2xl: 1536px - Large screens
```

## Responsive Grid

```tsx
// 1 → 2 → 3 → 4 columns
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-6">
  <Card />
</div>

// Sidebar + Main layout
<div className="flex flex-col lg:flex-row gap-6">
  <aside className="w-full lg:w-64 shrink-0">Sidebar</aside>
  <main className="flex-1 min-w-0">Main content</main>
</div>
```

## Responsive Navigation

```tsx
"use client"
import { useState } from "react"
import { Menu, X } from "lucide-react"
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet"

export function ResponsiveNav() {
  return (
    <nav className="bg-negosyo-blue text-white">
      <div className="container mx-auto px-4">
        <div className="flex h-16 items-center justify-between">
          <span className="font-bold">CSEA</span>

          {/* Desktop nav */}
          <div className="hidden md:flex items-center gap-6">
            <Link href="/marketplace">Marketplace</Link>
            <Link href="/cooperatives">Cooperatives</Link>
          </div>

          {/* Mobile menu */}
          <Sheet>
            <SheetTrigger asChild>
              <Button variant="ghost" size="icon" className="md:hidden text-white">
                <Menu className="h-6 w-6" />
              </Button>
            </SheetTrigger>
            <SheetContent side="right">
              <nav className="flex flex-col gap-4 mt-8">
                <Link href="/marketplace">Marketplace</Link>
                <Link href="/cooperatives">Cooperatives</Link>
              </nav>
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </nav>
  )
}
```

## Responsive Tables

```tsx
// Card view on mobile, table on desktop
export function ResponsiveTable({ data }) {
  return (
    <>
      {/* Mobile: Card view */}
      <div className="md:hidden space-y-4">
        {data.map((item) => (
          <Card key={item.id}>
            <CardContent className="p-4">
              <div className="flex justify-between items-start">
                <div>
                  <p className="font-medium">{item.name}</p>
                  <p className="text-sm text-gray-500">{item.type}</p>
                </div>
                <Badge>{item.status}</Badge>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Desktop: Table view */}
      <div className="hidden md:block">
        <Table>
          <TableHeader className="bg-negosyo-blue">
            <TableRow>
              <TableHead className="text-white">Name</TableHead>
              <TableHead className="text-white">Type</TableHead>
              <TableHead className="text-white">Status</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((item) => (
              <TableRow key={item.id}>
                <TableCell>{item.name}</TableCell>
                <TableCell>{item.type}</TableCell>
                <TableCell><Badge>{item.status}</Badge></TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </>
  )
}
```

## Responsive Typography

```tsx
<h1 className="text-2xl md:text-3xl lg:text-4xl font-bold">
  Responsive Heading
</h1>

<p className="text-sm md:text-base">
  Body text that adjusts
</p>
```

## Responsive Spacing

```tsx
<div className="p-4 md:p-6 lg:p-8">
  {/* Padding scales up with screen size */}
</div>

<div className="gap-4 md:gap-6 lg:gap-8">
  {/* Gap scales up */}
</div>
```

## Touch Targets

```tsx
// Minimum 44x44px for mobile touch targets
<Button className="min-h-[44px] min-w-[44px] p-3">
  <Icon className="h-5 w-5" />
</Button>
```

## Container Queries (Tailwind v4)

```tsx
<div className="@container">
  <div className="@md:flex @md:gap-4">
    {/* Responds to container width, not viewport */}
  </div>
</div>
```

