"""Tests that every component module exports the expected interface."""

import importlib
import pytest

COMPONENT_MODULES = [
    "scheme",
    "schemeauthdelim",
    "username",
    "userpassdelim",
    "password",
    "userinfohostdelim",
    "host",
    "hostportdelim",
    "port",
    "authpathdelim",
    "path",
    "pathquerydelim",
    "query",
    "queryfragdelim",
    "fragment",
]


@pytest.fixture(scope="module", params=COMPONENT_MODULES)
def component_module(request):
    return importlib.import_module(request.param)


class TestComponentInterface:
    def test_has_generate(self, component_module):
        assert hasattr(component_module, "generate"), \
            f"{component_module.__name__} missing generate()"

    def test_has_generate_with_choice(self, component_module):
        assert hasattr(component_module, "generate_with_choice"), \
            f"{component_module.__name__} missing generate_with_choice()"

    def test_has_serialize_weights(self, component_module):
        assert hasattr(component_module, "serialize_weights"), \
            f"{component_module.__name__} missing serialize_weights()"

    def test_generate_returns_str(self, component_module):
        result = component_module.generate()
        assert isinstance(result, str)

    def test_generate_with_choice_returns_tuple(self, component_module):
        result = component_module.generate_with_choice()
        assert isinstance(result, tuple) and len(result) == 3

    def test_generate_with_choice_chosen_key_is_str(self, component_module):
        _, chosen_key, _ = component_module.generate_with_choice()
        assert isinstance(chosen_key, str) and len(chosen_key) > 0

    def test_generate_with_choice_group_is_str(self, component_module):
        _, _, group = component_module.generate_with_choice()
        assert isinstance(group, str) and len(group) > 0

    def test_generate_with_choice_chosen_key_in_serialize(self, component_module):
        """The chosen_key should appear in the serialized weight dict."""
        serialized = component_module.serialize_weights()
        for _ in range(10):
            _, chosen_key, _ = component_module.generate_with_choice()
            assert chosen_key in serialized, \
                f"{component_module.__name__}: chosen_key {chosen_key!r} not in serialized weights"
