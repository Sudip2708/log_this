# test_config_loader_mixin.py
import pytest
import os
import json
import tempfile
from log_this.config.data._loader_mixin import ConfigLoaderMixin
from log_this.config.data.mixins_data import ConfigConstants


def test_load_config_updates_values():
    """Test, že _load_config správně aktualizuje hodnoty."""
    class TestConfig(ConfigLoaderMixin):
        values = {}
        indent = None
        blank_lines = None
        docstring_lines = None
        max_depth = None

    # Příprava mock konfigurace
    mock_config_path = os.path.join(tempfile.gettempdir(), 'test_config.json')
    with open(mock_config_path, 'w') as f:
        json.dump({
            'skip_this': 0,
            'one_line': 1,
            'simple': 2,
            'detailed': 3,
            'report': 4,
            'true': 0,
            'false': 1,
            'none': 0,
            'empty': 1,
            'indent': 4,
            'blank_lines': False,
            'docstring_lines': 10,
            'max_depth': 200
        }, f)

    try:
        TestConfig._load_config(mock_config_path)

        assert TestConfig.values[True] == 0
        assert TestConfig.values[False] == 1
        assert TestConfig.values[''] == 1
        assert TestConfig.indent == 4
        assert TestConfig.blank_lines is False
        assert TestConfig.docstring_lines == 10
        assert TestConfig.max_depth == 200
    finally:
        # Úklid - smazání dočasného souboru
        os.unlink(mock_config_path)


def test_default_config_structure():
    """Test, že výchozí konfigurace má správnou strukturu."""
    default_config = ConfigConstants.DEFAULT_CONFIG

    expected_keys = [
        'skip_this', 'one_line', 'simple',
        'detailed', 'report', 'true', 'false',
        'none', 'empty', 'indent', 'blank_lines',
        'docstring_lines', 'max_depth'
    ]

    for key in expected_keys:
        assert key in default_config, f"Chybí klíč {key} ve výchozí konfiguraci"