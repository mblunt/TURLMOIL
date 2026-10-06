"""REINFORCE policy gradient update for ParserWeights — per-component rewards.

Each URL component samples one categorical action (e.g. p_valid / p_invalid /
p_null) and receives the score for *that component's differential* as its
reward signal.  Generator components that map directly to a URL component field
(scheme, host, path, ...) use the per-component score.  Structural components
like delimiters and transformations, which have no direct output field to
compare, fall back to the overall job score.

Parameterisation
----------------
ParserWeights stores *logits* (unconstrained reals).  Probabilities are derived
via softmax at generation time.  The REINFORCE logit-space gradient is:

    ∂ log π(a) / ∂θ_i = 1[a == i] - π(i)

Update per logit:

    θ_chosen  += lr * advantage * (1 - π_chosen)
    θ_other   -= lr * advantage * π_other

where advantage = component_reward - baseline.

Stored weight format
--------------------
Each component column in ParserWeights is a JSON dict:

    {
        "p_valid":   {"logit": 0.0,  "group": "SCHEME"},
        "p_invalid": {"logit": 0.0,  "group": "SCHEME"},
        "p_null":    {"logit": -2.2, "group": "SCHEME"},
        ...
    }
"""

import math
import logging
from typing import Optional

from tasks.celery_app import app
from core.database import get_session
from core.models import ParserWeights, ParseJob
from sqlalchemy.orm.attributes import flag_modified

logger = logging.getLogger(__name__)

LEARNING_RATE = 0.05
BASELINE_WINDOW = 100  # recent scored jobs used to estimate the baseline

# Maps each generator component name to the COMPARISON_FIELDS value whose
# per-component score should drive its reward.  Delimiter components use the
# field they gate (e.g. pathquerydelim gates the query component).
# Components absent from this map fall back to job.score.
_GENERATOR_TO_FIELD: dict[str, str] = {
    "scheme":            "scheme",
    "username":          "username",
    "password":          "password",
    "host":              "host",
    "port":              "port",
    "path":              "path",
    "query":             "query",
    "fragment":          "fragment",
    "schemeauthdelim":   "authority",
    "userpassdelim":     "password",
    "userinfohostdelim": "userinfo",
    "hostportdelim":     "port",
    "authpathdelim":     "path",
    "pathquerydelim":    "query",
    "queryfragdelim":    "fragment",
}


def _softmax_probs(logits_dict: dict, group: str) -> dict[str, float]:
    """Return softmax probabilities for keys belonging to *group*."""
    keys = [k for k, v in logits_dict.items() if v.get("group") == group]
    logits = [logits_dict[k]["logit"] for k in keys]
    max_l = max(logits)
    exp_l = [math.exp(l - max_l) for l in logits]
    total = sum(exp_l)
    return {k: e / total for k, e in zip(keys, exp_l)}


@app.task(bind=True, name="tasks.feedback.reinforce.update_weights")
def update_weights(self, job_id: int) -> dict:
    """Apply a per-component REINFORCE update based on a scored job.

    For each generator component recorded in generation_choices, the reward is
    the score of the corresponding URL component differential (e.g. scheme
    generator uses the scheme differential score).  Components with no
    matching differential fall back to the overall job score.

    Args:
        job_id: ID of the scored ParseJob to learn from.
    """
    from tasks.scoring.score import component_scores

    with get_session() as session:
        job = session.get(ParseJob, job_id)
        if job is None:
            return {"error": f"Job {job_id} not found"}
        if job.score is None:
            return {"error": f"Job {job_id} has no score yet"}
        if not job.generation_choices:
            return {"skipped": "No generation choices recorded (pre-feedback URL)"}

        # Baseline: mean normalised score over the last BASELINE_WINDOW jobs.
        recent = (
            session.query(ParseJob.score)
            .filter(ParseJob.score.isnot(None), ParseJob.id != job_id)
            .order_by(ParseJob.id.desc())
            .limit(BASELINE_WINDOW)
            .all()
        )
        baseline = (
            sum(s for (s,) in recent) / len(recent) / 100.0
            if recent else 0.0
        )

        # Per-component scores keyed by COMPARISON_FIELDS value.
        comp_scores = component_scores(session, job_id)
        job_reward = job.score / 100.0  # fallback for unmapped components

        weights_row = ParserWeights.get(session)
        if weights_row is None:
            return {"error": "No ParserWeights singleton found"}

        updated = []
        component_advantages = {}

        for component, choice_info in job.generation_choices.items():
            chosen_key: str = choice_info["chosen"]
            group: str = choice_info["group"]

            logits_dict: Optional[dict] = getattr(weights_row, component, None)
            if not logits_dict:
                continue

            if chosen_key not in logits_dict:
                logger.warning(
                    "chosen key %r not found in %s logits — skipping",
                    chosen_key, component,
                )
                continue

            # Resolve the reward for this specific generator component.
            field = _GENERATOR_TO_FIELD.get(component)
            if field is not None and field in comp_scores:
                R = comp_scores[field] / 100.0
            else:
                R = job_reward

            advantage = R - baseline

            # REINFORCE logit update: θ_i += lr * A * (1[chosen] - π_i)
            probs = _softmax_probs(logits_dict, group)
            group_keys = list(probs.keys())

            new_logits = dict(logits_dict)
            for key in group_keys:
                indicator = 1.0 if key == chosen_key else 0.0
                new_logits[key] = {
                    **logits_dict[key],
                    "logit": logits_dict[key]["logit"]
                            + LEARNING_RATE * advantage * (indicator - probs[key]),
                }

            setattr(weights_row, component, new_logits)
            flag_modified(weights_row, component)
            updated.append(component)
            component_advantages[component] = round(advantage, 4)

        return {
            "job_id": job_id,
            "score": job.score,
            "component_advantages": component_advantages,
            "updated": updated,
        }
