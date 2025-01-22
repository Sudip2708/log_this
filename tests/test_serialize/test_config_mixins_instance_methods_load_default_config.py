import pytest
import json
import os
from unittest.mock import Mock, patch
from log_this.manager.config.init_mixins.instance_methods2 import LoadDefaultConfigMixin


# Fixture pro základní instanci mixinu
@pytest.fixture
def config_mixin():
    class TestMixin(LoadDefaultConfigMixin):
        def __init__(self):
            self._config_dir = os.path.normpath("/tmp/config")
            self.DEFAULTS = {
                "setting1": "default1",
                "setting2": True,
                "setting3": 42
            }

        def _read_config_file(self, path):
            # Bude mockováno v testech
            pass

        def _validate_config_dict(self, config):
            # Bude mockováno v testech
            pass

        def _save_config_to_file(self, path, config):
            # Bude mockováno v testech
            pass

    return TestMixin()


# Test úspěšného načtení existující konfigurace
def test_load_existing_valid_config(config_mixin):
    test_config = {
        "setting1": "value1",
        "setting2": False,
        "setting3": 100
    }

    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True
        config_mixin._read_config_file = Mock(return_value=test_config)
        config_mixin._validate_config_dict = Mock(return_value=True)

        result = config_mixin._load_default_config()
        assert result == test_config

        expected_path = os.path.normpath("/tmp/config/config.json")
        config_mixin._read_config_file.assert_called_once_with(expected_path)
        config_mixin._validate_config_dict.assert_called_once_with(test_config)



# Test načtení výchozí konfigurace při neexistujícím souboru
def test_load_defaults_when_file_not_exists(config_mixin):
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False
        config_mixin._save_config_to_file = Mock()

        result = config_mixin._load_default_config()
        assert result == config_mixin.DEFAULTS
        assert result is not config_mixin.DEFAULTS  # Ověření, že jde o kopii

        expected_path = os.path.normpath("/tmp/config/config.json")
        config_mixin._save_config_to_file.assert_called_once_with(
            expected_path,
            config_mixin.DEFAULTS
        )


# Test při nevalidní konfiguraci v souboru
def test_load_defaults_when_invalid_config(config_mixin):
    invalid_config = {"invalid_key": "invalid_value"}

    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True
        config_mixin._read_config_file = Mock(return_value=invalid_config)
        config_mixin._validate_config_dict = Mock(return_value=False)
        config_mixin._save_config_to_file = Mock()

        result = config_mixin._load_default_config()
        assert result == config_mixin.DEFAULTS

        expected_path = os.path.normpath("/tmp/config/config.json")
        config_mixin._save_config_to_file.assert_called_once_with(
            expected_path,
            config_mixin.DEFAULTS
        )


# Test při chybě JSON dekódování
def test_load_defaults_when_json_error(config_mixin):
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True
        config_mixin._read_config_file = Mock(
            side_effect=json.JSONDecodeError("Invalid JSON", "", 0)
        )
        config_mixin._save_config_to_file = Mock()

        with patch('logging.warning') as mock_logging:
            result = config_mixin._load_default_config()
            assert result == config_mixin.DEFAULTS

            mock_logging.assert_called_once()
            assert "Chyba při načítání konfigurace" in \
                   mock_logging.call_args[0][0]

            expected_path = os.path.normpath("/tmp/config/config.json")
            config_mixin._save_config_to_file.assert_called_once_with(
                expected_path,
                config_mixin.DEFAULTS
            )


# Test správného sestavení cesty ke konfiguračnímu souboru
def test_config_path_construction(config_mixin):
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False
        config_mixin._save_config_to_file = Mock()

        config_mixin._load_default_config()

        expected_path = os.path.join("/tmp/config", "config.json")
        expected_path = os.path.normpath(expected_path)
        config_mixin._save_config_to_file.assert_called_once_with(
            expected_path,
            config_mixin.DEFAULTS
        )