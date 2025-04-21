from typing import ChainMap, get_args
from collections import ChainMap as ChainMapOrigin

from .._base_mapping_validator import BaseMappingValidator
from .._base_type_variables import K, V


class ChainMapValidator(BaseMappingValidator):
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
    ORIGIN = ChainMapOrigin

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, self.ORIGIN)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Načtení vnitřních anotací pro klíče a hodnoty
        inner_args = get_args(annotation)

        # Pokud nemáme specifikované typy pro klíče a hodnoty, vrátíme True
        if not inner_args:
            return True

        # Načtení klíče a hodnoty
        key_type, value_type = inner_args

        # Validujeme každý jednotlivý mapping ve stacku
        for mapping in value.maps:

            # Každý mapping by měl být dict-typu (nebo kompatibilní)
            self.validate_native_type(mapping, dict)

            # Odpočet zanoření pro další kontrolu
            depth_check = self._reduce_depth_check(depth_check)

            # Cyklus pro kontrolu klíčů a hodnot
            for key, val in mapping.items():

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

        return True
