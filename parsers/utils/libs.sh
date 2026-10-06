#!/bin/sh

# Outputs a worker_parsers.json for the given language, filtered from parsers.json.
# Usage: ./libs.sh <language>
# Example: ./libs.sh python > /parsers/worker_parsers.json

LANG="$1"

if [ -z "$LANG" ]; then
    echo "Usage: $0 <language>" >&2
    exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
    echo "Error: jq is required but not installed." >&2
    exit 1
fi

PARSERS_JSON="/parsers/parsers.json"

if [ ! -f "$PARSERS_JSON" ]; then
    echo "Error: $PARSERS_JSON not found." >&2
    exit 1
fi

jq --arg lang "$LANG" '{"parsers": [.parsers[] | select(.language == $lang)]}' "$PARSERS_JSON"
