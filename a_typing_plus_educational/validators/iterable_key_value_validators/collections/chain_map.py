from typing import ChainMap
from collections import ChainMap as ChainMapOrigin

from ...._bases import DictionaryValidatorBase, K, V
from ....validators import dictionary_validator_for_chainmap


class ChainMapValidator(DictionaryValidatorBase):
    """
    Validátor pro typovou anotaci ChainMap[K, V]

    ChainMap reprezentuje řetězec (stack) více slovníků, které se dohromady
    chovají jako jeden sloučený slovník. Poskytuje jednotné rozhraní pro přístup k datům
    z několika různých zdrojů, přičemž při vyhledávání klíče prochází všechny slovníky
    ve stanoveném pořadí.

    Syntaxe:
        - ChainMap[K, V]               # Vyžaduje import z typing
        - collections.ChainMap[K, V]   # Od Python 3.9+
        - collections.ChainMap         # Obecný ChainMap bez specifikace typů

    Příklady použití:
        - ChainMap[str, int]           # ChainMap s řetězcovými klíči a celočíselnými hodnotami
        - ChainMap[str, Any]           # ChainMap s řetězcovými klíči a libovolnými hodnotami
        - ChainMap[Hashable, dict]     # ChainMap s hashable klíči a slovníkovými hodnotami

    Vnitřní typy:
        Anotace ChainMap vyžaduje specifikaci dvou typových parametrů:
        - K: Typ klíčů (musí být hashable) ve všech slovnících v řetězci
        - V: Typ hodnot ve všech slovnících v řetězci

    Validační proces:
        1. Ověří, zda hodnota je instance typu collections.ChainMap
        2. Pokud je požadována hloubková kontrola:
           a) Ověří, že každá mapa v řetězci je typu dict (nebo kompatibilní)
           b) Pro každou mapu v řetězci zkontroluje typy všech klíčů a hodnot
           c) Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def apply_settings(configs: ChainMap[str, Any]) -> None
        - Pro návratové hodnoty: def build_context() -> ChainMap[str, object]
        - Pro typování proměnných: contexts: ChainMap[str, int] = ChainMap(global_vars, local_vars)

    Srovnání s podobnými typy:
        - ChainMap vs dict: ChainMap umožňuje pracovat s více slovníky jako s jedním, se zachováním
          jejich samostatnosti a hierarchie
        - ChainMap vs update(): ChainMap zachovává původní slovníky beze změny, zatímco update()
          je modifikuje
        - ChainMap vs MutableMapping: ChainMap je konkrétní implementace MutableMapping
          s dodatečnými funkcemi pro správu hierarchie slovníků

    Běžné vzory použití:
        - Víceúrovňové konfigurace: ChainMap(user_settings, default_settings)
        - Kontextová hierarchie: ChainMap(local_vars, global_vars)
        - Zpracování argumentů: ChainMap(cli_args, env_vars, defaults)
        - Vrstvení přepisů: new_context = old_context.new_child(updates)

    Běžné chyby:
        - Zapomenutí importu: from typing import ChainMap nebo from collections import ChainMap
        - Nepochopení pořadí vyhledávání (první slovník má vždy přednost)
        - Nesprávné očekávání modifikace původních slovníků
        - Nerespektování konzistence typů mezi všemi slovníky v řetězci

    Reference:
        - https://docs.python.org/3/library/collections.html#collections.ChainMap
        - https://docs.python.org/3/library/typing.html#typing.ChainMap
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "chainmap"
    ANNOTATION = ChainMap[K, V]

    IS_INSTANCE = ChainMapOrigin
    HAS_ATTRS = "__getitem__", "__iter__", "__len__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Sloučené zobrazení více slovníků"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí ChainMap ze standardní knihovny collections. "
            "Umožňuje sjednocené zobrazení více mapovacích objektů bez jejich kopírování."
        )


    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Přetížení metody __call__ pro validaci slovníkových struktur."""

        # Navrácení výstupu funkce pro validaci slovníkových objektů upravené pro ChainMap
        return dictionary_validator_for_chainmap(
            value, self.ORIGIN, annotation, depth_check, custom_types, bool_only
        )