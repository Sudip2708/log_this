from typing import get_origin, get_args, Union, List, Dict, Set, Tuple, Any, Optional,


def verify(value, expected_type):
    """Ověří, zda hodnota odpovídá očekávanému typu, včetně generických typů."""

    # Ověří typu (je-li expected_type předáno jako typ)
    if verify_type(value, expected_type):
        return True

    # Ověří generického typu (je-li expected_type předáno jako generický typ)
    if verify_generic_type(value, expected_type):
        return True

    # Pokud ani jeedno ověření není pravdivé (nejedná se o typ ani generický typ)
    raise TypeError(f"Neplatný typ pro ověření: {expected_type}")


def verify_type(value, expected_type):
    """Ověří, zda hodnota odpovídá očekávanému typu."""

    # Přímé ověření typu (pokud expected_type je předán jako typ str, int, ...)
    if isinstance(expected_type, type):

        # Ověření pravdivosti
        if isinstance(value, expected_type):
            return True

        # Vyvolání výjimky pokud se ověření nepvedlo
        raise TypeError(
            f"Očekáván typ {expected_type}, obdržen {type(value)}")

    # Pokud expected_type není obyčejným typem
    return False

def verify_generic_type(value, generic_type):
    """Ověří, zda hodnota odpovídá očekávanému generickému typu."""

    # Ověření, zda jde o generický typ
    container_type = get_origin(generic_type)
    if container_type is None:
        return False  # Není generický typ

    # Oveření zda kontejner odpovídá danému typu
    if not verify_type(value, container_type):
        raise TypeError(f"Očekáván typ kontejneru {container_type}, obdržen {type(value)}")

    # Ověření, zda jsou uvedené i vnitřní typy:
    inner_types = get_args(generic_type)
    if not inner_types:
        return True  # Kontejner nemá vnitřní typy

    # Ověření podle typu kontejneru
    if container_type in {list, tuple, set, frozenset, deque}:
        verify_container_items(value, inner_types, container_type)

    elif container_type in {dict, defaultdict, OrderedDict, ChainMap, Counter}:
        verify_dict_items(args)

    elif container_type in {Union, Optional}:
        verify_union_items(args)

    elif container_type in {NamedTuple, TypedDict, Protocol}:
        verify_structured_type(args)

    elif container_type is Literal:
        verify_literal(value, args)

    elif container_type is Type:
        verify_class_type(value, args)

    elif container_type is Final:
        return True  # Final se neověřuje

    elif container_type is Concatenate:
        return True  # Concatenate se používá jen u Callable

    else:
        raise TypeError(
            f"Nebyl zadán podporovaný objekt knihovny Typing: {container_type}.")

    return True

