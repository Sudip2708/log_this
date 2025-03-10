import pytest
from log_this_old.manager.config import get_config
from log_this_old.manager.config._config_base import LogThisConfig
import os
import inspect

@pytest.fixture
def config_instance():
    """Fixture that create the singleton instance for config."""
    return get_config()


def test_singleton_initialisation(config_instance):
    """Test that get_config() consistently returns the same singleton instance"""
    config_instance1 = config_instance
    config_instance2 = get_config()
    assert config_instance1 is config_instance2


def test_default_attributes_presence(config_instance):
    """Test that config instance  is properly initialized"""
    assert hasattr(config_instance, '_instance')
    assert hasattr(config_instance, '_config_dir')
    assert hasattr(config_instance, 'config')
    assert hasattr(config_instance, '_initialized')


def test_default_attributes_values(config_instance):
    """Verify that config instance is initialized with correct default values"""
    assert config_instance._instance == config_instance
    assert isinstance(config_instance.config, dict)
    assert config_instance._initialized == True


def test_config_directory_path(config_instance):
    """Ověří správnost cesty k složce pro soubor pro ukládání konfiguračních hodnot"""
    config_file_path = inspect.getfile(LogThisConfig)
    config_directory_path = os.path.dirname(config_file_path)
    assert config_instance._config_dir == config_directory_path


def test_default_config_key_presence(config_instance):
    """Test že konfig obsahuje všechny defaultní klíče"""
    assert "skip_this" in config_instance.config
    assert "one_line" in config_instance.config
    assert "simple" in config_instance.config
    assert "detailed" in config_instance.config
    assert "report" in config_instance.config
    assert "true" in config_instance.config
    assert "false" in config_instance.config
    assert "none" in config_instance.config
    assert "empty" in config_instance.config
    assert "indent" in config_instance.config
    assert "blank_lines" in config_instance.config
    assert "docstring_lines" in config_instance.config


def test_default_config_key_values(config_instance):
    """Verify that konfig obsahujeke všm klíčů, správné defaultní hodnoty"""
    assert config_instance.config["skip_this"] is 0
    assert config_instance.config["one_line"] is 1
    assert config_instance.config["simple"] is 2
    assert config_instance.config["detailed"] is 3
    assert config_instance.config["report"] is 4
    assert config_instance.config["true"] is 1
    assert config_instance.config["false"] is 0
    assert config_instance.config["none"] is 0
    assert config_instance.config["empty"] is 0
    assert config_instance.config["indent"] is 2
    assert config_instance.config["blank_lines"] is True
    assert config_instance.config["docstring_lines"] is 3
    assert config_instance.config["max_depth"] is 100