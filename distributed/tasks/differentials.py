from typing import Dict, Any
from datetime import datetime, timezone
import io
import time
import logging

from sqlalchemy import update
from sqlalchemy.orm import Session

from tasks.celery_app import app
from core.database import get_session
from core.models import ParseJob, ParseResult, JobStatus, COMPARISON_FIELDS
from tasks.feedback.reinforce import update_weights

logger = logging.getLogger(__name__)

_DIFF_COLUMNS = ['job_id', 'parse_result_a_id', 'parse_result_b_id',
                 'library_a_id', 'library_b_id', 'differential_type']


def _copy_insert_differentials(session: Session, rows: list) -> None:
    """Insert differentials via COPY FROM STDIN — much faster than multi-row INSERT."""
    buf = io.StringIO()
    for row in rows:
        buf.write('\t'.join(str(row[c]) for c in _DIFF_COLUMNS) + '\n')
    buf.seek(0)
    raw_conn = session.connection().connection
    with raw_conn.cursor() as cur:
        cur.copy_from(buf, 'differentials', columns=_DIFF_COLUMNS)


@app.task(bind=True, name="tasks.differentials.run_differential")
def run_differential(self, parse_job_id: int) -> Dict[str, Any]:
    t0 = time.monotonic()

    with get_session() as session:
        t1 = time.monotonic()
        result = session.execute(
            update(ParseJob)
            .where(ParseJob.id == parse_job_id, ParseJob.status == JobStatus.COMPLETED.value)
            .values(status=JobStatus.PROCESSING.value)
        )
        if result.rowcount == 0:
            job = session.get(ParseJob, parse_job_id)
            if job is None:
                return {"error": f"Job {parse_job_id} not found"}
            return {"skipped": f"Job {parse_job_id} in state {job.status}"}
        session.commit()
        logger.info(f"[job {parse_job_id}] CAS+commit: {time.monotonic()-t1:.2f}s")

        job = session.get(ParseJob, parse_job_id)

        try:
            t2 = time.monotonic()
            _cols = [ParseResult.id, ParseResult.library_id] + [
                getattr(ParseResult, f.value) for f in COMPARISON_FIELDS
            ]
            rows = session.query(*_cols).filter(ParseResult.job_id == parse_job_id).all()
            logger.info(f"[job {parse_job_id}] fetch {len(rows)} results: {time.monotonic()-t2:.2f}s")

            field_names = [f.value for f in COMPARISON_FIELDS]
            results = [
                {"id": r[0], "library_id": r[1], **dict(zip(field_names, r[2:]))}
                for r in rows
            ]

            t3 = time.monotonic()
            new_differentials = []
            for i, a in enumerate(results):
                for b in results[i + 1:]:
                    for field in COMPARISON_FIELDS:
                        val_a = a[field.value]
                        val_b = b[field.value]
                        if val_a == "EXCLUDE" or val_b == "EXCLUDE":
                            continue
                        if val_a != val_b:
                            new_differentials.append({
                                "job_id": parse_job_id,
                                "parse_result_a_id": a["id"],
                                "parse_result_b_id": b["id"],
                                "library_a_id": min(a["library_id"], b["library_id"]),
                                "library_b_id": max(a["library_id"], b["library_id"]),
                                "differential_type": field.value,
                            })
            logger.info(f"[job {parse_job_id}] comparison loop ({len(new_differentials)} diffs): {time.monotonic()-t3:.2f}s")

            t4 = time.monotonic()
            if new_differentials:
                _copy_insert_differentials(session, new_differentials)
            logger.info(f"[job {parse_job_id}] bulk_insert ({len(new_differentials)} rows): {time.monotonic()-t4:.2f}s")

            t5 = time.monotonic()
            job.status = JobStatus.PROCESSED.value
            session.commit()
            logger.info(f"[job {parse_job_id}] final commit: {time.monotonic()-t5:.2f}s")

        except Exception as e:
            session.rollback()
            job.status = JobStatus.FAILED.value
            session.commit()
            return {"error": str(e)}

    logger.info(f"[job {parse_job_id}] TOTAL: {time.monotonic()-t0:.2f}s | diffs={len(new_differentials)}")
    score_and_update.delay(parse_job_id)
    return {"status": "success", "count": len(new_differentials)}


@app.task(bind=True, name="tasks.differentials.score_and_update")
def score_and_update(self, parse_job_id: int) -> Dict[str, Any]:
    """Compute job score and dispatch the REINFORCE weight update."""
    from tasks.scoring.score import _build_context, _MODULES
    from core.models import Differential

    t0 = time.monotonic()
    with get_session() as session:
        t1 = time.monotonic()
        job = session.get(ParseJob, parse_job_id)
        if job is None:
            return {"error": f"Job {parse_job_id} not found"}
        if job.status != JobStatus.PROCESSED.value:
            return {"skipped": f"Job {parse_job_id} not in PROCESSED state"}
        logger.info(f"[score {parse_job_id}] job fetch: {time.monotonic()-t1:.2f}s")

        t2 = time.monotonic()
        diffs = session.query(Differential).filter_by(job_id=parse_job_id).all()
        logger.info(f"[score {parse_job_id}] load {len(diffs)} diffs: {time.monotonic()-t2:.2f}s")

        if not diffs:
            score = 0
        else:
            t3 = time.monotonic()
            ctx = _build_context(session, parse_job_id, diffs)
            logger.info(f"[score {parse_job_id}] build_context pr={len(ctx['parse_results'])} pairs={len(ctx['pair_counts'])} components={len(ctx['distributions'])}: {time.monotonic()-t3:.2f}s")

            t4 = time.monotonic()
            score = max(
                round(sum(mod.score(ctx, d) * w for mod, w in _MODULES))
                for d in diffs
            )
            logger.info(f"[score {parse_job_id}] scoring loop: {time.monotonic()-t4:.2f}s")

        t5 = time.monotonic()
        job.score = score
        job.scored_at = datetime.now(timezone.utc)
        session.commit()
        logger.info(f"[score {parse_job_id}] commit: {time.monotonic()-t5:.2f}s")

    logger.info(f"[score {parse_job_id}] TOTAL: {time.monotonic()-t0:.2f}s | score={score}")
    update_weights.delay(parse_job_id)
    return {"score": score}
