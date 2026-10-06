"""URL generation Celery task."""

import sys
import os

from tasks.celery_app import app

# Path to the generator package (has local component imports)
_GEN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generator")


@app.task(bind=True, name="tasks.generate.generate_batch")
def generate_batch(self, n: int) -> dict:
    """Generate n URLs and dispatch a parse_url job for each.

    Args:
        n: Number of URLs to generate

    Returns:
        Dict with count of URLs generated
    """
    if _GEN_DIR not in sys.path:
        sys.path.insert(0, _GEN_DIR)

    from generator import generate_n

    job_ids = generate_n(n)
    return {"count": len(job_ids), "job_ids": job_ids}