# test_config.py
import os
import pytest
import json
from log_this.config.data import LogThisConfig


def test_singleton_instance():
    """Test, že LogThisConfig vrací vždy stejnou instanci."""
    config1 = LogThisConfig()
    config2 = LogThisConfig()
    assert config1 is config2


def test_default_values():
    """Test výchozích hodnot konfigurace."""
    config = LogThisConfig()
    assert config.values == {
        'skip_this': 0,
        'one_line': 1,
        'simple': 2,
        'detailed': 3,
        'report': 4,
        True: 1,
        False: 0,
        None: 0,
        '': 0,
    }
    assert config.indent == 2
    assert config.blank_lines is True
    assert config.docstring_lines == 3
    assert config.max_depth == 100


def test_config_file_exists():
    """Test existence konfiguračního souboru."""
    config_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'log_this',
        'config',
        'data',
        'config.json'
    )
    assert os.path.exists(config_path), "Konfigurační soubor neexistuje"



def test_config_file_structure():
    """Test struktury konfiguračního souboru."""
    config_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'log_this',
        'config',
        'data',
        'config.json'
    )
    with open(config_path, 'r') as f:
        config_data = json.load(f)

    expected_keys = [
        'skip_this', 'one_line', 'simple',
        'detailed', 'report', 'true', 'false',
        'none', 'empty', 'indent', 'blank_lines',
        'docstring_lines', 'max_depth'
    ]

    for key in expected_keys:
        assert key in config_data, f"Chybí klíč {key} v konfiguraci"


def test_config_value_types():
    """Test typů hodnot v konfiguraci."""
    config = LogThisConfig()

    # Test celočíselných hodnot
    int_keys = ['skip_this', 'one_line', 'simple', 'detailed', 'report']
    for key in int_keys:
        assert isinstance(config.values[key], int), f"{key} musí být celé číslo"

    # Test boolean hodnot
    assert isinstance(config.values[True], int)
    assert isinstance(config.values[False], int)
    assert isinstance(config.values[None], int)
    assert isinstance(config.values[''], int)


def test_config_indentation_and_formatting():
    """Test nastavení odsazení a formátování."""
    config = LogThisConfig()
    assert config.indent >= 0, "Odsazení musí být nezáporné"
    assert config.docstring_lines >= 0, "Počet řádků docstringu musí být nezáporný"
    assert isinstance(config.blank_lines, bool), "blank_lines musí být boolean"
