#!/usr/bin/env python3
"""Analyze slow database queries."""
import sys

print("""
# Run this in Django shell:
from django.db import connection
from django.db import reset_queries

# Enable query logging
settings.DEBUG = True

# Your code here
# ...

# Analyze queries
for query in connection.queries:
    if float(query['time']) > 0.01:  # Slow queries
        print(f"Time: {query['time']}s")
        print(f"SQL: {query['sql']}")
""")
