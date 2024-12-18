import pytest
from log_this.log_this import log_this, manager

import pytest
from log_this.log_this import log_this




def test_log_this_manager_context(mock_function):
    """Test, zda manager správně spravuje kontext logování."""
    initial_indent = manager.get_indent()
    initial_blank_lines = manager.get_blank_lines()

    @log_this(mode='simple')
    def decorated_mock_function(x, y):
        return mock_function(x, y)

    decorated_mock_function(2, 3)

    assert manager.get_indent() == initial_indent
    assert manager.get_blank_lines() == initial_blank_lines

