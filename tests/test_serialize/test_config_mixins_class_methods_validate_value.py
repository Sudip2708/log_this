import pytest
from log_this_old.manager.config.init_mixins.class_methods import ValidateValueMixin


@pytest.fixture
def validate_value():
    """Fixture providing the validation method."""
    return ValidateValueMixin._validate_value


@pytest.mark.parametrize("value", [True, False])
def test_validate_value_blank_lines_valid(validate_value, value):
    """Test platnosti hodnoty pro klíč 'blank_lines'."""
    assert validate_value("blank_lines", value) is True


@pytest.mark.parametrize("value", [None, -1, 0, 1, 1.1, "all"])
def test_validate_value_blank_lines_invalid(validate_value, value):
    """Test neplatnosti hodnoty pro klíč 'blank_lines'."""
    assert validate_value("blank_lines", value) is False


@pytest.mark.parametrize("value", ["all", 0, 1, 2, 5, 100])
def test_validate_value_docstring_lines_valid(validate_value, value):
    """Test platnosti hodnoty pro klíč 'docstring_lines'."""
    assert validate_value("docstring_lines", value) is True


@pytest.mark.parametrize("value", [True, False, None, "", -1, 1.1])
def test_validate_value_docstring_lines_invalid(validate_value, value):
    """Test neplatnosti hodnoty pro klíč 'docstring_lines'."""
    assert validate_value("docstring_lines", value) is False


@pytest.mark.parametrize("value", [0, 1, 2, 100])
def test_validate_value_max_depth_valid(validate_value, value):
    """Test platnosti hodnoty pro klíč 'max_depth'."""
    assert validate_value("max_depth", value) is True


@pytest.mark.parametrize("value", [True, False, None, "", "all",  -1, 1.1])
def test_validate_value_max_depth_invalid(validate_value, value):
    """Test neplatnosti hodnoty pro klíč 'max_depth'."""
    assert validate_value("max_depth", value) is False


@pytest.mark.parametrize("value", [0, 1, 2, 3, 4])
def test_validate_value_skip_this_valid(validate_value, value):
    """Test platnosti hodnoty pro klíč 'skip_this'."""
    assert validate_value("skip_this", value) is True


@pytest.mark.parametrize("value", [
    True, False, None, "", "all",  -1, 5, 100, 1.1])
def test_validate_value_skip_this_invalid(validate_value, value):
    """Test neplatnosti hodnoty pro klíč 'skip_this'."""
    assert validate_value("skip_this", value) is False


@pytest.mark.parametrize("keys", [
    'one_line', 'simple', 'detailed', 'report',
    'true', 'false', 'none', 'empty', 'indent'])
def test_validate_value_test_rest_keys(validate_value, keys):
    """
    Test platnosti hodnoty pro všechny ostatní klíče.

    Tyto klíče mají stejné spracování jako klíč 'skip_this'.
    """
    assert validate_value(keys, 0) is True


def test_validate_value_unknown_key(validate_value):
    """Test neplatnosti hodnoty pro neznámý klíč."""
    assert validate_value("unknown_key", 1) is False
