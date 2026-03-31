# Input Components

Specialized input components with shadcn/ui for CSEA.

## Text Input

```tsx
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

<div className="space-y-2">
  <Label htmlFor="name">Name *</Label>
  <Input id="name" placeholder="Enter name" className="focus-visible:ring-negosyo-blue" />
</div>
```

## Select Dropdown

```tsx
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

<Select onValueChange={onChange} defaultValue={value}>
  <SelectTrigger className="focus:ring-negosyo-blue">
    <SelectValue placeholder="Select type" />
  </SelectTrigger>
  <SelectContent>
    <SelectItem value="producer">Producer</SelectItem>
    <SelectItem value="consumer">Consumer</SelectItem>
  </SelectContent>
</Select>
```

## Combobox (Searchable Select)

```tsx
import { Command, CommandEmpty, CommandGroup, CommandInput, CommandItem, CommandList } from "@/components/ui/command"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"

<Popover open={open} onOpenChange={setOpen}>
  <PopoverTrigger asChild>
    <Button variant="outline" className="w-full justify-between">
      {value || "Select..."}
      <ChevronsUpDown className="ml-2 h-4 w-4 opacity-50" />
    </Button>
  </PopoverTrigger>
  <PopoverContent className="w-full p-0">
    <Command>
      <CommandInput placeholder="Search..." />
      <CommandList>
        <CommandEmpty>No results found.</CommandEmpty>
        <CommandGroup>
          {items.map((item) => (
            <CommandItem key={item.value} onSelect={() => setValue(item.value)}>
              {item.label}
            </CommandItem>
          ))}
        </CommandGroup>
      </CommandList>
    </Command>
  </PopoverContent>
</Popover>
```

## Date Picker

```tsx
import { Calendar } from "@/components/ui/calendar"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { format } from "date-fns"

<Popover>
  <PopoverTrigger asChild>
    <Button variant="outline" className="w-full justify-start">
      <CalendarIcon className="mr-2 h-4 w-4" />
      {date ? format(date, "PPP") : "Pick a date"}
    </Button>
  </PopoverTrigger>
  <PopoverContent className="w-auto p-0">
    <Calendar mode="single" selected={date} onSelect={setDate} />
  </PopoverContent>
</Popover>
```

## Switch

```tsx
import { Switch } from "@/components/ui/switch"

<div className="flex items-center space-x-2">
  <Switch id="notifications" checked={checked} onCheckedChange={setChecked} />
  <Label htmlFor="notifications">Enable notifications</Label>
</div>
```

## Textarea

```tsx
import { Textarea } from "@/components/ui/textarea"

<Textarea placeholder="Enter description..." rows={4} className="focus-visible:ring-negosyo-blue" />
```
