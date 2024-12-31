import pytest
from log_this.manager.thread import get_thread


@pytest.fixture
def instance():
    """Fixture vracející instanci SafeSerializer."""
    return get_thread()


def test_get_thread_singleton():
    """Ověření že se vrací pouze singleton instance"""
    instance1 = get_thread()
    instance2 = get_thread()
    assert instance1 is instance2, \
        "Metoda get_thread nevrací singleton instanci."


def test_attributes_presence(instance):
    """Ověření že instance má všechny atributy"""
    from threading import local
    assert hasattr(instance, "thread"), \
        "Instance nemá vytvořerný atribut thread."
    assert isinstance(instance.thread, local), \
        "Atribut thread není instancí třídy threading.local."
    assert hasattr(instance.thread, "current_depth"), \
        "Instance thread nemá vytvořerný atribut current_depth."
    assert instance.thread.current_depth == -1, \
        "Atribut current_depth, nemá výchozí hodnotu nastavenou na -1 (Důležité pro neodskočení od kraje pro první úroveň)."
    assert hasattr(instance.thread, "last_depth"), \
        "Instance thread nemá vytvořerný atribut last_depth."
    assert instance.thread.last_depth == 0, \
        "Atribut last_depth, nemá výchozí hodnotu nastavenou na 0."
    assert hasattr(instance.thread, "current_type"), \
        "Instance thread nemá vytvořerný atribut current_type."
    assert instance.thread.current_type == 0, \
        "Atribut current_type, nemá výchozí hodnotu nastavenou na 0."
    assert hasattr(instance.thread, "last_type"), \
        "Instance thread nemá vytvořerný atribut last_type."
    assert instance.thread.last_type == 0, \
        "Atribut last_type, nemá výchozí hodnotu nastavenou na 0."
    assert hasattr(instance, "_initialized"), \
        "Instance nemá vytvořerný atribut _initialized."
    assert instance._initialized == True, \
        "Atribut _initialized, nemá po inicializaci hodnotu True."

def test_property_current_depth(instance):
    assert instance.current_depth == -1, \
        "Property current_depth nevrací správnou hodnotu."

def test_property_last_depth(instance):
    assert instance.last_depth == 0, \
        "Property last_depth nevrací správnou hodnotu."

def test_property_current_type(instance):
    assert instance.current_type == 0, \
        "Property current_type nevrací správnou hodnotu."

def test_property_last_type(instance):
    assert instance.last_type == 0, \
        "Property last_type nevrací správnou hodnotu."

def test_change_property_current_depth(instance):
    instance.thread.current_depth = 10
    assert instance.current_depth == 10, \
        "Atribut thread.current_depth nelze měnit."
    instance.thread.current_depth = -1

def test_change_property_last_depth(instance):
    instance.thread.last_depth = 10
    assert instance.last_depth == 10, \
        "Atribut thread.last_depth nelze měnit."
    instance.thread.last_depth = 0

def test_change_property_current_type(instance):
    instance.thread.current_type = 10
    assert instance.current_type == 10, \
        "Atribut thread.current_type nelze měnit."
    instance.thread.current_type = 0

def test_change_property_last_type(instance):
    instance.thread.last_type = 10
    assert instance.last_type == 10, \
        "Atribut thread.last_depth nelze měnit."
    instance.thread.last_type = 0

def test_increase_depth_and_update_type(instance):
    # Kontrola aktuálního stavu
    assert instance.thread.current_depth == -1, \
        "Atribut thread.current_depth nemá nastavenou očekávanou výchozí hodnotu."
    assert instance.thread.last_type == 0, \
        "Atribut thread.last_type nemá nastavenou očekávanou výchozí hodnotu."
    assert instance.thread.current_type == 0, \
        "Atribut thread.current_type nemá nastavenou očekávanou výchozí hodnotu."
    # Volaní metody a kontrola změn
    instance.increase_depth_and_update_type(1)
    assert instance.thread.current_depth == 0, \
        "Atribut thread.current_depth nemá po změně očekávanou hodnotu."
    assert instance.thread.last_type == 0, \
        "Atribut thread.last_type nemá po změně očekávanou hodnotu."
    assert instance.thread.current_type == 1, \
        "Atribut thread.current_type nemá po změně očekávanou hodnotu"
    # Navrácení původních hodnot
    instance.thread.current_depth = -1
    instance.thread.last_type = 0
    instance.thread.current_type = 0

def test_decrease_depth(instance):
    # Nastavení hodnot
    instance.thread.current_depth = 1
    instance.thread.last_depth = 0
    # Volaní metody a kontrola změn
    instance.decrease_depth()
    assert instance.thread.current_depth == 0, \
        "Atribut thread.current_depth nemá po změně očekávanou hodnotu."
    assert instance.thread.last_depth == 1, \
        "Atribut thread.last_depth nemá po změně očekávanou hodnotu."
    # Navrácení původních hodnot
    instance.thread.current_depth = -1
    instance.thread.last_depth = 0


