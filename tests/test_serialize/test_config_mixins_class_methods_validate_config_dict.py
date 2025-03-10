import pytest
from typing import Dict, Any
from unittest.mock import patch
from log_this_old.manager.config.init_mixins.class_methods import ValidateConfigDictMixin


class MockConfigClass(ValidateConfigDictMixin):
    DEFAULTS = {
        "key1": int,
        "key2": str,
        "key3": bool,
    }

    @classmethod
    def _key_and_value_check(cls, key: str, value: Any) -> None:
        """Mock metoda pro kontrolu klíče a hodnoty."""
        if key not in cls.DEFAULTS:
            raise KeyError(f"Neplatný klíč: {key}")

        expected_type = cls.DEFAULTS[key]
        if not isinstance(value, expected_type):
            raise ValueError(f"Neplatná hodnota pro klíč {key}: {value}")


def test_validate_config_valid_dict():
    """Test úspěšné validace slovníku."""
    config = {"key1": 42, "key2": "value", "key3": True}
    assert MockConfigClass._validate_config_dict(config) is True


def test_validate_config_invalid_key():
    """Test nevalidního klíče ve slovníku."""
    config = {"invalid_key": 42, "key2": "value", "key3": True}
    with patch("logging.warning") as mock_log:
        assert MockConfigClass._validate_config_dict(config) is False
        mock_log.assert_called_once_with("Neplatný klíč: invalid_key")


def test_validate_config_invalid_value():
    """Test nevalidní hodnoty ve slovníku."""
    config = {"key1": "invalid", "key2": "value", "key3": True}  # `key1` by měl být int
    with patch("logging.warning") as mock_log:
        assert MockConfigClass._validate_config_dict(config) is False
        mock_log.assert_called_once_with("Neplatná hodnota pro klíč: key1: invalid")


def test_validate_config_partial_valid_dict():
    """Test částečně validního slovníku."""
    config = {"key1": 42, "key2": "value", "key3": 123}  # `key3` by měl být bool
    with patch("logging.warning") as mock_log:
        assert MockConfigClass._validate_config_dict(config) is False
        mock_log.assert_called_once_with("Neplatná hodnota pro klíč: key3: 123")


def test_validate_config_empty_dict():
    """Test prázdného slovníku."""
    config = {}
    assert MockConfigClass._validate_config_dict(config) is False


def test_validate_config_logs_on_failure():
    """Test logování při neúspěšné validaci."""
    config = {"key1": 42, "key3": "invalid_value"}  # `key3` by měl být bool
    with patch("logging.warning") as mock_log:
        assert MockConfigClass._validate_config_dict(config) is False
        mock_log.assert_called_once_with("Neplatná hodnota pro klíč: key3: invalid_value")
