#!/usr/bin/env bash
set -euo pipefail

# Build the manager image.
# Usage: build-manager.sh [--no-cache]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
PROD_REGISTRY="${PROD_REGISTRY:-registry.example.com}"

NO_CACHE=""
PROD=false
while [ "$#" -gt 0 ]; do
  case "$1" in
    --no-cache) NO_CACHE="--no-cache"; shift ;;
    --prod) PROD=true; shift ;;
    -h|--help) echo "Usage: $0 [--no-cache]"; exit 0 ;;
    *) echo "Unknown argument: $1"; echo "Usage: $0 [--no-cache]"; exit 2 ;;
  esac
done

MANAGER_TAG="url-parser-manager:latest"

echo "Building manager image..."
echo "Dockerfile: $SCRIPT_DIR/Dockerfile.manager"

if docker build $NO_CACHE -f "$SCRIPT_DIR/Dockerfile.manager" -t "$MANAGER_TAG" "$PROJECT_ROOT"; then
  echo "✓ Built $MANAGER_TAG"
else
  echo "✗ Failed to build $MANAGER_TAG" >&2
  exit 1
fi

if [ "$PROD" = true ]; then
  if docker tag "$MANAGER_TAG" "$PROD_REGISTRY/$MANAGER_TAG" && docker push "$PROD_REGISTRY/$MANAGER_TAG"; then
    echo "✓ Pushed $PROD_REGISTRY/$MANAGER_TAG"
  else
    echo "✗ Failed to push $PROD_REGISTRY/$MANAGER_TAG" >&2
    exit 1
  fi
else
  echo "Pushing $MANAGER_TAG to local registry..."
  if docker tag "$MANAGER_TAG" "localhost:5000/$MANAGER_TAG" && docker push "localhost:5000/$MANAGER_TAG"; then
    echo "✓ Pushed localhost:5000/$MANAGER_TAG"
  else
    echo "✗ Failed to push localhost:5000/$MANAGER_TAG" >&2
    exit 1
  fi
fi

echo ""
echo "Done."
echo ""
echo "Summary:"
echo "  Manager image: $MANAGER_TAG"
