import pytest
from unittest.mock import Mock
from typing import Tuple
from log_this_old.manager.methods._get_blank_lines_mixin import GetBlankLinesMethodsMixins


@pytest.fixture
def mock_thread():
    """Provides mocked thread object."""
    thread = Mock()
    thread.current_depth = 1
    thread.last_depth = 1
    thread.current_type = 1
    thread.last_type = 1
    return thread


@pytest.fixture
def mock_config():
    """Provides mocked config dictionary."""
    return {"blank_lines": True}


@pytest.fixture
def blank_lines_handler(mock_config, mock_thread):
    """Provides configured blank lines handler instance."""

    class TestHandler(GetBlankLinesMethodsMixins):
        def __init__(self):
            self.config = mock_config
            self.thread = mock_thread

    return TestHandler()


# Tests for main get_blank_lines method
def test_blank_lines_disabled(mock_config, blank_lines_handler):
    """Tests behavior when blank_lines is disabled."""
    mock_config["blank_lines"] = False
    assert blank_lines_handler.get_blank_lines() == ("", "")


def test_one_line_type(mock_thread, blank_lines_handler):
    """Tests behavior for one-line log type."""
    mock_thread.current_type = 1
    result = blank_lines_handler.get_blank_lines()
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(x, str) for x in result)


def test_multi_line_type(mock_thread, blank_lines_handler):
    """Tests behavior for multi-line log type."""
    mock_thread.current_type = 2
    result = blank_lines_handler.get_blank_lines()
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(x, str) for x in result)


# Tests for OneLineMixin
def test_one_line_after_one_line(mock_thread, blank_lines_handler):
    """Tests one-line log after another one-line log."""
    mock_thread.last_type = 1
    assert blank_lines_handler._handle_one_line_log() == ("", "\n")


def test_one_line_nested(mock_thread, blank_lines_handler):
    """Tests nested one-line log."""
    mock_thread.last_type = 2
    mock_thread.last_depth = 0
    mock_thread.current_depth = 1
    assert blank_lines_handler._handle_one_line_log() == ("\n", "\n")


def test_one_line_default_case(mock_thread, blank_lines_handler):
    """Tests one-line log in default case."""
    mock_thread.last_type = 2
    mock_thread.last_depth = 1
    mock_thread.current_depth = 1
    assert blank_lines_handler._handle_one_line_log() == ("", "\n")


# Tests for MultiLineMixin
def test_multi_line_after_one_line(mock_thread, blank_lines_handler):
    """Tests multi-line log after one-line log."""
    mock_thread.last_type = 1
    assert blank_lines_handler._handle_multi_line_log() == ("", "\n")


def test_multi_line_same_depth(mock_thread, blank_lines_handler):
    """Tests multi-line log at same depth."""
    mock_thread.last_type = 2
    mock_thread.last_depth = 1
    mock_thread.current_depth = 1
    assert blank_lines_handler._handle_multi_line_log() == ("", "\n")


def test_multi_line_nested(mock_thread, blank_lines_handler):
    """Tests nested multi-line log."""
    mock_thread.last_type = 2
    mock_thread.last_depth = 0
    mock_thread.current_depth = 1
    assert blank_lines_handler._handle_multi_line_log() == ("\n", "\n")


# Edge cases and combinations
def test_depth_transitions(mock_thread, blank_lines_handler):
    """Tests various depth transitions."""
    test_cases = [
        (0, 1, 2, 2, ("\n", "\n")),  # Increasing depth
        (1, 0, 1, 2, ("", "\n")),  # Decreasing depth
        (1, 1, 1, 2, ("", "\n")),  # Same depth
    ]

    for last_depth, current_depth, last_type, current_type, expected in test_cases:
        mock_thread.last_depth = last_depth
        mock_thread.current_depth = current_depth
        mock_thread.last_type = last_type
        mock_thread.current_type = current_type
        assert blank_lines_handler.get_blank_lines() == expected


def test_type_transitions(mock_thread, blank_lines_handler):
    """Tests various type transitions."""
    test_cases = [
        (1, 1, ("", "\n")),  # One-line to one-line
        (1, 2, ("", "\n")),  # One-line to multi-line
        (2, 1, ("", "\n")),  # Multi-line to one-line
        (2, 2, ("", "\n")),  # Multi-line to multi-line
    ]

    for last_type, current_type, expected in test_cases:
        mock_thread.last_type = last_type
        mock_thread.current_type = current_type
        mock_thread.last_depth = mock_thread.current_depth  # Same depth
        assert blank_lines_handler.get_blank_lines() == expected


def test_invalid_config_values(mock_config, blank_lines_handler):
    """Tests behavior with invalid config values."""
    invalid_values = [None, 0, "", [], {}]
    for value in invalid_values:
        mock_config["blank_lines"] = value
        assert blank_lines_handler.get_blank_lines() == ("", "")