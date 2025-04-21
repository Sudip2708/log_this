from typing import Counter, get_args
from collections import Counter as CounterOrigin

from .._base_mapping_validator import BaseMappingValidator
from .._base_type_variables import K


class CounterValidator(BaseMappingValidator):
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
    ORIGIN = CounterOrigin  # collections.Counter

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, self.ORIGIN)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Získání anotace typu klíče
        inner_args = get_args(annotation)

        # Pokud nemáme specifikované typy pro klíče a hodnoty, vrátíme True
        if not inner_args:
            return True

        # Načtení klíče
        key_type = inner_args[0]

        # Cyklus pro kontrolu klíčů a hodnot
        for key, val in value.items():

            # Odpočet zanoření pro další kontrolu
            depth_check = self._reduce_depth_check(depth_check)

            # Validace klíče podle anotace
            self.validate_typing(
                key, key_type, depth_check, custom_types, bool_only
            )

            # Hodnota musí být vždy typu int
            self.validate_typing(
                val, int, depth_check, custom_types, bool_only
            )

            # Kontrola vyčerpání zanoření (přerušení cyklu)
            if not depth_check:
                break

        return True
