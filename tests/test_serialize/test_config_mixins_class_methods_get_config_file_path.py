import pytest
from pathlib import Path

from log_this.manager.config.mixins.class_methods import GetConfigFilePathMixin

class MockConfigClass(GetConfigFilePathMixin):
    # Mockovaný atribut pro testování (upravený aby zobrazoval cestu ve formátu dle operačního systému)
    _config_dir = Path("/mock/config/dir")


def test_get_config_file_path_default():
    """Ověří, že metoda vrací správnou cestu při použití výchozího názvu souboru."""
    result = MockConfigClass._get_config_file_path()
    expected_path = Path("/mock/config/dir/config.json")
    assert result == expected_path


def test_custom_file_name_with_json():
    """Ověření, že uživatelem zadané jméno s příponou .json je správně zpracováno."""
    result = MockConfigClass._get_config_file_path("custom_file.json")
    expected_path = Path("/mock/config/dir/custom_file.json")
    assert result == expected_path


def test_custom_file_name_without_json():
    """Ověření, že přípona .json je automaticky přidána, pokud chybí."""
    result = MockConfigClass._get_config_file_path("custom_file")
    expected_path = Path("/mock/config/dir/custom_file.json")
    assert result == expected_path


def test_invalid_file_name_type():
    """Ověření, že metoda vyvolá výjimku při neplatném typu `file_name`."""
    with pytest.raises(ValueError, match="Argument `file_name` musí být typu `str`"):
        MockConfigClass._get_config_file_path(123)


def test_get_config_file_path_missing_config_dir():
    """Ověří chování metody, pokud _config_dir není definováno."""
    class IncompleteConfigClass(GetConfigFilePathMixin):
        pass

    with pytest.raises(AttributeError):
        IncompleteConfigClass._get_config_file_path()


def test_invalid_config_dir():
    """Ověří chování metody, pokud _config_dir není typu Path nebo str."""

    class InvalidConfigClass(GetConfigFilePathMixin):
        _config_dir = 123  # Nevalidní hodnota

    with pytest.raises(TypeError):
        InvalidConfigClass._get_config_file_path()


def test_config_dir_with_trailing_slash():
    """Ověří správné zpracování cesty s koncovým lomítkem."""

    class ConfigWithSlash(GetConfigFilePathMixin):
        _config_dir = "/mock/config/dir/"  # Koncové lomítko

    result = ConfigWithSlash._get_config_file_path()
    expected_path = Path("/mock/config/dir/config.json")
    assert result == expected_path

