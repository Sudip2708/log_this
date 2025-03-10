"""
Tests for thread initialization and default properties.

This module contains tests focused on the following aspects:
- Correct initialization of the singleton thread instance.
- Verification of default attributes and their values.
- Proper setup and structure of thread-local storage.
- Accessibility of default values through properties.

These tests ensure the foundational functionality of the thread instance
and its ability to provide consistent and isolated storage across threads.
"""

import pytest
from log_this_old.manager.thread import get_thread
from threading import local


@pytest.fixture
def thread_instance():
    """Fixture that create the singleton instance for thread."""
    return get_thread()


def test_thread_local_instance_type(thread_instance):
    """Test that thread local storage is of correct type"""
    assert isinstance(thread_instance.thread, local), \
        "Thread attribute should be an instance of threading.local"


def test_singleton_initialisation(thread_instance):
    """Test that get_thread() consistently returns the same singleton instance"""
    thread_instance1 = thread_instance
    thread_instance2 = get_thread()
    assert thread_instance1 is thread_instance2
    assert thread_instance1.thread is thread_instance2.thread


def test_default_attributes_presence(thread_instance):
    """Test that thread local storage is properly initialized"""
    assert hasattr(thread_instance, '_instance')
    assert hasattr(thread_instance, 'thread')
    assert hasattr(thread_instance.thread, 'current_depth')
    assert hasattr(thread_instance.thread, 'last_depth')
    assert hasattr(thread_instance.thread, 'current_type')
    assert hasattr(thread_instance.thread, 'last_type')
    assert hasattr(thread_instance, '_initialized')


def test_default_attributes_values(thread_instance):
    """Verify that thread local storage is initialized with correct default values"""
    assert thread_instance._instance == thread_instance
    assert thread_instance.thread.current_depth == -1
    assert thread_instance.thread.last_depth == 0
    assert thread_instance.thread.current_type == 0
    assert thread_instance.thread.last_type == 0
    assert thread_instance._initialized == True


def test_property_access_default_values(thread_instance):
    """Verify that default values are correctly accessible through properties"""
    assert thread_instance.current_depth == -1
    assert thread_instance.last_depth == 0
    assert thread_instance.current_type == 0
    assert thread_instance.last_type == 0