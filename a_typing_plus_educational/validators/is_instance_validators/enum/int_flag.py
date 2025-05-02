from enum import IntFlag

from ..._bases import BaseIsInstanceValidator


class IntFlagValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci enum.IntFlag

    Typ enum.IntFlag kombinuje vlastnosti IntEnum a Flag, reprezentuje výčtový typ
    pro bitové příznaky, které lze kombinovat pomocí bitových operací a zároveň se
    chová jako celé číslo.

    Syntaxe:
        - enum.IntFlag          # Vyžaduje import `from enum import IntFlag`
        - IntFlag               # Když je importováno `from enum import IntFlag`

    Příklady použití:
        - IntFlag               # Obecná typová anotace pro libovolný IntFlag
        - MyIntFlag             # Typová anotace pro konkrétní IntFlag typ

    Typický objekt IntFlag:
        ```python
        from enum import IntFlag, auto

        class Access(IntFlag):
            NONE = 0
            READ = auto()       # 1
            WRITE = auto()      # 2
            EXECUTE = auto()    # 4
            # Kombinace
            RW = READ | WRITE   # 3
            RWX = READ | WRITE | EXECUTE  # 7
        ```

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy enum.IntFlag pomocí isinstance()
        2. Neověřuje, zda hodnota patří ke konkrétnímu výčtovému typu příznaků

    Použití v kódu:
        - Pro parametry funkcí: def set_mode(mode: FileMode) -> None
        - Pro návratové hodnoty: def get_current_access() -> Access
        - Pro typování proměnných: flags: SystemFlags = SystemFlags.HIDDEN | SystemFlags.SYSTEM

    Specifické informace:
        - Kombinuje vlastnosti IntEnum a Flag
        - Podporuje bitové operace: OR (|), AND (&), XOR (^), NOT (~)
        - Lze přímo porovnávat s celými čísly: Access.READ == 1
        - Lze použít v aritmetických operacích: Access.READ + 2
        - Hodnoty jsou typicky mocniny dvou pro snadnou kombinaci
        - Nulová hodnota (0) je platná a reprezentuje prázdnou množinu příznaků
        - Reprezentuje kombinaci příznaků jako celočíselnou hodnotu

    Běžné chyby:
        - Opomenutí importu `from enum import IntFlag, auto`
        - Nepoužití auto() nebo nepoužití mocnin dvou pro hodnoty
        - Záměna IntFlag a Flag (IntFlag podporuje porovnání s celými čísly)
        - Nesprávné kombinování příznaků pomocí sčítání (+) místo bitového OR (|)
        - Nerozlišení mezi testováním identity (is), rovnosti (==) a příslušnosti (in)

    Reference:
        - https://docs.python.org/3/library/enum.html#enum.IntFlag
        - https://peps.python.org/pep-0435/ (Přidání Enum do standardní knihovny)
    """

    VALIDATOR_KEY = "IntFlag"
    ANNOTATION = IntFlag

    IS_INSTANCE = IntFlag
    HAS_ATTRS = "name", "__or__", "__and__", "__xor__", "__invert__", "__int__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Celočíselný výčtový typ s podporou bitových operací"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí nebo podtřídou enum.IntFlag, "
            "což kombinuje vlastnosti Flag a IntEnum - "
            "hodnoty jsou celá čísla a lze je kombinovat pomocí bitových operací."
        )
