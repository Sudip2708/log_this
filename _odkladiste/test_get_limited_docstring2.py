import pytest
from log_this.manager.methods._get_limited_docstring_mixin import GetLimitedDocstringMixin


@pytest.fixture
def test_class():
    """Fixture navrací třídu ve které je použit mixin s metodou."""
    class TestClass(GetLimitedDocstringMixin):
        def __init__(self):
            self.config = dict()
            self.config["docstring_lines"] = "all"
    return TestClass()


@pytest.fixture
def get_limited_docstring(test_class):
    """Fixture vracející pouze metodu get_limited_docstring."""
    return test_class.get_limited_docstring


@pytest.fixture
def sample_docstring():
    """Fixture poskytující ukázkový docstring pro testy."""
    return 'Line 1\n\nLine 2\n\nLine 3\n\n'


def test_if_not_docstring(get_limited_docstring):
    """Ověří navracení hodnoty, když docstring není uveden"""
    assert get_limited_docstring("") == "N/A"


def test_if_docstring_is_None(get_limited_docstring):
    """Ověří navracení hodnoty, když docstring je None"""
    assert get_limited_docstring(None) == "N/A"


def test_max_line_all(get_limited_docstring, sample_docstring):
    """Ověří navracení hodnoty, když docstring_lines má hodnotu 'all'"""
    assert get_limited_docstring(sample_docstring) == sample_docstring


def test_remove_empty_lines(test_class, sample_docstring):
    """Ověří zda se v navrácené hodnotyě vynechávají prázdné řádky."""
    test_class.config["docstring_lines"] = 3
    expected_result = "Line 1\nLine 2\nLine 3"
    assert test_class.get_limited_docstring(sample_docstring) == expected_result


def test_get_limited_docstring(test_class, sample_docstring):
    """Ověření správného výstupu při delším docstringu, než je hodnota docstring_lines"""
    test_class.config["docstring_lines"] = 2
    expected_result = 'Line 1\nLine 2 (...)'
    assert test_class.get_limited_docstring(sample_docstring) == expected_result


def test_for_docstring_with_empty_lines_all(get_limited_docstring):
    """Ověření výstupu pro prázdné řádky při nastavení 'all'."""
    docstring = "\n\n\n"
    assert get_limited_docstring(docstring) == "\n\n\n"


def test_for_docstring_with_empty_lines_limited(test_class):
    """Ověření výstupu pro prázdné řádky při nnastavení omezeného počtu řádků."""
    test_class.config["docstring_lines"] = 2
    docstring = "\n\n\n"
    assert test_class.get_limited_docstring(docstring) == ""


def test_for_docstring_with_indented_first_line(test_class):
    test_class.config["docstring_lines"] = 1
    docstring = "\n\n\nLine 1\n"
    assert test_class.get_limited_docstring(docstring) == "Line 1"
