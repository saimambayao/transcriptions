"""
Seed Data Management Command Template

Copy this template to:
backend/apps/<app_name>/management/commands/seed_<entity>.py

Usage:
    python manage.py seed_<entity>
    python manage.py seed_<entity> --count 50
    python manage.py seed_<entity> --clear --count 20
"""

from django.core.management.base import BaseCommand
from django.db import transaction
# from apps.<app_name>.models import <Entity>
# from apps.core.models import Organization
import random


class Command(BaseCommand):
    help = 'Seed database with sample <entity> data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding',
        )
        parser.add_argument(
            '--count',
            type=int,
            default=20,
            help='Number of records to create (default: 20)',
        )
        parser.add_argument(
            '--org',
            type=str,
            default='demo',
            help='Organization shortname to use (default: demo)',
        )

    @transaction.atomic
    def handle(self, *args, **options):
        # Uncomment and customize the following:

        # Clear existing data if requested
        # if options['clear']:
        #     <Entity>.objects.all().delete()
        #     self.stdout.write(self.style.WARNING('Cleared existing <entity> data'))

        # Get or create organization
        # org, created = Organization.objects.get_or_create(
        #     shortname=options['org'],
        #     defaults={'name': f"{options['org'].title()} Organization"}
        # )
        # if created:
        #     self.stdout.write(f'Created organization: {org.name}')

        # Sample data templates
        sample_data = [
            {'name': 'Sample Item 1', 'description': 'Description 1'},
            {'name': 'Sample Item 2', 'description': 'Description 2'},
            {'name': 'Sample Item 3', 'description': 'Description 3'},
        ]

        # Categories or other lookup data
        categories = ['category_a', 'category_b', 'category_c']

        created_count = 0
        for i in range(options['count']):
            sample = random.choice(sample_data)

            # Customize this creation logic:
            # <Entity>.objects.create(
            #     organization=org,
            #     name=f"{sample['name']} #{i+1}",
            #     description=sample['description'],
            #     category=random.choice(categories),
            #     is_active=True,
            #     # Add more fields as needed
            # )

            created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Created {created_count} <entity> records')
        )

        # Optionally print summary
        # total = <Entity>.objects.count()
        # self.stdout.write(f'Total <entity> records in database: {total}')
