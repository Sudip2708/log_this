import pytest
from unittest.mock import Mock
from log_this.manager_old._blank_lines_handler import BlankLinesHandler


@pytest.fixture
def mock_blank_lines_config():
    """Fixture pro konfiguraci prázdných řádků."""
    mock_config = Mock()
    mock_config.blank_lines = True
    return mock_config


def test_blank_lines_disabled(mock_blank_lines_config):
    """Test vypnutých prázdných řádků."""
    mock_config = Mock()
    mock_config.blank_lines = False
    mock_thread_context = Mock()

    handler = BlankLinesHandler(mock_config, mock_thread_context)
    assert handler.get_blank_lines() == ("", "")


def test_one_line_log_same_type(mock_blank_lines_config):
    """Test jednořádkového logu se stejným typem."""
    mock_thread_context = Mock()
    mock_thread_context.thread.current_type = 1
    mock_thread_context.thread.last_type = 1
    mock_thread_context.thread.last_depth = 0
    mock_thread_context.thread.current_depth = 0

    handler = BlankLinesHandler(mock_blank_lines_config, mock_thread_context)
    assert handler.get_blank_lines() == ("", "\n")


def test_multi_line_log_different_depth(mock_blank_lines_config):
    """Test víceřádkového logu s rozdílnou hloubkou."""
    mock_thread_context = Mock()
    mock_thread_context.thread.current_type = 2
    mock_thread_context.thread.last_type = 1
    mock_thread_context.thread.last_depth = 0
    mock_thread_context.thread.current_depth = 1

    handler = BlankLinesHandler(mock_blank_lines_config, mock_thread_context)
    assert handler.get_blank_lines() == ("", "\n")

def test_blank_lines_handler_unexpected_type():
    """Test chování s neočekávaným typem logu."""
    mock_config = Mock()
    mock_config.blank_lines = True
    mock_thread_context = Mock()
    mock_thread_context.thread.current_type = 999  # Neočekávaný typ
    mock_thread_context.thread.last_type = 888

    handler = BlankLinesHandler(mock_config, mock_thread_context)
    # Ověří, že metoda neselže a vrátí rozumné výchozí hodnoty
    start, end = handler.get_blank_lines()
    assert isinstance(start, str)
    assert isinstance(end, str)

def test_one_line_log_nested_call(mock_blank_lines_config):
    """Test jednořádkového logu při vnořeném volání."""
    mock_thread_context = Mock()
    mock_thread_context.thread.current_type = 2
    mock_thread_context.thread.last_type = 2
    mock_thread_context.thread.last_depth = 0
    mock_thread_context.thread.current_depth = 1  # Zvýšená hloubka logování (vnoření)

    handler = BlankLinesHandler(mock_blank_lines_config, mock_thread_context)
    assert handler._handle_one_line_log() == ("\n", "\n")
