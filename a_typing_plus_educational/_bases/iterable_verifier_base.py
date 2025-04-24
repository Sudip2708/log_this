from typing import Any, Tuple, Union, get_args

from ._base_verifier import BaseVerifier
from .._validators import iterable_validator

class IterableValidatorBase(BaseVerifier):
    """
    Základní třída pro validační třídy pracující se seznamovými strukturami.

    Slouží jako rodičovská třída pro validační logiku typů jako `List` nebo `Set`.

    Příklad použití:
        # TODO: doplnit konkrétní třídy, které dědí z této třídy a příklad použití
    """

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

        # Navrácení výstupu funkce pro validaci iterovatelných objektů
        return iterable_validator(
            value, self.ORIGIN, annotation, depth_check, custom_types, bool_only
        )


