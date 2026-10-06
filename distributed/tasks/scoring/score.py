import json
import time
import logging
from collections import defaultdict

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from core.models import Differential, ParseResult
from core.models.enums import COMPARISON_FIELDS
from tasks.scoring import delta, uncommon, targeted

logger = logging.getLogger(__name__)

_MODULES = [(delta, 0.33), (uncommon, 0.33), (targeted, 0.34)]

# Worker-process-level global pair-count cache.
# Stores the full (lib_a_id, lib_b_id, component) → count map for ALL pairs.
# From this we derive both per-pair counts and per-component distributions with zero extra queries.
_PAIR_CACHE_TTL = 300.0  # 5 minutes — large table, data changes slowly
_PAIR_CACHE_RECENT_JOBS = 500  # only count pairs seen in the most recent N jobs
_pair_cache_fetched_at: float = 0.0
_pair_cache: dict[tuple, int] = {}  # (lib_a_id, lib_b_id, component) → count
_pair_cache_loading: bool = False  # prevent concurrent refreshes within a process

import random as _random
# Spread initial cold-start load across workers by deferring first refresh randomly
_pair_cache_fetched_at = -_random.uniform(0, 60)  # jitter: 0–60s before first refresh


def _ensure_pair_cache(session: Session) -> None:
    global _pair_cache_fetched_at, _pair_cache, _pair_cache_loading
    now = time.monotonic()
    if now - _pair_cache_fetched_at < _PAIR_CACHE_TTL:
        return
    if _pair_cache_loading:
        return  # another task in this process is already refreshing — use stale data
    _pair_cache_loading = True
    try:
        t = time.monotonic()
        from core.models import ParseJob
        max_job_id = session.execute(select(func.max(ParseJob.id))).scalar() or 0
        rows = session.execute(
            select(
                Differential.library_a_id,
                Differential.library_b_id,
                Differential.differential_type,
                func.count().label("cnt"),
            ).where(
                Differential.job_id > max_job_id - _PAIR_CACHE_RECENT_JOBS
            ).group_by(
                Differential.library_a_id,
                Differential.library_b_id,
                Differential.differential_type,
            )
        ).all()
        _pair_cache = {(a, b, c): cnt for a, b, c, cnt in rows}
        _pair_cache_fetched_at = now
        logger.info(f"pair cache refreshed: {len(_pair_cache)} entries ({_PAIR_CACHE_RECENT_JOBS} recent jobs) in {time.monotonic()-t:.2f}s")
    finally:
        _pair_cache_loading = False


def _build_context(session: Session, job_id: int, diffs: list) -> dict:
    """Preload all data needed by scoring modules in bulk."""
    # Load all parse results for this job
    pr_rows = session.query(ParseResult).filter_by(job_id=job_id).all()
    parse_results = {pr.id: pr for pr in pr_rows}

    # Build component → list of (hashable) values for targeted scoring
    component_values: dict[str, list] = defaultdict(list)
    for pr in pr_rows:
        for f in COMPARISON_FIELDS:
            v = getattr(pr, f.value, None)
            if isinstance(v, (dict, list)):
                v = json.dumps(v, sort_keys=True)
            component_values[f.value].append(v)

    # Refresh global pair cache if stale (at most one DB hit per TTL per worker process)
    _ensure_pair_cache(session)

    # Derive pair_counts and distributions from cache — no additional DB queries
    components = {d.differential_type for d in diffs}
    pair_counts = {
        key: cnt for key, cnt in _pair_cache.items()
        if key[2] in components
    }
    distributions: dict[str, list[int]] = {comp: [] for comp in components}
    for (_, _, comp), cnt in _pair_cache.items():
        if comp in distributions:
            distributions[comp].append(cnt)

    return {
        "parse_results": parse_results,
        "pair_counts": pair_counts,
        "distributions": distributions,
        "component_values": dict(component_values),
    }


def _score_diff(ctx: dict, diff: Differential) -> float:
    return sum(module.score(ctx, diff) * weight for module, weight in _MODULES)


def job_score(session: Session, job_id: int) -> int:
    """Return a rarity score (0-100) for a parsed URL. Takes the max across all differentials."""
    diffs = session.query(Differential).filter_by(job_id=job_id).all()
    if not diffs:
        return 0
    ctx = _build_context(session, job_id, diffs)
    return max(round(_score_diff(ctx, d)) for d in diffs)


def component_scores(session: Session, job_id: int) -> dict[str, int]:
    """Return best score (0-100) per URL component that produced a differential."""
    diffs = session.query(Differential).filter_by(job_id=job_id).all()
    ctx = _build_context(session, job_id, diffs)
    scores: dict[str, int] = {}
    for diff in diffs:
        comp = diff.differential_type
        scores[comp] = max(scores.get(comp, 0), round(_score_diff(ctx, diff)))
    return scores
