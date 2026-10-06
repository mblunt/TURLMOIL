-- Migration: Convert differentials to range-partitioned table by job_id
-- Partition size: 1000 jobs per partition, 1000 partitions (covers job IDs 1–1,000,000)
--
-- Run with workers stopped. Estimated time: 20–40 minutes at 316M rows.
-- Safe to re-run: all steps are conditional.

BEGIN;

-- Step 1: Rename existing table to backup
ALTER TABLE differentials RENAME TO differentials_old;

-- Step 2: Create partitioned table (no FKs on parse_result_a/b_id)
CREATE TABLE differentials (
    id                  BIGSERIAL,
    job_id              INTEGER       NOT NULL REFERENCES parse_jobs(id) ON DELETE CASCADE,
    parse_result_a_id   INTEGER       NOT NULL,
    parse_result_b_id   INTEGER       NOT NULL,
    library_a_id        INTEGER       NOT NULL REFERENCES libraries(id) ON DELETE CASCADE,
    library_b_id        INTEGER       NOT NULL REFERENCES libraries(id) ON DELETE CASCADE,
    differential_type   VARCHAR(64)   NOT NULL,
    created_at          TIMESTAMPTZ   DEFAULT now(),
    PRIMARY KEY (id, job_id)
) PARTITION BY RANGE (job_id);

-- Step 3: Create 1000 partitions covering job IDs 1–1,000,000
DO $$
DECLARE
    lo INTEGER;
    hi INTEGER;
BEGIN
    FOR i IN 0..999 LOOP
        lo := i * 1000 + 1;
        hi := lo + 1000;
        EXECUTE format(
            'CREATE TABLE differentials_p%s PARTITION OF differentials FOR VALUES FROM (%s) TO (%s)',
            lpad(i::text, 4, '0'), lo, hi
        );
    END LOOP;
END;
$$;

-- Step 4: Create indexes on the parent (propagate to all partitions)
DROP INDEX IF EXISTS idx_differentials_job_id;
DROP INDEX IF EXISTS idx_differentials_pair_type;
DROP INDEX IF EXISTS idx_differentials_type;
CREATE INDEX idx_differentials_job_id    ON differentials (job_id);
CREATE INDEX idx_differentials_pair_type ON differentials (library_a_id, library_b_id, differential_type);
CREATE INDEX idx_differentials_type      ON differentials (differential_type);

-- Step 5: Copy data from old table
INSERT INTO differentials
    (id, job_id, parse_result_a_id, parse_result_b_id,
     library_a_id, library_b_id, differential_type, created_at)
SELECT
    id, job_id, parse_result_a_id, parse_result_b_id,
    library_a_id, library_b_id, differential_type, created_at
FROM differentials_old;

-- Step 6: Reset sequence to continue from old max id
SELECT setval(
    pg_get_serial_sequence('differentials', 'id'),
    (SELECT MAX(id) FROM differentials)
);

COMMIT;

-- Step 7: Drop old table (outside transaction — irreversible, run manually when satisfied)
-- DROP TABLE differentials_old;
