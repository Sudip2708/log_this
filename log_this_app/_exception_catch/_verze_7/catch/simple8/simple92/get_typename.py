from typing import (
    get_origin, get_args, List, Dict, Tuple, Set, FrozenSet, Deque, DefaultDict, OrderedDict, ChainMap,
    Counter, NamedTuple, TypedDict, Protocol, Literal, Type, Final, Concatenate, Any, Union, Optional,
    Callable, NoReturn, ClassVar, Self, NewType, Annotated, Generic, TypeVar, AnyStr, Sequence, Mapping,
    MutableMapping, Iterable, Iterator, AsyncIterable, AsyncIterator, Generator, Coroutine,
    ContextManager, AsyncContextManager
)

def get_typename(tp):
    """Vrátí čitelný název typu malými písmeny bez hranatých závorek."""
    origin = get_origin(tp)

    # Pokud má typ `__name__`, vrátíme jeho název malými písmeny
    if hasattr(tp, "__name__"):
        return tp.__name__.lower()

    # Speciální případy, kde origin je None
    special_types = {
        Any: "any",
        NoReturn: "noreturn",
        Final: "final",
        Self: "self",
    }
    if tp in special_types:
        return special_types[tp]

    # Pokud má origin, jde o generický typ -> vrátíme pouze název základu
    if origin:
        return origin.__name__.lower()

    # Pokud není nic nalezeno, vrátíme stringovou reprezentaci typu malými písmeny
    return str(tp).lower()

# Testy pro různé typy
print(get_typename(List[int]))           # "list"
print(get_typename(Dict[str, int]))      # "dict"
print(get_typename(Tuple[int, str]))     # "tuple"
print(get_typename(Callable[[int, str], bool]))  # "callable"
print(get_typename(Union[int, str, None]))  # "union"
print(get_typename(Optional[int]))       # "union"
print(get_typename(ClassVar[int]))       # "classvar"
print(get_typename(Annotated[int, "metadata"]))  # "annotated"
