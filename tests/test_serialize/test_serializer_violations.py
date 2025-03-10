import pytest
from log_this_old.manager.serializer import get_serializer
from dataclasses import dataclass


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


def test_first_try_exception(serializer_instance):
    """Zkouška vyvolání a zachycení výjimky před blokem pro práci s objekty"""
    serializer_instance.seen = dict()
    obj = 123
    result = serializer_instance(obj)
    assert isinstance(result, str) and "SerializationError" in result, \
        "Nepovedlo se zachytit při chybně nastaveném seen."


def test_serialize_exception(serializer_instance):
    """Zkouška vyvolání a zachycení výjimky uvnitř bloku pro práci s objekty"""
    class Unserializable:
        def __str__(self):
            raise ValueError("Chyba při převodu na string")
    obj = Unserializable()
    result = serializer_instance(obj)
    assert isinstance(result, str) and "SerializationError" in result, \
        "Nepovedlo se zachytit výjimku během serializace."


def test_max_dept_setting(serializer_instance):
    """Ověření nastavení maximální hloubky rekurze"""
    serializer_instance.max_depth = 4
    assert serializer_instance.max_depth == 4


def test_max_depth_exceeded_check_for_list(serializer_instance):
    """Ověření zachycení nastavené maximální hloubky rekurze pro seznam"""
    serializer_instance.max_depth = 4
    obj = [[[[[[42]]]]]]  # Pět úrovní vnoření.
    expected_result = "<SerializationError: Maximum serialization depth exceeded>"
    assert serializer_instance(obj) == expected_result


def test_dict_error_check_method(serializer_instance):
    """Ověří, zda metoda pro správu slovníku, vracení nezanořený oznam o chybě překročení maximální rekurze"""
    test_dict = {'key': {'nested_key': '<SerializationError: Maximum serialization depth exceeded>'}}
    expected_result = {'key': '<SerializationError: Maximum serialization depth exceeded>'}
    result = serializer_instance._dict_error_check(test_dict)
    assert result == expected_result


def test_max_depth_exceeded_check_for_dict(serializer_instance):
    """Ověření zachycení nastavené maximální hloubky rekurze pro slovník"""
    serializer_instance.max_depth = 2
    obj = {"key": {"nested_key": {"too_deep_nested_key": 42}}}
    expected_result = {'key': '<SerializationError: Maximum serialization depth exceeded>'}
    assert serializer_instance(obj) == expected_result


def test_max_depth_exceeded_check_for_dunder_dict(serializer_instance):
    """Ověření zachycení nastavené maximální hloubky rekurze pro objekty s __dict__"""
    serializer_instance.max_depth = 2
    @dataclass
    class Nested:
        value: int
    obj = Nested(Nested(Nested(42)))  # Tři úrovně
    expected_result = "<SerializationError: Maximum serialization depth exceeded>"
    assert expected_result in str(serializer_instance(obj))


def test_max_depth_exceeded_check_for_dataclass(serializer_instance):
    """Ověření zachycení nastavené maximální hloubky rekurze pro objekty dataclass"""
    serializer_instance.max_depth = 2
    @dataclass
    class Example:
        a: int
        b: str
        @property
        def __dict__(self):
            return {}  # Vrátíme prázdný slovník, aby první kontrola selhala
    # Vytvoření vnořené struktury
    inner = Example(None, "inner")
    middle = Example(inner, "middle")
    obj = Example(middle, "outer")  # Tři úrovně vnoření
    expected_result = "<SerializationError: Maximum serialization depth exceeded>"
    assert expected_result in str(serializer_instance(obj))


def test_cyclic_error_check_for_list(serializer_instance):
    """Ověření Kontroly cyklické rekurze pro seznam"""
    obj = []
    obj.append(obj)  # Cyclic reference.
    expected_result = "<SerializationError: Cyclic reference detected>"
    assert serializer_instance(obj) == expected_result


def test_cyclic_error_check_for_dict(serializer_instance):
    """Ověření Kontroly cyklické rekurze pro slovník"""
    obj = {}
    obj["key"] = obj  # Cyclic reference
    expected_result = {'key': '<SerializationError: Cyclic reference detected>'}
    assert serializer_instance(obj) == expected_result


def test_cyclic_error_check_for_tuple(serializer_instance):
    """Ověření Kontroly cyklické rekurze pro tuple"""
    obj = ([],)
    obj[0].append(obj)  # Cyclic reference
    expected_result = "<SerializationError: Cyclic reference detected>"
    assert serializer_instance(obj) == expected_result


