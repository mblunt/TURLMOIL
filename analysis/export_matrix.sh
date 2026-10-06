#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

kubectl port-forward -n url-parser-fuzzing svc/postgres 15432:5432 &
PF_PID=$!
trap 'kill $PF_PID 2>/dev/null' EXIT
sleep 2

PGPASSWORD=PLACEHOLDER_CHANGE_BEFORE_REPRO psql -h localhost -p 15432 -U parser -d url_parser --csv -c "
WITH
all_fields(field) AS (
    VALUES ('scheme'),('authority'),('userinfo'),('username'),('password'),
           ('host'),('port'),('path'),('query'),('query_dict'),('fragment')
),
-- For each (library, field), whether that library ever returns EXCLUDE for that field
excludes AS (
    SELECT DISTINCT library_id, field FROM (
        SELECT library_id, 'scheme'     AS field FROM parse_results WHERE scheme      = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'authority'  AS field FROM parse_results WHERE authority   = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'userinfo'   AS field FROM parse_results WHERE userinfo    = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'username'   AS field FROM parse_results WHERE username    = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'password'   AS field FROM parse_results WHERE password    = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'host'       AS field FROM parse_results WHERE host        = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'port'       AS field FROM parse_results WHERE port        = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'path'       AS field FROM parse_results WHERE path        = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'query'      AS field FROM parse_results WHERE query       = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'query_dict' AS field FROM parse_results WHERE TRIM('\"' FROM COALESCE(query_dict::text, '')) = 'EXCLUDE'
        UNION ALL
        SELECT library_id, 'fragment'   AS field FROM parse_results WHERE fragment    = 'EXCLUDE'
    ) t
),
-- Enabled library pairs (lo < hi to avoid duplicates)
lib_pairs AS (
    SELECT a.id AS lib_lo, b.id AS lib_hi
    FROM libraries a
    JOIN libraries b ON b.id > a.id
    WHERE a.enabled = TRUE AND b.enabled = TRUE
),
-- For each pair, fields where either library has EXCLUDE
pair_excluded_fields AS (
    SELECT DISTINCT
        LEAST(e.library_id, l2.id)    AS lib_lo,
        GREATEST(e.library_id, l2.id) AS lib_hi,
        e.field
    FROM excludes e
    JOIN libraries l2 ON l2.enabled = TRUE AND l2.id <> e.library_id
),
-- Eligible fields per pair: neither library excludes it
pair_eligible_fields AS (
    SELECT lp.lib_lo, lp.lib_hi, f.field
    FROM lib_pairs lp
    CROSS JOIN all_fields f
    WHERE NOT EXISTS (
        SELECT 1 FROM pair_excluded_fields pef
        WHERE pef.lib_lo = lp.lib_lo AND pef.lib_hi = lp.lib_hi AND pef.field = f.field
    )
),
-- Actual differentials, only on eligible fields
diff_counts AS (
    SELECT
        LEAST(d.library_a_id, d.library_b_id)    AS lib_lo,
        GREATEST(d.library_a_id, d.library_b_id) AS lib_hi,
        COUNT(DISTINCT d.differential_type)       AS diff_count
    FROM differentials d
    JOIN pair_eligible_fields pef
        ON pef.lib_lo  = LEAST(d.library_a_id, d.library_b_id)
       AND pef.lib_hi  = GREATEST(d.library_a_id, d.library_b_id)
       AND pef.field   = d.differential_type
    GROUP BY LEAST(d.library_a_id, d.library_b_id), GREATEST(d.library_a_id, d.library_b_id)
),
-- Eligible field count per pair
eligible_counts AS (
    SELECT lib_lo, lib_hi, COUNT(*) AS eligible_fields
    FROM pair_eligible_fields
    GROUP BY lib_lo, lib_hi
),
-- Excluded field count per pair
excluded_counts AS (
    SELECT lib_lo, lib_hi, COUNT(DISTINCT field) AS excluded_fields
    FROM pair_excluded_fields
    GROUP BY lib_lo, lib_hi
)
SELECT
    a.name                                          AS library_a,
    b.name                                          AS library_b,
    CASE WHEN a.id = b.id THEN 0
         ELSE COALESCE(dc.diff_count,      0) END   AS differential_count,
    CASE WHEN a.id = b.id THEN 11
         ELSE COALESCE(ec.eligible_fields, 0) END   AS eligible_fields,
    CASE WHEN a.id = b.id THEN 0
         ELSE COALESCE(xc.excluded_fields, 0) END   AS excluded_fields
FROM libraries a
CROSS JOIN libraries b
LEFT JOIN diff_counts     dc ON dc.lib_lo = LEAST(a.id, b.id)    AND dc.lib_hi = GREATEST(a.id, b.id)
LEFT JOIN eligible_counts ec ON ec.lib_lo = LEAST(a.id, b.id)    AND ec.lib_hi = GREATEST(a.id, b.id)
LEFT JOIN excluded_counts xc ON xc.lib_lo = LEAST(a.id, b.id)    AND xc.lib_hi = GREATEST(a.id, b.id)
WHERE a.enabled = TRUE AND b.enabled = TRUE
ORDER BY a.name, b.name ASC
" | awk -F',' 'BEGIN {OFS=","} NR==1 {print $0, "ratio"; next} {
    ratio = ($3+0 > 0 && $4+0 > 0) ? ($3/$4)*100 : 0
    printf "%s,%.2f\n", $0, ratio
}' > "$SCRIPT_DIR/scheme_matrix.csv"

echo "Done: $SCRIPT_DIR/scheme_matrix.csv"