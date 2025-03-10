"""
Operational tests for thread-local behavior and property updates.

This module contains tests that verify the functionality and behavior
of thread-local storage and its operations, including:

- Property setters and their validation.
- Methods for increasing and decreasing depth.
- Thread isolation to ensure independent storage across threads.
- Chaining operations that involve updates to both depth and type.
- The behavior of reinitialization and clearing thread-local values.

These tests focus on dynamic aspects of the thread instance,
ensuring that its state updates correctly under various conditions.
"""


import pytest
from log_this_old.manager.thread import get_thread


@pytest.fixture
def thread_instance():
    """Fixture that create the singleton instance for thread."""
    return get_thread()


@pytest.fixture(autouse=True)
def reset_singleton(thread_instance):
    """
    Fixture that resets the singleton state before each test.

    This ensures each test starts with a clean state, preventing test interference
    while maintaining the singleton pattern.
    """
    # Reset all thread-local values to their defaults
    thread_instance.thread.current_depth = -1
    thread_instance.thread.last_depth = 0
    thread_instance.thread.current_type = 0
    thread_instance.thread.last_type = 0
    yield
    # Reset again after test completion
    thread_instance.thread.current_depth = -1
    thread_instance.thread.last_depth = 0
    thread_instance.thread.current_type = 0
    thread_instance.thread.last_type = 0


def test_reinitialization():
    """Test that reinitialization doesn't reset values"""
    thread_instance1 = get_thread()
    thread_instance1.thread.current_depth = 5
    thread_instance2 = get_thread() # Try to reinitialize
    assert thread_instance2.thread.current_depth == 5


def test_clear_behavior():
    """Test __dict__.clear() behavior during initialization"""
    thread_instance1 = get_thread()
    thread_instance1.thread.__dict__['test_key'] = 'test_value'
    thread_instance2 = get_thread()   # This should not clear if already initialized
    assert hasattr(thread_instance2.thread, 'test_key')


def test_thread_local_properties_setters(thread_instance):
    """Test all properties behave correctly"""
    # Test current_depth
    thread_instance.thread.current_depth = 5
    assert thread_instance.current_depth == 5
    # Test last_depth
    thread_instance.thread.last_depth = 3
    assert thread_instance.last_depth == 3
    # Test current_type
    thread_instance.thread.current_type = 2
    assert thread_instance.current_type == 2
    # Test last_type
    thread_instance.thread.last_type = 1
    assert thread_instance.last_type == 1


def test_instance_property_setters(thread_instance):
    """Verify that values can be correctly set through property setters"""
    # Test current_depth
    thread_instance.current_depth = 5
    assert thread_instance.current_depth == 5
    # Test last_depth
    thread_instance.last_depth = 3
    assert thread_instance.last_depth == 3
    # Test current_type
    thread_instance.current_type = 2
    assert thread_instance.current_type == 2
    # Test last_type
    thread_instance.last_type = 1
    assert thread_instance.last_type == 1


def test_property_setters_validation_current_depth(thread_instance):
    """
    Verify that property setters properly validate input values for depth

    (Pokud se nevyvolá TypeError, setter neověřuje typ hodnoty.)
    """
    # Kontrola nezadání číslené hodnoty
    with pytest.raises(TypeError, match="Current depth must be an integer"):
        thread_instance.current_depth = "invalid"
    # Kontrola jiné zadání záporné číslené hodnoty než je povolená hodnota -1
    with pytest.raises(ValueError,
                       match="Current depth cannot be less than -1"):
        thread_instance.current_depth = -2


def test_property_setters_validation_current_type(thread_instance):
    """
    Verify that property setters properly validate input values for type

    (Pokud se nevyvolá TypeError, setter neověřuje typ hodnoty.)
    """
    # Kontrola nezadání číslené hodnoty
    with pytest.raises(TypeError, match="Current type must be an integer"):
        thread_instance.current_type = "invalid"
    # Kontrola zadání záporné číslené hodnoty
    with pytest.raises(ValueError, match="Current type cannot be negative"):
        thread_instance.current_type = -1


def test_increase_depth_and_update_type(thread_instance):
    """Test depth increase and type update behavior"""
    initial_depth = thread_instance.current_depth
    initial_type = thread_instance.current_type

    thread_instance.increase_depth_and_update_type(2)

    assert thread_instance.current_depth == initial_depth + 1, \
        f"Expected depth {initial_depth + 1}, got {thread_instance.current_depth}"
    assert thread_instance.last_type == initial_type, \
        f"Expected last_type {initial_type}, got {thread_instance.last_type}"
    assert thread_instance.current_type == 2, \
        f"Expected current_type 2, got {thread_instance.current_type}"


def test_multiple_depth_increases(thread_instance):
    """Test multiple consecutive depth increases"""
    initial_depth = thread_instance.current_depth

    for i in range(3):
        thread_instance.increase_depth_and_update_type(i)

    assert thread_instance.current_depth == initial_depth + 3, \
        f"Expected depth {initial_depth + 3}, got {thread_instance.current_depth}"
    assert thread_instance.current_type == 2, \
        f"Expected current_type 2 after last update, got {thread_instance.current_type}"


def test_decrease_depth(thread_instance):
    """Test depth decrease behavior"""
    thread_instance.thread.current_depth = 5

    thread_instance.decrease_depth()

    assert thread_instance.current_depth == 4, \
        f"Expected depth 4 after decrease, got {thread_instance.current_depth}"
    assert thread_instance.last_depth == 5, \
        f"Expected last_depth 5 after decrease, got {thread_instance.last_depth}"


def test_multiple_depth_decreases(thread_instance):
    """Test multiple consecutive depth decreases"""
    thread_instance.thread.current_depth = 5

    for _ in range(3):
        thread_instance.decrease_depth()

    assert thread_instance.current_depth == 2, \
        f"Expected depth 2 after three decreases, got {thread_instance.current_depth}"


import threading
def test_thread_isolation(thread_instance):
    """Test that different threads have isolated storage"""

    def modify_in_thread():
        thread_instance.thread.current_depth = 10
        assert thread_instance.current_depth == 10, \
            "Thread-local storage not isolated; current_depth mismatch in new thread"

    thread_instance.thread.current_depth = 5
    new_thread = threading.Thread(target=modify_in_thread)
    new_thread.start()
    new_thread.join()

    assert thread_instance.current_depth == 5, \
        "Main thread's current_depth should remain unchanged after thread modification"


def test_depth_type_update_chain(thread_instance):
    """Test the complete chain of depth and type updates"""

    # Initial state verification
    assert thread_instance.current_depth == -1, \
        f"Expected initial depth -1, got {thread_instance.current_depth}"
    assert thread_instance.current_type == 0, \
        f"Expected initial current_type 0, got {thread_instance.current_type}"
    assert thread_instance.last_type == 0, \
        f"Expected initial last_type 0, got {thread_instance.last_type}"

    # First update
    thread_instance.increase_depth_and_update_type(1)
    assert thread_instance.current_depth == 0, \
        f"Expected depth 0 after first update, got {thread_instance.current_depth}"
    assert thread_instance.last_type == 0, \
        f"Expected last_type 0 after first update, got {thread_instance.last_type}"
    assert thread_instance.current_type == 1, \
        f"Expected current_type 1 after first update, got {thread_instance.current_type}"

    # Second update
    thread_instance.increase_depth_and_update_type(2)
    assert thread_instance.current_depth == 1, \
        f"Expected depth 1 after second update, got {thread_instance.current_depth}"
    assert thread_instance.last_type == 1, \
        f"Expected last_type 1 after second update, got {thread_instance.last_type}"
    assert thread_instance.current_type == 2, \
        f"Expected current_type 2 after second update, got {thread_instance.current_type}"

    # Decrease depth
    thread_instance.decrease_depth()
    assert thread_instance.current_depth == 0, \
        f"Expected depth 0 after decrease, got {thread_instance.current_depth}"
    assert thread_instance.last_depth == 1, \
        f"Expected last_depth 1 after decrease, got {thread_instance.last_depth}"
