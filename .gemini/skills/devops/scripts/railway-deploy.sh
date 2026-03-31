#!/bin/bash
#
# Railway Deployment Script for OBCMS
# 
# ⚠️ IMPORTANT: This is a TEMPLATE script.
# Review and customize before using!
# This script is NOT auto-executed by the devops skill.
#
# Usage: ./railway-deploy.sh [staging|production]
#

set -e  # Exit on error

# Check arguments
if [ $# -eq 0 ]; then
    echo "Usage: ./railway-deploy.sh [staging|production]"
    exit 1
fi

ENVIRONMENT=$1

# Validate environment
if [ "$ENVIRONMENT" != "staging" ] && [ "$ENVIRONMENT" != "production" ]; then
    echo "Error: Environment must be 'staging' or 'production'"
    exit 1
fi

echo "========================================="
echo "OBCMS Railway Deployment"
echo "Environment: $ENVIRONMENT"
echo "========================================="
echo

# Step 1: Verify git status
echo "Step 1: Checking git status..."
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Warning: You have uncommitted changes"
    git status --short
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Step 2: Verify tests pass (optional - comment out if not applicable)
echo
echo "Step 2: Running tests..."
# cd src && pytest --tb=short || {
#     echo "❌ Tests failed!"
#     exit 1
# }
echo "✓ Tests passed (or skipped)"

# Step 3: Switch to correct Railway environment
echo
echo "Step 3: Switching to Railway environment: $ENVIRONMENT..."
railway environment $ENVIRONMENT || {
    echo "❌ Failed to switch environment"
    exit 1
}

# Step 4: Confirm deployment
echo
echo "⚠️  CONFIRMATION REQUIRED"
echo "You are about to deploy to: $ENVIRONMENT"
echo "Current branch: $(git branch --show-current)"
echo "Latest commit: $(git log -1 --oneline)"
echo
read -p "Deploy to $ENVIRONMENT? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled"
    exit 0
fi

# Step 5: Deploy
echo
echo "Step 5: Deploying to $ENVIRONMENT..."
if [ "$ENVIRONMENT" = "staging" ]; then
    git push origin staging
elif [ "$ENVIRONMENT" = "production" ]; then
    # Extra confirmation for production
    echo
    echo "⚠️⚠️⚠️  PRODUCTION DEPLOYMENT  ⚠️⚠️⚠️"
    read -p "Are you ABSOLUTELY SURE? (type 'yes'): " CONFIRM
    if [ "$CONFIRM" != "yes" ]; then
        echo "Production deployment cancelled"
        exit 0
    fi
    git push origin main
fi

# Step 6: Monitor deployment
echo
echo "Step 6: Monitoring deployment..."
echo "Opening Railway logs..."
echo "Press Ctrl+C to stop monitoring (deployment will continue)"
echo
sleep 2
railway logs --tail

echo
echo "========================================="
echo "Deployment command completed"
echo "Verify deployment success manually"
echo "========================================="
