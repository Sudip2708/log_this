import typing
import types
import inspect
from collections.abc import Mapping, Sequence

from ._a_base import _base_typing
from ._b_union import _union_typing
from ._c_any import _any_typing
from ._d_optional import _optional_typing


def parse_typing_annotation(annotation):
    """
    Rozloží typovou anotaci z knihovny typing na její základní komponenty.

    Args:
        annotation: Typová anotace (např. List[str], Union[int, str], atd.)

    Returns:
        Strukturovaná reprezentace typové anotace jako slovník nebo tuple
    """

    # Získání původního typu (pro generické typy)
    origin = typing.get_origin(annotation)
    args = typing.get_args(annotation)

    # Zpracování základních typů (str, int, bool, atd.)
    if origin is None and isinstance(annotation, type):
        return _base_typing(annotation, origin)

    # Zpracování Union typů
    if origin is typing.Union:
        return _union_typing(origin, args)

    # Zpracování Any
    if annotation is typing.Any:
        return _any_typing(annotation)

    # Zpracování Optional (což je vlastně Union[type, None])
    if origin is typing.Union and type(None) in args:
        return _optional_typing(origin, args)

    # Zpracování List, Tuple, Set, atd.
    if origin in (list, typing.List):
        return _list_typing(origin, args)

    if origin in (tuple, typing.Tuple):
        return _tuple_typing(origin, args)

    if origin in (dict, typing.Dict):
        return _dict_typing(origin, args)

    if origin in (set, typing.Set):
        return _set_typing(origin, args)

    # Zpracování Literal
    if origin is typing.Literal:
        return _literal_typing(origin, args)

    # Zpracování Callable
    if origin is typing.Callable:
        return _callable_typing(origin, args)

    # Zpracování TypedDict, NamedTuple
    if inspect.isclass(annotation) and hasattr(annotation, "__annotations__"):
        return _typed_dict_named_tuple_typing(annotation)

    # Zpracování dalších generických typů (Sequence, Mapping, atd.)
    if origin is not None:
        return _sequence_mapping_typing(origin, args)

    # Pro ostatní případy vrátíme název typu jako string
    if hasattr(annotation, "__name__"):
        return annotation.__name__

    # Pro neznámé typy vrátíme jejich string reprezentaci
    return str(annotation)

