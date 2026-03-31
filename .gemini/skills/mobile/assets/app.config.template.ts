/**
 * MoroMarket Mobile App Configuration Template
 *
 * Copy this file to your mobile project as app.config.ts
 * and customize the values.
 */

import { ExpoConfig, ConfigContext } from 'expo/config'

export default ({ config }: ConfigContext): ExpoConfig => ({
  ...config,

  // ==========================================================================
  // App Identity
  // ==========================================================================
  name: 'MoroMarket',
  slug: 'moromarket',
  version: '1.0.0',
  orientation: 'portrait',

  // ==========================================================================
  // Assets
  // ==========================================================================
  icon: './assets/icon.png',
  userInterfaceStyle: 'automatic',
  splash: {
    image: './assets/splash.png',
    resizeMode: 'contain',
    backgroundColor: '#0056D2', // Negosyo Blue
  },

  // ==========================================================================
  // iOS Configuration
  // ==========================================================================
  ios: {
    supportsTablet: true,
    bundleIdentifier: 'ph.bangsamoro.moromarket',
    buildNumber: '1',
    config: {
      usesNonExemptEncryption: false,
    },
    infoPlist: {
      NSCameraUsageDescription: 'MoroMarket needs camera access to scan QR codes and take product photos.',
      NSPhotoLibraryUsageDescription: 'MoroMarket needs photo library access to upload product images.',
      NSLocationWhenInUseUsageDescription: 'MoroMarket uses your location to find nearby cooperatives and estimate delivery.',
    },
  },

  // ==========================================================================
  // Android Configuration
  // ==========================================================================
  android: {
    adaptiveIcon: {
      foregroundImage: './assets/adaptive-icon.png',
      backgroundColor: '#0056D2',
    },
    package: 'ph.bangsamoro.moromarket',
    versionCode: 1,
    permissions: [
      'CAMERA',
      'READ_EXTERNAL_STORAGE',
      'WRITE_EXTERNAL_STORAGE',
      'ACCESS_COARSE_LOCATION',
      'ACCESS_FINE_LOCATION',
      'RECEIVE_BOOT_COMPLETED',
      'VIBRATE',
    ],
    googleServicesFile: './google-services.json',
  },

  // ==========================================================================
  // Web Configuration (Optional)
  // ==========================================================================
  web: {
    bundler: 'metro',
    favicon: './assets/favicon.png',
  },

  // ==========================================================================
  // Expo Updates (OTA)
  // ==========================================================================
  updates: {
    enabled: true,
    url: 'https://u.expo.dev/your-project-id',
    fallbackToCacheTimeout: 0,
    checkAutomatically: 'ON_LOAD',
  },
  runtimeVersion: {
    policy: 'sdkVersion',
  },

  // ==========================================================================
  // Deep Linking
  // ==========================================================================
  scheme: 'moromarket',

  // ==========================================================================
  // Environment Variables
  // ==========================================================================
  extra: {
    // API Configuration
    apiUrl: process.env.EXPO_PUBLIC_API_URL || 'https://api.moromarket.bangsamoro.site',

    // Feature Flags
    enableOfflineMode: true,
    enablePushNotifications: true,
    enableAnalytics: process.env.NODE_ENV === 'production',

    // App Info
    appName: 'MoroMarket',
    supportEmail: 'support@moromarket.bangsamoro.site',
    privacyPolicyUrl: 'https://moromarket.bangsamoro.site/privacy',
    termsOfServiceUrl: 'https://moromarket.bangsamoro.site/terms',

    // EAS Project
    eas: {
      projectId: 'your-eas-project-id',
    },
  },

  // ==========================================================================
  // Expo Owner (for EAS)
  // ==========================================================================
  owner: 'bangsamoro',

  // ==========================================================================
  // Plugins
  // ==========================================================================
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
          minSdkVersion: 24,
        },
        ios: {
          deploymentTarget: '15.0',
        },
      },
    ],
    [
      'expo-notifications',
      {
        icon: './assets/notification-icon.png',
        color: '#0056D2',
        sounds: [],
      },
    ],
    [
      'expo-location',
      {
        locationAlwaysAndWhenInUsePermission: 'MoroMarket uses your location to find nearby cooperatives.',
      },
    ],
    [
      'expo-camera',
      {
        cameraPermission: 'MoroMarket needs camera access to scan QR codes.',
      },
    ],
    [
      'expo-image-picker',
      {
        photosPermission: 'MoroMarket needs photo access to upload product images.',
      },
    ],
  ],

  // ==========================================================================
  // Experiments
  // ==========================================================================
  experiments: {
    typedRoutes: true,
  },
})
