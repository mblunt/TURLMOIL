-- 96x96 library cross-matrix for the "scheme" component.
-- Cell = 1 if a scheme differential exists between the pair,
--        OR if either library ever returned EXCLUDE for scheme.
-- Cell = 0 otherwise.
-- Output: (library_a, library_b, has_differential)

WITH excludes AS (
    -- Libraries that returned EXCLUDE for scheme on at least one job
    SELECT DISTINCT pr.library_id
    FROM parse_results pr
    WHERE pr.scheme = 'EXCLUDE'
),
scheme_diffs AS (
    -- Distinct pairs that have at least one scheme differential
    -- (stored with library_a_id <= library_b_id)
    SELECT DISTINCT library_a_id, library_b_id
    FROM differentials
    WHERE differential_type = 'scheme'
)
SELECT
    a.name  AS library_a,
    b.name  AS library_b,
    CASE
        WHEN sd.library_a_id IS NOT NULL THEN 1
        WHEN ea.library_id   IS NOT NULL THEN 1
        WHEN eb.library_id   IS NOT NULL THEN 1
        ELSE 0
    END AS has_differential
FROM libraries a
CROSS JOIN libraries b
LEFT JOIN scheme_diffs sd
    ON sd.library_a_id = LEAST(a.id, b.id)
   AND sd.library_b_id = GREATEST(a.id, b.id)
LEFT JOIN excludes ea ON ea.library_id = a.id
LEFT JOIN excludes eb ON eb.library_id = b.id
WHERE a.enabled = TRUE AND b.enabled = TRUE
ORDER BY has_differential ASC
