from typing import Any, Tuple, Union, get_args

from ._base_validator import BaseValidator
from ..._validators import validate_native_type, validate_typing
from .._tools import reduce_depth_check

class BaseIterableValidator(BaseValidator):
    """
    Základní třída pro validační třídy pracující se seznamovými strukturami.

    Slouží jako rodičovská třída pro validační logiku typů jako `List` nebo `Set`.

    Příklad použití:
        # TODO: doplnit konkrétní třídy, které dědí z této třídy a příklad použití
    """

    validate_native_type = validate_native_type
    validate_typing = validate_typing
    reduce_depth_check = reduce_depth_check

    def __call__(
        self,
        value: Any,
        annotation: Any,
        depth_check: Union[bool, int],
        custom_types: Tuple[Any, ...],
        bool_only: bool
    ) -> bool:
        """
        Přetížení metody __call__ pro validaci seznamových struktur.

        Validuje:
        - zda `value` odpovídá základnímu typu (např. list, set)
        - v případě potřeby validuje i vnitřní položky vůči zadané anotaci

        Returns:
            bool: True, pokud validace proběhne úspěšně, jinak vyhazuje výjimku
        """

        # Validace základního typu (např. list, set)
        self.validate_native_type(value, self.ORIGIN, bool_only)

        # Pokud není požadována vnitřní validace, návrat
        if not depth_check:
            return True

        # Získání vnitřních typových anotací
        inner_args = get_args(annotation)

        # Pokud nemáme specifikované vnitřní typy, vrátíme True
        if not inner_args:
            return True

        # Validace jednotlivých položek
        for item in value:

            # Odpočet zanoření pro další kontrolu
            depth_check = self.reduce_depth_check(depth_check)

            # Validace hdnoty na základě vnitřních položek
            self.validate_typing(
                item, inner_args[0], depth_check, custom_types, bool_only
            )

            # Kontrola vyčerpání zanoření (přerušení cyklu)
            if not depth_check:
                break

        return True
