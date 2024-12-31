import pytest
import json
import logging
from unittest.mock import Mock, patch
from log_this.manager.config.mixins.instance_methods import ImportConfigFromFileMixin


# Fixture pro základní instanci mixinu
@pytest.fixture
def config_mixin():
    class TestMixin(ImportConfigFromFileMixin):
        def __init__(self):
            self.config = {}

        def _read_config_file(self, path):
            # Bude mockováno v testech
            pass

        def _validate_config(self, config):
            # Bude mockováno v testech
            pass

        def _get_config_file_path(self):
            return "/tmp/config.json"

        def _save_config_to_file(self, path, config):
            # Simulace uložení konfigurace
            pass

    return TestMixin()


# Test úspěšného importu
def test_successful_import(config_mixin):
    test_config = {"test_key": "test_value"}

    config_mixin._read_config_file = Mock(return_value=test_config)
    config_mixin._validate_config = Mock(return_value=True)

    with patch('logging.info') as mock_logging:
        config_mixin.import_config_from_file("/path/to/config.json")

        # Ověření, že konfigurace byla nastavena
        assert config_mixin.config == test_config

        # Ověření, že bylo zalogováno potvrzení
        mock_logging.assert_called_once()
        assert "Konfigurace importována" in mock_logging.call_args[0][0]


# Test neexistujícího souboru
def test_file_not_found(config_mixin):
    config_mixin._read_config_file = Mock(
        side_effect=FileNotFoundError("Soubor nenalezen"))

    with patch('logging.error') as mock_logging:
        with pytest.raises(FileNotFoundError) as exc_info:
            config_mixin.import_config_from_file("/neexistující/soubor.json")

        assert "Soubor nenalezen" in str(exc_info.value)
        mock_logging.assert_called_once()
        assert "Chyba při importu konfigurace" in mock_logging.call_args[0][0]


# Test nevalidního JSON
def test_invalid_json(config_mixin):
    config_mixin._read_config_file = Mock(
        side_effect=json.JSONDecodeError("Invalid JSON", "", 0))

    with patch('logging.error') as mock_logging:
        with pytest.raises(json.JSONDecodeError):
            config_mixin.import_config_from_file("/path/to/invalid.json")

        mock_logging.assert_called_once()
        assert "Chyba při importu konfigurace" in mock_logging.call_args[0][0]


# Test neplatné konfigurace
def test_invalid_config(config_mixin):
    test_config = {"invalid_key": "invalid_value"}

    config_mixin._read_config_file = Mock(return_value=test_config)
    config_mixin._validate_config = Mock(return_value=False)

    with patch('logging.error') as mock_logging:
        with pytest.raises(ValueError) as exc_info:
            config_mixin.import_config_from_file("/path/to/config.json")

        assert "neplatné hodnoty" in str(exc_info.value)
        mock_logging.assert_called_once()
        assert "Chyba při importu konfigurace" in mock_logging.call_args[0][0]


# Test volání save_config_to_file
def test_save_config_called(config_mixin):
    test_config = {"test_key": "test_value"}
    mock_save = Mock()

    config_mixin._read_config_file = Mock(return_value=test_config)
    config_mixin._validate_config = Mock(return_value=True)
    config_mixin._save_config_to_file = mock_save

    config_mixin.import_config_from_file("/path/to/config.json")

    # Ověření, že save_config_to_file byla zavolána se správnými parametry
    mock_save.assert_called_once_with("/tmp/config.json", test_config)