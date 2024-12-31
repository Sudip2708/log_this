import pytest
from datetime import datetime
import os
from unittest.mock import Mock, patch
from log_this.manager.config.mixins.instance_methods import ExportConfigToFileMixin


# Fixture pro základní instanci mixinu
@pytest.fixture
def config_mixin():
    class TestMixin(ExportConfigToFileMixin):
        def __init__(self):
            self.config = {"test_key": "test_value"}

        def _get_config_file_path(self, filename):
            return os.path.join("/tmp", filename)

        def _save_config_to_file(self, path, config):
            # Simulace uložení konfigurace
            pass

    return TestMixin()


# Test exportu s vlastní cestou
def test_export_config_with_custom_path(config_mixin):
    custom_path = "/tmp/custom_config.json"
    result = config_mixin.export_config_to_file(custom_path)

    assert result == custom_path


# Test exportu s výchozí cestou - s aktuálním datem
def test_export_config_with_default_path(config_mixin):
    with patch('os.getpid') as mock_pid:
        mock_pid.return_value = 12345

        result = config_mixin.export_config_to_file()
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

        expected_filename = f'config_export_{current_time}_12345.json'
        expected_path = os.path.join("/tmp", expected_filename)

        assert result == expected_path


# Test chybového stavu při ukládání
def test_export_config_with_save_error(config_mixin):
    error_message = "Chyba při zápisu"

    # Přepsání metody _save_config_to_file aby vyvolala výjimku
    config_mixin._save_config_to_file = Mock(
        side_effect=Exception(error_message))

    with pytest.raises(Exception) as exc_info:
        config_mixin.export_config_to_file()

    assert str(exc_info.value) == error_message


# Test logování při chybě
def test_export_config_logs_error(config_mixin):
    with patch('logging.error') as mock_logging:
        error_message = "Testovací chyba"
        config_mixin._save_config_to_file = Mock(
            side_effect=Exception(error_message))

        with pytest.raises(Exception):
            config_mixin.export_config_to_file()

        mock_logging.assert_called_once()
        assert error_message in mock_logging.call_args[0][0]