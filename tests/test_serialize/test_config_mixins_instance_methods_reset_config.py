import pytest
from unittest.mock import Mock, patch
from log_this.manager.config.init_mixins.instance_methods2 import ResetConfigMixin


# Fixture pro základní instanci mixinu
@pytest.fixture
def config_mixin():
    class TestMixin(ResetConfigMixin):
        def __init__(self):
            self.DEFAULTS = {
                "setting1": "default1",
                "setting2": True,
                "setting3": 42
            }
            self.config = {
                "setting1": "custom1",
                "setting2": False,
                "setting3": 100
            }

        def _get_config_file_path(self):
            return "/tmp/config.json"

        def _save_config_to_file(self, path, config):
            # Bude mockováno v testech
            pass

        def _load_default_config(self):
            # Bude mockováno v testech
            pass

    return TestMixin()


# Test úspěšného resetu konfigurace
def test_successful_reset(config_mixin):
    config_mixin._save_config_to_file = Mock(return_value=True)

    with patch('logging.info') as mock_logging:
        config_mixin.reset_config()

        # Ověření, že konfigurace byla resetována na výchozí hodnoty
        assert config_mixin.config == config_mixin.DEFAULTS
        assert config_mixin.config is not config_mixin.DEFAULTS  # Ověření, že jde o kopii

        # Ověření, že byla volána metoda pro uložení
        config_mixin._save_config_to_file.assert_called_once_with(
            "/tmp/config.json",
            config_mixin.DEFAULTS
        )

        # Ověření logování
        mock_logging.assert_called_once_with(
            "Konfigurace byla resetována na výchozí hodnoty."
        )


# Test neúspěšného uložení a obnovení původní konfigurace
def test_failed_save_and_restore(config_mixin):
    config_mixin._save_config_to_file = Mock(return_value=False)
    config_mixin._load_default_config = Mock()

    with patch('logging.info') as mock_logging:
        config_mixin.reset_config()

        # Ověření volání metod
        config_mixin._save_config_to_file.assert_called_once()
        config_mixin._load_default_config.assert_called_once()

        # Ověření logování
        mock_logging.assert_called_once()


# Test zachování správné cesty k souboru
def test_correct_file_path(config_mixin):
    mock_path = "/tmp/config.json"
    config_mixin._get_config_file_path = Mock(return_value=mock_path)
    config_mixin._save_config_to_file = Mock(return_value=True)

    config_mixin.reset_config()

    config_mixin._save_config_to_file.assert_called_once_with(
        mock_path,
        config_mixin.config
    )


# Test izolace výchozí konfigurace
def test_defaults_isolation(config_mixin):
    original_defaults = config_mixin.DEFAULTS.copy()
    config_mixin._save_config_to_file = Mock(return_value=True)

    config_mixin.reset_config()
    config_mixin.config["setting1"] = "modified"

    # Ověření, že modifikace config neovlivnila DEFAULTS
    assert config_mixin.DEFAULTS == original_defaults