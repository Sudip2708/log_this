import pytest
from unittest.mock import Mock
from log_this.manager.methods._get_indent_mixin import GetIndentMethodMixins


@pytest.fixture
def test_class():
    """Fixture returns a class using the mixin."""
    class TestClass(GetIndentMethodMixins):
        def __init__(self):
            self.config = dict()
            self.config["indent"] = 0
            self.config["current_depth"] = 0
    return TestClass()

def test_indent_handler_no_indent(test_class):
    """Test chování bez odsazení."""
    test_class.config["current_depth"] = 5
    assert test_class.get_indent() == ""

def test_indent_handler_no_indent():
    """Test chování bez odsazení."""
    mock_config = Mock()
    mock_config.indent = 0
    mock_thread_context = Mock()
    mock_thread_context.thread.current_depth = 5

    handler = IndentHandler(mock_config, mock_thread_context)
    assert handler.get_indent() == ""


def test_indent_handler_with_indent():
    """Test generování odsazení."""
    mock_config = Mock()
    mock_config.indent = 2
    mock_thread_context = Mock()
    mock_thread_context.thread.current_depth = 3

    handler = IndentHandler(mock_config, mock_thread_context)
    assert handler.get_indent() == "      "  # 2 * 3 = 6 mezer

def test_indent_handler_large_indent():
    """Test velmi velkého odsazení."""
    mock_config = Mock()
    mock_config.indent = 100  # Extrémně velké odsazení
    mock_thread_context = Mock()
    mock_thread_context.thread.current_depth = 10

    handler = IndentHandler(mock_config, mock_thread_context)
    assert len(handler.get_indent()) == 1000  # 100 * 10