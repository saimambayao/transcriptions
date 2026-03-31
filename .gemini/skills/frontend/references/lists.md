# List Patterns

List and card grid patterns with shadcn/ui for CSEA.

## Card Grid

```tsx
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export function CooperativeGrid({ items }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {items.map((item) => (
        <Card key={item.id} className="hover:shadow-lg transition-shadow">
          <CardHeader>
            <CardTitle className="text-[negosyo-blue">{item.name}</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600 mb-4">{item.description}</p>
            <Badge className="bg-emerald-100 text-emerald-800">{item.status}</Badge>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
```

## Simple List

```tsx
import { ScrollArea } from "@/components/ui/scroll-area"

export function ItemList({ items }) {
  return (
    <ScrollArea className="h-[400px] rounded-md border p-4">
      <ul className="space-y-3">
        {items.map((item) => (
          <li key={item.id} className="flex items-center justify-between p-3 rounded-lg hover:bg-gray-50">
            <div>
              <p className="font-medium text-gray-900">{item.name}</p>
              <p className="text-sm text-gray-500">{item.subtitle}</p>
            </div>
            <ChevronRight className="h-5 w-5 text-gray-400" />
          </li>
        ))}
      </ul>
    </ScrollArea>
  )
}
```

## Action List

```tsx
import { Button } from "@/components/ui/button"
import { MoreHorizontal, Edit, Trash } from "lucide-react"
import {
  DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

<div className="flex items-center justify-between p-4 border-b">
  <div className="flex items-center gap-3">
    <div className="h-10 w-10 rounded-full bg-[negosyo-blue/10 flex items-center justify-center">
      <Building2 className="h-5 w-5 text-[negosyo-blue" />
    </div>
    <div>
      <p className="font-medium">{item.name}</p>
      <p className="text-sm text-gray-500">{item.type}</p>
    </div>
  </div>
  <DropdownMenu>
    <DropdownMenuTrigger asChild>
      <Button variant="ghost" size="sm">
        <MoreHorizontal className="h-4 w-4" />
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent>
      <DropdownMenuItem><Edit className="mr-2 h-4 w-4" />Edit</DropdownMenuItem>
      <DropdownMenuItem className="text-red-600"><Trash className="mr-2 h-4 w-4" />Delete</DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</div>
```

## Empty State

```tsx
import { FileX } from "lucide-react"

<div className="flex flex-col items-center justify-center py-12 text-gray-500">
  <FileX className="h-12 w-12 mb-4" />
  <p className="text-lg font-medium">No items found</p>
  <p className="text-sm">Try adjusting your filters</p>
</div>
```

