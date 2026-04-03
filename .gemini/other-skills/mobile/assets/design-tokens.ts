/**
 * MoroMarket Mobile Design Tokens
 *
 * Design system tokens aligned with Bangsamoro Digital Platform branding.
 * Primary color: Negosyo Blue (#0056D2)
 *
 * Usage:
 * import { Colors, Typography, Spacing, Shadows } from '@/constants/design-tokens'
 */

// =============================================================================
// Colors
// =============================================================================

export const Colors = {
  // Primary Brand Colors
  primary: '#0056D2', // Negosyo Blue
  primaryLight: '#3378DB',
  primaryDark: '#004BB5',
  primaryFaded: '#E6F0FA',

  // Secondary/Accent (for hero sections, promotions)
  accent: '#D30A28', // Negosyo Red
  accentLight: '#E53E55',
  accentDark: '#B00820',

  // Semantic Colors
  success: '#22C55E',
  successLight: '#DCFCE7',
  warning: '#F59E0B',
  warningLight: '#FEF3C7',
  error: '#EF4444',
  errorLight: '#FEE2E2',
  info: '#3B82F6',
  infoLight: '#DBEAFE',

  // Neutral/Gray Scale
  white: '#FFFFFF',
  black: '#000000',
  gray: {
    50: '#F9FAFB',
    100: '#F3F4F6',
    200: '#E5E7EB',
    300: '#D1D5DB',
    400: '#9CA3AF',
    500: '#6B7280',
    600: '#4B5563',
    700: '#374151',
    800: '#1F2937',
    900: '#111827',
  },

  // Background Colors
  background: {
    default: '#FFFFFF',
    secondary: '#F9FAFB',
    tertiary: '#F3F4F6',
  },

  // Text Colors
  text: {
    primary: '#111827',
    secondary: '#4B5563',
    tertiary: '#6B7280',
    inverse: '#FFFFFF',
    link: '#0056D2',
  },

  // Border Colors
  border: {
    default: '#E5E7EB',
    focused: '#0056D2',
    error: '#EF4444',
  },

  // Status Colors (for orders, inventory)
  status: {
    pending: '#F59E0B',
    processing: '#3B82F6',
    shipped: '#8B5CF6',
    delivered: '#22C55E',
    cancelled: '#EF4444',
    lowStock: '#F59E0B',
    outOfStock: '#EF4444',
    inStock: '#22C55E',
  },
} as const

// =============================================================================
// Typography
// =============================================================================

export const Typography = {
  // Font Families
  fontFamily: {
    regular: 'System',
    medium: 'System',
    semiBold: 'System',
    bold: 'System',
  },

  // Font Sizes
  fontSize: {
    xs: 11,
    sm: 13,
    base: 15,
    lg: 17,
    xl: 20,
    '2xl': 24,
    '3xl': 30,
    '4xl': 36,
  },

  // Line Heights
  lineHeight: {
    tight: 1.25,
    normal: 1.5,
    relaxed: 1.75,
  },

  // Font Weights
  fontWeight: {
    regular: '400' as const,
    medium: '500' as const,
    semiBold: '600' as const,
    bold: '700' as const,
  },

  // Pre-defined Text Styles
  styles: {
    // Headings
    h1: {
      fontSize: 30,
      fontWeight: '700' as const,
      lineHeight: 36,
    },
    h2: {
      fontSize: 24,
      fontWeight: '700' as const,
      lineHeight: 32,
    },
    h3: {
      fontSize: 20,
      fontWeight: '600' as const,
      lineHeight: 28,
    },
    h4: {
      fontSize: 17,
      fontWeight: '600' as const,
      lineHeight: 24,
    },

    // Body Text
    bodyLarge: {
      fontSize: 17,
      fontWeight: '400' as const,
      lineHeight: 26,
    },
    body: {
      fontSize: 15,
      fontWeight: '400' as const,
      lineHeight: 22,
    },
    bodySmall: {
      fontSize: 13,
      fontWeight: '400' as const,
      lineHeight: 20,
    },

    // Labels
    label: {
      fontSize: 13,
      fontWeight: '500' as const,
      lineHeight: 18,
    },
    labelSmall: {
      fontSize: 11,
      fontWeight: '500' as const,
      lineHeight: 16,
    },

    // Buttons
    button: {
      fontSize: 15,
      fontWeight: '600' as const,
      lineHeight: 20,
    },
    buttonSmall: {
      fontSize: 13,
      fontWeight: '600' as const,
      lineHeight: 18,
    },

    // Captions
    caption: {
      fontSize: 11,
      fontWeight: '400' as const,
      lineHeight: 16,
    },
  },
} as const

// =============================================================================
// Spacing
// =============================================================================

export const Spacing = {
  // Base spacing scale (4px increments)
  0: 0,
  0.5: 2,
  1: 4,
  1.5: 6,
  2: 8,
  2.5: 10,
  3: 12,
  3.5: 14,
  4: 16,
  5: 20,
  6: 24,
  7: 28,
  8: 32,
  9: 36,
  10: 40,
  12: 48,
  14: 56,
  16: 64,
  20: 80,
  24: 96,

  // Semantic spacing
  screenPadding: 16,
  cardPadding: 16,
  sectionGap: 24,
  listItemGap: 12,
  inputPadding: 12,
  buttonPaddingX: 16,
  buttonPaddingY: 12,
} as const

// =============================================================================
// Border Radius
// =============================================================================

export const BorderRadius = {
  none: 0,
  sm: 4,
  md: 8,
  lg: 12,
  xl: 16,
  '2xl': 20,
  full: 9999,

  // Semantic
  button: 8,
  card: 12,
  input: 8,
  modal: 16,
  avatar: 9999,
  badge: 4,
} as const

// =============================================================================
// Shadows
// =============================================================================

export const Shadows = {
  none: {
    shadowColor: 'transparent',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0,
    shadowRadius: 0,
    elevation: 0,
  },
  sm: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.05,
    shadowRadius: 2,
    elevation: 1,
  },
  md: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  lg: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.15,
    shadowRadius: 8,
    elevation: 4,
  },
  xl: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.2,
    shadowRadius: 16,
    elevation: 8,
  },

  // Semantic
  card: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.08,
    shadowRadius: 4,
    elevation: 2,
  },
  modal: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.25,
    shadowRadius: 24,
    elevation: 8,
  },
  bottomTab: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: -2 },
    shadowOpacity: 0.05,
    shadowRadius: 4,
    elevation: 4,
  },
} as const

// =============================================================================
// Animation
// =============================================================================

export const Animation = {
  duration: {
    fast: 150,
    normal: 250,
    slow: 400,
  },
  easing: {
    ease: 'ease',
    easeIn: 'ease-in',
    easeOut: 'ease-out',
    easeInOut: 'ease-in-out',
  },
} as const

// =============================================================================
// Z-Index
// =============================================================================

export const ZIndex = {
  base: 0,
  dropdown: 10,
  sticky: 20,
  fixed: 30,
  modalBackdrop: 40,
  modal: 50,
  popover: 60,
  tooltip: 70,
  toast: 80,
} as const

// =============================================================================
// Icon Sizes
// =============================================================================

export const IconSize = {
  xs: 12,
  sm: 16,
  md: 20,
  lg: 24,
  xl: 32,
  '2xl': 40,

  // Semantic
  tabBar: 24,
  button: 20,
  input: 20,
  listItem: 24,
  avatar: 40,
} as const
