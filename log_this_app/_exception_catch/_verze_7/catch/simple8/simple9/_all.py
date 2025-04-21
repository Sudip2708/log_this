from dataclasses import dataclass
from typing import Callable, Any, Dict, TypeVar, Optional, get_origin, get_args

T = TypeVar('T')


@dataclass
class TypeValidator:
    validate_type: Callable[[Any], bool]
    validate_items: Callable[..., bool]
    description: Optional[str] = None


# Globální registr validátorů
VALIDATORS: Dict[type, TypeValidator] = {}


# Funkce pro registraci validátorů
def register_validator(type_origin, validate_type, validate_items,
                       description=None):
    VALIDATORS[type_origin] = TypeValidator(
        validate_type=validate_type,
        validate_items=validate_items,
        description=description
    )


# Hlavní validační funkce
def verify(value, expected_type, deep_check=True):
    """Ověří, zda hodnota odpovídá očekávanému typu, včetně generických typů."""
    # Získat základní typ
    origin = get_origin(expected_type) or expected_type

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
    if not deep_check:
        return True

    # Ověřit vnitřní položky
    args = get_args(expected_type)
    return validator.validate_items(value, *args, deep_check=deep_check)


# Registrace validátorů
register_validator(
    list,
    validate_type=lambda value: isinstance(value, list),
    validate_items=lambda value, item_type, deep_check: all(
        verify(item, item_type, deep_check) for item in value),
    description="Validator for list types"
)

# Podobně pro další typy...