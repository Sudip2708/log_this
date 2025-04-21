from typing import Any, Type, Union, get_origin, get_args

TypingAnnotation = Any


TYPING_COMMANDS = {
    "list": lambda self: list_verification(self),
}


def list_verification(self):
    # Validace hodoty (vyvolá výjimku v případě nevalidní hodnoty)
    self.validate_native_type(self.value, list)
    # Pokud není požadavek na vnitřní kontrolu (a nebo je již vyčerpaná) vraď True
    if not self.inner_check:
        return True
    # Získání vnitřní anotace:
    item_annotation = get_args(self.annotation)
    # Ověření vnitřních položek
    for item in self.value:
        # Korekce hodnoty inner_check, a případné vrácení True při jejím vyčerpání
        inner_check = self.get_new_inner_check()
        # Validace položky
        self(item, item_annotation, inner_check)


class ValidateTypingData:

    value = None
    annotation = None
    inner_check = None
    command = None
    content = None

    def set_command_and_content(self):
        command, content = self.get_command_and_content()
        self.command, self.content = command, content

    def get_new_inner_check(self):
        if isinstance(self.inner_check, int):
            return self.inner_check - 1 if self.inner_check > 0 else False
        return self.inner_check

    def __call__(
            self,
            value: Any,
            type_annotation: Union[Type, TypingAnnotation],
            inner_check: Union[bool, int] = True
    ):
        self.value = value
        self.annotation = type_annotation
        self.inner_check = inner_check
        return self.validate_typing_annotation()

    def recursive_validation(self):
        # Vtyvoření obsahu atributů
        self.set_command_and_content()
        # Provedení ověření
        self.command(self)
        # Ověření požadavku na vnitřní kontrolu
        if not self.inner_check or not self.content:
            return True
        # Rekurzivní volání pro hlubší úroveň porovnání
        return self.recursive_validation()


    def validate_typing_annotation(self):
        # Přednostní vyřízení pro případy jednoduchého ověření typu (int, str, bool, ...)
        if isinstance(self.annotation, type):
            return self.validate_native_type(self.value, self.annotation)
        # Přednostní vyřízení pro případy jednoduchého ověření typu typové anotace knihovny typing
        if not self.inner_check and isinstance(get_origin(self.annotation), type):
            return self.validate_native_type(self.value, get_origin(self.annotation))
        # Zpracování všech ostatních případů
        return self.recursive_validation()

    @staticmethod
    def validate_native_type(value, annotation):
        # Ověření, zda hodnota odpovídá očekávané instanci
        if isinstance(value, annotation):
            return True

    def get_command_and_content(self):
        typing_code = self._get_typing_code()
        command_str = typing_code.pop(0)
        command = self._get_command_from_typing_code(command_str)
        content = self._clean_content_in_typing_code(typing_code)
        return command, content

    def _get_typing_code(self):
        """Funkce na převod anotace knihovny typing na tuple hodnot"""
        # Převod na řetězec a malé písmena
        string = str(self.annotation).lower()
        # Odstranění případných výskytů typing
        string = string.replace("typing.", "")
        # Obalení hramatých závorek čárkami
        string = string.replace("[", ",[,")
        string = string.replace("]", ",],")
        # Vymazání prázdných míst
        string = string.replace(" ", "")
        # Odstranění zdvojených čárek
        while ",," in string:
            string = string.replace(",,", ",")
        # Odstranění případné koncové čárky
        string = string[:-1] if string[-1] == "," else string
        # Navrácení tuple s hodnotami
        return list(string.split(","))

    @staticmethod
    def _get_command_from_typing_code(command_str):
        command = TYPING_COMMANDS.get(command_str)
        if not command:
            raise ValueError(
                f"Nepovedlo se rozpoznat příkaz: {command_str}"
            )
        return command

    @staticmethod
    def _clean_content_in_typing_code(typing_code):
        if typing_code:
            if typing_code[0] == "[":
                if typing_code[-1] == "]":
                    return typing_code[1:-1]
                raise ValueError("Špatný zápis, chybí koncová závorka")
        return typing_code
