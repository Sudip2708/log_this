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
    if container_type in {list, deque}:
        for item in value:
            verify(item, inner_types[0])

    elif container_type in {set, frozenset}:
        for item in value:
            verify(item, inner_types[0])

    elif container_type is tuple:
        if len(inner_types) == 2 and inner_types[1] is Ellipsis:
            for item in value:
                verify(item, inner_types[0])
        else:
            for inner_type, inner_value in zip(inner_types, value):
                verify(inner_value, inner_type)

    elif container_type in {dict, defaultdict, OrderedDict, ChainMap, Counter}:
        key_type, value_type = inner_types
        for key, val in value.items():
            verify(key, key_type)
            verify(val, value_type)

    elif container_type in {Union, Optional}:
        if not any(verify(value, t) for t in inner_types):
            raise TypeError(f"{value} neodpovídá žádnému z typů {inner_types}")

    elif container_type is Literal:
        if value not in inner_types:
            raise TypeError(f"{value} není mezi povolenými hodnotami {inner_types}")

    elif container_type is Type:
        if not isinstance(value, type) or not issubclass(value, inner_types[0]):
            raise TypeError(f"{value} není podtyp {inner_types[0]}")

    elif container_type is Final:
        return True  # Final se neověřuje

    elif container_type is Concatenate:
        return True  # Concatenate se používá jen u Callable

    else:
        raise TypeError(f"Nepodporovaný generický typ: {container_type}")

    return True

