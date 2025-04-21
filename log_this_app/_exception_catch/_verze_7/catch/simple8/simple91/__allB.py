from typing import Any, List, Dict, Tuple, Set, FrozenSet, Deque, DefaultDict, OrderedDict, ChainMap, Counter, NamedTuple,
    TypedDict, Protocol, Literal, Type, Final, Union, Optional, Callable, NoReturn, ClassVar, Self, NewType, Annotated,
    TypeVar, AnyStr, Sequence, Mapping, MutableMapping, Iterable, Iterator, AsyncIterable, AsyncIterator, Generator,
    Coroutine, ContextManager, AsyncContextManager
import collections
from dataclasses import dataclass

@dataclass
class TypeValidator:
    validate_type: callable
    validate_items: callable
    description: str

def verify(value, expected_type, deep_check):
    if expected_type in VALIDATORS:
        validator = VALIDATORS[expected_type]
        if not validator.validate_type(value):
            return False
        if deep_check:
            return validator.validate_items(value)
        return True
    return isinstance(value, expected_type)

VALIDATORS = {
    list: TypeValidator(
        validate_type=lambda value: isinstance(value, list),
        validate_items=lambda value, item_type, deep_check: all(verify(item, item_type, deep_check) for item in value),
        description="Validator for list types"
    ),
    dict: TypeValidator(
        validate_type=lambda value: isinstance(value, dict),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(v, value_type, deep_check)
            for k, v in value.items()
        ),
        description="Validator for dictionary types"
    ),
    tuple: TypeValidator(
        validate_type=lambda value: isinstance(value, tuple),
        validate_items=lambda value, *args, deep_check: (
            len(value) == len(args) and all(verify(value[i], args[i], deep_check) for i in range(len(args)))
        ),
        description="Validator for tuple types"
    ),
    set: TypeValidator(
        validate_type=lambda value: isinstance(value, set),
        validate_items=lambda value, item_type, deep_check: all(verify(item, item_type, deep_check) for item in value),
        description="Validator for set types"
    ),
    frozenset: TypeValidator(
        validate_type=lambda value: isinstance(value, frozenset),
        validate_items=lambda value, item_type, deep_check: all(verify(item, item_type, deep_check) for item in value),
        description="Validator for frozenset types"
    ),
    collections.deque: TypeValidator(
        validate_type=lambda value: isinstance(value, collections.deque),
        validate_items=lambda value, item_type, deep_check: all(verify(item, item_type, deep_check) for item in value),
        description="Validator for deque types"
    ),
    collections.defaultdict: TypeValidator(
        validate_type=lambda value: isinstance(value, collections.defaultdict),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(v, value_type, deep_check)
            for k, v in value.items()
        ),
        description="Validator for defaultdict types"
    ),
    collections.OrderedDict: TypeValidator(
        validate_type=lambda value: isinstance(value, collections.OrderedDict),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(v, value_type, deep_check)
            for k, v in value.items()
        ),
        description="Validator for OrderedDict types"
    ),
    collections.ChainMap: TypeValidator(
        validate_type=lambda value: isinstance(value, collections.ChainMap),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(map_item[k], value_type, deep_check)
            for map_item in value.maps for k in map_item
        ),
        description="Validator for ChainMap types"
    ),
    collections.Counter: TypeValidator(
        validate_type=lambda value: isinstance(value, collections.Counter),
        validate_items=lambda value, key_type, deep_check: all(verify(k, key_type, deep_check) for k in value),
        description="Validator for Counter types"
    ),
    Any: TypeValidator(
        validate_type=lambda value: True,
        validate_items=lambda value: True,
        description="Validator that always passes (Any)"
    ),
    Callable: TypeValidator(
        validate_type=lambda value: callable(value),
        validate_items=lambda value, return_type, deep_check: True,  # Signatura se neověřuje
        description="Validator for callable types"
    ),
}
