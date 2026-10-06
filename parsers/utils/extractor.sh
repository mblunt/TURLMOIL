#!/bin/sh

# Usage: ./version-extractor.sh <language> <key>
# Example: ./version-extractor.sh python version

ID="$1"
KEY="$2"

if [ -z "$ID" ] || [ -z "$KEY" ]; then
    echo "Usage: $0 <id> <key>"
    exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
    echo "Error: jq is required but not installed."
    exit 1
fi

PARSERS_JSON="/parsers/parsers.json"

if [ ! -f "$PARSERS_JSON" ]; then
    echo "Error: $PARSERS_JSON not found."
    exit 1
fi

jq -r --arg id "$ID" --arg key "$KEY" \
    '.parsers[] | select(.id == $id) | .[$key]' "$PARSERS_JSON"