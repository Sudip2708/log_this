from typing import Any, Tuple, Union, get_args

from .isinstance_validator import validate_is_instance
from .typing_validator import validate_typing
from ._reduce_depth_check import reduce_depth_check

class IterableValidator:
    """
    Základní třída pro validační třídy pracující se seznamovými strukturami.

    Slouží jako rodičovská třída pro validační logiku typů jako `List` nebo `Set`.

    Příklad použití:
        # TODO: doplnit konkrétní třídy, které dědí z této třídy a příklad použití
    """

    def __call__(
        self,
        value: Any,
        expected: Union[type, Tuple[type, ...]],
        annotation: Any = None,
        depth_check: Union[bool, int] = True,
        custom_types: Tuple[Any, ...] = None,
        bool_only: bool = False
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
        validate_is_instance(value, expected, bool_only)

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
            depth_check = reduce_depth_check(depth_check)

            # Validace hdnoty na základě vnitřních položek
            validate_typing(
                item, inner_args[0], depth_check, custom_types, bool_only
            )

            # Kontrola vyčerpání zanoření (přerušení cyklu)
            if not depth_check:
                break

        return True
