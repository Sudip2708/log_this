import pytest
from log_this.manager.serializer import get_serializer


@pytest.fixture
def serializer_instance():
    """Fixture vracející instanci SafeSerializer."""
    return get_serializer()


def test_singleton_initialisation(serializer_instance):
    """Test that get_serializer() consistently returns the same singleton instance"""
    serializer_instance1 = serializer_instance
    serializer_instance2 = get_serializer()
    assert serializer_instance1 is serializer_instance2


def test_default_attributes_presence(serializer_instance):
    """Ověření že instance má všechny atributy"""
    assert hasattr(serializer_instance, '_instance')
    assert hasattr(serializer_instance, 'max_depth')
    assert hasattr(serializer_instance, 'seen')
    assert hasattr(serializer_instance, '_initialized')


def test_default_attributes_values(serializer_instance):
    """Ověření že atributy se inicializuovali se správnou hodnotou."""
    assert serializer_instance._instance == serializer_instance
    assert serializer_instance.max_depth == 100
    assert serializer_instance.seen == set()
    assert serializer_instance._initialized == True