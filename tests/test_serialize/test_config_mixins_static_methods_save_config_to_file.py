import json
import logging
import os
import pytest
from unittest.mock import patch, mock_open
from log_this.manager.config.mixins.static_methods._save_config_to_file import SaveConfigToFileMixin


@pytest.fixture
def save_config_to_file():
    """Fixture that returns the _save_config_to_file method for use in tests."""
    return SaveConfigToFileMixin._save_config_to_file


def test_save_config_to_file_valid_path(save_config_to_file):
    """Tests saving a valid configuration file."""
    mock_data = {"key": "value"}
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("logging.info") as mock_log:
            result = save_config_to_file("valid_path.json", mock_data)
            mock_file.assert_called_once_with("valid_path.json", 'w')
            mock_log.assert_called_once_with(
                "Configuration has been saved to: valid_path.json"
            )
            assert result is True


def test_save_config_to_file_file_not_found(save_config_to_file):
    """Tests when the file path does not exist."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with patch("logging.error") as mock_log:
            result = save_config_to_file("missing_file.json", {"key": "value"})
            assert result is False
            mock_log.assert_called_once_with(
                "Error: The file path does not exist: FileNotFoundError()"
            )


def test_save_config_to_file_permission_error(save_config_to_file):
    """Tests when there are insufficient permissions to access the file."""
    with patch("builtins.open", side_effect=PermissionError):
        with patch("logging.error") as mock_log:
            result = save_config_to_file("protected_file.json", {"key": "value"})
            assert result is False
            mock_log.assert_called_once_with(
                "Error: Insufficient permissions to access the file: PermissionError()"
            )


def test_save_config_to_file_type_error(save_config_to_file):
    """Tests when data is not JSON serializable."""
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("json.dump", side_effect=TypeError):
            with patch("logging.error") as mock_log:
                result = save_config_to_file("invalid_data.json", {"key": "value"})
                assert result is False
                mock_log.assert_called_once_with(
                    "Error: Configuration data is not JSON serializable: TypeError()"
                )


def test_save_config_to_file_json_decode_error(save_config_to_file):
    """Tests when there is an error during JSON serialization."""
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("json.dump", side_effect=json.JSONDecodeError(
                "msg", "doc", 0)):
            with patch("logging.error") as mock_log:
                result = save_config_to_file("invalid_json.json", {"key": "value"})
                assert result is False
                mock_log.assert_called_once_with(
                    "Error during JSON deserialization: msg: line 1 column 1 (char 0)"
                )


def test_save_config_to_file_os_error(save_config_to_file):
    """Tests general OS errors when working with the file."""
    with patch("builtins.open", side_effect=OSError):
        with patch("logging.error") as mock_log:
            result = save_config_to_file("os_error_file.json", {"key": "value"})
            assert result is False
            mock_log.assert_called_once_with(
                "Error while working with the file: OSError()"
            )


def test_save_config_to_file_unknown_error(save_config_to_file):
    """Tests capturing an unknown exception."""
    with patch("builtins.open", side_effect=Exception("Unknown error")):
        with patch("logging.error") as mock_log:
            result = save_config_to_file("unknown_error.json", {"key": "value"})
            assert result is False
            mock_log.assert_called_once_with(
                "Unknown error occurred while reading the file: Exception(Unknown error)"
            )
