from typing import ItemsView, get_args
from collections.abc import ItemsView as ItemsViewOrigin

from ...._bases import DictionaryValidatorBase, K, V
from ....validators import dictionary_validator_for_itemsview


class ItemsViewValidator(DictionaryValidatorBase):
    """
    Validátor pro typovou anotaci ItemsView[K, V]

    ItemsView reprezentuje pohled na páry klíč-hodnota v mapování, získaný pomocí metody
    .items() na slovníku nebo jiném mapování. Tento objekt poskytuje read-only pohled
    na data bez vytváření kopie původního slovníku a implementuje rozhraní Set.

    Syntaxe:
        - ItemsView[K, V]              # Vyžaduje import z typing
        - collections.abc.ItemsView[K, V] # Od Python 3.9+
        - collections.abc.ItemsView    # Obecný ItemsView bez specifikace typů

    Příklady použití:
        - ItemsView[str, int]          # Pohled na páry str-int ve slovníku
        - ItemsView[int, List[str]]    # Pohled na páry int-seznam_stringů ve slovníku
        - ItemsView[str, Any]          # Pohled na páry s řetězcovými klíči a libovolnými hodnotami
        - ItemsView[K, V]              # Obecný pohled na páry klíč-hodnota

    Vnitřní typy:
        Anotace ItemsView vyžaduje specifikaci dvou typových parametrů:
        - K: Typ klíčů v mapování
        - V: Typ hodnot v mapování

    Validační proces:
        1. Ověří, zda hodnota je instance typu collections.abc.ItemsView
        2. Pokud je požadována hloubková kontrola:
           a) Projde všechny páry klíč-hodnota v objektu ItemsView
           b) Pro každý pár validuje typ klíče i hodnoty podle specifikovaných typů
           c) Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_items(items: ItemsView[str, int]) -> None
        - Pro návratové hodnoty: def get_entries() -> ItemsView[str, bytes]
        - Pro typování proměnných: entries: ItemsView[str, int] = my_dict.items()

    Srovnání s podobnými typy:
        - ItemsView vs Dict.items(): ItemsView je typ vrácený metodou items()
        - ItemsView vs KeysView: ItemsView obsahuje páry klíč-hodnota, KeysView pouze klíče
        - ItemsView vs ValuesView: ItemsView obsahuje páry klíč-hodnota, ValuesView pouze hodnoty
        - ItemsView vs Set[Tuple[K, V]]: ItemsView implementuje rozhraní Set, ale je read-only view

    Běžné vzory použití:
        - Iterace přes páry klíč-hodnota: for k, v in mapping.items()
        - Testování členství: (key, value) in mapping.items()
        - Set operace: intersection, union, difference s jinými kolekcemi párů
        - Efektivní práce s daty bez vytváření kopií slovníků

    Běžné chyby:
        - Zapomenutí importu: from typing import ItemsView nebo from collections.abc import ItemsView
        - Pokus o modifikaci ItemsView (je read-only)
        - Záměna s list(dict.items()) nebo tuple(dict.items())
        - Nesprávné testování členství (je třeba použít dvojici (key, value))

    Reference:
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.ItemsView
        - https://docs.python.org/3/library/typing.html#typing.ItemsView
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "itemsview"
    ANNOTATION = ItemsView[K, V]

    IS_INSTANCE = ItemsViewOrigin
    HAS_ATTRS =  "__iter__", "__len__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Pohled na dvojice klíč-hodnota ve slovníku"
    LONG_DESCRIPTION = (
            "Validuje, že objekt odpovídá typu ItemsView, "
            "který reprezentuje dynamický pohled na položky slovníku "
            "(klíče a hodnoty jako dvojice)."
        )


    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Přetížení metody __call__ pro validaci slovníkových struktur."""

        # Navrácení výstupu funkce pro validaci slovníkových objektů upravené pro ChainMap
        return dictionary_validator_for_itemsview(
            value, self.ORIGIN, annotation, depth_check, custom_types, bool_only
        )