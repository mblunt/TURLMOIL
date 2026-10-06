from core.models import Differential


def score(ctx: dict, diff: Differential) -> int:
    """
    Score (0-100) how rare this library pair's disagreement is on this component.

    100 = this pair has never disagreed on this component
      0 = this pair disagrees more than every other pair
    """
    component = diff.differential_type
    pair_count = ctx["pair_counts"].get((diff.library_a_id, diff.library_b_id, component), 0)

    if pair_count == 0:
        return 100

    all_counts = ctx["distributions"].get(component, [])
    if len(all_counts) < 2:
        return 100

    percentile = sum(1 for c in all_counts if c <= pair_count) / len(all_counts)
    return max(0, min(100, round(100 * (1.0 - percentile))))
