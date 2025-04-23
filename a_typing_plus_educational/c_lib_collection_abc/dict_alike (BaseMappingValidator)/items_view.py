from typing import ItemsView, get_args
from collections.abc import ItemsView as ItemsViewOrigin

from ..._bases import BaseMappingValidator, K, V


class ItemsViewValidator(BaseMappingValidator):
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

    VALIDATOR_KEY = "items_view"
    ANNOTATION = ItemsView[K, V]
    INFO = "Definuje pohled na dvojice (klíč, hodnota) v mapování."
    ORIGIN = ItemsViewOrigin

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):

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

        return True