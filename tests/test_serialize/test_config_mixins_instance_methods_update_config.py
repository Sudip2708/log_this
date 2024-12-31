import pytest
from unittest.mock import Mock, patch

from log_this.manager.config.mixins.instance_methods import UpdateConfigMixin


# Fixture pro základní instanci mixinu
@pytest.fixture
def config_mixin():
    class TestMixin(UpdateConfigMixin):
        def __init__(self):
            self.DEFAULTS = {
                "setting1": "default1",
                "setting2": True,
                "setting3": 42,
                "max_depth": 10
            }
            self.config = self.DEFAULTS.copy()

        def _key_and_value_check(self, key, value):
            # Bude mockováno v testech
            pass

        def _get_config_file_path(self):
            return "/tmp/config.json"

        def _save_config_to_file(self, path, config):
            # Bude mockováno v testech
            pass

        def _load_default_config(self):
            # Bude mockováno v testech
            pass

    return TestMixin()


# Test úspěšné aktualizace konfigurace
def test_successful_update(config_mixin):
    config_mixin._key_and_value_check = Mock()
    config_mixin._save_config_to_file = Mock(return_value=True)

    with patch('logging.info') as mock_logging:
        config_mixin.update_config("setting1", "new_value")

        # Ověření změny konfigurace
        assert config_mixin.config["setting1"] == "new_value"

        # Ověření volání metod
        config_mixin._key_and_value_check.assert_called_once_with("setting1",
                                                                  "new_value")
        config_mixin._save_config_to_file.assert_called_once_with(
            "/tmp/config.json",
            config_mixin.config
        )

        # Ověření logování
        mock_logging.assert_called_once()
        assert "setting1" in mock_logging.call_args[0][0]
        assert "new_value" in mock_logging.call_args[0][0]


# Test neúspěšného uložení a obnovení konfigurace
def test_failed_save_and_restore(config_mixin):
    original_config = config_mixin.config.copy()

    config_mixin._key_and_value_check = Mock()
    config_mixin._save_config_to_file = Mock(return_value=False)
    config_mixin._load_default_config = Mock()

    config_mixin.update_config("setting1", "new_value")

    # Ověření volání metod
    config_mixin._load_default_config.assert_called_once()


# Test kontroly klíče a hodnoty
def test_key_and_value_validation(config_mixin):
    config_mixin._key_and_value_check = Mock(
        side_effect=ValueError("Neplatná hodnota"))
    config_mixin._save_config_to_file = Mock()

    with pytest.raises(ValueError) as exc_info:
        config_mixin.update_config("setting1", "invalid_value")

    assert "Neplatná hodnota" in str(exc_info.value)
    config_mixin._save_config_to_file.assert_not_called()


# Test speciální logiky pro max_depth
def test_max_depth_update(config_mixin):
    mock_serializer = Mock()

    config_mixin._key_and_value_check = Mock()
    config_mixin._save_config_to_file = Mock(return_value=True)

    with patch('log_this.manager.serializer.get_serializer',
               return_value=mock_serializer):
        config_mixin.update_config("max_depth", 5)

        # Ověření nastavení hodnoty v serializeru
        assert mock_serializer.max_depth == 5


# Test aktualizace s různými typy hodnot
@pytest.mark.parametrize("key,value", [
    ("setting1", "string_value"),
    ("setting2", True),
    ("setting3", 42)
])
def test_update_with_different_types(config_mixin, key, value):
    config_mixin._key_and_value_check = Mock()
    config_mixin._save_config_to_file = Mock(return_value=True)

    config_mixin.update_config(key, value)

    assert config_mixin.config[key] == value


# Test zachování ostatních hodnot při aktualizaci
def test_other_values_preservation(config_mixin):
    original_config = config_mixin.config.copy()
    config_mixin._key_and_value_check = Mock()
    config_mixin._save_config_to_file = Mock(return_value=True)

    config_mixin.update_config("setting1", "new_value")

    # Ověření, že ostatní hodnoty zůstaly nezměněné
    for key in original_config:
        if key != "setting1":
            assert config_mixin.config[key] == original_config[key]