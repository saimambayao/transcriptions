# Common OCR Errors Reference

## Numeric OCR Errors

| Original | Misread As | Example |
|----------|-----------|---------|
| `5` | `9` | 542 → 942, 588 → 988 |
| `1` | `7` | 1.9 → 7.9 |
| `0` | `O` | 100 → 1OO |
| `8` | `3` | 8.5 → 3.5 |
| Missing decimal | - | 1.5 → 15 |
| Comma/period swap | - | 1,000 → 1.000 |

## Character Confusion

| Original | Misread As | Notes |
|----------|-----------|-------|
| `l` (lowercase L) | `1` or `I` | Context-dependent |
| `O` (letter) | `0` (zero) | Check if numeric context |
| `rn` | `m` | Common in serif fonts |
| `cl` | `d` | Kerning issue |
| `vv` | `w` | Rare |

## Special Characters

| Original | Misread As |
|----------|-----------|
| `—` (em dash) | `-` or `--` |
| `'` (smart quote) | `'` or missing |
| `"` (smart quotes) | `"` or `''` |
| `…` (ellipsis) | `...` or `. . .` |
| `°` (degree) | `o` or `0` |
| `×` (times) | `x` |

## Table OCR Issues

### Column Alignment
- Columns may merge when spacing is tight
- Headers may split across lines
- Numeric columns may lose alignment

### Cell Values
- Empty cells may be missed entirely
- Merged cells not recognized
- Row/header confusion in multi-page tables

### Fixes
1. Extract tables separately at higher DPI (600)
2. Manually reconstruct table structure
3. Cross-reference with source for numeric values

## Philippine/Filipino Context

Common issues with Philippine documents:

| Issue | Example |
|-------|---------|
| Peso sign | `₱` → `P` or missing |
| Filipino names | Diacritics may be lost |
| Barangay names | Local spellings may vary |
| Legal citations | RA/PD numbers may error |

## Verification Priority

When verifying transcriptions, prioritize:

1. **Numeric data** - Most critical, highest error rate
2. **Tables** - Structure and values
3. **Proper nouns** - Names, places, organizations
4. **Legal citations** - RA numbers, section references
5. **Dates** - Year confusion common
