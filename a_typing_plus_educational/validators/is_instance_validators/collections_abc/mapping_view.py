from collections.abc import MappingView

from ...._bases import BaseIsInstanceValidator


class MappingViewValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci MappingView

    MappingView reprezentuje abstraktní základní třídu pro pohledy na mapování (slovníky),
    od které dědí konkrétní implementace jako ItemsView, KeysView a ValuesView.
    Jde o iterovatelné objekty, které poskytují různé pohledy na data mapování bez kopírování.

    Syntaxe:
        - MappingView            # Vyžaduje import z collections.abc
        - collections.abc.MappingView  # Plně kvalifikovaný zápis

    Příklady použití:
        - MappingView            # Obecná anotace pro libovolný pohled na mapování
        - isinstance(view, MappingView)  # Kontrola, zda objekt je pohledem na mapování

    Validační proces:
        1. Ověření, zda hodnota je instance collections.abc.MappingView
        2. Vnitřní hodnoty nejsou validovány (pro typovou kontrolu vnitřních hodnot
           použijte specializované třídy KeysView[K], ValuesView[V] nebo ItemsView[K, V])

    Použití v kódu:
        - Pro parametry funkcí: def process_view(view: MappingView) -> None
        - Pro návratové hodnoty: def get_view() -> MappingView
        - Pro obecné funkce pracující s různými typy pohledů na mapování

    Vztah k jiným typům:
        - Nadřazená třída pro KeysView, ValuesView a ItemsView
        - Všechny implementace MappingView jsou neměnné (read-only)
        - Implementuje rozhraní Sized a Iterable

    Implementační detaily:
        - MappingView je abstraktní třída, v kódu se používají její konkrétní implementace
        - Poskytuje základní rozhraní pro všechny typy pohledů na mapování
        - Pohledy jsou aktualizovány automaticky při změnách v původním mapování

    Běžné chyby:
        - Snaha o modifikaci pohledu (všechny pohledy na mapování jsou neměnné)
        - Zaměňování abstraktní MappingView s konkrétními implementacemi
        - Nesprávné použití bez parametrizace pro konkrétní typy hodnot
        - Předpokládání, že pohled je nezávislá kopie dat z mapování

    Reference:
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.MappingView
        - https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
    """

    VALIDATOR_KEY = "mapping_view"
    ANNOTATION = MappingView

    IS_INSTANCE = MappingView
    DUCK_TYPING = {
        "has_attr": ("mapping", "__len__", "__iter__"),
    }

    DESCRIPTION = "Pohled na obsah mapování (slovníku)"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní MappingView z collections.abc, "
            "což je základní třída pro pohledy jako dict_keys, dict_values "
            "nebo dict_items, které poskytují dynamický pohled na slovník."
        )
