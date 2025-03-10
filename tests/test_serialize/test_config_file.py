import json
import pytest
from log_this_old.manager.config import get_config


@pytest.fixture(scope="module")
def config():
    """Fixture pro instanci konfigurace."""
    return get_config()


@pytest.fixture(scope="module")
def config_content(config):
    """Fixture pro obsah konfiguračního souboru."""
    with open(config._get_config_file_path()) as f:
        return json.load(f)


def test_config_file_exists(config):
    """Test existence konfiguračního souboru."""
    config_path = config._get_config_file_path()
    assert config_path.exists()


def test_config_file_is_valid_json(config):
    """Test, že soubor obsahuje validní JSON."""
    try:
        with open(config._get_config_file_path()) as f:
            config = json.load(f)
            assert isinstance(config, dict)
    except json.JSONDecodeError:
        pytest.fail("Konfigurační soubor není validní JSON")


def test_config_content_validity(config_content):
    """Test obsahu konfigurace."""
    assert len(config_content) == 13
    assert "skip_this" in config_content
    assert "one_line" in config_content
    assert "simple" in config_content
    assert "detailed" in config_content
    assert "report" in config_content
    assert "true" in config_content
    assert "false" in config_content
    assert "none" in config_content
    assert "empty" in config_content
    assert "indent" in config_content
    assert "blank_lines" in config_content
    assert "docstring_lines" in config_content
    assert "max_depth" in config_content


def test_config_values_types(config_content):
    """Test správných typů hodnot."""
    # Definice očekávaných typů pro každý klíč
    type_checks = {
        "skip_this": (int, lambda x: 0 <= x <= 4),
        "one_line": (int, lambda x: 0 <= x <= 4),
        "simple": (int, lambda x: 0 <= x <= 4),
        "detailed": (int, lambda x: 0 <= x <= 4),
        "report": (int, lambda x: 0 <= x <= 4),
        "true": (int, lambda x: 0 <= x <= 4),
        "false": (int, lambda x: 0 <= x <= 4),
        "none": (int, lambda x: 0 <= x <= 4),
        "empty": (int, lambda x: 0 <= x <= 4),
        "indent": (int, lambda x: 0 <= x <= 4),
        "blank_lines": (bool, None),
        "docstring_lines": ((int, str), lambda x: x >= 0 or x == 'all'),
        "max_depth": (int, lambda x: x > 0)
    }

    for key, (expected_type, validator) in type_checks.items():
        value = config_content[key]
        assert isinstance(value, expected_type), f"Klíč {key} má nesprávný typ"
        if validator:
            assert validator(value), f"Hodnota pro {key} je mimo povolený rozsah"

