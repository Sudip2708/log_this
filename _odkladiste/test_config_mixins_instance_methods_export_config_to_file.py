import os
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from log_this.manager.config.mixins.instance_methods2._export_config_to_file import ExportConfigToFileMixin


@pytest.fixture
def export_config_to_file():
    """Fixture vrací instanci třídy ExportConfigToFileMixin pro použití v testech."""
    return ExportConfigToFileMixin.export_config_to_file


def test_export_config_to_file_with_default_path(export_config):
    """Testuje export konfigurace s výchozí cestou a jménem souboru."""
    # Mockování metod
    with patch.object(export_config, '_get_config_file_path',
                      return_value='/mock/path/config_export_20241229_123456_1234.json'):
        with patch.object(export_config, '_save_config_to_file') as mock_save_config:
            export_path = export_config.export_config_to_file()

            # Kontrola volání metody pro získání cesty
            export_config._get_config_file_path.assert_called_once()

            # Ověření, že cesta k souboru je správná
            assert export_path == '/mock/path/config_export_20241229_123456_1234.json'

            # Ověření, že konfigurace byla uložena
            mock_save_config.assert_called_once_with(export_path, export_config.config)


def test_export_config_to_file_with_custom_path(export_config):
    """Testuje export konfigurace s vlastní cestou pro export."""
    custom_path = '/mock/path/custom_export.json'

    # Mockování metod
    with patch.object(export_config, '_save_config_to_file') as mock_save_config:
        export_path = export_config.export_config_to_file(export_path=custom_path)

        # Ověření, že metoda pro export použila vlastní cestu
        assert export_path == custom_path

        # Ověření, že konfigurace byla uložena na vlastní cestu
        mock_save_config.assert_called_once_with(custom_path, export_config.config)


def test_export_config_to_file_error(export_config):
    """Testuje selhání při exportu konfigurace."""
    # Mockování metod
    with patch.object(export_config, '_get_config_file_path',
                      return_value='/mock/path/config_export_error.json'):
        with patch.object(export_config, '_save_config_to_file',
                          side_effect=Exception("Export failed")):
            with patch("logging.error") as mock_log:
                # Pokusíme se o export a očekáváme, že bude vyhozena výjimka
                with pytest.raises(Exception, match="Export failed"):
                    export_config.export_config_to_file()

                # Ověření, že došlo k logování chyby
                mock_log.assert_called_once_with('Chyba při exportu konfigurace: Export failed')
