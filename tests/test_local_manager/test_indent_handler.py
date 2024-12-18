import pytest
from unittest.mock import Mock
from log_this.local_manager._indent_handler import IndentHandler


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