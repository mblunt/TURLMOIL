"""Tests for _softmax_probs in reinforce.py."""

import math
import pytest


@pytest.fixture(scope="module")
def softmax_probs():
    from tasks.feedback.reinforce import _softmax_probs
    return _softmax_probs


def _logits(mapping, group):
    return {k: {"logit": v, "group": group} for k, v in mapping.items()}


class TestSoftmaxProbs:
    def test_uniform_logits_equal_probs(self, softmax_probs):
        d = _logits({"p_valid": 0.0, "p_invalid": 0.0, "p_null": 0.0}, "SCHEME")
        probs = softmax_probs(d, "SCHEME")
        for v in probs.values():
            assert abs(v - 1/3) < 1e-9

    def test_probs_sum_to_one(self, softmax_probs):
        d = _logits({"p_valid": 1.5, "p_invalid": -0.5, "p_null": 0.2}, "SCHEME")
        probs = softmax_probs(d, "SCHEME")
        assert abs(sum(probs.values()) - 1.0) < 1e-9

    def test_all_probs_non_negative(self, softmax_probs):
        d = _logits({"p_valid": -5.0, "p_invalid": 3.0, "p_null": 0.0}, "SCHEME")
        probs = softmax_probs(d, "SCHEME")
        for v in probs.values():
            assert v >= 0.0

    def test_highest_logit_has_highest_prob(self, softmax_probs):
        d = _logits({"p_valid": 10.0, "p_invalid": 0.0, "p_null": -5.0}, "SCHEME")
        probs = softmax_probs(d, "SCHEME")
        assert probs["p_valid"] == max(probs.values())

    def test_large_logit_numerically_stable(self, softmax_probs):
        d = _logits({"p_valid": 1000.0, "p_invalid": 999.0, "p_null": 998.0}, "SCHEME")
        probs = softmax_probs(d, "SCHEME")
        for v in probs.values():
            assert math.isfinite(v)

    def test_only_keys_for_given_group_returned(self, softmax_probs):
        d = {
            "p_valid":   {"logit": 0.0, "group": "SCHEME"},
            "p_invalid": {"logit": 0.0, "group": "SCHEME"},
            "p_null":    {"logit": 0.0, "group": "SCHEME"},
            "inv_recurse": {"logit": 0.0, "group": "OTHER"},
        }
        probs = softmax_probs(d, "SCHEME")
        assert set(probs.keys()) == {"p_valid", "p_invalid", "p_null"}
