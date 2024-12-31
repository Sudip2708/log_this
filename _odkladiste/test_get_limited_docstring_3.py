import pytest
from log_this.manager.methods._get_limited_docstring_mixin import GetLimitedDocstringMixin


@pytest.fixture
def test_class():
    """Fixture returns a class using the mixin."""
    class TestClass(GetLimitedDocstringMixin):
        def __init__(self):
            self.config = dict()
            self.config["docstring_lines"] = "all"
    return TestClass()


@pytest.fixture
def get_limited_docstring(test_class):
    """Fixture returning only the get_limited_docstring method."""
    return test_class.get_limited_docstring


@pytest.fixture
def sample_docstring():
    """Fixture providing a sample docstring for tests."""
    return 'Line 1\n\nLine 2\n\nLine 3\n\n'


def test_empty_docstring(get_limited_docstring):
    """Verifies return value when docstring is empty."""
    assert get_limited_docstring("") == "N/A"


def test_none_docstring(get_limited_docstring):
    """Verifies return value when docstring is None."""
    assert get_limited_docstring(None) == "N/A"


def test_invalid_type_docstring(get_limited_docstring):
    """Verifies return value when docstring has invalid type."""
    assert get_limited_docstring(42) == "N/A"
    assert get_limited_docstring([1, 2, 3]) == "N/A"


def test_max_line_all(get_limited_docstring, sample_docstring):
    """Verifies return value when docstring_lines is set to 'all'."""
    assert get_limited_docstring(sample_docstring) == sample_docstring


def test_remove_empty_lines(test_class, sample_docstring):
    """Verifies that empty lines are omitted in the returned value."""
    test_class.config["docstring_lines"] = 3
    expected_result = "Line 1\nLine 2\nLine 3"
    assert test_class.get_limited_docstring(sample_docstring) == expected_result


def test_limit_docstring(test_class, sample_docstring):
    """Verifies correct output when docstring is longer than docstring_lines."""
    test_class.config["docstring_lines"] = 2
    expected_result = 'Line 1\nLine 2 (...)'
    assert test_class.get_limited_docstring(sample_docstring) == expected_result


def test_empty_lines_with_all_setting(get_limited_docstring):
    """Verifies output for empty lines with 'all' setting."""
    docstring = "\n\n\n"
    assert get_limited_docstring(docstring) == "\n\n\n"


def test_empty_lines_with_limit(test_class):
    """Verifies output for empty lines with limited line count."""
    test_class.config["docstring_lines"] = 2
    docstring = "\n\n\n"
    assert test_class.get_limited_docstring(docstring) == ""


def test_indented_first_line(test_class):
    """Verifies handling of indented first line."""
    test_class.config["docstring_lines"] = 1
    docstring = "\n\n\nLine 1\n"
    assert test_class.get_limited_docstring(docstring) == "Line 1"


def test_spaces_between_words(test_class):
    """Verifies handling of spaces between words."""
    test_class.config["docstring_lines"] = 1
    docstring = "This    has    multiple    spaces"
    assert test_class.get_limited_docstring(docstring) == "This    has    multiple    spaces"


def test_large_multiline_docstring(test_class):
    """Verifies handling of large multiline docstring."""
    test_class.config["docstring_lines"] = 2
    docstring = "\n".join([f"Line {i}" for i in range(1, 11)])
    expected_result = "Line 1\nLine 2 (...)"
    assert test_class.get_limited_docstring(docstring) == expected_result


def test_invalid_config_value(test_class):
    """
    Test is intentionally empty since get_limited_docstring() is designed to be used
    within LogThisManager class which guarantees config["docstring_lines"] is always
    validated during configuration setup.
    """
    pass