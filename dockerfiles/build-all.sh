#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

LANGUAGES=(
    ada
    analysis
    bin
    clojure
    cpp
    crystal
    csharp
    dart
    elixir
    erlang
    go
    haskell
    java
    javascript
    kotlin
    perl
    php
    python
    r
    ruby
    rust
    swift
    zig
)

DEPLOY=false
NAMESPACE="url-parser-fuzzing"
EXTRA_ARGS=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --no-cache|--rebuild-worker|--prod) EXTRA_ARGS+=("$1"); shift ;;
    --deploy) DEPLOY=true; shift ;;
    -h|--help)
      echo "Usage: $0 [--no-cache] [--rebuild-worker] [--prod] [--deploy]"
      echo "  --deploy   Rolling-restart each StatefulSet in k8s after its build succeeds"
      exit 0 ;;
    *) echo "Unknown argument: $1"; exit 2 ;;
  esac
done

SUCCEEDED=()
FAILED=()

for lang in "${LANGUAGES[@]}"; do
    echo ""
    echo "=== Building $lang ==="
    if "$SCRIPT_DIR/build-single.sh" "$lang" "${EXTRA_ARGS[@]}"; then
        SUCCEEDED+=("$lang")
        if [ "$DEPLOY" = true ]; then
            sts="${lang}-worker"
            if kubectl get statefulset "$sts" -n "$NAMESPACE" &>/dev/null; then
                echo "[$lang] rolling restart $sts..."
                kubectl rollout restart statefulset/"$sts" -n "$NAMESPACE"
            else
                echo "[$lang] no StatefulSet $sts, skipping deploy"
            fi
        fi
    else
        FAILED+=("$lang")
    fi
done

echo ""
echo "Succeeded (${#SUCCEEDED[@]}): ${SUCCEEDED[*]}"
[ ${#FAILED[@]} -gt 0 ] && echo "Failed (${#FAILED[@]}): ${FAILED[*]}"
echo "Total: ${#SUCCEEDED[@]}/${#LANGUAGES[@]}"
