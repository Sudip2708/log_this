from typing import Any, ChainMap
from collections import ChainMap as ChainMapOrigin

from ._dict_alike_base import DictAlikeBase

K = V = Any

class ChainMapValidator(DictAlikeBase):
    """
    Validátor pro zápis ChainMap[K, V]

    ChainMap reprezentuje řetězec (stack) více slovníků, které se dohromady
    chovají jako jeden sloučený slovník.

    Validace probíhá zvlášť pro každý vnořený mapping (`dict`) uvnitř `ChainMap`.

    Příklad:
        ChainMap[str, int] znamená, že všechny klíče musí být `str` a hodnoty `int`,
        napříč všemi mapami ve struktuře.

    Vhodné pro slučování různých kontextů nebo konfigurací.
    """

    VALIDATOR_KEY = "chainmap"
    ANNOTATION = ChainMap[K, V]
    INFO = "Definuje ChainMap – řetězení více slovníků s typy klíčů K a hodnot V."
    GET_ORIGIN = ChainMapOrigin

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace origin typu
        self.validate_native_type(value, self.GET_ORIGIN)

        # Pokud nemáme validaci vnitřních typů, končíme
        if not depth_check:
            return True

        # Vytvoření proměné pro zanoření
        depth = depth_check

        # Načtení vnitřních anotací pro klíče a hodnoty
        inner_args = self._get_all_args_as_tuple(annotation)

        # Pokud nemáme specifikované typy pro klíče a hodnoty, vrátíme True
        if len(inner_args) < 2:
            return True

        # Načtení klíče a hodnoty
        key_type, value_type = inner_args[0], inner_args[1]

        # Validujeme každý jednotlivý mapping ve stacku
        for mapping in value.maps:

            # Kontrola zanoření
            if not depth:
                break

            # Odpočet zanoření pro další kontrolu
            depth = self._reduce_depth_check(depth)

            # Každý mapping by měl být dict-typu (nebo kompatibilní)
            self.validate_native_type(mapping, dict)

            # Cyklus pro kontrolu klíčů a hodnot
            for key, val in mapping.items():

                # Validace klíče
                self.validate_typing(key, key_type, depth, custom_types, bool_only)

                # Validace hodnoty
                self.validate_typing(val, value_type, depth, custom_types, bool_only)

        return True
