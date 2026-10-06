"""Tests for _logits_to_probs — the logit→probability conversion in generator.py."""

import math
import pytest


@pytest.fixture(scope="module")
def logits_to_probs():
    from generator import _logits_to_probs
    return _logits_to_probs


class TestLogitsToProbs:
    def test_uniform_logits_give_equal_probs(self, logits_to_probs):
        logits = {
            "p_valid":   {"logit": 0.0, "group": "SCHEME"},
            "p_invalid": {"logit": 0.0, "group": "SCHEME"},
            "p_null":    {"logit": 0.0, "group": "SCHEME"},
        }
        probs = logits_to_probs(logits)
        for key in logits:
            assert abs(probs[key]["weight"] - 1/3) < 1e-9

    def test_probs_sum_to_one(self, logits_to_probs):
        logits = {
            "p_valid":   {"logit": 1.2,  "group": "SCHEME"},
            "p_invalid": {"logit": -0.5, "group": "SCHEME"},
            "p_null":    {"logit": 0.3,  "group": "SCHEME"},
        }
        probs = logits_to_probs(logits)
        total = sum(v["weight"] for v in probs.values())
        assert abs(total - 1.0) < 1e-9

    def test_high_logit_dominates(self, logits_to_probs):
        logits = {
            "p_valid":   {"logit": 100.0, "group": "SCHEME"},
            "p_invalid": {"logit": 0.0,   "group": "SCHEME"},
            "p_null":    {"logit": 0.0,   "group": "SCHEME"},
        }
        probs = logits_to_probs(logits)
        assert probs["p_valid"]["weight"] > 0.999

    def test_negative_logit_suppresses(self, logits_to_probs):
        logits = {
            "p_valid":   {"logit": 0.0,    "group": "SCHEME"},
            "p_invalid": {"logit": 0.0,    "group": "SCHEME"},
            "p_null":    {"logit": -100.0, "group": "SCHEME"},
        }
        probs = logits_to_probs(logits)
        assert probs["p_null"]["weight"] < 1e-6

    def test_group_field_preserved(self, logits_to_probs):
        logits = {
            "p_valid":   {"logit": 0.0, "group": "SCHEME"},
            "p_invalid": {"logit": 0.0, "group": "SCHEME"},
            "p_null":    {"logit": 0.0, "group": "SCHEME"},
        }
        probs = logits_to_probs(logits)
        for v in probs.values():
            assert v["group"] == "SCHEME"

    def test_two_groups_normalised_independently(self, logits_to_probs):
        logits = {
            "p_valid":   {"logit": 0.0, "group": "SCHEME"},
            "p_invalid": {"logit": 0.0, "group": "SCHEME"},
            "p_null":    {"logit": 0.0, "group": "SCHEME"},
            "inv_recurse": {"logit": 5.0, "group": "INVALID_DELIM"},
            "inv_stop":    {"logit": 0.0, "group": "INVALID_DELIM"},
        }
        probs = logits_to_probs(logits)
        scheme_sum = sum(probs[k]["weight"] for k in ["p_valid", "p_invalid", "p_null"])
        delim_sum  = sum(probs[k]["weight"] for k in ["inv_recurse", "inv_stop"])
        assert abs(scheme_sum - 1.0) < 1e-9
        assert abs(delim_sum  - 1.0) < 1e-9

    def test_numerical_stability_with_large_logits(self, logits_to_probs):
        """Should not overflow or produce NaN with very large logits."""
        logits = {
            "p_valid":   {"logit": 1000.0, "group": "SCHEME"},
            "p_invalid": {"logit": 999.0,  "group": "SCHEME"},
            "p_null":    {"logit": 998.0,  "group": "SCHEME"},
        }
        probs = logits_to_probs(logits)
        for v in probs.values():
            assert math.isfinite(v["weight"])
            assert v["weight"] >= 0


class TestGenerateWithChoices:
    @pytest.fixture(scope="class")
    def gen_fn(self):
        from generator import _generate_with_choices, _COMPONENTS_WITH_CHOICE
        return _generate_with_choices, _COMPONENTS_WITH_CHOICE

    def test_returns_url_and_choices(self, gen_fn):
        fn, _ = gen_fn
        url, choices = fn()
        assert isinstance(url, str)
        assert isinstance(choices, dict)

    def test_choices_covers_all_components(self, gen_fn):
        fn, components = gen_fn
        _, choices = fn()
        expected = {name for name, _ in components}
        assert set(choices.keys()) == expected

    def test_each_choice_has_chosen_and_group(self, gen_fn):
        fn, _ = gen_fn
        _, choices = fn()
        for name, info in choices.items():
            assert "chosen" in info, f"{name}: missing 'chosen'"
            assert "group"  in info, f"{name}: missing 'group'"

    def test_chosen_is_non_empty_string(self, gen_fn):
        fn, _ = gen_fn
        _, choices = fn()
        for name, info in choices.items():
            assert isinstance(info["chosen"], str) and info["chosen"], \
                f"{name}: 'chosen' is empty"

    def test_url_is_string(self, gen_fn):
        fn, _ = gen_fn
        url, _ = fn()
        assert isinstance(url, str)

    def test_choices_vary_across_calls(self, gen_fn):
        """Choices should not always be identical (would indicate the sampler is broken)."""
        fn, _ = gen_fn
        all_choices = [fn()[1]["scheme"]["chosen"] for _ in range(50)]
        assert len(set(all_choices)) > 1, "scheme choice never varied across 50 calls"
