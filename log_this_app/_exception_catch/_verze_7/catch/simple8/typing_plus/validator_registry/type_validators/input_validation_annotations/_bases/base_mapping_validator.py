from typing import Any, Tuple, Union, get_args

from ._base_validator import BaseValidator
from ..._validators import validate_native_type, validate_typing
from .._tools import reduce_depth_check


class BaseMappingValidator(BaseValidator):
    """
    Základní třída pro validační třídy pracující se slovníkovými strukturami.

    Slouží jako rodičovská třída pro validační logiku typů jako `Dict`, `Mapping`, `DefaultDict` nebo `OrderedDict`.

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
        Přetížení metody __call__ pro validaci slovníkových struktur.

        Validuje:
        - zda `value` odpovídá základnímu typu (např. dict)
        - klíče a hodnoty, pokud je požadována vnitřní validace

        Returns:
            bool: True, pokud validace proběhne úspěšně, jinak vyhazuje výjimku
        """

        # Validace základního typu (např. dict)
        self.validate_native_type(value, self.ORIGIN)

        # Pokud není požadována vnitřní validace, návrat
        if not depth_check:
            return True

        # Získání typových anotací pro klíč a hodnotu
        inner_args = get_args(annotation)

        # Pokud nemáme specifikované typy pro klíče a hodnoty, vrátíme True
        if not inner_args:
            return True

        # Načtení klíče a hodnoty
        key_type, value_type = inner_args

        # Validace každého klíče a hodnoty
        for key, val in value.items():

            # Odpočet zanoření pro další kontrolu
            depth_check = self.reduce_depth_check(depth_check)

            # Validace klíče
            self.validate_typing(
                key, key_type, depth_check, custom_types, bool_only
            )

            # Validace hodnoty
            self.validate_typing(
                val, value_type, depth_check, custom_types, bool_only
            )

            # Kontrola vyčerpání zanoření (přerušení cyklu)
            if not depth_check:
                break

        # Pokud vše proběhne v pořádku a bez chyb
        return True
