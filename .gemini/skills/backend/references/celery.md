# Celery Background Tasks

Guide for asynchronous task processing with Celery.

## Setup

```python
# celery.py
from celery import Celery
import os

os.setdefault('DJANGO_SETTINGS_MODULE', 'obc_management.settings')

app = Celery('obc_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Manila'
```

## Basic Tasks

```python
# tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_assessment_notification(assessment_id):
    """Send notification when assessment is completed."""
    assessment = Assessment.objects.get(pk=assessment_id)
    send_mail(
        'Assessment Completed',
        f'Assessment for {assessment.community.name} is complete.',
        'noreply@obcms.gov.ph',
        [assessment.created_by.email],
    )

# Usage in views
from .tasks import send_assessment_notification

def complete_assessment(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    assessment.status = 'COMPLETED'
    assessment.save()
    
    # Run task asynchronously
    send_assessment_notification.delay(assessment.id)
    
    return redirect('assessment:detail', pk=pk)
```

## Periodic Tasks

```python
from celery import shared_task
from celery.schedules import crontab

@shared_task
def generate_monthly_report():
    """Generate monthly statistics report."""
    # Generate report logic
    pass

# settings.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'generate-monthly-report': {
        'task': 'communities.tasks.generate_monthly_report',
        'schedule': crontab(day_of_month='1', hour='0', minute='0'),
    },
}
```

## Task Chaining

```python
from celery import chain

@shared_task
def process_import(file_path):
    """Process imported data."""
    # Processing logic
    return {'records_processed': 100}

@shared_task
def send_import_summary(result):
    """Send import summary email."""
    send_mail(
        'Import Complete',
        f'Processed {result["records_processed"]} records',
        'noreply@obcms.gov.ph',
        ['admin@obcms.gov.ph'],
    )

# Chain tasks
chain(process_import.s(file_path), send_import_summary.s()).apply_async()
```

For file handling, see [files.md](files.md).
