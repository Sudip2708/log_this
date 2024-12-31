import pytest
from log_this.manager.config.mixins.class_methods import KeyAndValueCheckMixin


class MockConfigClass(KeyAndValueCheckMixin):
    DEFAULTS = {
        "key1": int,
        "key2": str,
        "key3": bool,
    }

    @classmethod
    def _validate_value(cls, key, value):
        """Mock validace hodnoty na základě typu v DEFAULTS."""
        expected_type = cls.DEFAULTS.get(key)
        return isinstance(value, expected_type)


@pytest.fixture
def check_invalid_value():
    """Fixture pro ověření ValueError"""
    def _check_invalid_value(key, value):
        with pytest.raises(ValueError, match=f"Neplatná hodnota pro {key}: {value}"):
            MockConfigClass._key_and_value_check(key, value)
    return _check_invalid_value


def test_valid_key_and_value():
    """Test úspěšného ověření klíče a hodnoty."""
    MockConfigClass._key_and_value_check("key1", 42)
    MockConfigClass._key_and_value_check("key2", "valid string")
    MockConfigClass._key_and_value_check("key3", True)
    # Pokud metoda nezvedne výjimku, test je úspěšný.


def test_valid_edge_cases():
    """Test hraničních hodnot pro validní klíče a hodnoty."""
    MockConfigClass._key_and_value_check("key1", 0)  # Int ok
    MockConfigClass._key_and_value_check("key2", "")  # Prázdný string je validní
    MockConfigClass._key_and_value_check("key3", False)  # Bool ok


def test_invalid_key():
    """Test vyvolání KeyError pro neznámý klíč."""
    with pytest.raises(KeyError, match="Neznámý klíč konfigurace: invalid_key"):
        MockConfigClass._key_and_value_check("invalid_key", 42)


def test_invalid_value_type(check_invalid_value):
    """Test vyvolání ValueError pro neplatnou hodnotu."""
    check_invalid_value("key1", "invalid")  # Měl by být `int`, ale je `str`
    check_invalid_value("key3", 123)  # Měl by být `bool`, ale je `int`


def test_invalid_edge_cases(check_invalid_value):
    """Test hraničních hodnot pro neplatné hodnoty."""
    check_invalid_value("key1", -1.1)  # Pokud by validace nepřijímala záporné hodnoty
    check_invalid_value("key2", None)  # None není `str`
    check_invalid_value("key3", None)  # None není `bool`
