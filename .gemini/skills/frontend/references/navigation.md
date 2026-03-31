# Navigation Patterns

Navigation components with Next.js and shadcn/ui for CSEA.

## Top Navbar

```tsx
import Link from "next/link"
import { Button } from "@/components/ui/button"

export function Navbar() {
  return (
    <nav className="bg-negosyo-blue text-white">
      <div className="container mx-auto px-4">
        <div className="flex h-16 items-center justify-between">
          <Link href="/" className="text-xl font-bold">CSEA</Link>
          <div className="hidden md:flex items-center gap-6">
            <Link href="/marketplace" className="hover:text-white/80">Marketplace</Link>
            <Link href="/cooperatives" className="hover:text-white/80">Cooperatives</Link>
            <Link href="/social-enterprises" className="hover:text-white/80">Social Enterprises</Link>
          </div>
          <Button variant="secondary" className="bg-white text-negosyo-blue hover:bg-gray-100">
            Login
          </Button>
        </div>
      </div>
    </nav>
  )
}
```

## Sidebar Navigation

```tsx
"use client"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
import { Home, Building2, FileText, Settings } from "lucide-react"

const navItems = [
  { href: "/portal/dashboard", label: "Dashboard", icon: Home },
  { href: "/portal/business", label: "Business", icon: Building2 },
  { href: "/portal/compliance", label: "Compliance", icon: FileText },
  { href: "/portal/settings", label: "Settings", icon: Settings },
]

export function Sidebar() {
  const pathname = usePathname()

  return (
    <aside className="w-64 bg-white border-r min-h-screen">
      <div className="p-4 border-b bg-negosyo-blue">
        <h2 className="text-white font-bold">C/SE Portal</h2>
      </div>
      <nav className="p-4 space-y-1">
        {navItems.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className={cn(
              "flex items-center gap-3 px-3 py-2 rounded-md text-sm",
              pathname === item.href
                ? "bg-negosyo-blue text-white"
                : "text-gray-700 hover:bg-gray-100"
            )}
          >
            <item.icon className="h-5 w-5" />
            {item.label}
          </Link>
        ))}
      </nav>
    </aside>
  )
}
```

## Tabs Navigation

```tsx
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

<Tabs defaultValue="overview" className="w-full">
  <TabsList className="bg-gray-100">
    <TabsTrigger value="overview" className="data-[state=active]:bg-negosyo-blue data-[state=active]:text-white">
      Overview
    </TabsTrigger>
    <TabsTrigger value="details" className="data-[state=active]:bg-negosyo-blue data-[state=active]:text-white">
      Details
    </TabsTrigger>
    <TabsTrigger value="documents" className="data-[state=active]:bg-negosyo-blue data-[state=active]:text-white">
      Documents
    </TabsTrigger>
  </TabsList>
  <TabsContent value="overview">{/* Content */}</TabsContent>
  <TabsContent value="details">{/* Content */}</TabsContent>
  <TabsContent value="documents">{/* Content */}</TabsContent>
</Tabs>
```

## Breadcrumbs

```tsx
import Link from "next/link"
import { ChevronRight } from "lucide-react"

export function Breadcrumbs({ items }) {
  return (
    <nav className="flex items-center gap-2 text-sm text-gray-500">
      {items.map((item, index) => (
        <div key={item.href} className="flex items-center gap-2">
          {index > 0 && <ChevronRight className="h-4 w-4" />}
          {index === items.length - 1 ? (
            <span className="text-gray-900 font-medium">{item.label}</span>
          ) : (
            <Link href={item.href} className="hover:text-negosyo-blue">{item.label}</Link>
          )}
        </div>
      ))}
    </nav>
  )
}

// Usage
<Breadcrumbs items={[
  { href: "/portal", label: "Portal" },
  { href: "/portal/compliance", label: "Compliance" },
  { href: "/portal/compliance/registration", label: "Registration" },
]} />
```

## Mobile Menu

```tsx
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet"
import { Menu } from "lucide-react"

<Sheet>
  <SheetTrigger asChild>
    <Button variant="ghost" size="icon" className="md:hidden">
      <Menu className="h-6 w-6" />
    </Button>
  </SheetTrigger>
  <SheetContent side="left" className="w-64 p-0">
    <Sidebar />
  </SheetContent>
</Sheet>
```

