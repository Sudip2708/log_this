from typing import Any, Type, Union, get_origin, ParamSpec

from .typing_data import TypingData
from .validate_native_type import ValidateNativeType

# Definice typové anotace pro typové anotace knihovny typing
TypingAnnotation = Union[ParamSpec, Any]


class ValidateTypingAnnotation:
    """Validátor pro ověření hodnoty na základě typových anotací knihovny typing"""

    # Načtení instance pro validaci typu
    validate_native_type = ValidateNativeType()

    def __call__(
            self,
            value: Any,
            type_annotation: Union[Type, TypingAnnotation],
            inner_check: Union[bool, int] = True
    ):

        # Přednostní vyřízení pro případy jednoduchého ověření typu (int, str, bool, ...)
        # (zde nehraje roli, zda je vnitřní kontrola)
        if isinstance(type_annotation, type):
            return self.validate_native_type(value, type_annotation)

        # Přednostní vyřízení pro případy jednoduchého ověření typu typové anotace knihovny typing
        # (bez kontroly vnitřních položek)
        if isinstance(get_origin(type_annotation), type) and not inner_check:
            return self.validate_native_type(value, get_origin(type_annotation))

        # Zpracování všech ostatních případů
        typing_data = TypingData(self, value, type_annotation, inner_check)
        return typing_data.recursive_validation()
