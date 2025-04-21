from typing import Any, get_args

from ._base_type_validator import BaseTypeValidator


class IterableValidatorBase(BaseTypeValidator):
    """
    Základní třídy pro seznamové anotace.

    Použito pro: List, Set
    """

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, self.GET_ORIGIN)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Načtení vnitřních anotací
        inner_args = get_args(annotation)

        # Pokud nemáme specifikované vnitřní typy, vrátíme True
        if not inner_args:
            return True

        # Cyklus pro vnitřní validaci
        for item in value:

            # Odpočet zanoření pro další kontrolu
            depth_check = self._reduce_depth_check(depth_check)

            # Validace hdnoty na základě vnitřních položek
            self.validate_typing(item, inner_args[0], depth_check, custom_types, bool_only)

            # Kontrola vyčerpání zanoření (přerušení cyklu)
            if not depth_check:
                break

        return True

