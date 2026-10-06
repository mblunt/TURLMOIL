#!/usr/bin/env bash
set -euo pipefail

# Build a single parser builder image and the unified worker image.
# Usage: build-single-builder-worker.sh <language> [--rebuild-worker] [--no-cache]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
PROD_REGISTRY="${PROD_REGISTRY:-registry.example.com}"

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <language> [--rebuild-worker] [--no-cache] [--prod]"
  echo "Example: $0 cpp"
  exit 2
fi

LANG="$1"


NO_CACHE=""
REBUILD_WORKER=false
PROD=false
shift || true
while [ "$#" -gt 0 ]; do
  case "$1" in
    --no-cache) NO_CACHE="--no-cache"; shift ;;
    --rebuild-worker) REBUILD_WORKER=true; shift ;;
    --prod) PROD=true; shift ;;
    -h|--help) echo "Usage: $0 <language> [--rebuild-worker] [--no-cache]"; exit 0 ;;
    *) echo "Unknown argument: $1"; echo "Usage: $0 <language> [--rebuild-worker] [--no-cache]"; exit 2 ;;
  esac
done

if [ "$LANG" = "analysis" ]; then
  BUILDER_DOCKERFILE="$SCRIPT_DIR/Dockerfile.analysis"
else
  BUILDER_DOCKERFILE="$SCRIPT_DIR/builders/Dockerfile.$LANG"
fi

if [ ! -f "$BUILDER_DOCKERFILE" ]; then
  echo "Builder Dockerfile not found: $BUILDER_DOCKERFILE"
  echo "Available builder Dockerfiles in: $SCRIPT_DIR/builders"
  ls -1 "$SCRIPT_DIR/builders" || true
  exit 1
fi

WORKER_TAG="url-parser-$LANG:latest"

echo "Building worker image for language: $LANG"
echo "Dockerfile: $WORKER_TAG"

if [ "$PROD" = true ]; then
  if docker build $NO_CACHE --platform linux/amd64 -f "$BUILDER_DOCKERFILE" -t "$WORKER_TAG" "$PROJECT_ROOT"; then
    echo "✓ Built $PROD_REGISTRY/$WORKER_TAG"
  else
    echo "✗ Failed to build $PROD_REGISTRY/$WORKER_TAG" >&2
    exit 1
  fi
else
  if docker build $NO_CACHE -f "$BUILDER_DOCKERFILE" -t "$WORKER_TAG" "$PROJECT_ROOT"; then
    echo "✓ Built $WORKER_TAG"
  else
    echo "✗ Failed to build $WORKER_TAG" >&2
    exit 1
  fi
fi






if [ "$PROD" = true ]; then
  if docker tag "$WORKER_TAG" "$PROD_REGISTRY/$WORKER_TAG" && docker push "$PROD_REGISTRY/$WORKER_TAG"; then
    echo "✓ Pushed $PROD_REGISTRY/$WORKER_TAG"
  else
    echo "✗ Failed to push $PROD_REGISTRY/$WORKER_TAG" >&2
    exit 1
  fi
else
  echo "Pushing $WORKER_TAG to local registry..."
  if docker tag "$WORKER_TAG" "localhost:5000/$WORKER_TAG" && docker push "localhost:5000/$WORKER_TAG"; then
    echo "✓ Pushed localhost:5000/$WORKER_TAG"
  else
    echo "✗ Failed to push localhost:5000/$WORKER_TAG" >&2
    exit 1
  fi
fi


echo "Done."

echo "Summary:"
echo "  Worker image: $WORKER_TAG"