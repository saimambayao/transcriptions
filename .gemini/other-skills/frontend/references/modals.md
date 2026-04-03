# Modal Patterns

Dialog components with shadcn/ui for CSEA.

## Basic Dialog

```tsx
import {
  Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger,
} from "@/components/ui/dialog"

<Dialog>
  <DialogTrigger asChild>
    <Button className="bg-negosyo-blue hover:bg-negosyo-blue/90">Open</Button>
  </DialogTrigger>
  <DialogContent className="sm:max-w-[500px]">
    <DialogHeader>
      <DialogTitle>Title</DialogTitle>
      <DialogDescription>Description</DialogDescription>
    </DialogHeader>
    <div className="py-4">{/* Content */}</div>
    <DialogFooter>
      <Button variant="outline">Cancel</Button>
      <Button className="bg-negosyo-blue hover:bg-negosyo-blue/90">Confirm</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

## Dialog with CSEA Header

```tsx
<DialogContent className="sm:max-w-[500px] p-0 overflow-hidden">
  <DialogHeader className="bg-negosyo-blue px-6 py-4">
    <DialogTitle className="text-white">Title</DialogTitle>
    <DialogDescription className="text-white/80">Description</DialogDescription>
  </DialogHeader>
  <div className="p-6">{/* Content */}</div>
  <DialogFooter className="bg-gray-50 px-6 py-4">
    <Button variant="outline">Cancel</Button>
    <Button className="bg-negosyo-blue hover:bg-negosyo-blue/90">Save</Button>
  </DialogFooter>
</DialogContent>
```

## Confirmation Dialog

```tsx
import {
  AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent,
  AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle,
} from "@/components/ui/alert-dialog"

<AlertDialog open={open} onOpenChange={setOpen}>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you sure?</AlertDialogTitle>
      <AlertDialogDescription>This action cannot be undone.</AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction className="bg-red-600 hover:bg-red-700">Delete</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

## Sheet (Side Panel)

```tsx
import { Sheet, SheetContent, SheetHeader, SheetTitle } from "@/components/ui/sheet"

<Sheet open={open} onOpenChange={setOpen}>
  <SheetContent className="sm:max-w-[500px]">
    <SheetHeader className="bg-negosyo-blue -m-6 mb-6 p-6">
      <SheetTitle className="text-white">Edit Details</SheetTitle>
    </SheetHeader>
    {children}
  </SheetContent>
</Sheet>
```
