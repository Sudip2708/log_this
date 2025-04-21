from typing import ItemsView, KeysView, ValuesView
from collections.abc import MappingView as MappingViewOrigin

from .._base_mapping_validator import BaseMappingValidator
from .._base_type_variables import K, V


class MappingEntryTypeValidator(BaseMappingValidator):
    """
    Validátor pro zápis MappingView a jeho podtřídy (ItemsView, KeysView, ValuesView)

    MappingView reprezentuje abstraktní třídu pro pohledy na mapování (klíče, hodnoty, položky).
    Jedná se o iterovatelné objekty, které poskytují různé pohledy na data mapování.

    Hint:
        ItemsView[K, V] = Pohled na dvojice (klíč, hodnota) v mapování
        KeysView[K] = Pohled na klíče v mapování
        ValuesView[V] = Pohled na hodnoty v mapování

    Reprezentuje pohled na mapování:
        MappingView je abstraktní třída pro různé pohledy na mapování.
        Je implementováno jako Sized a Iterable.

    Konkrétní podtřídy:
        * ItemsView: Pohled na položky (páry klíč-hodnota)
        * KeysView: Pohled na klíče
        * ValuesView: Pohled na hodnoty

    Základní operace:
        * Iterace přes prvky pohledu (for item in view)
        * Zjištění délky pohledu (len(view))
        * Kontrola členství (item in view) - významově se liší podle typu pohledu

    Vztah s Mapping:
        MappingView je objekt vytvořený metodami Mapping:
        * items() -> ItemsView
        * keys() -> KeysView
        * values() -> ValuesView

    Příklady:
        dict_items, dict_keys, dict_values a podobné objekty z ostatních mapování.

    Použití v typových anotacích:
        Používá se k označení, že funkce nebo proměnná očekává pohled na mapování.
    """

    VALIDATOR_KEY = "mapping_entry_type"
    ANNOTATION = MappingViewOrigin  # Obecná anotace, v praxi bys pravděpodobně chtěl rozlišit mezi ItemsView, KeysView, ValuesView
    INFO = "Definuje pohled na mapování (klíče, hodnoty nebo položky)."
    GET_ORIGIN = MappingViewOrigin