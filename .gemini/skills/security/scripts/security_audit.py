#!/usr/bin/env python3
"""Run security audit checks."""
import sys

print("""
# Django Security Checklist

1. Check settings:
   - DEBUG = False in production
   - SECRET_KEY is secret and unique
   - ALLOWED_HOSTS configured
   - CSRF_TRUSTED_ORIGINS set

2. Run Django check:
   python manage.py check --deploy

3. Check dependencies:
   pip-audit

4. Review permissions and access controls
""")
