#!/bin/bash
# PostToolUse hook: check guidebook files for banned phrases and known fabrication patterns
# Read-only (grep only). Returns JSON warning if violations found.

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_response.filePath // empty' 2>/dev/null)

# Skip if not a guidebook markdown file
if [ -z "$FILE_PATH" ]; then echo '{}'; exit 0; fi
case "$FILE_PATH" in */guidebooks/*.md) ;; *) echo '{}'; exit 0 ;; esac
if [ ! -f "$FILE_PATH" ]; then echo '{}'; exit 0; fi

V=""

# --- BANNED PHRASES ---

# 1. Guidebooks framed as a series
H=$(grep -n -i "guidebook series\|in this series\|of this series" "$FILE_PATH" 2>/dev/null | head -3)
[ -n "$H" ] && V="${V}BANNED 'guidebook series': lines $(echo "$H" | cut -d: -f1 | tr '\n' ',' | sed 's/,$//') | "

# 2. Co-Authored-By
H=$(grep -n -i "Co-Authored-By" "$FILE_PATH" 2>/dev/null | head -3)
[ -n "$H" ] && V="${V}BANNED 'Co-Authored-By' | "

# 3. Government compliance framing
H=$(grep -n "BARMM staff must\|BARMM staff shall\|the Government shall\|government employees must" "$FILE_PATH" 2>/dev/null | head -3)
[ -n "$H" ] && V="${V}CHECK FRAMING: govt compliance language lines $(echo "$H" | cut -d: -f1 | tr '\n' ',' | sed 's/,$//') | "

# 4. Banned power labels
H=$(grep -n -i "exclusive power\|shared power\|concurrent power" "$FILE_PATH" 2>/dev/null | head -3)
[ -n "$H" ] && V="${V}BANNED power labels: lines $(echo "$H" | cut -d: -f1 | tr '\n' ',' | sed 's/,$//') | "

# 5. Cross-referencing other guidebooks as authoritative sources
H=$(grep -n -i "Bill Drafting Guidebook\|Strategic Planning Guidebook\|CSW Guidebook\|Supervision Guidebook\|MOP Formulation Guidebook\|Cooperative Development Guidebook\|Speech Writing Guidebook" "$FILE_PATH" 2>/dev/null | grep -v "companion publication\|in development\|same author" | head -3)
[ -n "$H" ] && V="${V}CROSS-REF: other guidebook cited as source (not allowed — use enacted law): lines $(echo "$H" | cut -d: -f1 | tr '\n' ',' | sed 's/,$//') | "

# 6. Internal file paths leaked into published content
H=$(grep -n "~/Vault\|~/apps\|~/Library\|~/.gemini\|/Users/saidamen" "$FILE_PATH" 2>/dev/null | head -3)
[ -n "$H" ] && V="${V}INTERNAL PATH LEAKED: remove file paths from published content: lines $(echo "$H" | cut -d: -f1 | tr '\n' ',' | sed 's/,$//') | "

# --- KNOWN FABRICATION PATTERNS ---

# 5. BAA numbers > 89
H=$(grep -noP 'BAA\s*(No\.\s*)?([9][0-9]|[1-9][0-9]{2,})' "$FILE_PATH" 2>/dev/null | head -3)
[ -n "$H" ] && V="${V}FABRICATION: BAA number >89 found: lines $(echo "$H" | cut -d: -f1 | tr '\n' ',' | sed 's/,$//') | "

# 6. Shari'ah Appellate Court (should be Shari'ah High Court)
H=$(grep -n -i "Shari.ah Appellate Court" "$FILE_PATH" 2>/dev/null | head -3)
[ -n "$H" ] && V="${V}FABRICATION: 'Shari'ah Appellate Court' should be 'Shari'ah High Court' | "

# 7. Six provinces (should be 5 after Sulu ruling)
H=$(grep -n -i "six provinces\|6 provinces" "$FILE_PATH" 2>/dev/null | head -3)
[ -n "$H" ] && V="${V}FABRICATION: '6 provinces' should be 5 after Sulu ruling | "

# 8. Wrong ministry abbreviations
H=$(grep -n -w "MOL\b\|MST\b\|MPWH\b\|MOSD\b" "$FILE_PATH" 2>/dev/null | head -3)
[ -n "$H" ] && V="${V}FABRICATION: wrong ministry abbreviation: lines $(echo "$H" | cut -d: -f1 | tr '\n' ',' | sed 's/,$//') | "

if [ -n "$V" ]; then
  SFP=$(echo "$FILE_PATH" | sed 's/"/\\"/g')
  SV=$(echo "$V" | sed 's/"/\\"/g')
  echo "{\"systemMessage\": \"VIOLATION in ${SFP}: ${SV}Fix before proceeding.\", \"hookSpecificOutput\": {\"hookEventName\": \"PostToolUse\", \"additionalContext\": \"VIOLATION FOUND. Fix the issues listed in systemMessage IMMEDIATELY before telling the user the file is ready.\"}}"
else
  echo '{}'
fi
