from typing import get_origin, get_args, List, Dict, Tuple, Set


def verify_type(value, expected_type):
    """Ověří, zda hodnota odpovídá očekávanému typu, včetně zanořených generických typů."""

    # 1️⃣ Ověření, zda se jedná o obyčejný typ (int, str, float, ...)
    if isinstance(expected_type, type):
        if isinstance(value, expected_type):
            return True
        raise TypeError(f"Očekáván typ {expected_type}, obdržen {type(value)}")

    # 2️⃣ Ověření, zda jde o generický typ
    if _verify_generic_type(value, expected_type):
        return True

    # 3️⃣ Pokud to není ani obyčejný typ, ani generický typ → chyba
    raise TypeError(f"Neplatný typ pro ověření: {expected_type}")


def _verify_generic_type(value, expected_type):
    """Ověří, zda hodnota odpovídá generickému typu, včetně vnořených struktur."""

    origin = get_origin(expected_type)  # Např. `list` pro `List[int]`
    args = get_args(expected_type)  # Např. `(int,)` pro `List[int]`

    if origin is None:
        return False  # Není to generický typ, vracíme False

    if not isinstance(value, origin):
        raise TypeError(f"Očekáván typ {origin}, obdržen {type(value)}")

    # Rekurzivní ověření vnořených typů
    _verify_inner_contents(value, args)
    return True


def _verify_inner_contents(container, expected_inner_types):
    """Rekurzivně ověřuje obsah generických typů."""

    if isinstance(container, (list, set, tuple)):
        inner_type = expected_inner_types[0]

        for index, item in enumerate(container):
            try:
                verify_type(item, inner_type)
            except TypeError as e:
                raise TypeError(f"Chyba na indexu [{index}]: {e}")

    elif isinstance(container, dict):
        key_type, value_type = expected_inner_types

        for key, value in container.items():
            try:
                verify_type(key, key_type)
            except TypeError as e:
                raise TypeError(f"Chyba v klíči `{key}`: {e}")

            try:
                verify_type(value, value_type)
            except TypeError as e:
                raise TypeError(f"Chyba v hodnotě `{key}: {value}`: {e}")
