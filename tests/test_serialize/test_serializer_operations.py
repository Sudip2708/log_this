import pytest
from log_this.manager.serializer import get_serializer


@pytest.fixture
def serializer_instance():
    """Fixture vracející instanci SafeSerializer."""
    return get_serializer()


@pytest.fixture(autouse=True)
def reset_singleton(serializer_instance):
    """
    Fixture that resets the singleton state before each test.

    This ensures each test starts with a clean state, preventing test interference
    while maintaining the singleton pattern.
    """
    # Reset all thread-local values to their defaults
    serializer_instance.max_depth = 100
    serializer_instance.seen = set()
    yield
    # Reset again after test completion
    serializer_instance.max_depth = 100
    serializer_instance.seen = set()


def test_call_method(serializer_instance):
    """Ověření metody call"""
    assert serializer_instance(123) == 123, \
        "Chyba při ověření zda instance může fungovat jako funkce."


def test_serialize_int(serializer_instance):
    """
    Test serializace pro typ int. P

    odmínka: if isinstance(obj, (int, float, str, bool, type(None))).
    """
    obj = 123
    assert serializer_instance(obj) == 123


def test_serialize_float(serializer_instance):
    """
    Test serializace pro typ float.

    Podmínka: if isinstance(obj, (int, float, str, bool, type(None))).
    """
    obj = 1.23
    assert serializer_instance(obj) == 1.23


def test_serialize_str(serializer_instance):
    """
    Test serializace pro typ str.

    Podmínka: if isinstance(obj, (int, float, str, bool, type(None))).
    """
    obj = "x123"
    assert serializer_instance(obj) == "x123"


def test_serialize_bool(serializer_instance):
    """
    Test serializace pro typ bool.

    Podmínka: if isinstance(obj, (int, float, str, bool, type(None))).
    """
    obj = True
    assert serializer_instance(obj) == True
    obj = False
    assert serializer_instance(obj) == False


def test_serialize_none(serializer_instance):
    """
    Test serializace pro typ None.

    Podmínka: if isinstance(obj, (int, float, str, bool, type(None))).
    """
    obj = None
    assert serializer_instance(obj) == None


def test_serialize_list(serializer_instance):
    """
    Test serializace pro typ list.

    Podmínka: if isinstance(obj, (list, tuple, set)).
    """
    obj = [1, 2, 3]
    assert serializer_instance(obj) == [1, 2, 3]


def test_serialize_tuple(serializer_instance):
    """
    Test serializace pro typ tuple.

    Podmínka: if isinstance(obj, (list, tuple, set)).
    (Objekty se převádějí na seznam.)
    """
    obj = (1, 2, 3)
    assert serializer_instance(obj) == [1, 2, 3]


def test_serialize_set(serializer_instance):
    """
    Test serializace pro typ množina.

    Podmínka: if isinstance(obj, (list, tuple, set)).
    (Objekty se převádějí na seznam.)
    """
    values = (1, 2, 3)
    obj = set(values)
    assert serializer_instance(obj) == [1, 2, 3]


def test_serialize_dict(serializer_instance):
    """
    Test serializace pro typ dict.

    Podmínka: if isinstance(obj, dict).
    """
    obj = {"key": "value", "number": 42}
    assert serializer_instance(obj) == {"key": "value", "number": 42}


def test_serialize_dunder_dict(serializer_instance):
    """
    Test serializace pro objekt s __dict__.

    Podmínka: if hasattr(obj, '__dict__') and obj.__dict__.
    """
    class Example:
        def __init__(self):
            self.a, self.b = 1, "test"
    obj = Example()
    assert serializer_instance(obj) == {"a": 1, "b": "test"}


def test_serialize_namedtuple(serializer_instance):
    """
    Test serializace pro objekt s _asdict.

    Podmínka: if hasattr(obj, '_asdict').
    """
    from collections import namedtuple
    Example = namedtuple("Example", ["a", "b"])
    obj = Example(1, "test")
    assert serializer_instance(obj) == {"a": 1, "b": "test"}


def test_serialize_dataclass(serializer_instance):
    """
    Test serializace pro objekt s __dataclass_fields__.

    Podmínka: if hasattr(obj, '__dataclass_fields__').
    """
    from dataclasses import dataclass
    @dataclass
    class Example:
        a: int
        b: str
        @property
        def __dict__(self):
            return {}  # Vrátíme prázdný slovník, aby první kontrola selhala
    obj = Example(1, "test")
    assert serializer_instance(obj) == {"a": 1, "b": "test"}


def test_serialize_fallback(serializer_instance):
    """
    Kontrola zachycení 'Poslední záchrana'.

    Pro případ, pokud žádná z předchozích podmínek nebude splněna.
    Vrací str(obj)
    """
    class Unserializable:
        def __str__(self):
            return "UnserializableObject"
    obj = Unserializable()
    assert serializer_instance(obj) == "UnserializableObject"


def test_branch_finally(serializer_instance):
    """Zkouška větve finally"""
    obj = 123
    id_obj = id(obj)
    assert id_obj not in serializer_instance.seen, \
        "Nepovedlo se ověřit přítomnost objektu v atributu seen."
    _ = serializer_instance(obj)
    assert id_obj not in serializer_instance.seen, \
        "Id objektu se po serializaci neodstraní z atributu seen."







