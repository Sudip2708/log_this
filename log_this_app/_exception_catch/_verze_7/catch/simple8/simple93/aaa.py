import typing
import types
import inspect
from collections.abc import Mapping, Sequence


# def parse_typing_annotation(annotation):
#     """
#     Rozloží typovou anotaci z knihovny typing na její základní komponenty.
#
#     Args:
#         annotation: Typová anotace (např. List[str], Union[int, str], atd.)
#
#     Returns:
#         Strukturovaná reprezentace typové anotace jako slovník nebo tuple
#     """
#     # Získání původního typu (pro generické typy)
#     origin = typing.get_origin(annotation)
#     args = typing.get_args(annotation)
#
#     # Zpracování základních typů (str, int, bool, atd.)
#     if origin is None and isinstance(annotation, type):
#         return annotation.__name__
#
#     # Zpracování Union typů
#     if origin is typing.Union:
#         return {"union": tuple(parse_typing_annotation(arg) for arg in args)}
#
#     # Zpracování Any
#     if annotation is typing.Any:
#         return "Any"
#
#     # Zpracování Optional (což je vlastně Union[type, None])
#     if origin is typing.Union and type(None) in args:
#         non_none_args = [arg for arg in args if arg is not type(None)]
#         if len(non_none_args) == 1:
#             return {"optional": parse_typing_annotation(non_none_args[0])}
#         else:
#             return {"optional": {"union": tuple(
#                 parse_typing_annotation(arg) for arg in non_none_args)}}
#
#     # Zpracování List, Tuple, Set, atd.
#     if origin in (list, typing.List):
#         if len(args) == 0:
#             return {"list": "Any"}
#         elif len(args) == 1:
#             return {"list": parse_typing_annotation(args[0])}
#         else:
#             return {"list": tuple(parse_typing_annotation(arg) for arg in args)}
#
#     if origin in (tuple, typing.Tuple):
#         if len(args) == 0:
#             return {"tuple": "Any"}
#         elif len(args) == 2 and args[1] is Ellipsis:
#             # Tuple[T, ...] - homogenní tuple
#             return {"tuple": {"repeat": parse_typing_annotation(args[0])}}
#         else:
#             # Tuple[T1, T2, ...] - heterogenní tuple
#             return {
#                 "tuple": tuple(parse_typing_annotation(arg) for arg in args)}
#
#     if origin in (dict, typing.Dict):
#         if len(args) == 0:
#             return {"dict": ("Any", "Any")}
#         elif len(args) == 2:
#             return {"dict": (
#             parse_typing_annotation(args[0]), parse_typing_annotation(args[1]))}
#
#     if origin in (set, typing.Set):
#         if len(args) == 0:
#             return {"set": "Any"}
#         elif len(args) == 1:
#             return {"set": parse_typing_annotation(args[0])}
#
#     # Zpracování Literal
#     if origin is typing.Literal:
#         return {"literal": args}
#
#     # Zpracování Callable
#     if origin is typing.Callable:
#         if len(args) == 0 or args[0] is Ellipsis:
#             return {"callable": ("Any", parse_typing_annotation(args[1]) if len(
#                 args) > 1 else "Any")}
#         else:
#             params = [parse_typing_annotation(arg) for arg in args[0]]
#             return_type = parse_typing_annotation(args[1]) if len(
#                 args) > 1 else "Any"
#             return {"callable": (params, return_type)}
#
#     # Zpracování TypedDict, NamedTuple
#     if inspect.isclass(annotation) and hasattr(annotation, "__annotations__"):
#         if issubclass(annotation, typing.TypedDict) or issubclass(annotation,
#                                                                   tuple) and hasattr(
#                 annotation, "_field_types"):
#             field_types = {}
#             if issubclass(annotation, typing.TypedDict):
#                 for field, field_type in annotation.__annotations__.items():
#                     field_types[field] = parse_typing_annotation(field_type)
#                 return {"typed_dict": field_types}
#             else:  # NamedTuple
#                 for field, field_type in annotation._field_types.items():
#                     field_types[field] = parse_typing_annotation(field_type)
#                 return {"named_tuple": field_types}
#
#     # Zpracování dalších generických typů (Sequence, Mapping, atd.)
#     if origin is not None:
#         origin_name = getattr(origin, "__name__", str(origin))
#         if len(args) == 0:
#             return {origin_name.lower(): "Any"}
#         elif len(args) == 1:
#             return {origin_name.lower(): parse_typing_annotation(args[0])}
#         else:
#             return {origin_name.lower(): tuple(
#                 parse_typing_annotation(arg) for arg in args)}
#
#     # Pro ostatní případy vrátíme název typu jako string
#     if hasattr(annotation, "__name__"):
#         return annotation.__name__
#
#     # Pro neznámé typy vrátíme jejich string reprezentaci
#     return str(annotation)


def check_type(value, type_annotation):
    """
    Zkontroluje, zda hodnota odpovídá dané typové anotaci.

    Args:
        value: Hodnota k ověření
        type_annotation: Typová anotace (např. List[str], Union[int, str], atd.)

    Returns:
        bool: True, pokud hodnota odpovídá typové anotaci, jinak False
    """
    parsed_type = parse_typing_annotation(type_annotation)
    return validate_value(value, parsed_type)


def validate_value(value, parsed_type):
    """
    Ověří hodnotu proti rozložené typové anotaci.

    Args:
        value: Hodnota k ověření
        parsed_type: Rozložená typová anotace z funkce parse_typing_annotation

    Returns:
        bool: True, pokud hodnota odpovídá typové anotaci, jinak False
    """
    # Kontrola pro základní typy (str, int, bool, atd.)
    if isinstance(parsed_type, str):
        if parsed_type == "Any":
            return True
        if parsed_type == "None" and value is None:
            return True
        try:
            type_class = eval(parsed_type)
            return isinstance(value, type_class)
        except (NameError, SyntaxError):
            return str(type(value).__name__) == parsed_type

    # Kontrola pro složené typy
    if isinstance(parsed_type, dict):
        # Kontrola pro Union
        if "union" in parsed_type:
            return any(
                validate_value(value, arg) for arg in parsed_type["union"])

        # Kontrola pro Optional
        if "optional" in parsed_type:
            return value is None or validate_value(value,
                                                   parsed_type["optional"])

        # Kontrola pro List
        if "list" in parsed_type:
            if not isinstance(value, list):
                return False
            if parsed_type["list"] == "Any":
                return True
            if isinstance(parsed_type["list"], tuple):
                # Heterogenní list se specifickými typy pro každý prvek
                if len(value) != len(parsed_type["list"]):
                    return False
                return all(
                    validate_value(value[i], parsed_type["list"][i]) for i in
                    range(len(value)))
            else:
                # Homogenní list s jedním typem pro všechny prvky
                return all(
                    validate_value(item, parsed_type["list"]) for item in value)

        # Kontrola pro Tuple
        if "tuple" in parsed_type:
            if not isinstance(value, tuple):
                return False
            if parsed_type["tuple"] == "Any":
                return True
            if isinstance(parsed_type["tuple"], dict) and "repeat" in \
                    parsed_type["tuple"]:
                # Homogenní tuple (Tuple[T, ...])
                return all(
                    validate_value(item, parsed_type["tuple"]["repeat"]) for
                    item in value)
            if isinstance(parsed_type["tuple"], tuple):
                # Heterogenní tuple (Tuple[T1, T2, ...])
                if len(value) != len(parsed_type["tuple"]):
                    return False
                return all(
                    validate_value(value[i], parsed_type["tuple"][i]) for i in
                    range(len(value)))

        # Kontrola pro Dict
        if "dict" in parsed_type:
            if not isinstance(value, dict):
                return False
            if parsed_type["dict"] == ("Any", "Any"):
                return True
            key_type, value_type = parsed_type["dict"]
            return all(
                validate_value(k, key_type) and validate_value(v, value_type)
                for k, v in value.items())

        # Kontrola pro Set
        if "set" in parsed_type:
            if not isinstance(value, set):
                return False
            if parsed_type["set"] == "Any":
                return True
            return all(
                validate_value(item, parsed_type["set"]) for item in value)

        # Kontrola pro Literal
        if "literal" in parsed_type:
            return value in parsed_type["literal"]

        # Kontrola pro Callable
        if "callable" in parsed_type:
            if not callable(value):
                return False
            # Pro úplnou kontrolu bychom potřebovali analyzovat signaturu funkce,
            # což by bylo složitější. Prozatím jen kontrolujeme, zda je to callable.
            return True

        # Kontrola pro další generické typy
        for type_name, type_args in parsed_type.items():
            if type_name == "sequence":
                if not isinstance(value, Sequence) or isinstance(value,
                                                                 (str, bytes)):
                    return False
                if type_args == "Any":
                    return True
                return all(validate_value(item, type_args) for item in value)

            if type_name == "mapping":
                if not isinstance(value, Mapping):
                    return False
                if type_args == ("Any", "Any"):
                    return True
                key_type, value_type = type_args
                return all(validate_value(k, key_type) and validate_value(v,
                                                                          value_type)
                           for k, v in value.items())

    # Pokud nejsme schopni rozhodnout, vrátíme False
    return False

# def parse_typing_annotation(annotation):
#     name = annotation.__name__
#     origin = typing.get_origin(annotation).__name__
#     args = []
#     for arg in typing.get_args(annotation):
#         # print(str(arg))
#         if arg is Ellipsis:
#             args.append('ellipsis')
#         elif arg is int:
#             args.append('int')
#         else:
#             try:
#                 args.append(arg.__name__)
#             except Exception:
#                 args.append(arg)
#
#     return name, origin, args


# def parse_typing_annotation(annotation):
#     name = annotation.__name__
#     origin = typing.get_origin(annotation).__name__
#     args = typing.get_args(annotation)
#
#     if len(args) == 1:
#         try:
#             print("var1: ", typing.get_origin(args).__name__)
#         except Exception:
#             print("var2: ", type(args))

# def rozloz_typ_anotaci(typ_anotace):
#     typ_anotace = str(typ_anotace) #převedeme na string
#     typ_anotace = typ_anotace.replace("typing.", "") # odstraníme "typing."
#     typ_anotace = typ_anotace.replace("[", ", [") #nahradíme hranatou závorku čárkou a mezerou
#     typ_anotace = typ_anotace.replace("]", "") #odstraníme zavírací hranatou závorku
#     rozlozena_anotace = tuple(typ_anotace.split(", ")) #rozdělíme string na tuple pomocí split(", ")
#     return rozlozena_anotace
import re

# def parse_typing_expression(expr: str):
#     # Používáme regulární výraz pro rozdělení na jednotlivé části
#     expr = expr.replace("typing.", "")
#     expr = expr.replace("[", ",[,")
#     expr = expr.replace("]", ",],")
#     expr = expr.replace(" ", "")
#     expr = expr.replace(",,", ",")
#     return tuple(expr.strip().lower().split(","))

    # pattern = r'([a-zA-Z]+|\[|\]|\d+|,)'
    # xresult = tuple(re.findall(pattern, expr))
    # return xresult

def parse_typing_annotation(annotation):
    str_annotation = str(annotation).lower()
    expr = str_annotation.replace("typing.", "")
    expr = expr.replace("[", ",[,")
    expr = expr.replace("]", ",],")
    expr = expr.replace(" ", "")
    expr = expr.replace(",,", ",")
    expr = expr[:-1] if expr[-1] == "," else expr
    return tuple(expr.split(","))

# def parse_typing_annotation(annotation):
#     # Získáme stringovou reprezentaci
#     str_annotation = str(annotation)
#
#     # Odstraníme 'typing.' prefix, který se může objevit
#     expr = str_annotation.replace("typing.", "")
#
#     # Přidáme mezery kolem speciálních znaků pro snazší tokenizaci
#     expr = expr.replace("[", " [ ")
#     expr = expr.replace("]", " ] ")
#     expr = expr.replace(",", " , ")
#
#     # Rozdělíme na tokeny a odstraníme prázdné tokeny
#     tokens = [token.strip().lower() for token in expr.split() if token.strip()]
#
#     return tuple(tokens)

# Příklad použití
if __name__ == "__main__":
    # Příklady parsování typových anotací
    examples = [
        typing.List[str],
        typing.List[typing.Union[int, str]],
        typing.Dict[str, int],
        typing.Tuple[int, str, bool],
        typing.Tuple[int, ...],
        typing.Union[int, str, None],
        typing.Optional[int],
        typing.Literal[1, 2, 3],
        typing.Callable[[int, str], bool],
        typing.Sequence[int],
    ]

    # for example in examples:
    #     print(f"{example} => {parse_typing_annotation(example)}")

    # Příklady kontrol typů
    test_cases = [
        (["hello", "world"], typing.List[str]),
        (["hello", 123], typing.List[typing.Union[str, int]]),
        ({"name": "John", "age": 30}, typing.Dict[str, int]),
        ((1, "hello", True), typing.Tuple[int, str, bool]),
        ((1, 2, 3), typing.Tuple[int, ...]),
        (42, typing.Union[int, str, None]),
        (None, typing.Optional[int]),
        (2, typing.Literal[1, 2, 3]),
        (lambda x, y: x == y, typing.Callable[[int, str], bool]),
        ([1, 2, 3], typing.Sequence[int]),
    ]

    for value, type_annotation in test_cases:

        # result = check_type(value, type_annotation)
        # print(f"Hodnota {value} odpovídá typu {type_annotation}? {result}")

        result = parse_typing_annotation(type_annotation)
        print(f"Výstup pro: {type_annotation} >>> {result}")