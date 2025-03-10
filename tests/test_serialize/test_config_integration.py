import pytest
from pathlib import Path
import json
from log_this_old.manager.config import get_config


@pytest.fixture
def config_instance():
    """Fixture that create the singleton instance for config."""
    return get_config()


def test_get_config_file_path(config_instance):
    """Integrační test pro metodu _get_config_file_path."""
    result = config_instance._get_config_file_path()
    assert result == Path(config_instance._config_dir / "config.json")


def test_read_config_file(config_instance, tmp_path):
    """Integrační test pro metodu read_config_file"""
    # Příprava dat a vytvoření testovacího souboru s dočasným adresářem
    config_instance._config_dir = tmp_path
    config_path = config_instance._get_config_file_path()
    # Příprava dat pro test
    expected_result = {"key": "value"}
    config_path.write_text(json.dumps(expected_result))
    result = config_instance._read_config_file(config_path)
    assert result == expected_result


def test_validate_value(config_instance):
    """Integrační test pro metodu validate_value"""
    result = config_instance._validate_value('blank_lines', True)
    assert result is True
    result = config_instance._validate_value('docstring_lines', "all")
    assert result is True
    result = config_instance._validate_value('unknown_key', 1)
    assert result is False


def test_key_and_value_check(config_instance):
    """Integrační test pro metodu key_and_value_check"""
    result = config_instance._key_and_value_check('blank_lines', True)
    assert result is True


def test_validate_config_dict(config_instance):
    """Integrační test pro metodu validate_config_dict"""
    pass



def test_save_config_to_file(config_instance):
    """Integrační test pro metodu save_config_to_file"""
    pass

def test_load_default_config(config_instance):
    """Integrační test pro metodu load_default_config"""
    pass

def test_update_config(config_instance):
    """Integrační test pro metodu update_config"""
    pass

def test_update_configs(config_instance):
    """Integrační test pro metodu update_configs"""
    pass

def test_reset_config(config_instance):
    """Integrační test pro metodu reset_config"""
    pass

def test_import_config_from_file(config_instance):
    """Integrační test pro metodu import_config_from_file"""
    pass

def test_export_config_to_file(config_instance):
    """Integrační test pro metodu """
    pass

def test_str(config_instance):
    """Integrační test pro metodu __str__"""
    pass

def test_getitem(config_instance):
    """Integrační test pro metodu __getitem__"""
    pass