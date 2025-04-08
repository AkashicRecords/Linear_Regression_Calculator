#!/bin/bash
# Script to archive handoff documents and set them to read-only

# Get current date in YYYY-MM-DD format
CURRENT_DATE=$(date +%Y-%m-%d)
ARCHIVE_DIR="HandOff-History/${CURRENT_DATE}_HandOff"

echo "Linear Regression Calculator - Handoff Archiving Script"
echo "======================================================="
echo "Archiving current handoff documents to: $ARCHIVE_DIR"

# Create archive directory
mkdir -p "$ARCHIVE_DIR"

# Copy all handoff documents to archive
cp -r HandOff/* "$ARCHIVE_DIR/"

# Set archive to read-only
chmod -R 444 "$ARCHIVE_DIR"

echo "Archive completed successfully."
echo "Files are now set to read-only to preserve integrity."
echo ""
echo "To make these files writable again (if needed), use:"
echo "  chmod -R 644 $ARCHIVE_DIR"
echo ""
echo "Don't forget to update the version numbers for the next development cycle!" 