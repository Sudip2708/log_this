from typing import Any, Counter
from collections import Counter as CounterOrigin

from ._dict_alike_base import DictAlikeBase

K = Any

class CounterValidator(DictAlikeBase):
    """
    Validátor pro zápis Counter[K]

    Counter reprezentuje speciální typ slovníku, který slouží k počítání výskytů jednotlivých klíčů.

    Každý klíč (`K`) je validován, zatímco jeho hodnota je vždy typu `int`,
    reprezentující počet výskytů daného prvku.

    Typická použití zahrnují analýzu frekvence prvků v kolekci.

    Příklad:
        Counter[str] bude validovat, že všechny klíče jsou řetězce
        a hodnoty jsou automaticky považovány za celá čísla (`int`).
    """

    VALIDATOR_KEY = "counter"
    ANNOTATION = Counter[K]
    INFO = "Definuje Counter – klíče libovolného typu K, hodnoty vždy int."
    GET_ORIGIN = CounterOrigin  # collections.Counter

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, self.GET_ORIGIN)

        # Pokud nemáme validaci zanoření, validujeme jen typ
        if not depth_check:
            return True

        # Vytvoření proměné pro zanoření
        depth = depth_check

        # Získání anotace typu klíče
        inner_args = self._get_inner_args(annotation)

        # Pokud není uveden typ pro klíč, nemáme co validovat
        if len(inner_args) < 1:
            return True

        # Načtení klíče
        key_type = inner_args[0]

        # Cyklus pro kontrolu klíčů a hodnot
        for key, val in value.items():

            # Kontrola zanoření
            if not depth:
                break

            # Odpočet zanoření pro další kontrolu
            depth = self._reduce_depth_check(depth)

            # Validace klíče podle anotace
            self.validate_typing(key, key_type, depth, custom_types, bool_only)

            # Hodnota musí být vždy typu int
            self.validate_typing(val, int, depth, custom_types, bool_only)

        return True
