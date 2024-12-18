import pytest
from unittest.mock import Mock, patch
from log_this.local_manager.local_manager import LocalManager


def test_local_manager_initialization():
    """Test inicializace LocalManageru."""
    with patch('log_this.config.get_config') as mock_config:
        mock_config.return_value = Mock()
        local_manager = LocalManager()

        assert hasattr(local_manager, 'config')
        assert hasattr(local_manager, 'thread_context')
        assert hasattr(local_manager, 'indent_handler')
        assert hasattr(local_manager, 'blank_lines_handler')


def test_local_manager_context_methods():
    """Test metod pro správu kontextu."""
    with patch('log_this.config.get_config') as mock_config:
        mock_config.return_value = Mock()
        local_manager = LocalManager()

        # Mock metod v thread_context
        with patch.object(local_manager.thread_context,
                          'update_context') as mock_update:
            local_manager.update_context(1)
            mock_update.assert_called_once_with(1)

        with patch.object(local_manager.thread_context,
                          'revert_context') as mock_revert:
            local_manager.revert_context()
            mock_revert.assert_called_once()


def test_local_manager_handlers():
    """Test handlerů pro indent a blank lines."""
    with patch('log_this.config.get_config') as mock_config:
        mock_config.return_value = Mock()
        local_manager = LocalManager()

        with patch.object(local_manager.indent_handler, 'get_indent',
                          return_value='  ') as mock_indent:
            assert local_manager.get_indent() == '  '
            mock_indent.assert_called_once()

        with patch.object(local_manager.blank_lines_handler, 'get_blank_lines',
                          return_value=('\n', '\n')) as mock_blank_lines:
            assert local_manager.get_blank_lines() == ('\n', '\n')
            mock_blank_lines.assert_called_once()