import json
import logging
import os
import pytest
from unittest.mock import patch, mock_open
from log_this.manager.config.mixins.static_methods._read_config_file import ReadConfigFileMixin


@pytest.fixture
def read_config_file():
    """Fixture, která vrací metodu _read_config_file pro použití v testech."""
    return ReadConfigFileMixin._read_config_file


def test_read_config_file_valid_path(read_config_file):
    """Testuje načtení validního souboru s konfigurací."""
    mock_data = {"key": "value"}
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("logging.info") as mock_log:
            result = read_config_file("valid_path.json")
            assert result == mock_data
            mock_log.assert_called_once_with(
                "Configuration has been loaded from: "
                "valid_path.json"
            )

def test_read_config_file_file_not_found(read_config_file):
    """Testuje situaci, kdy soubor neexistuje."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with patch("logging.error") as mock_log:
            result = read_config_file("missing_file.json")
            assert result is False
            mock_log.assert_called_once_with(
                "Error: The file path does not exist: "
                "FileNotFoundError()"
            )


def test_read_config_file_permission_error(read_config_file):
    """Testuje situaci, kdy nejsou dostatečná oprávnění k souboru."""
    with patch("builtins.open", side_effect=PermissionError):
        with patch("logging.error") as mock_log:
            result = read_config_file("protected_file.json")
            assert result is False
            mock_log.assert_called_once_with(
                "Error: Insufficient permissions to access the file: "
                "PermissionError()"
            )


def test_read_config_file_type_error(read_config_file):
    """Testuje situaci, kdy data nejsou serializovatelná do JSON."""
    with patch("builtins.open", mock_open(read_data="invalid_json")):
        with patch("json.load", side_effect=TypeError):
            with patch("logging.error") as mock_log:
                result = read_config_file("invalid_data.json")
                assert result is False
                mock_log.assert_called_once_with(
                    "Error: Configuration data is not JSON serializable: "
                    "TypeError()"
                )


def test_read_config_file_json_decode_error(read_config_file):
    """Testuje situaci, kdy JSON není validní."""
    with patch("builtins.open", mock_open(read_data="invalid_json")):
        with patch("json.load", side_effect=json.JSONDecodeError(
                "msg", "doc", 0)):
            with patch("logging.error") as mock_log:
                result = read_config_file("invalid_json.json")
                assert result is False
                mock_log.assert_called_once_with(
                    "Error during JSON deserialization: "
                    "msg: line 1 column 1 (char 0)"
                )


def test_read_config_file_os_error(read_config_file):
    """Testuje obecnou chybu OS při práci se souborem."""
    with patch("builtins.open", side_effect=OSError):
        with patch("logging.error") as mock_log:
            result = read_config_file("os_error_file.json")
            assert result is False
            mock_log.assert_called_once_with(
                "Error while working with the file: "
                "OSError()"
            )


def test_read_config_file_unknown_error(read_config_file):
    """Testuje zachycení neznámé výjimky."""
    with patch("builtins.open", side_effect=Exception("Unknown error")):
        with patch("logging.error") as mock_log:
            result = read_config_file("unknown_error.json")
            assert result is False
            mock_log.assert_called_once_with(
                "Unknown error occurred while reading the file: "
                "Exception(Unknown error)"
            )
