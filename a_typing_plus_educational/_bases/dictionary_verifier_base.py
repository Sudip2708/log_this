from typing import Any, Tuple, Union, get_args

from ._base_verifier import BaseVerifier
from .._validators import dictionary_validator


class DictionaryValidatorBase(BaseVerifier):
    """
    Základní třída pro validační třídy pracující se slovníkovými strukturami.

    Slouží jako rodičovská třída pro validační logiku typů jako `Dict`, `Mapping`, `DefaultDict` nebo `OrderedDict`.

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
        Přetížení metody __call__ pro validaci slovníkových struktur.

        Validuje:
        - zda `value` odpovídá základnímu typu (např. dict)
        - klíče a hodnoty, pokud je požadována vnitřní validace

        Returns:
            bool: True, pokud validace proběhne úspěšně, jinak vyhazuje výjimku
        """

        # Navrácení výstupu funkce pro validaci slovníkových objektů
        return dictionary_validator(
            value, self.ORIGIN, annotation, depth_check, custom_types, bool_only
        )

