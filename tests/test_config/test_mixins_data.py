import os
import json
import tempfile
import pytest
from log_this.config.data.mixins_data import (
    ConfigConstants,
    ensure_config_file,
    validate_and_update_config,
)
from log_this.config.data.mixins_data._read_config import read_config
from log_this.config.data.mixins_data._validate_value import validate_value


def test_config_constants():
    """Test výchozích konstant konfigurace."""
    default_config = ConfigConstants.DEFAULT_CONFIG

    # Kontrola přítomnosti klíčů
    expected_keys = [
        'skip_this', 'one_line', 'simple', 'detailed', 'report',
        'true', 'false', 'none', 'empty',
        'indent', 'blank_lines', 'docstring_lines', 'max_depth'
    ]

    for key in expected_keys:
        assert key in default_config, f"Chybí klíč {key} v default konfiguraci"

    # Kontrola výchozích hodnot
    assert default_config['skip_this'] == 0
    assert default_config['indent'] == 2
    assert default_config['blank_lines'] is True
    assert default_config['docstring_lines'] == 3
    assert default_config['max_depth'] == 100


def test_ensure_config_file():
    """Test funkce pro zajištění existence konfiguračního souboru."""
    # Příprava dočasného adresáře a souboru
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, 'test_config.json')

        # Ujistíme se, že soubor neexistuje
        assert not os.path.exists(config_path)

        # Zavolání ensure_config_file
        result = ensure_config_file(config_path, ConfigConstants.DEFAULT_CONFIG)

        # Ověření, že soubor byl vytvořen
        assert os.path.exists(config_path)

        # Ověření obsahu souboru
        with open(config_path, 'r') as f:
            saved_config = json.load(f)

        # Kontrola, zda uložená konfigurace odpovídá default konfiguraci
        assert saved_config == ConfigConstants.DEFAULT_CONFIG

        # Kontrola vrácené konfigurace
        assert result == ConfigConstants.DEFAULT_CONFIG


def test_read_config():
    """Test funkce pro čtení konfigurace."""
    # Test s validním JSON souborem
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, 'test_config.json')
        test_config = {
            'skip_this': 1,
            'indent': 4,
            'blank_lines': False
        }

        # Uložení testovací konfigurace
        with open(config_path, 'w') as f:
            json.dump(test_config, f)

        # Čtení konfigurace
        result = read_config(config_path)

        # Kontrola, zda jsou některé klíče zachovány
        assert result['skip_this'] == 1
        assert result['indent'] == 4
        assert result['blank_lines'] is False

    # Test se špatným JSON souborem
    with tempfile.TemporaryDirectory() as tmpdir:
        bad_config_path = os.path.join(tmpdir, 'bad_config.json')

        # Zápis špatného JSON
        with open(bad_config_path, 'w') as f:
            f.write('{ "invalid": json }')

        # Mělo by vrátit default konfiguraci
        result = read_config(bad_config_path)
        assert result == ConfigConstants.DEFAULT_CONFIG


def test_validate_and_update_config():
    """Test funkce pro validaci a aktualizaci konfigurace."""
    # Testovací konfigurace s částečně validními hodnotami
    test_config = {
        'skip_this': 2,  # Validní
        'indent': 3,  # Validní
        'blank_lines': False,  # Validní
        'docstring_lines': 5,  # Validní
        'max_depth': 150,  # Validní
        'unknown_key': 'some_value'  # Bude ignorováno
    }

    result = validate_and_update_config(
        test_config,
        ConfigConstants.DEFAULT_CONFIG
    )

    # Kontrola zachování validních hodnot
    assert result['skip_this'] == 2
    assert result['indent'] == 3
    assert result['blank_lines'] is False
    assert result['docstring_lines'] == 5
    assert result['max_depth'] == 150

    # Kontrola, že neznámé klíče nejsou přidány
    assert 'unknown_key' not in result


def test_validate_value():
    """Test funkce pro validaci jednotlivých hodnot."""
    # Testy pro různé klíče a hodnoty
    test_cases = [
        # key, value, default_value, expected_result
        ('max_depth', 200, 100, 200),
        ('max_depth', 'invalid', 100, 100),
        ('blank_lines', True, False, True),
        ('blank_lines', 1, False, 1),
        ('blank_lines', 'invalid', False, False),
        ('docstring_lines', 5, 3, 5),
        ('docstring_lines', 'all', 3, 'all'),
        ('docstring_lines', 'invalid', 3, 3),
        ('skip_this', 3, 0, 3),
        ('skip_this', 5, 0, 0),
        ('skip_this', -1, 0, 0),
    ]

    for key, value, default_value, expected in test_cases:
        result = validate_value(value, default_value, key)
        assert result == expected, f"Selhání pro key={key}, value={value}"