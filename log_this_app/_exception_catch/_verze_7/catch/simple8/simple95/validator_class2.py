from typing import Any, Type, Union, get_origin, get_args

from .recursive_validator import recursive_validator
from .validate_native_type import ValidateNativeType
from .get_typing_code import get_typing_code
from .get_typing_command_and_content import get_typing_command_and_content

# Definice typové anotace pro typové anotace knihovny typing
TypingAnnotation = Any

from .get_typing_code import GetTypingCodeMixin
from .get_typing_command_and_content import GetTypingCommandAndContentMixin
from .typing_commands import ListMixin
from .typing_commands._list2 import list_verifier


class TypingValidator(
    GetTypingCodeMixin,
    GetTypingCommandAndContentMixin,
    ListMixin
):
    """Validátor pro ověření hodnoty na základě typových anotací knihovny typing"""

    # Slovník s příkazy
    TYPING_COMMANDS = {
        "tuple": lambda c, v, e, i: _tuple(c, v, e, i),
        "list": lambda instance: _list_verifier(instance),
        "list2": _list,
        "union": lambda c, v, e, i: _union(c, v, e, i),

    }

    # Načtení instance pro validaci typu
    validate_native_type = ValidateNativeType()
    _value = None
    _annotation = None
    _inner_check = None
    _typing_code = None
    _command = None
    _content = None

    def validate_typing(
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
        self._value = value
        self._annotation = type_annotation
        self._inner_check = inner_check

        # Získání sezamu s textovými příkazy anotace
        self._typing_code = self.get_typing_code()
        # Oddělení první podmínky a zbytku
        self._command, self._content = self.get_typing_command_and_content()
        return self.recursive_validator()
