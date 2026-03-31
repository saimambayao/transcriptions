#!/bin/bash
#
# Post-Deployment Verification Script for OBCMS
#
# ⚠️ IMPORTANT: This is a TEMPLATE script.
# Customize endpoints and tests for your application.
#
# Usage: ./verify-deployment.sh [staging|production]
#

set -e

if [ $# -eq 0 ]; then
    echo "Usage: ./verify-deployment.sh [staging|production]"
    exit 1
fi

ENVIRONMENT=$1

echo "========================================="
echo "OBCMS Deployment Verification"
echo "Environment: $ENVIRONMENT"
echo "========================================="
echo

# Switch to environment
railway environment $ENVIRONMENT

# Get Railway URL
echo "Getting deployment URL..."
RAILWAY_URL=$(railway vars get RAILWAY_PUBLIC_DOMAIN)
if [ -z "$RAILWAY_URL" ]; then
    echo "⚠️  Could not get Railway URL"
    read -p "Enter deployment URL: " RAILWAY_URL
fi

BASE_URL="https://$RAILWAY_URL"
echo "Testing URL: $BASE_URL"
echo

# Test 1: Health check
echo "Test 1: Health check endpoint..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/health/" || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "✓ Health check passed (200 OK)"
else
    echo "❌ Health check failed (HTTP $HTTP_CODE)"
fi

# Test 2: Home page
echo
echo "Test 2: Home page..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/" || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "✓ Home page accessible (200 OK)"
else
    echo "⚠️  Home page returned HTTP $HTTP_CODE"
fi

# Test 3: Static files
echo
echo "Test 3: Static files..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/static/css/main.css" || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "✓ Static files served (200 OK)"
else
    echo "⚠️  Static files check returned HTTP $HTTP_CODE"
fi

# Test 4: Database migrations
echo
echo "Test 4: Database migrations..."
railway run python manage.py showmigrations --plan | tail -n 5
echo

# Test 5: Monitor logs
echo "Test 5: Checking recent logs for errors..."
railway logs | grep -i "error\|exception\|failed" | head -n 10 || echo "✓ No recent errors in logs"

echo
echo "========================================="
echo "Verification complete"
echo "Review results above"
echo "========================================="
echo
echo "Monitor deployment for next 10 minutes:"
echo "  railway logs --tail"
