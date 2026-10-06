"""Tests for update_weights Celery task in reinforce.py.

Each test gets an isolated file-based SQLite DB via the `db` fixture
in conftest.py, so there is no cross-test state leakage.
"""

import pytest
from datetime import datetime, timezone


# ── helpers ───────────────────────────────────────────────────────────────────

def _make_scored_job(session, score, choices=None):
    from core.models import ParseJob, JobStatus
    job = ParseJob(
        url="http://example.com",
        status=JobStatus.PROCESSED,
        score=score,
        scored_at=datetime.now(timezone.utc),
        generation_choices=choices,
    )
    session.add(job)
    session.flush()
    return job.id


def _get_logit(session, component: str, key: str) -> float:
    from core.models import ParserWeights
    row = ParserWeights.get(session)
    return row.__dict__[component][key]["logit"]


# ── error / skip paths ────────────────────────────────────────────────────────

class TestUpdateWeightsGuards:
    def test_missing_job_returns_error(self, db):
        from tasks.feedback.reinforce import update_weights
        result = update_weights(99999)
        assert "error" in result

    def test_unscored_job_returns_error(self, db):
        from core.database import get_session
        from core.models import ParseJob, JobStatus
        from tasks.feedback.reinforce import update_weights
        with get_session() as session:
            job = ParseJob(url="x", status=JobStatus.PROCESSED, score=None)
            session.add(job)
            session.flush()
            job_id = job.id
        result = update_weights(job_id)
        assert "error" in result

    def test_job_with_no_choices_is_skipped(self, db):
        from core.database import get_session
        from tasks.feedback.reinforce import update_weights
        with get_session() as session:
            job_id = _make_scored_job(session, score=80, choices=None)
        result = update_weights(job_id)
        assert "skipped" in result

    def test_missing_parser_weights_returns_error(self, db):
        """If ParserWeights row is absent, update_weights should error gracefully."""
        from core.database import get_session
        from core.models import ParserWeights
        from tasks.feedback.reinforce import update_weights
        # Delete the singleton
        with get_session() as session:
            row = ParserWeights.get(session)
            if row:
                session.delete(row)
        with get_session() as session:
            job_id = _make_scored_job(
                session, score=50,
                choices={"scheme": {"chosen": "p_invalid", "group": "SCHEME"}},
            )
        result = update_weights(job_id)
        assert "error" in result


# ── gradient direction ────────────────────────────────────────────────────────

class TestUpdateWeightsGradient:
    def test_high_score_increases_chosen_logit(self, db):
        """Score=100 with baseline≈0 → advantage>0 → chosen logit increases."""
        from core.database import get_session
        from tasks.feedback.reinforce import update_weights

        choices = {"scheme": {"chosen": "p_invalid", "group": "SCHEME"}}
        with get_session() as session:
            job_id = _make_scored_job(session, score=100, choices=choices)
            before = _get_logit(session, "scheme", "p_invalid")

        update_weights(job_id)

        with get_session() as session:
            after = _get_logit(session, "scheme", "p_invalid")

        assert after > before

    def test_zero_score_with_positive_baseline_decreases_chosen_logit(self, db):
        """Score=0 with positive baseline → advantage<0 → chosen logit decreases."""
        from core.database import get_session
        from core.models import ParseJob, JobStatus
        from tasks.feedback.reinforce import update_weights

        choices = {"scheme": {"chosen": "p_valid", "group": "SCHEME"}}

        with get_session() as session:
            # Seed high-scoring jobs so baseline is positive
            for _ in range(5):
                session.add(ParseJob(
                    url="x", status=JobStatus.PROCESSED,
                    score=90, scored_at=datetime.now(timezone.utc),
                ))
            job_id = _make_scored_job(session, score=0, choices=choices)
            before = _get_logit(session, "scheme", "p_valid")

        update_weights(job_id)

        with get_session() as session:
            after = _get_logit(session, "scheme", "p_valid")

        assert after < before

    def test_unchosen_logits_move_opposite_to_chosen(self, db):
        """When chosen logit goes up, the other top-level logits go down."""
        from core.database import get_session
        from tasks.feedback.reinforce import update_weights

        choices = {"scheme": {"chosen": "p_invalid", "group": "SCHEME"}}
        with get_session() as session:
            job_id = _make_scored_job(session, score=100, choices=choices)
            before_valid = _get_logit(session, "scheme", "p_valid")
            before_null  = _get_logit(session, "scheme", "p_null")

        update_weights(job_id)

        with get_session() as session:
            after_valid = _get_logit(session, "scheme", "p_valid")
            after_null  = _get_logit(session, "scheme", "p_null")

        assert after_valid < before_valid
        assert after_null  < before_null

    def test_score_at_baseline_produces_no_update(self, db):
        """When score == baseline, advantage≈0 and logits should not change materially."""
        from core.database import get_session
        from core.models import ParseJob, JobStatus
        from tasks.feedback.reinforce import update_weights

        target_score = 50

        choices = {"scheme": {"chosen": "p_invalid", "group": "SCHEME"}}
        with get_session() as session:
            # Fill the baseline window with the same score
            for _ in range(10):
                session.add(ParseJob(
                    url="x", status=JobStatus.PROCESSED,
                    score=target_score, scored_at=datetime.now(timezone.utc),
                ))
            job_id = _make_scored_job(session, score=target_score, choices=choices)
            before = _get_logit(session, "scheme", "p_invalid")

        update_weights(job_id)

        with get_session() as session:
            after = _get_logit(session, "scheme", "p_invalid")

        assert abs(after - before) < 1e-6


# ── return value ──────────────────────────────────────────────────────────────

class TestUpdateWeightsReturnValue:
    def test_returns_dict(self, db):
        from core.database import get_session
        from tasks.feedback.reinforce import update_weights
        with get_session() as session:
            job_id = _make_scored_job(
                session, score=75,
                choices={"scheme": {"chosen": "p_invalid", "group": "SCHEME"}},
            )
        result = update_weights(job_id)
        assert isinstance(result, dict)

    def test_result_contains_job_id(self, db):
        from core.database import get_session
        from tasks.feedback.reinforce import update_weights
        with get_session() as session:
            job_id = _make_scored_job(
                session, score=75,
                choices={"scheme": {"chosen": "p_invalid", "group": "SCHEME"}},
            )
        result = update_weights(job_id)
        assert result.get("job_id") == job_id

    def test_result_contains_component_advantages(self, db):
        from core.database import get_session
        from tasks.feedback.reinforce import update_weights
        with get_session() as session:
            job_id = _make_scored_job(
                session, score=60,
                choices={"host": {"chosen": "p_valid", "group": "HOST"}},
            )
        result = update_weights(job_id)
        assert "component_advantages" in result
        assert "host" in result["component_advantages"]

    def test_updated_list_contains_components_with_choices(self, db):
        from core.database import get_session
        from tasks.feedback.reinforce import update_weights
        choices = {
            "scheme": {"chosen": "p_invalid", "group": "SCHEME"},
            "host":   {"chosen": "p_valid",   "group": "HOST"},
            "path":   {"chosen": "p_null",    "group": "PATH"},
        }
        with get_session() as session:
            job_id = _make_scored_job(session, score=80, choices=choices)
        result = update_weights(job_id)
        for component in choices:
            assert component in result.get("updated", [])

    def test_components_not_in_choices_not_in_updated(self, db):
        from core.database import get_session
        from tasks.feedback.reinforce import update_weights
        choices = {"scheme": {"chosen": "p_invalid", "group": "SCHEME"}}
        with get_session() as session:
            job_id = _make_scored_job(session, score=80, choices=choices)
        result = update_weights(job_id)
        updated = result.get("updated", [])
        assert "host" not in updated
        assert "path" not in updated
