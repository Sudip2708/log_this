from typing import ItemsView, get_args
from collections.abc import ItemsView as ItemsViewOrigin

from .._base_mapping_validator import BaseMappingValidator
from .._base_type_variables import K, V


class ItemsViewValidator(BaseMappingValidator):
    """
    Validátor pro zápis ItemsView[K, V]

    ItemsView reprezentuje pohled na položky (páry klíč-hodnota) mapování,
    získaný pomocí metody dict.items() nebo podobné metody jiných mapování.

    Hint:
        ItemsView[K, V] = Pohled na dvojice (klíč, hodnota) v mapování

    Reprezentuje pohled na položky:
        ItemsView je druh MappingView, který poskytuje pohled na páry (klíč, hodnota) z mapování.
        Implementuje rozhraní Set, takže podporuje operace jako průnik, sjednocení, atd.

    Základní operace:
        * Iterace přes páry klíč-hodnota: for k, v in mapping.items()
        * Testování členství: (key, value) in mapping.items()
        * Zjištění délky: len(mapping.items())

    Specifické chování:
        * Členství se testuje jako dvojice (klíč, hodnota)
        * Umožňuje set-like operace s jinými kolekcemi dvojic

    Příklady:
        dict_items a podobné objekty z ostatních implementací mapování

    Použití v typových anotacích:
        Používá se k označení, že funkce nebo proměnná očekává výsledek metody items()
        ze slovníku nebo jiného mapování.
    """

    VALIDATOR_KEY = "items_view"
    ANNOTATION = ItemsView[K, V]
    INFO = "Definuje pohled na dvojice (klíč, hodnota) v mapování."
    ORIGIN = ItemsViewOrigin

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        self.validate_native_type(value, self.ORIGIN)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Načtení vnitřních anotací
        inner_args = get_args(annotation)

        # Pokud nemáme specifikované vnitřní typy, vrátíme True
        if not inner_args:
            return True

        # Načtení typů pro klíč a hodnotu
        key_type, value_type = inner_args

        # Cyklus pro vnitřní validaci
        for key, val in value:  # ItemsView poskytuje páry (key, value)

            # Odpočet zanoření pro další kontrolu
            depth_check = self._reduce_depth_check(depth_check)

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