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



# def test_attributes_presence(instance):
#     """Ověření že instance má všechny atributy"""
#     assert hasattr(instance, "max_depth"), \
#         "Instance nemá vytvořerný atribut max_dept."
#     assert instance.max_depth == 100, \
#         "Atribut max_depth, nemá výchozí hodnotu nastavenou na 100."
#     assert hasattr(instance, "seen"), \
#         "Instance nemá vytvořerný atribut seen."
#     assert instance.seen == set(), \
#         "Atribut seen, nemá výchozí hodnotu nastavenou na prázdnou množinu."
#     assert hasattr(instance, "_initialized"), \
#         "Instance nemá vytvořerný atribut _initialized."
#     assert instance._initialized == True, \
#         "Atribut _initialized, nemá po inicializaci hodnotu True."
#
#
# def test_dunder_call_method(instance):
#     """Ověření metody call"""
#     assert instance(123) == 123, \
#         "Chyba při ověření zda instance může fungovat jako funkce."
#
#
# def test_max_dept_setting(instance):
#     """Ověření nastavení maximální hloubky rekurze"""
#     instance.max_depth = 4
#     assert instance.max_depth == 4, \
#         "Nepovedlo se správně nastavit atribut max_depth "
#     instance.max_depth = 100
#
#
# def test_max_depth_exceeded_check(instance):
#     """Ověření zachycení nastavené maximální hloubky rekurze pro seznam"""
#     instance = get_serializer()
#     obj = [[[[[[42]]]]]]  # Pět úrovní vnoření.
#     instance.max_depth = 4
#     assert instance(obj) == "<SerializationError: Maximum serialization depth exceeded>", \
#         "Nepovedlo se správně zachytit překročení nastavené hloubky pro rekurzy."
#     instance.max_depth = 100
#
#
# def test_dict_error_check(instance):
#     test_dict = {'value': {'value': '<SerializationError: Maximum serialization depth exceeded>'}}
#     result = instance._dict_error_check(test_dict)
#     assert result == {'value': '<SerializationError: Maximum serialization depth exceeded>'}
#
#
def test_max_depth_dict(instance):
    """Ověření zachycení nastavené maximální hloubky rekurze pro slovník"""
    instance.max_depth = 2
    obj = {"key": {"nested_key": {"too_deep": 42}}}
    result = instance(obj)
    assert "<SerializationError: Maximum serialization depth exceeded>" in str(result), \
        "Nepovedlo se správně zachytit překročení maximální hloubky pro slovník."
    instance.max_depth = 100
#
#
# def test_max_depth_dunder_dict(instance):
#     """Ověření zachycení nastavené maximální hloubky rekurze pro objekty s __dict__"""
#     from dataclasses import dataclass
#     @dataclass
#     class Nested:
#         value: int
#     obj = Nested(Nested(Nested(42)))  # Tři úrovně
#     instance.max_depth = 2
#     result = instance(obj)
#     assert "<SerializationError: Maximum serialization depth exceeded>" in str(result), \
#         "Nepovedlo se správně zachytit překročení maximální hloubky pro datovou třídu."
#     instance.max_depth = 100
#
#
# def test_max_depth_dataclass(instance):
#     """Ověření zachycení nastavené maximální hloubky rekurze pro objekty dataclass"""
#     from dataclasses import dataclass
#     @dataclass
#     class Example:
#         a: int
#         b: str
#         @property
#         def __dict__(self):
#             return {}  # Vrátíme prázdný slovník, aby první kontrola selhala
#     # Vytvoření vnořené struktury
#     inner = Example(None, "inner")
#     middle = Example(inner, "middle")
#     obj = Example(middle, "outer")  # Tři úrovně vnoření
#     # Nastavení maximální hloubky rekurze
#     instance.max_depth = 2
#     result = instance(obj)
#     assert "<SerializationError: Maximum serialization depth exceeded>" in str(result), \
#         "Nepovedlo se správně zachytit překročení maximální hloubky pro '__dataclass_fields__')."
#     instance.max_depth = 100
#
#
# def test_cyclic_reference(instance):
#     """Ověření Kontroly cyklické rekurze pro seznam"""
#     obj = []
#     obj.append(obj)  # Cyclic reference.
#     assert instance(obj) == "<SerializationError: Cyclic reference detected>", \
#         "Nepovedlo se správně rachytit cyklickou rekurzy."
#
#
# def test_cyclic_reference_in_dict(instance):
#     """Ověření Kontroly cyklické rekurze pro slovník"""
#     obj = {}
#     obj["key"] = obj  # Cyclic reference
#     result = instance(obj)
#     assert result["key"] == "<SerializationError: Cyclic reference detected>", \
#         "Nepovedlo se správně zachytit cyklickou referenci ve slovníku."
#
#
# def test_cyclic_reference_in_tuple(instance):
#     """Ověření Kontroly cyklické rekurze pro tuple"""
#     obj = ([],)
#     obj[0].append(obj)  # Cyclic reference
#     assert instance(obj) == "<SerializationError: Cyclic reference detected>", \
#         "Nepovedlo se správně zachytit cyklickou referenci v tuple."

#
# def test_serialize_dunder_dict(instance):
#     """Kontrola zachycení objektu s __dict__"""
#     class Example:
#         def __init__(self):
#             self.a, self.b = 1, "test"
#     obj = Example()
#     assert instance(obj) == {"a": 1, "b": "test"}, \
#         "Nepovedlo se správně zpracovat podmínku if hasattr(obj, '__dict__')."
#
#
# def test_serialize_namedtuple(instance):
#     """Kontrola zachycení objektu s _asdict"""
#     from collections import namedtuple
#     Example = namedtuple("Example", ["a", "b"])
#     obj = Example(1, "test")
#     assert instance(obj) == {"a": 1, "b": "test"}, \
#         "Nepovedlo se správně zpracovat podmínku if hasattr(obj, '_asdict')."
#
#
# def test_serialize_dataclass(instance):
#     """Kontrola zachycení objektu s __dataclass_fields__"""
#     from dataclasses import dataclass
#     @dataclass
#     class Example:
#         a: int
#         b: str
#         @property
#         def __dict__(self):
#             return {}  # Vrátíme prázdný slovník, aby první kontrola selhala
#     obj = Example(1, "test")
#     assert instance(obj) == {"a": 1, "b": "test"}, \
#         "Nepovedlo se správně zpracovat podmínku if hasattr(obj, '__dataclass_fields__')."
#
#
# def test_serialize_list(instance):
#     """Kontrola zachycení list"""
#     obj = [1, 2, 3]
#     assert instance(obj) == [1, 2, 3], \
#         "Nepovedlo se správně spracovat serializaci seznamu."
#
#
# def test_serialize_tuple(instance):
#     """Kontrola zachycení tuple. (Objekty se převádějí na seznam.)"""
#     obj = (1, 2, 3)
#     assert instance(obj) == [1, 2, 3], \
#         "Nepovedlo se správně spracovat serializaci tuple."
#
#
# def test_serialize_set(instance):
#     """Kontrola zachycení množiny. (Objekty se převádějí na seznam.)"""
#     obj = set((1, 2, 3))
#     assert instance(obj) == [1, 2, 3], \
#         "Nepovedlo se správně spracovat serializaci množiny."
#
#
# def test_serialize_dict(instance):
#     """Kontrola zachycení dict"""
#     obj = {"key": "value", "number": 42}
#     assert instance(obj) == {"key": "value", "number": 42}, \
#         "Nepovedlo se správně zpracovat podmínku if isinstance(obj, dict)."
#
#
# def test_serialize_int(instance):
#     """Kontrola zachycení int"""
#     obj = 123
#     assert instance(obj) == 123, \
#         "Nepovedlo se správně spracovat serializaci int."
#
#
# def test_serialize_float(instance):
#     """Kontrola zachycení float"""
#     obj = 1.23
#     assert instance(obj) == 1.23, \
#         "Nepovedlo se správně spracovat serializaci float."
#
#
# def test_serialize_str(instance):
#     """Kontrola zachycení str"""
#     obj = "x123"
#     assert instance(obj) == "x123", \
#         "Nepovedlo se správně spracovat serializaci str."
#
#
# def test_serialize_bool(instance):
#     """Kontrola zachycení bool"""
#     obj = True
#     assert instance(obj) == True, \
#         "Nepovedlo se správně spracovat serializaci bool."
#     assert instance(obj) == 1, \
#         "Nepovedlo se správně spracovat serializaci bool."
#     obj = False
#     assert instance(obj) == False, \
#         "Nepovedlo se správně spracovat serializaci bool."
#     assert instance(obj) == 0, \
#         "Nepovedlo se správně spracovat serializaci bool."
#
#
# def test_serialize_none(instance):
#     """Kontrola zachycení None"""
#     obj = None
#     assert instance(obj) == None, \
#         "Nepovedlo se správně spracovat serializaci type(None)."
#
#
# def test_serialize_fallback(instance):
#     """Kontrola zachycení 'Poslední záchrana'"""
#     class Unserializable:
#         def __str__(self):
#             return "UnserializableObject"
#     obj = Unserializable()
#     assert instance(obj) == "UnserializableObject", \
#         "Nepovedlo se správně zpracovat poslední záchranu (fallback)."
#
#
# def test_serialize_exception(instance):
#     """Zkouška vyvolání výjimky uvnitř bloku pro práci s objekty"""
#     class Unserializable:
#         def __str__(self):
#             raise ValueError("Chyba při převodu na string")
#     obj = Unserializable()
#     result = instance(obj)
#     assert isinstance(result, str) and "SerializationError" in result, \
#         "Nepovedlo se zachytit výjimku během serializace."
#
#
# def test_branch_finally(instance):
#     """Zkouška větve finally"""
#     obj = 123
#     id_obj = id(obj)
#     assert id_obj not in instance.seen, \
#         "Nepovedlo se ověřit přítomnost objektu v atributu seen."
#     _ = instance(obj)
#     assert id_obj not in instance.seen, \
#         "Id objektu se po serializaci neodstraní z atributu seen."
#
#
# def test_first_try_exception(instance):
#     """Zkouška vyvolání výjimky před blokem pro práci s objekty"""
#     instance.seen = dict()
#     obj = 123
#     result = instance(obj)
#     assert isinstance(result, str) and "SerializationError" in result, \
#         "Nepovedlo se zachytit při chybně nastaveném seen."
#     instance.seen = set()
#
#





