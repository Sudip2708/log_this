from typing import Any, List, Union, get_args
import traceback

from ..typing_data import ValidateTypingData



TYPING_COMMANDS = {
    "_list": lambda self: list_verification(self),
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

