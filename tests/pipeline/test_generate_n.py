"""Integration tests for generate_n — the top-level URL generation entry point."""

import pytest


class TestGenerateNOutput:
    def test_returns_list(self, db, eager_celery):
        from generator import generate_n
        result = generate_n(3)
        assert isinstance(result, list)

    def test_returns_correct_count(self, db, eager_celery):
        from generator import generate_n
        result = generate_n(5)
        assert len(result) == 5

    def test_all_elements_are_strings(self, db, eager_celery):
        from generator import generate_n
        result = generate_n(4)
        for url in result:
            assert isinstance(url, str)


class TestGenerateNDatabaseEffect:
    def test_creates_parse_jobs(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob
        from generator import generate_n

        generate_n(3)

        with get_session() as session:
            count = session.query(ParseJob).count()
        assert count == 3

    def test_jobs_have_correct_urls(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob
        from generator import generate_n

        urls = generate_n(3)

        with get_session() as session:
            stored = {j.url for j in session.query(ParseJob).all()}

        for url in urls:
            assert url in stored

    def test_generation_choices_stored_on_each_job(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob
        from generator import generate_n

        generate_n(3)

        with get_session() as session:
            jobs = session.query(ParseJob).all()
            for job in jobs:
                assert job.generation_choices is not None, \
                    f"Job {job.id} missing generation_choices"

    def test_choices_cover_all_components(self, db, eager_celery):
        from core.database import get_session
        from core.models import ParseJob
        from generator import generate_n, _COMPONENTS_WITH_CHOICE

        generate_n(2)

        expected = {name for name, _ in _COMPONENTS_WITH_CHOICE}
        with get_session() as session:
            jobs = session.query(ParseJob).all()
            for job in jobs:
                assert set(job.generation_choices.keys()) == expected
