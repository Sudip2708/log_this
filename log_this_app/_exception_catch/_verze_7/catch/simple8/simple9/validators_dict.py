from typing import Dict

from .type_validator_dataclass import TypeValidator


# Globální registr validátorů
VALIDATORS: Dict[type, TypeValidator] = {}


# Funkce pro registraci validátorů
def register_validator(
        type_origin,
        validate_type,
        validate_items,
        description=None
):
    VALIDATORS[type_origin] = TypeValidator(
        validate_type=validate_type,
        validate_items=validate_items,
        description=description
    )