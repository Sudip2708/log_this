from typing import TypeVar, get_origin, get_args

from .validators_dict import VALIDATORS


# Hlavní validační funkce
def verify(value, expected_type, deep_check=True):
    """Ověří, zda hodnota odpovídá očekávanému typu, včetně generických typů."""

    # Získat základní typ
    origin = get_origin(expected_type) or expected_type

    # Pokud deep_check=False nebo deep_check=0, neověřujeme vnitřní strukturu
    if not deep_check:
        deep_check = 0

    # Pokud není generický typ, ověřit přímo
    if isinstance(expected_type, type):
        if not isinstance(value, expected_type):
            raise TypeError(
                f"Očekáván typ {expected_type}, obdržen {type(value)}")
        return True

    # Ověřit, zda existuje validátor pro daný typ
    if origin not in VALIDATORS:
        raise TypeError(f"Nepodporovaný typ pro validaci: {expected_type}")

    validator = VALIDATORS[origin]

    # Ověřit samotný typ
    if not validator.validate_type(value):
        raise TypeError(f"Očekáván typ {origin}, obdržen {type(value)}")

    # Při deep_check=False vracíme True zde
    # Pokud deep_check je 0, ukončit validaci zde
    if deep_check == 0:
        return True

    # Ověřit vnitřní položky
    args = get_args(expected_type)
    return validator.validate_items(
        value,
        *args,
        deep_check=(
            deep_check - 1
            if isinstance(deep_check, int)
            else deep_check
        )
    )
