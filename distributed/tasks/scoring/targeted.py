from collections import Counter

from core.models import Differential


def score(ctx: dict, diff: Differential) -> int:
    """
    Score (0-100) how narrowly this differential affects parsers on this component.

    Finds the majority consensus value across all libraries for this job and
    component, then counts how many libraries disagree (the "affected" count).

        100 = exactly one library differs from the rest
          0 = all libraries produce unique values (no consensus)
          0 = no differential (all agree — should not occur in practice)
    """
    component = diff.differential_type
    values = ctx["component_values"].get(component, [])
    n = len(values)
    if n < 2:
        return 0

    majority = Counter(values).most_common(1)[0][1]
    affected = n - majority

    if affected == 0:
        return 0

    # Complete disagreement — no two libraries share a value
    if majority == 1:
        return 0

    return max(0, min(100, round(100 * (1 - (affected - 1) / (n - 1)))))


if __name__ == "__main__":
    from unittest.mock import MagicMock
    from core.models.enums import COMPARISON_FIELDS

    def _make_session(values: list[str | None]) -> MagicMock:
        sess = MagicMock()
        sess.execute.return_value.all.return_value = [(v,) for v in values]
        return sess

    def _make_diff(job_id: int, component: COMPARISON_FIELDS) -> MagicMock:
        diff = MagicMock()
        diff.job_id = job_id
        diff.differential_type = component
        return diff

    def run_tests():
        component = COMPARISON_FIELDS.SCHEME

        # --- Test 1: one library differs → 100 ---
        sess = _make_session(["https", "https", "https", "https", "http"])
        assert score(sess, _make_diff(1, component)) == 100, "one outlier should score 100"

        # --- Test 2: all unique values → 0 ---
        sess = _make_session(["http", "https", "ftp", "ws", "wss"])
        assert score(sess, _make_diff(1, component)) == 0, "complete disagreement should score 0"

        # --- Test 3: all agree → 0 ---
        sess = _make_session(["https", "https", "https"])
        assert score(sess, _make_diff(1, component)) == 0, "no differential should score 0"

        # --- Test 4: half disagree → between 0 and 100 ---
        sess = _make_session(["https", "https", "http", "http"])
        s = score(sess, _make_diff(1, component))
        assert 0 < s < 100, f"half split should be between 0 and 100, got {s}"

        # --- Test 5: no results → 0 ---
        sess = _make_session([])
        assert score(sess, _make_diff(1, component)) == 0, "empty results should score 0"

        # --- Test 6: scores decrease as more libraries are affected ---
        # Only tested up to n//2: past that point the minority/majority roles flip
        # and the score mirrors back up (e.g. 6 "http" + 4 "https" → 4 are the outliers).
        n = 10
        scores = []
        for affected in range(1, n // 2 + 1):
            values = ["https"] * (n - affected) + ["http"] * affected
            sess = _make_session(values)
            scores.append(score(sess, _make_diff(1, component)))
        assert scores == sorted(scores, reverse=True), f"scores should decrease as affected grows: {scores}"

        print("All tests passed.")

    run_tests()
