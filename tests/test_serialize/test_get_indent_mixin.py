import pytest
from unittest.mock import Mock
from log_this_old.manager.methods._get_indent_mixin import GetIndentMethodMixins


@pytest.fixture
def mock_thread():
    """Provides mocked thread object."""
    thread = Mock()
    thread.current_depth = 2
    return thread


@pytest.fixture
def mock_config():
    """Provides mocked config dictionary."""
    return {"indent": 4}


@pytest.fixture
def indent_handler(mock_config, mock_thread):
    """Provides configured indent handler instance."""
    class TestHandler(GetIndentMethodMixins):
        def __init__(self):
            self.config = mock_config
            self.thread = mock_thread
    return TestHandler()


def test_no_indent(mock_config, indent_handler):
    """Tests behavior when indent is 0."""
    mock_config["indent"] = 0
    assert indent_handler.get_indent() == ""


def test_no_indent_config_missing(mock_config, indent_handler):
    """Tests behavior when indent config is missing."""
    mock_config["indent"] = None
    assert indent_handler.get_indent() == ""


def test_basic_indent(indent_handler):
    """Tests basic indentation calculation."""
    assert indent_handler.get_indent() == " " * 8  # 4 spaces * depth 2


def test_different_depth(mock_thread, indent_handler):
    """Tests indentation with varying depths."""
    mock_thread.current_depth = 3
    assert indent_handler.get_indent() == " " * 12

    mock_thread.current_depth = 0
    assert indent_handler.get_indent() == ""


def test_different_indent_size(mock_config, indent_handler):
    """Tests different indentation sizes."""
    mock_config["indent"] = 2
    assert indent_handler.get_indent() == " " * 4  # 2 spaces * depth 2


def test_large_values(mock_config, mock_thread, indent_handler):
    """Tests behavior with large values."""
    mock_config["indent"] = 10
    mock_thread.current_depth = 5
    assert indent_handler.get_indent() == " " * 50