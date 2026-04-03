# React Native + Expo Setup Guide

## Prerequisites

- Node.js 22+
- npm or yarn
- Expo CLI: `npm install -g expo-cli`
- iOS Simulator (macOS) or Android Studio (for emulator)
- Expo Go app on physical device (optional)

## Project Initialization

```bash
# Create new Expo project with TypeScript
npx create-expo-app@latest MoroMarketMobile --template expo-template-blank-typescript

cd MoroMarketMobile

# Install core dependencies
npx expo install @react-navigation/native @react-navigation/native-stack @react-navigation/bottom-tabs
npx expo install react-native-screens react-native-safe-area-context
npx expo install @tanstack/react-query
npx expo install expo-secure-store
npx expo install react-native-gesture-handler react-native-reanimated
```

## Project Structure

```
MoroMarketMobile/
├── app/                    # Expo Router (file-based routing)
│   ├── (auth)/             # Auth screens (login, register)
│   ├── (consumer)/         # Consumer tab screens
│   ├── (seller)/           # Seller tab screens
│   └── _layout.tsx         # Root layout
├── components/
│   ├── ui/                 # Reusable UI components
│   ├── consumer/           # Consumer-specific components
│   └── seller/             # Seller-specific components
├── lib/
│   ├── api/                # API client and endpoints
│   ├── hooks/              # Custom hooks
│   ├── services/           # Service classes
│   ├── stores/             # State management
│   └── types/              # TypeScript types
├── assets/
│   ├── images/
│   └── fonts/
└── constants/
    ├── Colors.ts           # Design tokens
    └── Layout.ts           # Layout constants
```

## Environment Configuration

Create `app.config.ts`:

```typescript
import { ExpoConfig, ConfigContext } from 'expo/config'

export default ({ config }: ConfigContext): ExpoConfig => ({
  ...config,
  name: 'MoroMarket',
  slug: 'moromarket',
  version: '1.0.0',
  orientation: 'portrait',
  icon: './assets/icon.png',
  userInterfaceStyle: 'automatic',
  splash: {
    image: './assets/splash.png',
    resizeMode: 'contain',
    backgroundColor: '#0056D2', // Negosyo Blue
  },
  ios: {
    supportsTablet: true,
    bundleIdentifier: 'ph.bangsamoro.moromarket',
  },
  android: {
    adaptiveIcon: {
      foregroundImage: './assets/adaptive-icon.png',
      backgroundColor: '#0056D2',
    },
    package: 'ph.bangsamoro.moromarket',
  },
  extra: {
    apiUrl: process.env.EXPO_PUBLIC_API_URL || 'https://api.moromarket.bangsamoro.site',
    eas: {
      projectId: 'your-project-id',
    },
  },
  plugins: [
    'expo-router',
    'expo-secure-store',
    [
      'expo-build-properties',
      {
        android: {
          compileSdkVersion: 34,
          targetSdkVersion: 34,
          buildToolsVersion: '34.0.0',
        },
        ios: {
          deploymentTarget: '15.0',
        },
      },
    ],
  ],
})
```

## Expo Router Setup

Create `app/_layout.tsx`:

```typescript
import { Stack } from 'expo-router'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { AuthProvider } from '@/lib/providers/AuthProvider'
import { ThemeProvider } from '@/lib/providers/ThemeProvider'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5, // 5 minutes
      retry: 2,
    },
  },
})

export default function RootLayout() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider>
        <AuthProvider>
          <Stack screenOptions={{ headerShown: false }}>
            <Stack.Screen name="(auth)" />
            <Stack.Screen name="(consumer)" />
            <Stack.Screen name="(seller)" />
          </Stack>
        </AuthProvider>
      </ThemeProvider>
    </QueryClientProvider>
  )
}
```

## TypeScript Configuration

Update `tsconfig.json`:

```json
{
  "extends": "expo/tsconfig.base",
  "compilerOptions": {
    "strict": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"],
      "@/components/*": ["components/*"],
      "@/lib/*": ["lib/*"],
      "@/constants/*": ["constants/*"]
    }
  },
  "include": ["**/*.ts", "**/*.tsx", ".expo/types/**/*.ts", "expo-env.d.ts"]
}
```

## Running the App

```bash
# Start development server
npx expo start

# Run on iOS Simulator
npx expo run:ios

# Run on Android Emulator
npx expo run:android

# Run on physical device (scan QR code with Expo Go)
npx expo start --tunnel
```

## EAS Build Configuration

Create `eas.json` for production builds:

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
      }
    },
    "preview": {
      "distribution": "internal",
      "android": {
        "buildType": "apk"
      }
    },
    "production": {
      "autoIncrement": true
    }
  },
  "submit": {
    "production": {}
  }
}
```
