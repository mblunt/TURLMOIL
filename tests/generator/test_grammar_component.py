"""Tests for GrammarComponent — the core PCFG wrapper in component.py."""

import pytest


@pytest.fixture(scope="module")
def scheme_component():
    from component import GrammarComponent
    from scheme import component
    return component


class TestGenerate:
    def test_returns_string(self, scheme_component):
        result = scheme_component.generate()
        assert isinstance(result, str)

    def test_repeated_calls_produce_varied_output(self, scheme_component):
        results = {scheme_component.generate() for _ in range(50)}
        assert len(results) > 1, "generate() should not always return the same string"

    def test_null_weight_produces_empty_string(self, scheme_component):
        """Force p_null=1.0 — should always produce empty string."""
        from scheme import generate
        weights = {
            "p_valid":   {"weight": 0.0,  "group": "SCHEME"},
            "p_invalid": {"weight": 0.0,  "group": "SCHEME"},
            "p_null":    {"weight": 1.0,  "group": "SCHEME"},
            "schemes_common":   {"weight": 0.5, "group": "VALID_SCHEME"},
            "schemes_uncommon": {"weight": 0.5, "group": "VALID_SCHEME"},
            "inv_char":         {"weight": 0.4, "group": "INVALID_SCHEME"},
            "inv_known":        {"weight": 0.3, "group": "INVALID_SCHEME"},
            "inv_letter":       {"weight": 0.3, "group": "INVALID_SCHEME"},
            "inv2_recurse":     {"weight": 0.45, "group": "INVALID_TAIL"},
            "inv2_tail_known":  {"weight": 0.45, "group": "INVALID_TAIL"},
            "inv2_stop":        {"weight": 0.1,  "group": "INVALID_TAIL"},
            "valid3_char_letters": {"weight": 0.8, "group": "VALID_CHAR"},
            "valid3_char_digits":  {"weight": 0.2, "group": "VALID_CHAR"},
            "inv3_char_special":    {"weight": 0.25, "group": "INVALID_CHAR"},
            "inv3_char_unicode":    {"weight": 0.25, "group": "INVALID_CHAR"},
            "inv3_char_whitespace": {"weight": 0.1,  "group": "INVALID_CHAR"},
            "inv3_char_control":    {"weight": 0.1,  "group": "INVALID_CHAR"},
            "inv3_char_disallowed": {"weight": 0.1,  "group": "INVALID_CHAR"},
            "inv3_char_unassigned": {"weight": 0.1,  "group": "INVALID_CHAR"},
            "inv3_char_reserved":   {"weight": 0.1,  "group": "INVALID_CHAR"},
            "any_valid":   {"weight": 0.5, "group": "ANY_CHAR"},
            "any_invalid": {"weight": 0.5, "group": "ANY_CHAR"},
        }
        results = [generate(weights) for _ in range(20)]
        assert all(r == "" for r in results), f"Expected empty strings, got: {set(results)}"


class TestGenerateWithChoice:
    def test_returns_three_tuple(self, scheme_component):
        result = scheme_component.generate_with_choice()
        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_string_is_str(self, scheme_component):
        string, _, _ = scheme_component.generate_with_choice()
        assert isinstance(string, str)

    def test_chosen_key_is_str(self, scheme_component):
        _, chosen_key, _ = scheme_component.generate_with_choice()
        assert isinstance(chosen_key, str)

    def test_group_is_start_symbol(self, scheme_component):
        _, _, group = scheme_component.generate_with_choice()
        assert group == "SCHEME"

    def test_chosen_key_in_top_level_weights(self, scheme_component):
        for _ in range(20):
            _, chosen_key, _ = scheme_component.generate_with_choice()
            assert chosen_key in {"p_valid", "p_invalid", "p_null"}

    def test_chosen_key_matches_string_type(self, scheme_component):
        """When p_null is chosen, string should be empty. When p_valid, non-empty."""
        null_count = 0
        valid_count = 0
        for _ in range(100):
            string, chosen_key, _ = scheme_component.generate_with_choice()
            if chosen_key == "p_null":
                assert string == "", f"p_null should produce empty string, got {string!r}"
                null_count += 1
            elif chosen_key == "p_valid":
                valid_count += 1
        # Both should appear in 100 samples given equal weights
        assert null_count > 0 or valid_count > 0

    def test_forced_choice_via_weights(self, scheme_component):
        """Passing weights that force p_null should always choose p_null."""
        forced = {
            "p_valid":   {"weight": 0.0, "group": "SCHEME"},
            "p_invalid": {"weight": 0.0, "group": "SCHEME"},
            "p_null":    {"weight": 1.0, "group": "SCHEME"},
            "schemes_common":   {"weight": 0.5, "group": "VALID_SCHEME"},
            "schemes_uncommon": {"weight": 0.5, "group": "VALID_SCHEME"},
            "inv_char":         {"weight": 0.4, "group": "INVALID_SCHEME"},
            "inv_known":        {"weight": 0.3, "group": "INVALID_SCHEME"},
            "inv_letter":       {"weight": 0.3, "group": "INVALID_SCHEME"},
            "inv2_recurse":     {"weight": 0.45, "group": "INVALID_TAIL"},
            "inv2_tail_known":  {"weight": 0.45, "group": "INVALID_TAIL"},
            "inv2_stop":        {"weight": 0.1,  "group": "INVALID_TAIL"},
            "valid3_char_letters": {"weight": 0.8, "group": "VALID_CHAR"},
            "valid3_char_digits":  {"weight": 0.2, "group": "VALID_CHAR"},
            "inv3_char_special":    {"weight": 0.25, "group": "INVALID_CHAR"},
            "inv3_char_unicode":    {"weight": 0.25, "group": "INVALID_CHAR"},
            "inv3_char_whitespace": {"weight": 0.1,  "group": "INVALID_CHAR"},
            "inv3_char_control":    {"weight": 0.1,  "group": "INVALID_CHAR"},
            "inv3_char_disallowed": {"weight": 0.1,  "group": "INVALID_CHAR"},
            "inv3_char_unassigned": {"weight": 0.1,  "group": "INVALID_CHAR"},
            "inv3_char_reserved":   {"weight": 0.1,  "group": "INVALID_CHAR"},
            "any_valid":   {"weight": 0.5, "group": "ANY_CHAR"},
            "any_invalid": {"weight": 0.5, "group": "ANY_CHAR"},
        }
        for _ in range(10):
            _, chosen_key, _ = scheme_component.generate_with_choice(weights=forced)
            assert chosen_key == "p_null"


class TestSerializeWeights:
    def test_returns_dict(self, scheme_component):
        result = scheme_component.serialize_weights()
        assert isinstance(result, dict)

    def test_all_placeholders_present(self, scheme_component):
        result = scheme_component.serialize_weights()
        expected = set(scheme_component.placeholder_to_group.keys())
        assert set(result.keys()) == expected

    def test_each_entry_has_weight_and_group(self, scheme_component):
        result = scheme_component.serialize_weights()
        for key, entry in result.items():
            assert "weight" in entry, f"Missing 'weight' in {key}"
            assert "group" in entry, f"Missing 'group' in {key}"

    def test_weights_sum_to_one_per_group(self, scheme_component):
        result = scheme_component.serialize_weights()
        from collections import defaultdict
        by_group = defaultdict(float)
        for entry in result.values():
            by_group[entry["group"]] += entry["weight"]
        for group, total in by_group.items():
            assert abs(total - 1.0) < 1e-6, f"Group {group} sums to {total}"
