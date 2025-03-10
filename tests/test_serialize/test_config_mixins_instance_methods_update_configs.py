import pytest
from unittest.mock import Mock, patch

from log_this_old.manager.config.init_mixins.instance_methods2 import UpdateConfigsMixin


# Fixture pro základní instanci mixinu
@pytest.fixture
def config_mixin():
    class TestMixin(UpdateConfigsMixin):
        def __init__(self):
            self.config = {
                "setting1": "default1",
                "setting2": True,
                "setting3": 42
            }

        def _validate_config_dict(self, config):
            # Bude mockováno v testech
            pass

        def _get_config_file_path(self):
            return "/tmp/config.json"

        def _save_config_to_file(self, path, config):
            # Bude mockováno v testech
            pass

    return TestMixin()


# Test úspěšné aktualizace více hodnot
def test_successful_multiple_updates(config_mixin):
    updates = {
        "setting1": "new_value1",
        "setting2": False,
        "setting3": 100
    }

    config_mixin._validate_config_dict = Mock(return_value=True)
    config_mixin._save_config_to_file = Mock()

    with patch('logging.info') as mock_logging:
        config_mixin.update_configs(updates)

        # Ověření aktualizace všech hodnot
        assert config_mixin.config["setting1"] == "new_value1"
        assert config_mixin.config["setting2"] is False
        assert config_mixin.config["setting3"] == 100

        # Ověření volání save
        config_mixin._save_config_to_file.assert_called_once_with(
            "/tmp/config.json",
            config_mixin.config
        )

        # Ověření logování
        mock_logging.assert_called_once()
        log_message = mock_logging.call_args[0][0]
        assert "Aktualizovány konfigurace" in log_message
        assert all(key in log_message for key in updates.keys())


# Test neúspěšné validace
def test_failed_validation(config_mixin):
    original_config = config_mixin.config.copy()
    updates = {"setting1": "new_value", "setting2": "invalid_bool"}

    config_mixin._validate_config_dict = Mock(return_value=False)
    config_mixin._save_config_to_file = Mock()

    with patch('logging.error') as mock_logging:
        config_mixin.update_configs(updates)

        # Ověření, že konfigurace zůstala nezměněná
        assert config_mixin.config == original_config

        # Ověření, že save nebyl volán
        config_mixin._save_config_to_file.assert_not_called()

        # Ověření logování chyby
        mock_logging.assert_called_once()
        assert "nezdařila" in mock_logging.call_args[0][0]


# Test aktualizace prázdného slovníku
def test_empty_updates(config_mixin):
    original_config = config_mixin.config.copy()

    config_mixin._validate_config_dict = Mock(return_value=True)
    config_mixin._save_config_to_file = Mock()

    with patch('logging.info') as mock_logging:
        config_mixin.update_configs({})

        # Ověření, že konfigurace zůstala nezměněná
        assert config_mixin.config == original_config

        # Ověření logování
        mock_logging.assert_called_once()
        assert "[]" in mock_logging.call_args[0][0]


# Test částečné aktualizace
def test_partial_update(config_mixin):
    updates = {"setting1": "new_value1"}
    original_setting2 = config_mixin.config["setting2"]
    original_setting3 = config_mixin.config["setting3"]

    config_mixin._validate_config_dict = Mock(return_value=True)
    config_mixin._save_config_to_file = Mock()

    config_mixin.update_configs(updates)

    # Ověření, že se změnil pouze setting1
    assert config_mixin.config["setting1"] == "new_value1"
    assert config_mixin.config["setting2"] == original_setting2
    assert config_mixin.config["setting3"] == original_setting3


# Test zachování typu hodnot
@pytest.mark.parametrize("updates", [
    {"setting1": "str", "setting2": True, "setting3": 42},
    {"setting1": "test", "setting2": False, "setting3": 0},
    {"setting1": "", "setting2": True, "setting3": -1}
])
def test_value_types_preservation(config_mixin, updates):
    config_mixin._validate_config_dict = Mock(return_value=True)
    config_mixin._save_config_to_file = Mock()

    config_mixin.update_configs(updates)

    # Ověření typů hodnot
    assert isinstance(config_mixin.config["setting1"], str)
    assert isinstance(config_mixin.config["setting2"], bool)
    assert isinstance(config_mixin.config["setting3"], int)