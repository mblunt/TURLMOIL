import re
import random
from collections import defaultdict
from dataclasses import dataclass
from typing import Any

from nltk import PCFG

from terminal import (
    ASCII_DIGITS,
    ASCII_LETTERS,
    ASCII_SPECIAL,
    ASCII_WHITESPACE,
    ASCII_CONTROL,
    HEXDIGIT,
)
from terminal import (
    UNICODE_VALID,
    UNICODE_DISALLOWED,
    UNICODE_UNASSIGNED,
    UNICODE_RESERVED,
)
from terminal import (
    KNOWN_SCHEMES,
    NULL,
    PATH_SPECIAL,
    PATH_FORBIDDEN,
    QUERY_SPECIAL,
    HOST_SPECIAL,
    COMMON_SCHEMES,
)

from utils import generate_sample


BASE_TERMINAL_MAP = {
    "ASCII_DIGITS": ASCII_DIGITS,
    "ASCII_LETTERS": ASCII_LETTERS,
    "ASCII_SPECIAL": ASCII_SPECIAL,
    "ASCII_WHITESPACE": ASCII_WHITESPACE,
    "ASCII_CONTROL": ASCII_CONTROL,
    "UNICODE_VALID": UNICODE_VALID,
    "UNICODE_DISALLOWED": UNICODE_DISALLOWED,
    "UNICODE_UNASSIGNED": UNICODE_UNASSIGNED,
    "UNICODE_RESERVED": UNICODE_RESERVED,
    "KNOWN_SCHEMES": KNOWN_SCHEMES,
    "NULL": NULL,
    "PATH_SPECIAL": PATH_SPECIAL,
    "PATH_FORBIDDEN": PATH_FORBIDDEN,
    "QUERY_SPECIAL": QUERY_SPECIAL,
    "HOST_SPECIAL": HOST_SPECIAL,
    "COMMON_SCHEMES": COMMON_SCHEMES,
    "HEXDIGIT": HEXDIGIT,
}


@dataclass(frozen=True)
class WeightSpec:
    weight: float
    group: str


class GrammarComponent:
    _RULE_RE = re.compile(r"^\s*([A-Z_][A-Z0-9_]*)\s*->\s*(.+)$")
    _PLACEHOLDER_RE = re.compile(r"\[\{([a-zA-Z_][a-zA-Z0-9_]*)\}\]")

    def __init__(self, pcfg_template, default_weights, extra_terminals=None):
        self.pcfg_template = pcfg_template
        self.terminal_map = {**BASE_TERMINAL_MAP, **(extra_terminals or {})}
        self.placeholder_to_group = self._extract_placeholder_groups(self.pcfg_template)

        self.default_weights = self._resolve_weight_map(
            default_weights,
            require_complete=True,
        )
        self._validate_group_sums(self.default_weights)

        self._default_grammar = PCFG.fromstring(
            self.pcfg_template.format(**self.default_weights)
        )

    def _extract_placeholder_groups(self, template: str) -> dict[str, str]:
        mapping: dict[str, str] = {}

        for raw_line in template.splitlines():
            line = raw_line.strip()
            if not line:
                continue

            match = self._RULE_RE.match(line)
            if not match:
                continue

            lhs, rhs = match.groups()
            placeholders = self._PLACEHOLDER_RE.findall(rhs)

            for placeholder in placeholders:
                if placeholder in mapping and mapping[placeholder] != lhs:
                    raise ValueError(
                        f"Placeholder '{placeholder}' appears in multiple productions "
                        f"within the same template: '{mapping[placeholder]}' and '{lhs}'"
                    )
                mapping[placeholder] = lhs

        if not mapping:
            raise ValueError("No placeholders found in PCFG template")

        return mapping

    def _coerce_to_spec(self, key: str, value: Any) -> WeightSpec:
        """
        Supported inputs:
          1) 0.6
          2) {"weight": 0.6, "group": "HOST"}
        """
        if key not in self.placeholder_to_group:
            raise ValueError(
                f"Unknown weight key '{key}'. Expected one of: "
                f"{sorted(self.placeholder_to_group.keys())}"
            )

        expected_group = self.placeholder_to_group[key]

        if isinstance(value, (int, float)):
            return WeightSpec(weight=float(value), group=expected_group)

        if isinstance(value, dict):
            if "weight" not in value:
                raise ValueError(f"Weight entry for '{key}' must contain 'weight'")

            group = value.get("group") or value.get("grouping")
            if group is None:
                raise ValueError(f"Weight entry for '{key}' must contain 'group'")

            return WeightSpec(weight=float(value["weight"]), group=str(group))

        if isinstance(value, list):
            raise ValueError(
                f"Weight entry for '{key}' no longer supports list-valued specs"
            )

        raise ValueError(
            f"Unsupported weight entry for '{key}': {type(value).__name__}"
        )

    def _resolve_entry(self, key: str, value: Any) -> float:
        """
        Resolve one provided entry to the float for this component's expected group.
        """
        expected_group = self.placeholder_to_group[key]
        spec = self._coerce_to_spec(key, value)

        if spec.group != expected_group:
            raise ValueError(
                f"Weight '{key}' needs group '{expected_group}' for this component, "
                f"but got group '{spec.group}'"
            )

        return spec.weight

    def serialize_weights(self, weights=None) -> dict[str, dict]:
        """
        Serialize weights into canonical structured form:

        {
            "p_valid": {"weight": 0.9, "group": "SCHEME"},
            "p_invalid": {"weight": 0.1, "group": "SCHEME"},
            ...
        }

        - If weights is None, serialize self.default_weights
        - If weights is provided, merge it the same way generate() does
        """
        if weights:
            overrides = self._resolve_weight_map(weights, require_complete=False)
            source = {**self.default_weights, **overrides}
            self._validate_group_sums(source)
        else:
            source = self.default_weights

        serialized: dict[str, dict] = {}

        for key in sorted(self.placeholder_to_group.keys()):
            if key not in source:
                raise ValueError(f"Missing weight for key '{key}' during serialization")

            serialized[key] = {
                    "weight": float(source[key]),
                    "group": self.placeholder_to_group[key],
                }

        return serialized

    def _resolve_weight_map(
        self,
        weights: dict[str, Any],
        *,
        require_complete: bool,
    ) -> dict[str, float]:
        resolved: dict[str, float] = {}

        for key, value in weights.items():
            resolved[key] = self._resolve_entry(key, value)

        if require_complete:
            expected = set(self.placeholder_to_group.keys())
            actual = set(resolved.keys())

            missing = sorted(expected - actual)
            extra = sorted(actual - expected)

            if missing:
                raise ValueError(f"Missing weights for placeholders: {missing}")
            if extra:
                raise ValueError(f"Unexpected weight keys: {extra}")

        return resolved

    def _validate_group_sums(self, weights: dict[str, float], tol: float = 1e-9) -> None:
        grouped_totals = defaultdict(float)

        for key, weight in weights.items():
            grouped_totals[self.placeholder_to_group[key]] += weight

        bad = {
            group: total
            for group, total in grouped_totals.items()
            if abs(total - 1.0) > tol
        }

        if bad:
            raise ValueError(
                "Weights must sum to 1.0 within each grouping; got: "
                + ", ".join(f"{group}={total}" for group, total in sorted(bad.items()))
            )

    def generate(self, weights=None):
        if weights:
            overrides = self._resolve_weight_map(weights, require_complete=False)
            merged = {**self.default_weights, **overrides}
            self._validate_group_sums(merged)

            grammar = PCFG.fromstring(
                self.pcfg_template.format(**merged)
            )
        else:
            grammar = self._default_grammar

        return generate_sample(grammar, grammar.start(), self.terminal_map)

    def generate_with_choice(self, weights=None):
        """Generate a string and record which top-level branch was chosen.

        Explicitly samples the start-group production so the choice can be
        serialised and used as the action in a REINFORCE update.

        This is the per-component bandit variant of REINFORCE: a single
        categorical action per component, with the full job score as the
        shared reward.  Components are treated as conditionally independent —
        a known approximation when the reward is a joint function of all
        components.

        Returns:
            (string, chosen_key, start_group) — chosen_key is the weight
            placeholder sampled at the top level (e.g. 'p_valid').
        """
        if weights:
            overrides = self._resolve_weight_map(weights, require_complete=False)
            merged = {**self.default_weights, **overrides}
            self._validate_group_sums(merged)
        else:
            merged = self.default_weights

        start_group = str(self._default_grammar.start())
        top_keys = [k for k, g in self.placeholder_to_group.items() if g == start_group]
        top_weights = [merged[k] for k in top_keys]

        chosen_key = random.choices(top_keys, weights=top_weights)[0]

        # Force the grammar to always expand the chosen branch.
        # Near-zero epsilon keeps NLTK's probability validator happy.
        # We format all floats as fixed-point decimals because NLTK's PCFG
        # parser rejects scientific notation (e.g. "1e-06").
        eps = 0.000001
        n_others = len(top_keys) - 1
        forced = {
            k: (f"{1.0 - eps * n_others:.6f}" if k == chosen_key else f"{eps:.6f}")
            if k in top_keys
            else f"{v:.6f}"
            for k, v in merged.items()
        }

        grammar = PCFG.fromstring(self.pcfg_template.format(**forced))
        string = generate_sample(grammar, grammar.start(), self.terminal_map)

        return string, chosen_key, start_group