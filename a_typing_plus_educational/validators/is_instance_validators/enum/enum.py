from enum import Enum

from ..._bases import BaseIsInstanceValidator


class EnumValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci enum.Enum

    Typ enum.Enum reprezentuje výčtový typ - kolekci pojmenovaných hodnot, které tvoří
    symbolická jména (identifikátory) pro sadu konstantních hodnot. Enum zajišťuje, že
    tyto hodnoty jsou jedinečné a neměnné.

    Syntaxe:
        - enum.Enum             # Vyžaduje import `from enum import Enum`
        - Enum                  # Když je importováno `from enum import Enum`
        - typing.Enum           # Vyžaduje import `from typing import Enum` (od Python 3.8+)

    Příklady použití:
        - Enum                  # Obecná typová anotace pro libovolný výčtový typ
        - MyEnum                # Typová anotace pro konkrétní výčtový typ

    Typický objekt Enum:
        ```python
        from enum import Enum

        class Color(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3
        ```

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy enum.Enum pomocí isinstance()
        2. Neověřuje, zda hodnota patří ke konkrétnímu výčtovému typu (pro to by byl potřeba samostatný validátor)

    Použití v kódu:
        - Pro parametry funkcí: def process_color(color: Color) -> None
        - Pro návratové hodnoty: def get_status() -> Status
        - Pro typování proměnných: current_state: State = State.ACTIVE

    Specifické informace:
        - Hodnoty výčtu jsou instancí třídy výčtu (např. Color.RED je instance Color)
        - Výčty podporují iteraci, stringovou reprezentaci a porovnávání
        - Každá hodnota výčtu má atributy name (jméno) a value (hodnota)
        - Výčty jsou neměnné (immutable) - nelze přidávat ani odebírat hodnoty za běhu
        - Existují specializované varianty: IntEnum, StrEnum, Flag, IntFlag, auto()
        - Od Pythonu 3.8 je Enum také dostupný v modulu typing

    Běžné chyby:
        - Opomenutí importu `from enum import Enum`
        - Záměna hodnoty a třídy výčtu (Color vs. Color.RED)
        - Pokus o změnu hodnoty výčtu po definici
        - Nesprávné použití v typových anotacích (např. použití konkrétní hodnoty místo třídy)
        - Nedodržení konvence UPPERCASE pro jména hodnot výčtu

    Reference:
        - https://docs.python.org/3/library/enum.html
        - https://peps.python.org/pep-0435/ (Přidání Enum do standardní knihovny)
    """

    VALIDATOR_KEY = "Enum"
    ANNOTATION = Enum

    IS_INSTANCE = Enum
    HAS_ATTRS = "name", "value"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Výčtový typ"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí nebo podtřídou enum.Enum, "
            "tedy výčtového typu umožňujícího definovat "
            "pojmenované konstanty s jedinečnými hodnotami."
        )
