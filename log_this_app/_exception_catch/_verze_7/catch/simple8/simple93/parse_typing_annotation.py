import typing
import types
import inspect
from collections.abc import Mapping, Sequence


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
        return annotation.__name__

    # Zpracování Union typů
    if origin is typing.Union:
        return {"union": tuple(parse_typing_annotation(arg) for arg in args)}

    # Zpracování Any
    if annotation is typing.Any:
        return "Any"

    # Zpracování Optional (což je vlastně Union[type, None])
    if origin is typing.Union and type(None) in args:
        non_none_args = [arg for arg in args if arg is not type(None)]
        if len(non_none_args) == 1:
            return {"optional": parse_typing_annotation(non_none_args[0])}
        else:
            return {"optional": {"union": tuple(
                parse_typing_annotation(arg) for arg in non_none_args)}}

    # Zpracování List, Tuple, Set, atd.
    if origin in (list, typing.List):
        if len(args) == 0:
            return {"list": "Any"}
        elif len(args) == 1:
            return {"list": parse_typing_annotation(args[0])}
        else:
            return {"list": tuple(parse_typing_annotation(arg) for arg in args)}

    if origin in (tuple, typing.Tuple):
        if len(args) == 0:
            return {"tuple": "Any"}
        elif len(args) == 2 and args[1] is Ellipsis:
            # Tuple[T, ...] - homogenní tuple
            return {"tuple": {"repeat": parse_typing_annotation(args[0])}}
        else:
            # Tuple[T1, T2, ...] - heterogenní tuple
            return {
                "tuple": tuple(parse_typing_annotation(arg) for arg in args)}

    if origin in (dict, typing.Dict):
        if len(args) == 0:
            return {"dict": ("Any", "Any")}
        elif len(args) == 2:
            return {"dict": (
            parse_typing_annotation(args[0]), parse_typing_annotation(args[1]))}

    if origin in (set, typing.Set):
        if len(args) == 0:
            return {"set": "Any"}
        elif len(args) == 1:
            return {"set": parse_typing_annotation(args[0])}

    # Zpracování Literal
    if origin is typing.Literal:
        return {"literal": args}

    # Zpracování Callable
    if origin is typing.Callable:
        if len(args) == 0 or args[0] is Ellipsis:
            return {"callable": ("Any", parse_typing_annotation(args[1]) if len(
                args) > 1 else "Any")}
        else:
            params = [parse_typing_annotation(arg) for arg in args[0]]
            return_type = parse_typing_annotation(args[1]) if len(
                args) > 1 else "Any"
            return {"callable": (params, return_type)}

    # Zpracování TypedDict, NamedTuple
    if inspect.isclass(annotation) and hasattr(annotation, "__annotations__"):
        if issubclass(annotation, typing.TypedDict) or issubclass(annotation,
                                                                  tuple) and hasattr(
                annotation, "_field_types"):
            field_types = {}
            if issubclass(annotation, typing.TypedDict):
                for field, field_type in annotation.__annotations__.items():
                    field_types[field] = parse_typing_annotation(field_type)
                return {"typed_dict": field_types}
            else:  # NamedTuple
                for field, field_type in annotation._field_types.items():
                    field_types[field] = parse_typing_annotation(field_type)
                return {"named_tuple": field_types}

    # Zpracování dalších generických typů (Sequence, Mapping, atd.)
    if origin is not None:
        origin_name = getattr(origin, "__name__", str(origin))
        if len(args) == 0:
            return {origin_name.lower(): "Any"}
        elif len(args) == 1:
            return {origin_name.lower(): parse_typing_annotation(args[0])}
        else:
            return {origin_name.lower(): tuple(
                parse_typing_annotation(arg) for arg in args)}

    # Pro ostatní případy vrátíme název typu jako string
    if hasattr(annotation, "__name__"):
        return annotation.__name__

    # Pro neznámé typy vrátíme jejich string reprezentaci
    return str(annotation)

