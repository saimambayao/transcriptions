#!/bin/bash
#
# Database Backup Script for OBCMS
#
# ⚠️ IMPORTANT: This is a TEMPLATE script.
# Review and customize before using!
#
# Usage: ./backup-database.sh [staging|production]
#

set -e

if [ $# -eq 0 ]; then
    echo "Usage: ./backup-database.sh [staging|production]"
    exit 1
fi

ENVIRONMENT=$1
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE="obcms-${ENVIRONMENT}-backup-${TIMESTAMP}.sql"

echo "========================================="
echo "OBCMS Database Backup"
echo "Environment: $ENVIRONMENT"
echo "Backup file: $BACKUP_FILE"
echo "========================================="
echo

# Switch to environment
echo "Switching to Railway environment: $ENVIRONMENT..."
railway environment $ENVIRONMENT

# Create backup
echo "Creating database backup..."
railway run pg_dump > "$BACKUP_FILE"

# Verify backup
if [ -f "$BACKUP_FILE" ]; then
    SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo "✓ Backup created: $BACKUP_FILE ($SIZE)"
    echo
    echo "Backup location: $(pwd)/$BACKUP_FILE"
    echo
    echo "⚠️  Store this backup securely!"
    echo "To restore: railway run psql < $BACKUP_FILE"
else
    echo "❌ Backup failed!"
    exit 1
fi
