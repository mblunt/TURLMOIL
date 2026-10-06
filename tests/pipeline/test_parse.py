"""Integration tests for the parse_url / parse_all / parse_single task chain."""

import pytest


def _create_job(url="http://example.com"):
    from core.database import get_session
    from core.models import ParseJob, JobStatus
    with get_session() as session:
        job = ParseJob(url=url, status=JobStatus.PENDING)
        session.add(job)
        session.flush()
        return job.id


class TestParseAll:
    def test_creates_results_for_each_library(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseResult, Library
        from tasks.parse_url import parse_all

        job_id = _create_job()
        parse_all(job_id)

        with get_session() as session:
            n_libs = session.query(Library).filter_by(enabled=True).count()
            n_results = session.query(ParseResult).filter_by(job_id=job_id).count()

        assert n_results == n_libs

    def test_job_reaches_completed_status(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob, JobStatus
        from tasks.parse_url import parse_all

        job_id = _create_job("https://example.com/path?q=1")
        parse_all(job_id)

        with get_session() as session:
            job = session.get(ParseJob, job_id)
            assert job.status == JobStatus.COMPLETED

    def test_libraries_completed_equals_total(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob
        from tasks.parse_url import parse_all

        job_id = _create_job()
        parse_all(job_id)

        with get_session() as session:
            job = session.get(ParseJob, job_id)
            assert job.libraries_completed == job.libraries_total


class TestParseSingle:
    def test_result_row_created(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseResult, Library
        from tasks.parse_url import parse_single

        job_id = _create_job("http://test.example.org")

        with get_session() as session:
            lib_id = session.query(Library).filter_by(enabled=True).first().id

        parse_single(job_id, lib_id)

        with get_session() as session:
            result = session.query(ParseResult).filter_by(
                job_id=job_id, library_id=lib_id
            ).first()
        assert result is not None

    def test_result_is_idempotent(self, db, eager_celery):
        """Calling parse_single twice for the same job+library should not duplicate results."""
        from core.database import get_session
        from core.models import ParseResult, Library
        from tasks.parse_url import parse_single

        job_id = _create_job()

        with get_session() as session:
            lib_id = session.query(Library).filter_by(enabled=True).first().id

        parse_single(job_id, lib_id)
        parse_single(job_id, lib_id)  # second call should be a no-op

        with get_session() as session:
            count = session.query(ParseResult).filter_by(
                job_id=job_id, library_id=lib_id
            ).count()
        assert count == 1

    def test_result_has_parse_time(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseResult, Library
        from tasks.parse_url import parse_single

        job_id = _create_job("https://foo.bar/baz")

        with get_session() as session:
            lib_id = session.query(Library).filter_by(enabled=True).first().id

        parse_single(job_id, lib_id)

        with get_session() as session:
            result = session.query(ParseResult).filter_by(
                job_id=job_id, library_id=lib_id
            ).first()
        assert result.parse_time_ms is not None
        assert result.parse_time_ms >= 0
