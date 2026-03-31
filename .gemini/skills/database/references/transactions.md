# Database Transactions

Transactions ensure data consistency by making multiple database operations atomic - either all succeed or all fail together.

## Table of Contents
- [Basic Transactions](#basic-transactions)
- [Transaction Decorators](#transaction-decorators)
- [Atomic Blocks](#atomic-blocks)
- [Nested Transactions (Savepoints)](#nested-transactions-savepoints)
- [Transaction Isolation](#transaction-isolation)
- [Common Pitfalls](#common-pitfalls)
- [Performance Considerations](#performance-considerations)
- [OBCMS-Specific Patterns](#obcms-specific-patterns)
- [Testing Transactions](#testing-transactions)
- [Related Patterns](#related-patterns)

## Basic Transactions

Use `transaction.atomic()` context manager for atomic operations.

```python
from django.db import transaction

def create_work_item_with_budget(work_item_data, budget_data):
    """Create work item and budget atomically."""
    with transaction.atomic():
        work_item = WorkItem.objects.create(**work_item_data)
        budget = Budget.objects.create(
            work_item=work_item,
            **budget_data
        )
        return work_item, budget
```

**Why this works:** If budget creation fails, work item creation is automatically rolled back.

**Without transactions:**
```python
# ❌ DANGEROUS - Work item created even if budget fails
work_item = WorkItem.objects.create(**work_item_data)
budget = Budget.objects.create(work_item=work_item, **budget_data)  # Fails!
# Now we have orphaned work item
```

## Transaction Decorators

Use `@transaction.atomic` for entire view functions.

```python
from django.db import transaction
from django.shortcuts import render, redirect

@transaction.atomic
def bulk_import_communities(request):
    """Import multiple communities from file."""
    if request.method == 'POST':
        file = request.FILES['import_file']

        # Parse file
        communities_data = parse_csv(file)

        # Create all communities - all or nothing
        for data in communities_data:
            Community.objects.create(**data)

        return redirect('success')

    return render(request, 'import.html')
```

**When to use:** When entire view should succeed or fail as a unit.

## Atomic Blocks

Wrap specific code sections in transactions, not entire functions.

```python
def process_assessment(assessment_id):
    """Process assessment and update community status."""
    assessment = Assessment.objects.get(id=assessment_id)

    # This runs in transaction
    with transaction.atomic():
        assessment.status = 'processed'
        assessment.processed_at = timezone.now()
        assessment.save()

        # Update community based on assessment
        community = assessment.community
        community.last_assessment_date = timezone.now()
        community.needs_assessment = False
        community.save()

    # This runs outside transaction (slow, external)
    send_notification_email(assessment)
```

**Why separate:** Email sending shouldn't be in transaction - it's slow and external. If email fails, database changes should still be committed.

## Nested Transactions (Savepoints)

Django uses savepoints for nested atomic blocks.

```python
from django.db import transaction

def import_with_validation(data_list):
    """Import data with per-record validation."""
    successful = 0
    failed = []

    with transaction.atomic():  # Outer transaction
        for data in data_list:
            try:
                with transaction.atomic():  # Creates savepoint
                    record = Community.objects.create(**data)
                    validate_record(record)
                    successful += 1
            except Exception as e:
                # Inner transaction rolled back to savepoint
                # Outer transaction continues
                failed.append((data, str(e)))

    return successful, failed
```

**How it works:**
- Outer `atomic()` creates database transaction
- Inner `atomic()` creates savepoint
- If inner fails, rollback to savepoint
- Outer transaction can still commit

**Example with explicit savepoint:**
```python
from django.db import transaction

def complex_operation():
    with transaction.atomic():
        # Create savepoint
        sid = transaction.savepoint()

        try:
            # Risky operation
            perform_risky_operation()
            transaction.savepoint_commit(sid)
        except Exception:
            # Rollback to savepoint
            transaction.savepoint_rollback(sid)
```

## Transaction Isolation

PostgreSQL default is READ COMMITTED. Use row locking for stricter control.

```python
from django.db import transaction

@transaction.atomic
def allocate_budget(budget_id, requested_amount):
    """Allocate budget preventing race conditions."""
    # Lock the row until transaction commits
    budget = Budget.objects.select_for_update().get(id=budget_id)

    if budget.available_amount >= requested_amount:
        budget.available_amount -= requested_amount
        budget.save()

        allocation = Allocation.objects.create(
            budget=budget,
            amount=requested_amount
        )
        return allocation
    else:
        raise InsufficientFunds()
```

**Why this works:** `select_for_update()` locks row until transaction commits, preventing concurrent modifications.

**Without locking:**
```python
# ❌ RACE CONDITION POSSIBLE
# User 1: Reads available=1000
# User 2: Reads available=1000
# User 1: Allocates 800 (available=200)
# User 2: Allocates 800 (available=-600)  # OOPS!
```

**Select for update with timeout:**
```python
# Don't wait forever for lock
budget = Budget.objects.select_for_update(nowait=True).get(id=budget_id)

# Or wait with timeout (PostgreSQL 9.5+)
budget = Budget.objects.select_for_update(skip_locked=True).get(id=budget_id)
```

## Common Pitfalls

**Pitfall 1: Long-running transactions**
```python
# ❌ BAD - External API call in transaction
with transaction.atomic():
    record.save()
    response = requests.post(external_api_url, data)  # SLOW!

# ✅ GOOD - External calls outside transaction
with transaction.atomic():
    record.save()

response = requests.post(external_api_url, data)
```

**Pitfall 2: Not handling transaction errors**
```python
# ❌ BAD - Exception escapes, transaction rolled back silently
with transaction.atomic():
    record.save()
    raise ValueError("Oops")  # Transaction rolled back

# ✅ GOOD - Handle errors appropriately
try:
    with transaction.atomic():
        record.save()
        if not valid:
            raise ValidationError("Invalid data")
except ValidationError as e:
    return JsonResponse({'error': str(e)}, status=400)
```

**Pitfall 3: Mixing autocommit and transactions**
```python
# ❌ BAD - Inconsistent approach
record.save()  # Autocommit
with transaction.atomic():
    other_record.save()

# ✅ GOOD - Use consistent approach
with transaction.atomic():
    record.save()
    other_record.save()
```

**Pitfall 4: Transactions in loops**
```python
# ❌ SLOW - One transaction per iteration
for data in large_dataset:
    with transaction.atomic():
        Community.objects.create(**data)

# ✅ FAST - Single transaction for all
with transaction.atomic():
    for data in large_dataset:
        Community.objects.create(**data)
```

## Performance Considerations

**Batch operations in single transaction:**
```python
# ❌ SLOW - One transaction per record
for data in large_dataset:
    Community.objects.create(**data)

# ✅ FAST - Single transaction for all
with transaction.atomic():
    for data in large_dataset:
        Community.objects.create(**data)

# ✅ FASTEST - Bulk create
with transaction.atomic():
    communities = [Community(**data) for data in large_dataset]
    Community.objects.bulk_create(communities, batch_size=500)
```

**Transaction size matters:**
```python
# ❌ BAD - Huge transaction locks database
with transaction.atomic():
    for i in range(1000000):  # Million records!
        Record.objects.create(value=i)

# ✅ GOOD - Batch into smaller transactions
batch_size = 1000
for batch_start in range(0, 1000000, batch_size):
    with transaction.atomic():
        for i in range(batch_start, batch_start + batch_size):
            Record.objects.create(value=i)
```

## OBCMS-Specific Patterns

**Multi-step work item creation:**
```python
@transaction.atomic
def create_work_item_hierarchy(parent_data, children_data):
    """Create parent work item and children atomically."""
    # Create parent
    parent = WorkItem.objects.create(**parent_data)

    # Create children
    children = []
    for child_data in children_data:
        child = WorkItem.objects.create(
            parent=parent,
            organization=parent.organization,
            **child_data
        )
        children.append(child)

    # Create budget allocations
    for child in children:
        Budget.objects.create(
            work_item=child,
            amount=child.estimated_cost
        )

    return parent, children
```

**Organization-scoped atomic operations:**
```python
@transaction.atomic
def transfer_budget(from_budget_id, to_budget_id, amount):
    """Transfer budget between allocations atomically."""
    # Lock both rows in consistent order (prevent deadlock)
    ids = sorted([from_budget_id, to_budget_id])
    budgets = Budget.objects.select_for_update().filter(id__in=ids)
    from_budget = budgets.get(id=from_budget_id)
    to_budget = budgets.get(id=to_budget_id)

    # Verify same organization
    if from_budget.organization != to_budget.organization:
        raise ValueError("Cannot transfer across organizations")

    # Perform transfer
    if from_budget.available_amount < amount:
        raise InsufficientFunds()

    from_budget.available_amount -= amount
    to_budget.available_amount += amount

    from_budget.save()
    to_budget.save()

    # Log transaction
    BudgetTransfer.objects.create(
        from_budget=from_budget,
        to_budget=to_budget,
        amount=amount
    )
```

**Audit log with transactions:**
```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=WorkItem)
def log_work_item_change(sender, instance, created, **kwargs):
    """Log work item changes within same transaction."""
    # This runs in same transaction as work item save
    AuditLog.objects.create(
        model='WorkItem',
        object_id=instance.id,
        action='created' if created else 'updated',
        user=get_current_user(),
        changes=get_model_changes(instance)
    )
```

## Testing Transactions

```python
from django.test import TestCase, TransactionTestCase

class TransactionTest(TransactionTestCase):
    """Use TransactionTestCase to test transaction behavior."""

    def test_rollback_on_error(self):
        """Verify transaction rolls back on error."""
        initial_count = Community.objects.count()

        with self.assertRaises(ValueError):
            with transaction.atomic():
                Community.objects.create(name="Test")
                raise ValueError("Forced error")

        # Verify rollback happened
        self.assertEqual(Community.objects.count(), initial_count)

    def test_nested_savepoint(self):
        """Test nested transaction with savepoint."""
        with transaction.atomic():
            community1 = Community.objects.create(name="Community 1")

            try:
                with transaction.atomic():  # Savepoint
                    community2 = Community.objects.create(name="Community 2")
                    raise ValueError("Error in nested")
            except ValueError:
                pass  # Nested rolled back

            # Outer transaction continues
            community3 = Community.objects.create(name="Community 3")

        # community1 and community3 exist, community2 doesn't
        self.assertEqual(Community.objects.count(), 2)
```

**Testing race conditions:**
```python
import threading
from django.test import TransactionTestCase

class ConcurrencyTest(TransactionTestCase):
    def test_concurrent_allocation(self):
        """Test concurrent budget allocation."""
        budget = Budget.objects.create(available_amount=1000)

        def allocate():
            try:
                allocate_budget(budget.id, 800)
            except InsufficientFunds:
                pass

        # Run two threads concurrently
        t1 = threading.Thread(target=allocate)
        t2 = threading.Thread(target=allocate)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        # Only one allocation should succeed
        budget.refresh_from_db()
        self.assertEqual(Allocation.objects.count(), 1)
        self.assertEqual(budget.available_amount, 200)
```

## Related Patterns

- See [queries.md](queries.md) for select_for_update and query optimization
- See [data-management.md](data-management.md) for bulk operations
- See [indexes.md](indexes.md) for avoiding lock contention with proper indexes
