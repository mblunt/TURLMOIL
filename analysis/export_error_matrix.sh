#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

kubectl port-forward -n url-parser-fuzzing svc/postgres 15432:5432 &
PF_PID=$!
trap 'kill $PF_PID 2>/dev/null' EXIT
sleep 2

PGPASSWORD=PLACEHOLDER_CHANGE_BEFORE_REPRO psql -h localhost -p 15432 -U parser -d url_parser --csv -c "
SELECT
    a.name                                          AS library_a,
    b.name                                          AS library_b,
    CASE WHEN EXISTS (
        SELECT 1
        FROM parse_results pr_a
        JOIN parse_results pr_b
            ON pr_b.job_id = pr_a.job_id
           AND pr_b.library_id = b.id
        WHERE pr_a.library_id = a.id
          AND pr_a.success <> pr_b.success
        LIMIT 1
    ) THEN 1 ELSE 0 END                             AS has_error_differential
FROM libraries a
CROSS JOIN libraries b
WHERE a.enabled = TRUE AND b.enabled = TRUE
  AND a.id <> b.id
ORDER BY a.name, b.name
" > "$SCRIPT_DIR/error_matrix.csv"

echo "Done: $SCRIPT_DIR/error_matrix.csv"
