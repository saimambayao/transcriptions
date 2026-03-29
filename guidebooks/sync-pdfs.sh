#!/bin/bash
# Copies the latest PDF from each guidebook into _guidebook-pdf-copies/
# Run from: guidebooks/ directory
# Usage: bash sync-pdfs.sh

DEST="$(dirname "$0")/_guidebook-pdf-copies"
mkdir -p "$DEST"

count=0
for dir in $(dirname "$0")/*/; do
    name=$(basename "$dir")
    # Skip the destination folder and archive
    [[ "$name" == "_guidebook-pdf-copies" || "$name" == "_archive" ]] && continue

    # Find PDFs in the guidebook root (not subdirectories like appendices/)
    pdf=$(find "$dir" -maxdepth 1 -name "*.pdf" -print -quit 2>/dev/null)
    if [ -n "$pdf" ]; then
        cp "$pdf" "$DEST/"
        echo "  Copied: $(basename "$pdf")"
        count=$((count + 1))
    fi
done

echo ""
echo "Done. $count PDFs copied to $DEST/"
ls -lh "$DEST/"*.pdf 2>/dev/null

# Also sync to iCloud
ICLOUD_DEST="$HOME/Library/Mobile Documents/com~apple~CloudDocs/_agentic-workflows/_guidebook-pdf-copies"
if [ -d "$ICLOUD_DEST" ]; then
    icount=0
    for pdf in "$DEST"/*.pdf; do
        cp "$pdf" "$ICLOUD_DEST/"
        icount=$((icount + 1))
    done
    echo "Also synced $icount PDFs to iCloud: $ICLOUD_DEST/"
fi
