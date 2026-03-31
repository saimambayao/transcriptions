# Data Migration Template
from django.db import migrations

def forward_migration(apps, schema_editor):
    """Apply data changes."""
    Model = apps.get_model('app', 'Model')
    # Your migration logic here
    pass

def reverse_migration(apps, schema_editor):
    """Reverse data changes."""
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('app', 'previous_migration'),
    ]
    
    operations = [
        migrations.RunPython(forward_migration, reverse_migration),
    ]
