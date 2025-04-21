from typing import Any, Type, Union, get_origin, get_args

from .recursive_validator import recursive_validator
from .validate_native_type import validate_native_type
from .get_typing_code import get_typing_code
from .get_typing_command_and_content import get_typing_command_and_content

# Definice typové anotace pro typové anotace knihovny typing
TypingAnnotation = Any

def validator(
        value: Any,
        type_annotation: Union[Type, TypingAnnotation],
        inner_check: Union[bool, int] = True
):
    """Validátor pro ověření hodnoty na základě typových anotací knihovny typing"""

    # Přednostní vyřízení pro případy jednoduchého ověření typu (int, str, bool, ...)
    # (zde nehraje roli, zda je vnitřní kontrola)
    if isinstance(type_annotation, type):
        return validate_native_type(value, type_annotation)

    # Přednostní vyřízení pro případy jednoduchého ověření typu typové anotace knihovny typing
    # (bez kontroly vnitřních položek)
    if isinstance(get_origin(type_annotation), type) and not inner_check:
        return validate_native_type(value, get_origin(type_annotation))

    # Zpracování všech ostatních případů
    # Získání sezamu s textovými příkazy anotace
    typing_code = get_typing_code(type_annotation)
    # Oddělení první podmínky a zbytku
    command, content = get_typing_command_and_content(typing_code)
    return recursive_validator(
        command,
        content,
        value,
        type_annotation,
        inner_check
    )
