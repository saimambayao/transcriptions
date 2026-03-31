# Seller Portal User Journeys

User journey maps and UX patterns for Cooperatives and Social Enterprises managing their shops on the Negosyo platform.

## Table of Contents
- [User Personas](#user-personas)
- [Onboarding Journey](#onboarding-journey)
- [Product Management Journey](#product-management-journey)
- [Order Fulfillment Journey](#order-fulfillment-journey)
- [Dashboard & Analytics Journey](#dashboard--analytics-journey)

## User Personas

### New Cooperative Manager
- **Goal**: Get their cooperative's products online
- **Behavior**: First-time digital seller, needs guidance
- **Pain Points**: Overwhelmed by setup, unsure of requirements
- **Needs**: Step-by-step onboarding, clear instructions, templates

### Experienced Seller
- **Goal**: Efficiently manage daily operations
- **Behavior**: Checks orders daily, updates inventory
- **Pain Points**: Repetitive tasks, manual processes
- **Needs**: Quick actions, bulk operations, automation

### Compliance Officer
- **Goal**: Maintain regulatory compliance
- **Behavior**: Uploads documents, tracks renewal dates
- **Pain Points**: Missing deadlines, lost documents
- **Needs**: Reminders, document storage, compliance dashboard

---

## Onboarding Journey

### Progressive Disclosure Flow

Don't overwhelm new sellers. Reveal complexity gradually:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Account    │───▶│  Business   │───▶│  First      │───▶│  Ready to   │
│  Creation   │    │  Profile    │    │  Product    │    │  Sell       │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │                  │
      ▼                  ▼                  ▼                  ▼
   5 min              10 min             5 min              Live!
   Email, name        Logo, desc,        Add one            Dashboard
   Password           Location           product            tour
```

### Step 1: Account Creation (Minimal Friction)

**Only collect what's essential**:
```tsx
// Registration Form - Minimal Fields
<Card className="max-w-md mx-auto">
  <CardHeader className="text-center">
    <CardTitle>Start Selling on Negosyo</CardTitle>
    <CardDescription>
      Join 500+ cooperatives and social enterprises
    </CardDescription>
  </CardHeader>
  <CardContent className="space-y-4">
    <div className="space-y-2">
      <Label>Organization Name *</Label>
      <Input placeholder="e.g., Sulu Weavers Cooperative" />
    </div>
    <div className="space-y-2">
      <Label>Email Address *</Label>
      <Input type="email" placeholder="manager@cooperative.org" />
    </div>
    <div className="space-y-2">
      <Label>Password *</Label>
      <Input type="password" />
      <p className="text-xs text-muted-foreground">
        At least 8 characters with one number
      </p>
    </div>
    <Button className="w-full" size="lg">Create Account</Button>
    <p className="text-xs text-center text-muted-foreground">
      By signing up, you agree to our Terms of Service
    </p>
  </CardContent>
</Card>
```

### Step 2: Business Profile (Guided Setup)

**Use a checklist with progress**:
```tsx
// Onboarding Checklist
<Card>
  <CardHeader>
    <CardTitle className="flex items-center justify-between">
      Complete Your Shop
      <Badge variant="outline">60% Complete</Badge>
    </CardTitle>
    <Progress value={60} className="h-2" />
  </CardHeader>
  <CardContent className="space-y-2">
    {tasks.map((task) => (
      <div
        key={task.id}
        className={cn(
          "flex items-center gap-3 p-3 rounded-lg border cursor-pointer hover:bg-muted/50",
          task.completed && "bg-muted/30"
        )}
        onClick={() => openTask(task.id)}
      >
        <div className={cn(
          "h-6 w-6 rounded-full flex items-center justify-center",
          task.completed ? "bg-green-100 text-green-600" : "bg-muted"
        )}>
          {task.completed ? (
            <Check className="h-4 w-4" />
          ) : (
            <span className="text-xs font-medium">{task.step}</span>
          )}
        </div>
        <div className="flex-1">
          <p className={cn(
            "font-medium",
            task.completed && "text-muted-foreground line-through"
          )}>
            {task.title}
          </p>
          <p className="text-sm text-muted-foreground">{task.description}</p>
        </div>
        <ChevronRight className="h-4 w-4 text-muted-foreground" />
      </div>
    ))}
  </CardContent>
</Card>

// Example tasks
const tasks = [
  { id: 1, step: 1, title: 'Add your logo', description: 'Upload a logo for your shop', completed: true },
  { id: 2, step: 2, title: 'Write your description', description: 'Tell customers about your cooperative', completed: true },
  { id: 3, step: 3, title: 'Add your location', description: 'Where are you based?', completed: false },
  { id: 4, step: 4, title: 'Upload compliance documents', description: 'CDA registration, permits', completed: false },
  { id: 5, step: 5, title: 'Add your first product', description: 'List something to sell', completed: false },
];
```

### Step 3: First Product (Templated)

**Reduce cognitive load with smart defaults**:
```tsx
// Simplified Product Form
<form className="space-y-6">
  {/* Essential Fields Only */}
  <div className="space-y-2">
    <Label>Product Name *</Label>
    <Input placeholder="e.g., Handwoven Malong - Traditional Design" />
  </div>

  <div className="space-y-2">
    <Label>Category *</Label>
    <Select>
      <SelectTrigger>
        <SelectValue placeholder="Select category" />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="textiles">Textiles & Woven Products</SelectItem>
        <SelectItem value="food">Food & Beverages</SelectItem>
        <SelectItem value="handicrafts">Handicrafts</SelectItem>
        {/* ... */}
      </SelectContent>
    </Select>
  </div>

  <div className="space-y-2">
    <Label>Price (PHP) *</Label>
    <Input type="number" placeholder="0.00" />
  </div>

  <div className="space-y-2">
    <Label>Photos *</Label>
    <ImageUploader
      maxFiles={5}
      hint="Add up to 5 photos. First photo will be the main image."
    />
  </div>

  <div className="space-y-2">
    <Label>Description *</Label>
    <Textarea
      placeholder="Describe your product - materials, dimensions, story behind it..."
      rows={4}
    />
  </div>

  {/* Collapsible Advanced Options */}
  <Collapsible>
    <CollapsibleTrigger className="flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground">
      <Settings2 className="h-4 w-4" />
      Advanced Options
      <ChevronDown className="h-4 w-4" />
    </CollapsibleTrigger>
    <CollapsibleContent className="space-y-4 pt-4">
      <div className="space-y-2">
        <Label>SKU</Label>
        <Input placeholder="Optional - for your reference" />
      </div>
      <div className="space-y-2">
        <Label>Weight (grams)</Label>
        <Input type="number" placeholder="For shipping calculation" />
      </div>
      <div className="space-y-2">
        <Label>Stock Quantity</Label>
        <Input type="number" defaultValue="10" />
      </div>
    </CollapsibleContent>
  </Collapsible>

  <div className="flex gap-4">
    <Button type="submit" className="flex-1">
      Publish Product
    </Button>
    <Button type="button" variant="outline">
      Save as Draft
    </Button>
  </div>
</form>
```

### Onboarding Completion

**Celebrate & guide to next action**:
```tsx
// Success State
<div className="text-center py-12">
  <div className="h-20 w-20 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-6">
    <PartyPopper className="h-10 w-10 text-green-600" />
  </div>
  <h1 className="text-3xl font-bold">Your Shop is Live!</h1>
  <p className="text-muted-foreground mt-2 max-w-md mx-auto">
    Congratulations! Your first product is now visible to thousands of buyers.
  </p>

  {/* Quick Actions */}
  <div className="flex flex-col sm:flex-row gap-4 justify-center mt-8">
    <Button asChild>
      <Link href="/portal/products/new">
        <Plus className="h-4 w-4 mr-2" />
        Add More Products
      </Link>
    </Button>
    <Button variant="outline" asChild>
      <Link href={`/store/${slug}`} target="_blank">
        <ExternalLink className="h-4 w-4 mr-2" />
        View Your Shop
      </Link>
    </Button>
  </div>

  {/* Tips Card */}
  <Card className="max-w-md mx-auto mt-8 text-left">
    <CardHeader>
      <CardTitle className="text-base">Tips for Success</CardTitle>
    </CardHeader>
    <CardContent className="space-y-3">
      <div className="flex gap-3">
        <Camera className="h-5 w-5 text-muted-foreground shrink-0" />
        <p className="text-sm">Add multiple photos from different angles</p>
      </div>
      <div className="flex gap-3">
        <FileText className="h-5 w-5 text-muted-foreground shrink-0" />
        <p className="text-sm">Write detailed descriptions with materials used</p>
      </div>
      <div className="flex gap-3">
        <Tag className="h-5 w-5 text-muted-foreground shrink-0" />
        <p className="text-sm">Set competitive prices by checking similar products</p>
      </div>
    </CardContent>
  </Card>
</div>
```

---

## Product Management Journey

### Product List View

**Enable quick actions without leaving the list**:
```tsx
// Product List with Quick Actions
<div className="space-y-4">
  {/* Toolbar */}
  <div className="flex items-center justify-between">
    <div className="flex items-center gap-4">
      <Input placeholder="Search products..." className="w-64" />
      <Select defaultValue="all">
        <SelectTrigger className="w-40">
          <SelectValue />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Status</SelectItem>
          <SelectItem value="active">Active</SelectItem>
          <SelectItem value="draft">Draft</SelectItem>
          <SelectItem value="out-of-stock">Out of Stock</SelectItem>
        </SelectContent>
      </Select>
    </div>
    <Button>
      <Plus className="h-4 w-4 mr-2" />
      Add Product
    </Button>
  </div>

  {/* Product Table */}
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead className="w-12">
          <Checkbox />
        </TableHead>
        <TableHead>Product</TableHead>
        <TableHead>Status</TableHead>
        <TableHead>Stock</TableHead>
        <TableHead>Price</TableHead>
        <TableHead>Sales</TableHead>
        <TableHead className="w-12"></TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      {products.map((product) => (
        <TableRow key={product.id}>
          <TableCell>
            <Checkbox />
          </TableCell>
          <TableCell>
            <div className="flex items-center gap-3">
              <Image
                src={product.image}
                alt={product.name}
                width={48}
                height={48}
                className="rounded-md object-cover"
              />
              <div>
                <p className="font-medium">{product.name}</p>
                <p className="text-sm text-muted-foreground">{product.sku}</p>
              </div>
            </div>
          </TableCell>
          <TableCell>
            <ProductStatusBadge status={product.status} />
          </TableCell>
          <TableCell>
            <StockIndicator stock={product.stock} lowThreshold={5} />
          </TableCell>
          <TableCell>PHP {product.price.toLocaleString()}</TableCell>
          <TableCell>{product.sales}</TableCell>
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
                  View
                </DropdownMenuItem>
                <DropdownMenuItem>
                  <Pencil className="h-4 w-4 mr-2" />
                  Edit
                </DropdownMenuItem>
                <DropdownMenuItem>
                  <Copy className="h-4 w-4 mr-2" />
                  Duplicate
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem className="text-destructive">
                  <Trash2 className="h-4 w-4 mr-2" />
                  Delete
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>

  {/* Bulk Actions Bar */}
  {selectedCount > 0 && (
    <BulkActionsBar
      selectedCount={selectedCount}
      actions={[
        { label: 'Publish', icon: Globe, onClick: bulkPublish },
        { label: 'Unpublish', icon: EyeOff, onClick: bulkUnpublish },
        { label: 'Delete', icon: Trash2, onClick: bulkDelete, variant: 'destructive' },
      ]}
    />
  )}
</div>
```

### Quick Edit Pattern

**Inline editing for common updates**:
```tsx
// Inline Stock Edit
<TableCell>
  <Popover>
    <PopoverTrigger asChild>
      <Button variant="ghost" size="sm" className="h-8 px-2">
        {product.stock}
        <Pencil className="h-3 w-3 ml-2" />
      </Button>
    </PopoverTrigger>
    <PopoverContent className="w-48">
      <div className="space-y-2">
        <Label>Update Stock</Label>
        <Input
          type="number"
          defaultValue={product.stock}
          onChange={(e) => setNewStock(e.target.value)}
        />
        <div className="flex gap-2">
          <Button size="sm" onClick={saveStock} className="flex-1">
            Save
          </Button>
          <PopoverClose asChild>
            <Button size="sm" variant="outline">Cancel</Button>
          </PopoverClose>
        </div>
      </div>
    </PopoverContent>
  </Popover>
</TableCell>
```

---

## Order Fulfillment Journey

### Order Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Pending   │───▶│  Processing │───▶│   Shipped   │───▶│  Delivered  │
│             │    │             │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │                  │
      ▼                  ▼                  ▼                  ▼
  Notification      Confirm &         Add tracking       Auto-complete
  Sound/badge       Prepare           number             after 7 days
```

### Order Dashboard

**Prioritize actionable orders**:
```tsx
// Order Dashboard
<div className="space-y-6">
  {/* Stats Row */}
  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
    <StatCard
      title="Pending"
      value={stats.pending}
      icon={Clock}
      highlight={stats.pending > 0}
    />
    <StatCard title="Processing" value={stats.processing} icon={Package} />
    <StatCard title="Shipped" value={stats.shipped} icon={Truck} />
    <StatCard title="Completed" value={stats.completed} icon={CheckCircle} />
  </div>

  {/* Urgent Orders Alert */}
  {urgentOrders.length > 0 && (
    <Alert variant="destructive">
      <AlertTriangle className="h-4 w-4" />
      <AlertTitle>Action Required</AlertTitle>
      <AlertDescription>
        {urgentOrders.length} orders need to be processed within 24 hours
      </AlertDescription>
    </Alert>
  )}

  {/* Order Tabs */}
  <Tabs defaultValue="pending">
    <TabsList>
      <TabsTrigger value="pending" className="relative">
        Pending
        {stats.pending > 0 && (
          <Badge className="ml-2 h-5 w-5 p-0 justify-center">
            {stats.pending}
          </Badge>
        )}
      </TabsTrigger>
      <TabsTrigger value="processing">Processing</TabsTrigger>
      <TabsTrigger value="shipped">Shipped</TabsTrigger>
      <TabsTrigger value="completed">Completed</TabsTrigger>
    </TabsList>

    <TabsContent value="pending">
      <OrderList orders={pendingOrders} />
    </TabsContent>
    {/* ... other tabs */}
  </Tabs>
</div>
```

### Order Card (Mobile-Optimized)

```tsx
// Order Card
<Card>
  <CardContent className="p-4">
    <div className="flex items-start justify-between">
      <div>
        <div className="flex items-center gap-2">
          <p className="font-medium">Order #{order.id}</p>
          <OrderStatusBadge status={order.status} />
        </div>
        <p className="text-sm text-muted-foreground">
          {formatRelativeTime(order.createdAt)}
        </p>
      </div>
      <p className="font-bold">PHP {order.total.toLocaleString()}</p>
    </div>

    {/* Items Preview */}
    <div className="mt-4 space-y-2">
      {order.items.slice(0, 2).map((item) => (
        <div key={item.id} className="flex items-center gap-3">
          <Image
            src={item.image}
            alt={item.name}
            width={40}
            height={40}
            className="rounded"
          />
          <div className="flex-1 min-w-0">
            <p className="text-sm truncate">{item.name}</p>
            <p className="text-xs text-muted-foreground">Qty: {item.quantity}</p>
          </div>
        </div>
      ))}
      {order.items.length > 2 && (
        <p className="text-sm text-muted-foreground">
          +{order.items.length - 2} more items
        </p>
      )}
    </div>

    {/* Customer Info */}
    <div className="mt-4 pt-4 border-t">
      <div className="flex items-center gap-2">
        <User className="h-4 w-4 text-muted-foreground" />
        <span className="text-sm">{order.customer.name}</span>
      </div>
      <div className="flex items-center gap-2 mt-1">
        <MapPin className="h-4 w-4 text-muted-foreground" />
        <span className="text-sm text-muted-foreground truncate">
          {order.shippingAddress.city}
        </span>
      </div>
    </div>

    {/* Actions */}
    <div className="mt-4 flex gap-2">
      {order.status === 'pending' && (
        <>
          <Button size="sm" className="flex-1" onClick={() => processOrder(order.id)}>
            <Check className="h-4 w-4 mr-2" />
            Process
          </Button>
          <Button size="sm" variant="outline">
            View Details
          </Button>
        </>
      )}
      {order.status === 'processing' && (
        <Button size="sm" className="flex-1" onClick={() => openShipDialog(order)}>
          <Truck className="h-4 w-4 mr-2" />
          Mark as Shipped
        </Button>
      )}
    </div>
  </CardContent>
</Card>
```

### Ship Order Dialog

```tsx
// Ship Order Dialog
<Dialog>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Ship Order #{order.id}</DialogTitle>
      <DialogDescription>
        Enter shipping details to notify the customer
      </DialogDescription>
    </DialogHeader>

    <div className="space-y-4">
      <div className="space-y-2">
        <Label>Courier *</Label>
        <Select>
          <SelectTrigger>
            <SelectValue placeholder="Select courier" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="jt">J&T Express</SelectItem>
            <SelectItem value="lbc">LBC</SelectItem>
            <SelectItem value="grab">Grab Express</SelectItem>
            <SelectItem value="other">Other</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <div className="space-y-2">
        <Label>Tracking Number *</Label>
        <Input placeholder="Enter tracking number" />
      </div>

      <div className="space-y-2">
        <Label>Estimated Delivery</Label>
        <DatePicker />
      </div>
    </div>

    <DialogFooter>
      <Button variant="outline">Cancel</Button>
      <Button>
        <Truck className="h-4 w-4 mr-2" />
        Mark as Shipped
      </Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

---

## Dashboard & Analytics Journey

### Main Dashboard Layout

```tsx
// Seller Dashboard
<div className="space-y-6">
  {/* Welcome & Quick Actions */}
  <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
    <div>
      <h1 className="text-2xl font-bold">Good morning, {user.name}</h1>
      <p className="text-muted-foreground">
        Here's what's happening with your shop today
      </p>
    </div>
    <div className="flex gap-2">
      <Button variant="outline" asChild>
        <Link href={`/store/${slug}`} target="_blank">
          <ExternalLink className="h-4 w-4 mr-2" />
          View Shop
        </Link>
      </Button>
      <Button>
        <Plus className="h-4 w-4 mr-2" />
        Add Product
      </Button>
    </div>
  </div>

  {/* Alerts */}
  {alerts.length > 0 && (
    <div className="space-y-2">
      {alerts.map((alert) => (
        <Alert key={alert.id} variant={alert.variant}>
          <alert.icon className="h-4 w-4" />
          <AlertTitle>{alert.title}</AlertTitle>
          <AlertDescription>{alert.description}</AlertDescription>
        </Alert>
      ))}
    </div>
  )}

  {/* Stats Grid */}
  <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
    <StatCard
      title="Today's Sales"
      value={`PHP ${stats.todaySales.toLocaleString()}`}
      change={{ value: stats.salesChange, trend: stats.salesChange > 0 ? 'up' : 'down' }}
      icon={TrendingUp}
    />
    <StatCard
      title="Pending Orders"
      value={stats.pendingOrders}
      icon={Clock}
      highlight={stats.pendingOrders > 0}
      action={{ label: 'View', href: '/portal/orders?status=pending' }}
    />
    <StatCard
      title="Products"
      value={stats.totalProducts}
      sublabel={`${stats.activeProducts} active`}
      icon={Package}
    />
    <StatCard
      title="Shop Rating"
      value={stats.rating.toFixed(1)}
      sublabel={`${stats.reviewCount} reviews`}
      icon={Star}
    />
  </div>

  {/* Charts & Activity */}
  <div className="grid lg:grid-cols-3 gap-6">
    {/* Sales Chart */}
    <Card className="lg:col-span-2">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle>Sales Overview</CardTitle>
          <Select defaultValue="7d">
            <SelectTrigger className="w-32">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="7d">Last 7 days</SelectItem>
              <SelectItem value="30d">Last 30 days</SelectItem>
              <SelectItem value="90d">Last 90 days</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </CardHeader>
      <CardContent>
        <SalesChart data={salesData} />
      </CardContent>
    </Card>

    {/* Recent Activity */}
    <Card>
      <CardHeader>
        <CardTitle>Recent Activity</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {activities.map((activity) => (
          <div key={activity.id} className="flex gap-3">
            <div className={cn(
              "h-8 w-8 rounded-full flex items-center justify-center shrink-0",
              activity.type === 'order' && "bg-blue-100 text-blue-600",
              activity.type === 'review' && "bg-yellow-100 text-yellow-600",
              activity.type === 'message' && "bg-green-100 text-green-600"
            )}>
              <activity.icon className="h-4 w-4" />
            </div>
            <div>
              <p className="text-sm">{activity.message}</p>
              <p className="text-xs text-muted-foreground">
                {formatRelativeTime(activity.timestamp)}
              </p>
            </div>
          </div>
        ))}
      </CardContent>
      <CardFooter>
        <Button variant="ghost" className="w-full" asChild>
          <Link href="/portal/activity">View All Activity</Link>
        </Button>
      </CardFooter>
    </Card>
  </div>

  {/* Top Products */}
  <Card>
    <CardHeader>
      <CardTitle>Top Products</CardTitle>
    </CardHeader>
    <CardContent>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Product</TableHead>
            <TableHead>Sales</TableHead>
            <TableHead>Revenue</TableHead>
            <TableHead>Stock</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {topProducts.map((product) => (
            <TableRow key={product.id}>
              <TableCell>
                <div className="flex items-center gap-3">
                  <Image src={product.image} alt="" width={40} height={40} className="rounded" />
                  <span className="font-medium">{product.name}</span>
                </div>
              </TableCell>
              <TableCell>{product.sales} sold</TableCell>
              <TableCell>PHP {product.revenue.toLocaleString()}</TableCell>
              <TableCell>
                <StockIndicator stock={product.stock} lowThreshold={5} />
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </CardContent>
  </Card>
</div>
```

---

## Key UX Principles for Sellers

### 1. Minimize Time to First Value
- Get first product live in <15 minutes
- Skip non-essential steps initially
- Provide templates and defaults

### 2. Surface Actionable Information
- Show pending orders prominently
- Alert on low stock, expiring documents
- Highlight opportunities (trending categories)

### 3. Enable Bulk Operations
- Multi-select for products
- Bulk price updates
- Batch order processing

### 4. Mobile-First for On-the-Go Management
- Order notifications
- Quick status updates
- Photo upload from phone

### 5. Contextual Help
- Tooltips on complex features
- Inline tips during onboarding
- Help center easily accessible
