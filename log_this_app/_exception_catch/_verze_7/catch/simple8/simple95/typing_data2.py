from typing import Any, Type, Union, get_origin, get_args

from .get_typing_code import GetTypingCode
from .typing_commands._list2 import ListVerification


TypingAnnotation = Any

@dataclasses
class TypingData:
    value = None
    annotation = None
    inner_check = None
    command = ListVerification()
    content = None


    def set_command_and_content(self):
        get_method = GetTypingCode()
        command, content = get_method(self.annotation)
        self.command, self.content = command, content

    def command_verification(self, validator):
        self.command(self, validator)

    def get_new_inner_check(self):
        if isinstance(self.inner_check, int):
            if self.inner_check > 0:
                return self.inner_check - 1
            else:
                return False
        return self.inner_check


class ValidateTypingData:


    def __call__(
            self,
            value: Any,
            type_annotation: Union[Type, TypingAnnotation],
            inner_check: Union[bool, int] = True
    ):
        self.data = TypingData(self)
        self.data.value = value
        self.data.annotation = type_annotation
        self.data.inner_check = inner_check
        return self._validate_typing_annotation()



    def _recursive_validation(self):

        # Vtyvoření obsahu atributů
        self.data.set_command_and_content()

        # Provedení ověření
        self.data.command_verification(self)

        # Ověření požadavku na vnitřní kontrolu
        if not self.data.inner_check or not self.data.content:
            return True

        # Rekurzivní volání pro hlubší úroveň porovnání
        self._recursive_validation()


    def validate_typing_annotation(self):

        # Přednostní vyřízení pro případy jednoduchého ověření typu (int, str, bool, ...)
        # (zde nehraje roli, zda je vnitřní kontrola)
        if isinstance(self.data.annotation, type):
            return self.validate_native_type()

        # Přednostní vyřízení pro případy jednoduchého ověření typu typové anotace knihovny typing
        # (bez kontroly vnitřních položek)
        if (
                not self.data.inner_check
                and isinstance(get_origin(self.data.annotation), type)
        ):
            self.data.annotation = get_origin(self.data.annotation)
            return self.validate_native_type()

        # Zpracování všech ostatních případů
        return self._recursive_validation()


    def validate_native_type(self):
        """
        Ověří, zda je poskytnutá hodnota instancí očekávaného typu.

        Args:
            value: Hodnota k ověření. Může být libovolného typu.
            expected: Očekávaný typ nebo tuple očekávaných typů.

        Returns:
            True, pokud je `value` instancí `expected` typu (nebo jednoho z typů v `expected` tuple).

        Raises:
            VerifyValueTypeError: Pokud `value` není instancí očekávaného typu.
            VerifyExpectedTypeError: Pokud `expected` není platný typ nebo tuple typů.
            VerifyInternalUnexpectedError: Pokud během validace dojde k neočekávané vnitřní chybě.
        """

        # Ověření, zda hodnota odpovídá očekávané instanci
        if isinstance(self.value, self.type_annotation):
            return True
