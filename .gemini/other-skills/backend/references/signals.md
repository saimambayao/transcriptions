# Django Signals

Guide for Django signals and audit logging.

## Model Signals

```python
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=Community)
def community_created(sender, instance, created, **kwargs):
    """Handle community creation."""
    if created:
        # Create initial assessment placeholder
        Assessment.objects.create(
            community=instance,
            status='PENDING',
            created_by=instance.created_by
        )

@receiver(pre_save, sender=Program)
def program_status_change(sender, instance, **kwargs):
    """Track status changes."""
    if instance.pk:
        old = Program.objects.get(pk=instance.pk)
        if old.status != instance.status:
            # Log status change
            StatusLog.objects.create(
                program=instance,
                old_status=old.status,
                new_status=instance.status,
                changed_by=instance.updated_by
            )

@receiver(post_delete, sender=Beneficiary)
def beneficiary_deleted(sender, instance, **kwargs):
    """Log deletion."""
    import logging
    logger = logging.getLogger('deletions')
    logger.info(f'Beneficiary {instance.id} deleted')
```

## Custom Signals

```python
# communities/signals.py
from django.dispatch import Signal

assessment_approved = Signal()  # Custom signal

# Send signal
assessment_approved.send(sender=Assessment, instance=assessment, approved_by=user)

# Receive signal
@receiver(assessment_approved)
def handle_assessment_approval(sender, instance, approved_by, **kwargs):
    """Handle assessment approval."""
    # Send notification
    send_notification(instance.created_by, f'Your assessment was approved by {approved_by}')
```

For background tasks, see [celery.md](celery.md).
