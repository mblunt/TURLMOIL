from Levenshtein import distance as ldistance

from core.models import Differential


def score(ctx: dict, diff: Differential) -> int:
    """
    Score (0-100) how different the two parsed values are for this component,
    using normalized Levenshtein distance.

        100 = strings share nothing (maximum edit distance relative to length)
          0 = strings are identical
    """
    component = diff.differential_type
    pr = ctx["parse_results"]
    val_a = str(getattr(pr.get(diff.parse_result_a_id), component, None) or "")
    val_b = str(getattr(pr.get(diff.parse_result_b_id), component, None) or "")

    if val_a == "EXCLUDE" or val_b == "EXCLUDE":
        return 0

    max_len = max(len(val_a), len(val_b))
    if max_len == 0:
        return 0

    return min(100, round(100 * ldistance(val_a, val_b) / max_len))


if __name__ == "__main__":
    from unittest.mock import MagicMock
    from core.models.enums import COMPARISON_FIELDS

    def _make_diff(val_a: str, val_b: str, component: COMPARISON_FIELDS) -> MagicMock:
        diff = MagicMock()
        diff.differential_type = component
        diff.differential_type.value = component.value
        setattr(diff.parse_result_a, component.value, val_a)
        setattr(diff.parse_result_b, component.value, val_b)
        return diff

    def run_tests():
        component = COMPARISON_FIELDS.SCHEME

        # --- Test 1: identical strings → 0 ---
        diff = _make_diff("https", "https", component)
        assert score(None, diff) == 0, "identical strings should score 0"

        # --- Test 2: completely different → 100 ---
        diff = _make_diff("http", "ftp", component)
        s = score(None, diff)
        assert s > 0, f"different strings should score > 0, got {s}"

        # --- Test 3: EXCLUDE → 0 ---
        diff = _make_diff("https", "EXCLUDE", component)
        assert score(None, diff) == 0, "EXCLUDE should score 0"

        # --- Test 4: empty both → 0 ---
        diff = _make_diff("", "", component)
        assert score(None, diff) == 0, "empty strings should score 0"

        # --- Test 5: score increases with edit distance ---
        diffs = [
            _make_diff("https", "https"[:-i], component) for i in range(1, 5)
        ]
        scores = [score(None, d) for d in diffs]
        assert scores == sorted(scores), f"scores should increase with edit distance: {scores}"

        print("All tests passed.")

    run_tests()
