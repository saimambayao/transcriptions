#!/bin/bash
#
# Rollback Script for OBCMS
#
# ⚠️ IMPORTANT: This is a TEMPLATE script.
# This script helps rollback failed deployments.
#
# Usage: ./rollback.sh [staging|production]
#

set -e

if [ $# -eq 0 ]; then
    echo "Usage: ./rollback.sh [staging|production]"
    exit 1
fi

ENVIRONMENT=$1

echo "========================================="
echo "OBCMS Deployment Rollback"
echo "Environment: $ENVIRONMENT"
echo "========================================="
echo

# Confirm rollback
echo "⚠️  ROLLBACK CONFIRMATION"
echo "This will rollback the $ENVIRONMENT deployment"
read -p "Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Rollback cancelled"
    exit 0
fi

# Switch to environment
railway environment $ENVIRONMENT

# List recent deployments
echo
echo "Recent deployments:"
railway deployments

echo
echo "To rollback via Railway dashboard:"
echo "1. Go to https://railway.app/project/<your-project>"
echo "2. Click on Deployments tab"
echo "3. Find previous successful deployment"
echo "4. Click 'Redeploy'"
echo
echo "To rollback via git:"
echo "1. Identify commit to revert to"
echo "2. git revert HEAD  (or git reset --hard <commit>)"
echo "3. git push origin <branch>"
echo
read -p "Open Railway dashboard? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    railway open
fi
