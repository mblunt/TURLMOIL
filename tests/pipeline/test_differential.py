"""Integration tests for run_differential and the scoring chain."""

import pytest
from datetime import datetime, timezone


def _run_full_parse(url="http://example.com"):
    """Create a job, parse with all libraries, return job_id."""
    from core.database import get_session
    from core.models import ParseJob, JobStatus
    from tasks.parse_url import parse_all

    with get_session() as session:
        job = ParseJob(url=url, status=JobStatus.PENDING)
        session.add(job)
        session.flush()
        job_id = job.id

    parse_all(job_id)
    return job_id


class TestRunDifferential:
    def test_job_reaches_processed_status(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob, JobStatus
        from tasks.differentials import run_differential

        job_id = _run_full_parse()
        run_differential(job_id)

        with get_session() as session:
            job = session.get(ParseJob, job_id)
        assert job.status == JobStatus.PROCESSED

    def test_returns_success(self, db, eager_celery):
        from tasks.differentials import run_differential

        job_id = _run_full_parse()
        result = run_differential(job_id)
        assert result.get("status") == "success"

    def test_returns_count(self, db, eager_celery):
        from tasks.differentials import run_differential

        job_id = _run_full_parse()
        result = run_differential(job_id)
        assert "count" in result
        assert isinstance(result["count"], int)

    def test_idempotency_guard_on_rerun(self, db, eager_celery):
        """Calling run_differential twice on the same job should be rejected."""
        from tasks.differentials import run_differential

        job_id = _run_full_parse()
        run_differential(job_id)  # first run — succeeds
        result = run_differential(job_id)  # second run — should be rejected
        assert "error" in result

    def test_rejects_pending_job(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob, JobStatus
        from tasks.differentials import run_differential

        with get_session() as session:
            job = ParseJob(url="x", status=JobStatus.PENDING)
            session.add(job)
            session.flush()
            job_id = job.id

        result = run_differential(job_id)
        assert "error" in result


class TestScoring:
    def test_job_has_score_after_differential(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob
        from tasks.differentials import run_differential

        job_id = _run_full_parse()
        run_differential(job_id)

        with get_session() as session:
            job = session.get(ParseJob, job_id)
        assert job.score is not None

    def test_score_is_integer_in_range(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob
        from tasks.differentials import run_differential

        job_id = _run_full_parse()
        run_differential(job_id)

        with get_session() as session:
            job = session.get(ParseJob, job_id)
        assert isinstance(job.score, int)
        assert 0 <= job.score <= 100

    def test_score_is_zero_when_no_differentials(self, db, eager_celery):
        """Parsers agree on a simple valid URL — score should be 0."""
        from core.database import get_session
        from core.models import ParseJob
        from tasks.differentials import run_differential

        # Both stub parsers handle this canonical URL identically
        job_id = _run_full_parse("http://example.com/path")
        run_differential(job_id)

        with get_session() as session:
            job = session.get(ParseJob, job_id)
        assert job.score == 0

    def test_scored_at_is_set(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob
        from tasks.differentials import run_differential

        job_id = _run_full_parse()
        run_differential(job_id)

        with get_session() as session:
            job = session.get(ParseJob, job_id)
        assert job.scored_at is not None


class TestCountMatrix:
    def test_matrix_updated_when_differentials_exist(self, db, eager_celery):
        """If parsers disagree, DifferentialCountMatrix should have at least one row."""
        from core.database import get_session
        from core.models import Differential, DifferentialCountMatrix
        from tasks.differentials import run_differential

        # Generate many URLs to increase chance of disagreement
        results = []
        for i in range(10):
            job_id = _run_full_parse(f"ht tp://b ad url {i}")  # intentionally weird
            result = run_differential(job_id)
            results.append(result)

        with get_session() as session:
            n_diffs = session.query(Differential).count()
            n_matrix = session.query(DifferentialCountMatrix).count()

        if n_diffs > 0:
            assert n_matrix > 0, "Differentials exist but matrix was not updated"
