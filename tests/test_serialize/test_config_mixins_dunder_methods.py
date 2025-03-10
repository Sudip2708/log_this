import pytest
from log_this_old.manager.config.init_mixins.dunder_methods import GetItemMixin
from log_this_old.manager.config.init_mixins.dunder_methods import StrMixin


# Mockovaná základní třída pro testování
class MockConfig(GetItemMixin, StrMixin):
    def __init__(self, config):
        self.config = config


# Testy pro GetItemMixin
def test_getitem_existing_key():
    """Testuje vrácení hodnoty pro existující klíč."""
    obj = MockConfig({"key": "value"})
    assert obj["key"] == "value"


def test_getitem_non_existing_key():
    """Testuje vrácení None pro neexistující klíč."""
    obj = MockConfig({})
    assert obj["missing"] is None


def test_getitem_true_key():
    """Testuje podporu klíče True (převedeného na 'true')."""
    obj = MockConfig({"true": "value"})
    assert obj[True] == "value"


def test_getitem_false_key():
    """Testuje podporu klíče False (převedeného na 'false')."""
    obj = MockConfig({"false": "value"})
    assert obj[False] == "value"


def test_getitem_none_key():
    """Testuje podporu klíče None (převedeného na 'none')."""
    obj = MockConfig({"none": "value"})
    assert obj[None] == "value"


# Testy pro StrMixin
def test_str_with_empty_config():
    """Testuje výstup pro prázdnou konfiguraci."""
    obj = MockConfig({})
    assert str(obj) == "LogThisConfig:\n"


def test_str_with_single_item():
    """Testuje výstup s jednou položkou v konfiguraci."""
    obj = MockConfig({"key": "value"})
    expected = "LogThisConfig:\nkey: value"
    assert str(obj) == expected


def test_str_with_multiple_items():
    """Testuje výstup s více položkami v konfiguraci."""
    obj = MockConfig({"key1": "value1", "key2": "value2"})
    expected = "LogThisConfig:\nkey1: value1\nkey2: value2"
    assert str(obj) == expected


