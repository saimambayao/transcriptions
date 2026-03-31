# App Store Deployment Guide

## Prerequisites

1. **Apple Developer Account** ($99/year) - For iOS App Store
2. **Google Play Developer Account** ($25 one-time) - For Play Store
3. **EAS CLI**: `npm install -g eas-cli`
4. **Expo Account**: Run `eas login`

## EAS Build Setup

### Initialize EAS

```bash
cd MoroMarketMobile
eas build:configure
```

### Configure `eas.json`

```json
{
  "cli": {
    "version": ">= 7.0.0"
  },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal",
      "ios": {
        "simulator": true
      },
      "env": {
        "EXPO_PUBLIC_API_URL": "http://localhost:8090"
      }
    },
    "preview": {
      "distribution": "internal",
      "android": {
        "buildType": "apk"
      },
      "env": {
        "EXPO_PUBLIC_API_URL": "https://staging-api.moromarket.bangsamoro.site"
      }
    },
    "production": {
      "autoIncrement": true,
      "env": {
        "EXPO_PUBLIC_API_URL": "https://api.moromarket.bangsamoro.site"
      }
    }
  },
  "submit": {
    "production": {
      "ios": {
        "appleId": "your@email.com",
        "ascAppId": "your-app-store-connect-id"
      },
      "android": {
        "serviceAccountKeyPath": "./google-service-account.json"
      }
    }
  }
}
```

## iOS Deployment

### 1. App Store Connect Setup

1. Go to [App Store Connect](https://appstoreconnect.apple.com)
2. Create new app with bundle ID: `ph.bangsamoro.moromarket`
3. Fill in app information, screenshots, description

### 2. Build for iOS

```bash
# Production build
eas build --platform ios --profile production

# Submit to App Store
eas submit --platform ios --latest
```

### 3. App Store Metadata

**App Name**: MoroMarket - Bangsamoro Marketplace

**Subtitle**: Shop from Cooperatives & Social Enterprises

**Description**:
```
MoroMarket is the official marketplace app of the Bangsamoro Autonomous Region, connecting you directly with cooperatives and social enterprises across BARMM.

FOR CONSUMERS:
- Browse products from verified cooperatives and social enterprises
- Support local businesses and community development
- Track orders from purchase to delivery
- Save favorites and get notified of deals

FOR SELLERS (Coops & SEs):
- Manage your product catalog on-the-go
- Process orders instantly with push notifications
- Track inventory and get low-stock alerts
- View sales analytics and performance metrics

FEATURES:
- Secure payments via GCash, Maya, and bank transfer
- Offline browsing for areas with limited connectivity
- Multi-language support (English, Filipino, Tausug)
- Direct chat with sellers

Download MoroMarket and join the Bangsamoro digital economy!
```

**Keywords**: marketplace, bangsamoro, cooperative, social enterprise, BARMM, halal, local products, community trade

**Category**: Shopping

### 4. iOS Screenshots Sizes

- 6.7" (iPhone 14 Pro Max): 1290 x 2796
- 6.5" (iPhone 11 Pro Max): 1242 x 2688
- 5.5" (iPhone 8 Plus): 1242 x 2208
- 12.9" iPad Pro: 2048 x 2732

## Android Deployment

### 1. Google Play Console Setup

1. Go to [Google Play Console](https://play.google.com/console)
2. Create new app with package: `ph.bangsamoro.moromarket`
3. Complete store listing

### 2. Service Account for Automated Submission

1. Google Cloud Console > Create service account
2. Grant "Service Account User" role
3. Download JSON key as `google-service-account.json`
4. In Play Console, invite service account email with "Release Manager" access

### 3. Build for Android

```bash
# Production AAB (for Play Store)
eas build --platform android --profile production

# Submit to Play Store
eas submit --platform android --latest
```

### 4. Play Store Metadata

**Title**: MoroMarket - Bangsamoro Marketplace

**Short Description** (80 chars):
Shop directly from Bangsamoro cooperatives and social enterprises

**Full Description**: (Same as iOS)

**Category**: Shopping

### 5. Android Screenshots Sizes

- Phone: 1080 x 1920 (minimum)
- 7" Tablet: 1200 x 1920
- 10" Tablet: 1920 x 1200

## Version Management

### Semantic Versioning

```
MAJOR.MINOR.PATCH
1.0.0 - Initial release
1.1.0 - New feature (offline support)
1.1.1 - Bug fix
2.0.0 - Breaking change (new architecture)
```

### Auto-increment with EAS

In `eas.json`, `autoIncrement: true` handles build numbers:
- iOS: Increments `buildNumber`
- Android: Increments `versionCode`

## Over-the-Air (OTA) Updates

For JavaScript-only updates (no native changes):

```bash
# Create update
eas update --branch production --message "Bug fix for cart"

# Preview before release
eas update --branch preview --message "Testing new feature"
```

Configure in `app.config.ts`:

```typescript
{
  updates: {
    enabled: true,
    url: 'https://u.expo.dev/your-project-id',
    fallbackToCacheTimeout: 0,
    checkAutomatically: 'ON_LOAD',
  },
}
```

## Pre-Submission Checklist

### Both Platforms
- [ ] App icons (all sizes)
- [ ] Splash screen
- [ ] Privacy policy URL
- [ ] Terms of service URL
- [ ] Support email
- [ ] Screenshots for all required sizes
- [ ] App description (localized if needed)
- [ ] Test on physical devices

### iOS Specific
- [ ] App Store Connect metadata complete
- [ ] Export compliance (uses encryption?)
- [ ] Age rating questionnaire
- [ ] App Preview video (optional)

### Android Specific
- [ ] Content rating questionnaire
- [ ] Data safety form
- [ ] Target API level compliance (currently API 34)
- [ ] Feature graphic (1024 x 500)

## CI/CD with GitHub Actions

Create `.github/workflows/eas-build.yml`:

```yaml
name: EAS Build

on:
  push:
    branches: [main]
    paths:
      - 'mobile/**'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: mobile/package-lock.json

      - name: Setup EAS
        uses: expo/expo-github-action@v8
        with:
          eas-version: latest
          token: ${{ secrets.EXPO_TOKEN }}

      - name: Install dependencies
        run: npm ci
        working-directory: mobile

      - name: Build iOS
        run: eas build --platform ios --profile production --non-interactive
        working-directory: mobile

      - name: Build Android
        run: eas build --platform android --profile production --non-interactive
        working-directory: mobile
```

## Monitoring & Analytics

### Expo Insights

Built-in crash reporting and analytics:
- Crash reports
- Update adoption
- Build performance

### Optional: Sentry Integration

```bash
npx expo install @sentry/react-native
```

```typescript
// app/_layout.tsx
import * as Sentry from '@sentry/react-native'

Sentry.init({
  dsn: 'your-sentry-dsn',
  environment: __DEV__ ? 'development' : 'production',
})
```
