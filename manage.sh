#!/bin/bash
# Management script for URL parser system (Kubernetes mode)
set -e

COMMAND="${1:-help}"

NAMESPACE="${NAMESPACE:-url-parser-fuzzing}"

# Function to get manager pod name
get_manager_pod() {
  kubectl get pods -n "$NAMESPACE" --selector=app=manager -o jsonpath='{.items[0].metadata.name}' 2>/dev/null
}

# Function to get postgres pod name
get_postgres_pod() {
  kubectl get pods -n "$NAMESPACE" --selector=app=postgres -o jsonpath='{.items[0].metadata.name}' 2>/dev/null
}

# Function to get redis pod name
get_redis_pod() {
  kubectl get pods -n "$NAMESPACE" --selector=app=redis -o jsonpath='{.items[0].metadata.name}' 2>/dev/null
}

# Function to get worker pod name (first one)
get_worker_pod() {
  kubectl get pods -n "$NAMESPACE" --selector=app=worker -o jsonpath='{.items[0].metadata.name}' 2>/dev/null
}

case "$COMMAND" in
    
  build-single)
    LANG="${2:-cpp}"
    SKIP_WORKER=false
    NO_CACHE=""
    shift 2 || true
    while [ "$#" -gt 0 ]; do
      case "$1" in
        --no-cache) NO_CACHE="--no-cache"; shift ;;
        -h|--help) echo "Usage: $0 build-single <language> [--no-cache]"; exit 0 ;;
        *) echo "Unknown argument: $1"; echo "Usage: $0 build-single <language> [--no-cache]"; exit 2 ;;
      esac
    done

    echo "Building single builder and unified worker for language: $LANG"
    ./dockerfiles/build-single.sh "$LANG" $NO_CACHE

    docker build -t localhost:6000/url-parser-manager:latest -f dockerfiles/Dockerfile.manager . || exit 1
    docker build -t localhost:6000/url-parser-unified-worker:latest -f dockerfiles/Dockerfile.unified-worker . || exit 1

    echo "✓ Build completed"
    echo ""
    ;;

  local-push)
    echo "Pushing images to local registry..."
    docker push localhost:6000/url-parser-manager:latest || exit 1
    docker push localhost:6000/url-parser-unified-worker:latest || exit 1
    docker push localhost:6000/url-parser-webui:latest || exit 1
    echo "✓ Images pushed"
    echo ""

    echo "To deploy with these images, ensure your Kubernetes manifests reference:"
    echo "  localhost:6000/url-parser-manager:latest"
    echo "  localhost:6000/url-parser-unified-worker:latest"
    echo "  localhost:6000/url-parser-webui:latest"
    echo ""
    ;;

  remote-push)
    echo "Pushing images to remote registry..."
    docker tag localhost:6000/url-parser-manager:latest localhost:5000/url-parser-manager:latest
    docker tag localhost:6000/url-parser-unified-worker:latest localhost:5000/url-parser-unified-worker:latest
    docker tag localhost:6000/url-parser-webui:latest localhost:5000/url-parser-webui:latest

    docker push localhost:5000/url-parser-manager:latest || exit 1
    docker push localhost:5000/url-parser-unified-worker:latest || exit 1
    docker push localhost:5000/url-parser-webui:latest || exit 1
    echo "✓ Images pushed to remote registry"
    echo ""
    ;;

  rebuild)
      # Build images (assuming Docker is available for building; push to registry if needed)
      echo "Building parser builder images..."
      ./dockerfiles/build-builders.sh || echo "⚠ Failed to build builder images"
      echo "✓ Builder images built"
      echo ""
      
      echo "Building images..."
      docker build -t localhost:6000/url-parser-manager:latest -f dockerfiles/Dockerfile.manager . || exit 1
      docker build -t localhost:6000/url-parser-unified-worker:latest -f dockerfiles/Dockerfile.unified-worker . || exit 1
      docker build -t localhost:6000/url-parser-webui:latest -f dockerfiles/Dockerfile.webui . || exit 1
      echo "✓ Images built"
      echo ""
      ;;

  build-webui)
    echo "Building web UI image..."
    docker build -t localhost:6000/url-parser-webui:latest -f dockerfiles/Dockerfile.webui . || exit 1
    echo "✓ Web UI image built"
    echo ""
    ;;

  start)
    shift
    ENABLED_WORKERS=("$@")   # e.g. (python java haskell) — empty means all

    echo "Starting Kubernetes services..."

    # Apply Kubernetes manifests
    echo "Applying Kubernetes manifests..."
    kubectl apply -f compose.yaml -n "$NAMESPACE"
    echo "✓ Manifests applied"
    echo ""

    # Scale workers based on supplied filter
    ALL_WORKERS=$(kubectl get statefulsets -n "$NAMESPACE" --no-headers \
      -o custom-columns=NAME:.metadata.name | grep -- '-worker$')

    if [ "${#ENABLED_WORKERS[@]}" -gt 0 ]; then
      echo "Enabling workers: ${ENABLED_WORKERS[*]}"
      echo "Disabling all others..."
      for sts in $ALL_WORKERS; do
        lang="${sts%-worker}"   # strip trailing -worker
        match=false
        for w in "${ENABLED_WORKERS[@]}"; do
          [ "$w" = "$lang" ] && match=true && break
        done
        if $match; then
          kubectl scale statefulset "$sts" --replicas=1 -n "$NAMESPACE" > /dev/null
          echo "  enabled:  $sts"
        else
          kubectl scale statefulset "$sts" --replicas=0 -n "$NAMESPACE" > /dev/null
          echo "  disabled: $sts"
        fi
      done
      echo ""
    fi

    # Wait for PostgreSQL
    echo "Waiting for PostgreSQL..."
    kubectl wait --for=condition=ready pod -l app=postgres -n "$NAMESPACE" --timeout=300s
    POSTGRES_POD=$(get_postgres_pod)
    until kubectl exec "$POSTGRES_POD" -n "$NAMESPACE" -- pg_isready -U parser -d url_parser > /dev/null 2>&1; do
      echo "  PostgreSQL not ready yet, waiting..."
      sleep 2
    done
    echo "✓ PostgreSQL ready"
    echo ""

    # Wait for Redis
    echo "Waiting for Redis..."
    kubectl wait --for=condition=ready pod -l app=redis -n "$NAMESPACE" --timeout=300s
    REDIS_POD=$(get_redis_pod)
    until kubectl exec "$REDIS_POD" -n "$NAMESPACE" -- redis-cli ping > /dev/null 2>&1; do
      echo "  Redis not ready yet, waiting..."
      sleep 2
    done
    echo "✓ Redis ready"
    echo ""

    # Wait for all enabled worker pods to be ready
    echo "Waiting for worker pods..."
    WORKER_STSS=$(kubectl get statefulsets -n "$NAMESPACE" --no-headers \
      -o custom-columns=NAME:.metadata.name,REPLICAS:.spec.replicas | awk '$2>0 {print $1}' | grep -- '-worker$')
    for sts in $WORKER_STSS; do
      echo "  waiting: $sts"
      kubectl rollout status statefulset/"$sts" -n "$NAMESPACE" --timeout=300s 2>/dev/null || true
    done
    echo "✓ Workers ready"
    echo ""

    echo "========================================"
    echo "✅ System Ready!"
    echo "========================================"
    echo ""
    echo "Pods running:"
    kubectl get pods -n "$NAMESPACE"
    echo ""
    echo "Management commands:"
    echo "  ./manage.sh list        # List parsers"
    echo "  ./manage.sh test URL    # Test a URL"
    echo "  ./manage.sh fuzz N      # Fuzz N URLs"
    echo "  ./manage.sh stats       # View stats"
    echo "  ./manage.sh monitor     # Monitor Celery events"
    echo "  ./manage.sh logs        # View logs"
    echo "  ./manage.sh stop        # Stop system"
    ;;
    
  start-registry)
    echo "Starting local Docker registry on port 6000..."
    if docker ps --filter name=registry | grep -q registry; then
      echo "Registry is already running"
    else
      docker run -d -p 6000:5000 --name registry registry:2
      echo "✓ Local registry started"
    fi
    echo "You can now run 'local-push' to build and push images"
    ;;

  sql-shell)
    POSTGRES_POD=$(get_postgres_pod)
    if [ -n "$POSTGRES_POD" ]; then
      echo "Opening psql shell in PostgreSQL pod..."
      kubectl exec -it "$POSTGRES_POD" -n "$NAMESPACE" -- psql -U parser -d url_parser
    else
      echo "Could not find PostgreSQL pod"
    fi
    ;;

  list)
    echo "Registered parsers:"
    MANAGER_POD=$(get_manager_pod)
    kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python manager.py list
    ;;
    
  test)
    URL="${2:-https://example.com/test}"
    MANAGER_POD=$(get_manager_pod)
    if [ -z "${3:-}" ]; then
      echo "Testing URL: $URL"
      kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python manager.py test "$URL"
    else
      COLUMN="$3"
      echo "Testing URL: $URL (column: $COLUMN)"
      kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python manager.py test "$URL" "$COLUMN"
    fi
    ;;

  fuzz)
    BATCH="${2:-100}"
    MAX_PENDING="${3:-1000}"
    MANAGER_POD=$(get_manager_pod)
    echo "Fuzzing (batch-size=$BATCH, max-pending=$MAX_PENDING, press Ctrl+C to stop)..."
    kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python manager.py fuzz --batch-size "$BATCH" --max-pending "$MAX_PENDING"
    ;;

  analyze)
    MAX_PENDING="${2:-50}"
    MANAGER_POD=$(get_manager_pod)
    echo "Running differential analysis (max-pending=$MAX_PENDING, press Ctrl+C to stop)..."
    kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python manager.py analyze --max-pending "$MAX_PENDING"
    ;;
    
  stats)
    echo "Showing fuzzing statistics (updates every 5s, press Ctrl+C to exit)"
    MANAGER_POD=$(get_manager_pod)
    while true; do
      kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python manager.py stats
      sleep 1
    done
    ;;
    
  db-init)
    echo "Reinitializing database schema..."
    MANAGER_POD=$(get_manager_pod)
    kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python -c "from core.database import init_db; init_db(); print('✓ Database schema created')"
    echo "Registering parsers..."
    kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python init_unified_parsers.py
    ;;
    
  db-reset)
    echo "⚠️  This will drop and recreate all database tables!"
    read -p "Are you sure? (yes/no): " -r
    if [ "$REPLY" = "yes" ]; then
      MANAGER_POD=$(get_manager_pod)
      kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python -c "from core.database import drop_db, init_db; drop_db(); init_db(); print('✓ Database reset')"
      kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- python init_unified_parsers.py
      echo "✓ Database reset and parsers registered"
    else
      echo "Cancelled"
    fi
    ;;
    
  shell)
    echo "Opening shell in manager pod..."
    MANAGER_POD=$(get_manager_pod)
    kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- /bin/bash
    ;;

  worker-shell)
    WORKER_POD=$(get_worker_pod)
    if [ -n "$WORKER_POD" ]; then
      echo "Opening shell in unified worker pod..."
      kubectl exec -it "$WORKER_POD" -n "$NAMESPACE" -- /bin/bash
    else
      echo "Could not find unified worker pod"
    fi
    ;;
    
  scale)
    # Usage: scale N [worker-name]  or  scale worker-name N
    if echo "${2:-}" | grep -qE '^[0-9]+$'; then
      NUM="$2"
      WORKER="${3:-}"
    else
      WORKER="${2:-}"
      NUM="${3:-2}"
    fi
    if [ -n "$WORKER" ]; then
      # Normalise: accept "r", "r-worker", etc.
      STS=$(echo "$WORKER" | grep -q '\-worker$' && echo "$WORKER" || echo "${WORKER}-worker")
      echo "Scaling $STS to $NUM replicas..."
      kubectl scale statefulset "$STS" --replicas="$NUM" -n "$NAMESPACE"
    else
      echo "Scaling all workers to $NUM replicas..."
      kubectl get statefulsets -n "$NAMESPACE" --no-headers -o custom-columns=NAME:.metadata.name \
        | grep '\-worker$' \
        | xargs -I{} kubectl scale statefulset {} --replicas="$NUM" -n "$NAMESPACE"
    fi
    kubectl get pods -n "$NAMESPACE"
    ;;
    
  logs)
    if [ -n "${2:-}" ]; then
      # If arg ends in a digit, treat it as a pod name (statefulset-N); otherwise use statefulset
      if [[ "${2}" =~ -[0-9]+$ ]]; then
        kubectl logs -f pod/"$2" -n "$NAMESPACE"
      else
        kubectl logs -f statefulset/"$2" -n "$NAMESPACE"
      fi
    else
      if command -v stern &>/dev/null; then
        stern --namespace "$NAMESPACE" --selector 'app in (ada-worker,analysis-worker)' \
          --selector '' -n "$NAMESPACE" '.*-worker' 2>/dev/null || \
        stern --namespace "$NAMESPACE" '.*-worker'
      else
        echo "Tailing all worker pods (Ctrl+C to stop)..."
        PODS=$(kubectl get pods -n "$NAMESPACE" --no-headers -o custom-columns=NAME:.metadata.name \
          | grep -E '\-worker\-')
        PIDS=()
        for POD in $PODS; do
          kubectl logs -f "$POD" -n "$NAMESPACE" --prefix 2>/dev/null &
          PIDS+=($!)
        done
        trap 'kill "${PIDS[@]}" 2>/dev/null' INT TERM
        wait
      fi
    fi
    ;;
    
  monitor)
    echo "Starting Celery events monitor..."
    echo "Press Ctrl+C to exit"
    echo ""
    MANAGER_POD=$(get_manager_pod)
    kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- celery --broker=redis://redis:6379/0 events
    ;;
    
  flower)
    PORT="${2:-5555}"
    echo "Starting Flower monitoring on http://localhost:$PORT"
    echo "Press Ctrl+C to stop"
    echo ""
    MANAGER_POD=$(get_manager_pod)
    kubectl exec -it "$MANAGER_POD" -n "$NAMESPACE" -- celery --broker=redis://redis:6379/0 flower --port="$PORT" --address=0.0.0.0
    ;;
    
  exec)
    POD_NAME="${2:-}"
    SHELL="${3:-/bin/bash}"
    if [ -z "$POD_NAME" ]; then
      echo "Usage: $0 exec <pod-name> [shell]"
      echo "Example: $0 exec rust-worker"
      kubectl get pods -n "$NAMESPACE" --no-headers -o custom-columns=NAME:.metadata.name
      exit 1
    fi
    FULL_POD=$(kubectl get pods -n "$NAMESPACE" --no-headers -o custom-columns=NAME:.metadata.name | grep "^${POD_NAME}" | head -1)
    if [ -z "$FULL_POD" ]; then
      echo "No pod found matching: $POD_NAME"
      kubectl get pods -n "$NAMESPACE" --no-headers -o custom-columns=NAME:.metadata.name
      exit 1
    fi
    echo "Exec into $FULL_POD..."
    kubectl exec -it "$FULL_POD" -n "$NAMESPACE" -- "$SHELL"
    ;;

  ps)
    kubectl get pods -n "$NAMESPACE"
    ;;
    
  stop)
    echo "Stopping system (scaling to 0, PVCs preserved)..."
    kubectl scale statefulset --all --replicas=0 -n "$NAMESPACE"
    echo "✓ All pods stopped (PVCs intact, use 'purge' to delete everything)"
    ;;
    
  update)
    TARGET="${2:-}"
    if [ -z "$TARGET" ]; then
      echo "Usage: $0 update <statefulset-name>"
      echo "Examples:"
      echo "  $0 update perl-worker"
      echo "  $0 update manager"
      echo ""
      echo "Available StatefulSets:"
      kubectl get statefulsets -n "$NAMESPACE" --no-headers -o custom-columns=NAME:.metadata.name
      exit 1
    fi
    # Verify the StatefulSet exists
    if ! kubectl get statefulset "$TARGET" -n "$NAMESPACE" &>/dev/null; then
      echo "StatefulSet '$TARGET' not found in namespace $NAMESPACE"
      echo ""
      echo "Available StatefulSets:"
      kubectl get statefulsets -n "$NAMESPACE" --no-headers -o custom-columns=NAME:.metadata.name
      exit 1
    fi
    echo "Rolling restart of StatefulSet '$TARGET'..."
    kubectl rollout restart statefulset/"$TARGET" -n "$NAMESPACE"
    kubectl rollout status statefulset/"$TARGET" -n "$NAMESPACE"
    ;;

  restart)
    echo "Restarting workers..."
    kubectl rollout restart statefulset worker -n "$NAMESPACE"
    ;;
    
  clean)
    echo "Cleaning up (keeps PVCs)..."
    kubectl scale statefulset --all --replicas=0 -n "$NAMESPACE"
    kubectl delete statefulset,deployment,service,configmap --all -n "$NAMESPACE" --ignore-not-found
    echo "Removing images..."
    docker rmi url-parser-manager:latest url-parser-unified-worker:latest 2>/dev/null || true
    echo "✓ Cleaned up (PVCs preserved)"
    ;;
        
  purge)
    echo "⚠️  Purging everything including PVCs..."
    read -p "Are you sure? (yes/no): " -r
    if [ "$REPLY" = "yes" ]; then
      kubectl delete -f . -n "$NAMESPACE" || true
      kubectl delete pvc -l app=postgres -n "$NAMESPACE" 2>/dev/null || true
      kubectl delete pvc -l app=redis -n "$NAMESPACE" 2>/dev/null || true
      docker rmi url-parser-manager:latest url-parser-unified-worker:latest 2>/dev/null || true
      echo "✓ Purged all data"
    else
      echo "Cancelled"
    fi
    ;;
  help|*)
    cat <<EOF
URL Parser System Management (Kubernetes)

Usage: ./manage.sh <command> [args]

Commands:
  start [lang ...]  Start all services; if languages given, only those workers run
  list              List all registered parsers
  local-push        Build and push images to local k3s registry
  test [URL]        Test a specific URL (default: https://example.com/test)
  fuzz [N] [M]      Fuzz URLs (batch-size=N default 100, max-pending=M default 1000)
  analyze [N]       Run differential analysis (max-pending=N default 50)
  stats             Show fuzzing statistics
  db-init           Initialize/update database schema
  db-reset          Drop and recreate database (destructive!)
  exec <pod>        Exec into a pod by name (prefix match, e.g. rust-worker)
  shell             Open bash shell in manager pod
  scale N [worker]  Scale all workers (or a specific one) to N replicas
  scale worker N    Scale a specific worker (e.g. r, r-worker, cpp-worker)
  monitor           Monitor Celery events in real-time
  flower [PORT]     Start Flower web UI (default port: 5555)
  logs [service]    View logs (default: worker)
  ps                Show running pods
  stop              Stop all services
  update <sts>      Rolling restart a specific StatefulSet (e.g. perl-worker, manager)
  restart           Restart workers
  clean             Remove pods and images (keep PVCs)
  purge             Remove everything including PVCs
  help              Show this help

Examples:
  ./manage.sh start
  ./manage.sh local-push
  ./manage.sh test "https://user:pass@example.com:8080/path?q=1"
  ./manage.sh fuzz 1000
  ./manage.sh scale 10
  ./manage.sh flower 5555
  ./manage.sh logs worker
  ./manage.sh exec rust-worker

Namespace: $NAMESPACE
EOF
    ;;
esac
