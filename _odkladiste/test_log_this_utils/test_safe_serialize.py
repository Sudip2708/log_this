# tests/serialization/test_safe_serialize.py

import pytest
from dataclasses import dataclass
from collections import namedtuple
from log_this.modes.utils._safe_serialize import safe_serialize
# from log_this.config import Config, set_config


# Přípravné třídy a struktury pro testování
@dataclass
class SimpleDataClass:
    name: str
    age: int
    active: bool


Person = namedtuple('Person', ['name', 'age'])


class ComplexObject:
    def __init__(self, name):
        self.name = name
        self._private_attr = "secret"
        self.nested = [1, 2, 3]
        self.method = lambda x: x


class CyclicReferenceObject:
    def __init__(self):
        self.self_ref = None
        self.self_ref = self


# def setup_module(module):
#     """Nastavení konfigurace před spuštěním testů"""
#     set_config(Config(max_depth=10))


def test_primitive_types():
    """Test serializace primitivních typů"""
    test_cases = [
        42,
        3.14,
        "hello",
        True,
        None
    ]

    for case in test_cases:
        result = safe_serialize(case)
        assert result == case, f"Selhání serializace pro {case}"


def test_simple_list():
    """Test serializace jednoduché listy"""
    test_list = [1, 2, 3, "text"]
    result = safe_serialize(test_list)
    assert result == test_list


def test_nested_list():
    """Test serializace vnořené listy"""
    test_list = [1, [2, 3], {"key": "value"}]
    result = safe_serialize(test_list)
    assert result == test_list


def test_dictionary():
    """Test serializace slovníku"""
    test_dict = {
        "name": "John",
        "age": 30,
        "skills": ["Python", "Testing"]
    }
    result = safe_serialize(test_dict)
    assert result == test_dict


def test_dataclass():
    """Test serializace dataclass"""
    obj = SimpleDataClass("Alice", 25, True)
    result = safe_serialize(obj)

    assert result == {
        "name": "Alice",
        "age": 25,
        "active": True
    }


def test_namedtuple():
    """Test serializace namedtuple"""
    person = Person("Bob", 35)
    result = safe_serialize(person)

    assert result == {"name": "Bob", "age": 35}


def test_object_with_dict():
    """Test serializace objektu s __dict__"""

    class SimpleClass:
        def __init__(self):
            self.x = 10
            self.y = "hello"
            self._private = "secret"

    obj = SimpleClass()
    result = safe_serialize(obj)

    assert result == {"x": 10, "y": "hello"}


# def test_max_depth_limit():
#     """Test omezení maximální hloubky serializace"""
#     complex_nested = [1, [2, [3, [4, [5]]]]]
#
#     # set_config(Config(max_depth=3))
#     result = safe_serialize(complex_nested)
#
#     assert "SerializationError" in result
#     assert "Maximum serialization depth" in result


def test_cyclic_reference():
    """Test detekce cyklické reference"""
    cyclic_obj = CyclicReferenceObject()
    result = safe_serialize(cyclic_obj)

    assert "SerializationError" in str(result)
    assert "Cyclic reference" in str(result)


def test_complex_object():
    """Test serializace komplexního objektu"""
    obj = ComplexObject("TestName")
    result = safe_serialize(obj)

    assert result == {
        "name": "TestName",
        "nested": [1, 2, 3]
    }


def test_unsupported_object():
    """Test serializace nepodporovaného objektu"""

    class UnsupportedClass:
        pass

    obj = UnsupportedClass()
    result = safe_serialize(obj)

    assert isinstance(result, dict)
    assert result == {}


def test_mixed_complex_structure():
    """Test serializace komplexní smíšené struktury"""
    mixed_struct = {
        "users": [
            SimpleDataClass("Alice", 25, True),
            Person("Bob", 35)
        ],
        "settings": {
            "debug": True,
            "version": 1.2
        }
    }

    result = safe_serialize(mixed_struct)

    assert result == {
        "users": [
            {"name": "Alice", "age": 25, "active": True},
            {"name": "Bob", "age": 35}
        ],
        "settings": {
            "debug": True,
            "version": 1.2
        }
    }


# Požadavky pro spuštění testů
if __name__ == "__main__":
    pytest.main([__file__])