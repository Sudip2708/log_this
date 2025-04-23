from typing import Any, Tuple, Union, get_args

from .isinstance_validator import validate_is_instance
from .typing_validator import validate_typing
from ._reduce_depth_check import reduce_depth_check


class BaseMappingValidator:
    """
    Základní třída pro validační třídy pracující se slovníkovými strukturami.

    Slouží jako rodičovská třída pro validační logiku typů jako `Dict`, `Mapping`, `DefaultDict` nebo `OrderedDict`.

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
        Přetížení metody __call__ pro validaci slovníkových struktur.

        Validuje:
        - zda `value` odpovídá základnímu typu (např. dict)
        - klíče a hodnoty, pokud je požadována vnitřní validace

        Returns:
            bool: True, pokud validace proběhne úspěšně, jinak vyhazuje výjimku
        """

        # Validace základního typu (např. dict)
        validate_is_instance(value, expected, bool_only)

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
            depth_check = reduce_depth_check(depth_check)

            # Validace klíče
            validate_typing(
                key, key_type, depth_check, custom_types, bool_only
            )

            # Validace hodnoty
            validate_typing(
                val, value_type, depth_check, custom_types, bool_only
            )

            # Kontrola vyčerpání zanoření (přerušení cyklu)
            if not depth_check:
                break

        # Pokud vše proběhne v pořádku a bez chyb
        return True
