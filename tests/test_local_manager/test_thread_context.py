import pytest
from log_this.local_manager._thread_context import ThreadContext


def test_thread_context_initialization():
    """Test inicializace kontextu vlákna."""
    context = ThreadContext()
    context.initialize_state()

    assert hasattr(context.thread, 'current_depth')
    assert context.thread.current_depth == 0
    assert context.thread.last_depth == 0
    assert context.thread.current_type == 0
    assert context.thread.last_type == 0


def test_thread_context_update():
    """Test aktualizace kontextu."""
    context = ThreadContext()

    context.update_context(1)
    assert context.thread.current_depth == 0
    assert context.thread.current_type == 1

    context.update_context(2)
    assert context.thread.current_depth == 1
    assert context.thread.last_type == 1
    assert context.thread.current_type == 2


def test_thread_context_revert():
    """Test návratu kontextu."""
    context = ThreadContext()

    # Inicializace na hloubku 0
    context.update_context(1)  # current_depth = 0
    context.update_context(2)  # current_depth = 1
    context.revert_context()   # current_depth = 0

    # Ověříme aktuální a minulou hloubku
    assert context.thread.current_depth == 0  # Po revertu by měla být 0
    assert context.thread.last_depth == 1     # Předchozí hloubka byla 1

def test_thread_context_extreme_depth():
    """Test chování při extrémní hloubce zanoření."""
    context = ThreadContext()

    # Simulace velmi hlubokého zanoření
    for _ in range(1000):
        context.update_context(1)

    assert context.thread.current_depth == 999

