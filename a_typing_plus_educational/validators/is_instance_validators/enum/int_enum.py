from enum import IntEnum

from ...._bases import BaseIsInstanceValidator


class IntEnumValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci enum.IntEnum

    Typ enum.IntEnum reprezentuje výčtový typ s celočíselnými hodnotami, který se
    zároveň chová jako celé číslo. Na rozdíl od základního Enum lze hodnoty IntEnum
    porovnávat přímo s celými čísly a lze je použít všude, kde je očekáváno celé číslo.

    Syntaxe:
        - enum.IntEnum          # Vyžaduje import `from enum import IntEnum`
        - IntEnum               # Když je importováno `from enum import IntEnum`

    Příklady použití:
        - IntEnum               # Obecná typová anotace pro libovolný IntEnum
        - MyIntEnum             # Typová anotace pro konkrétní IntEnum typ

    Typický objekt IntEnum:
        ```python
        from enum import IntEnum

        class Status(IntEnum):
            ERROR = 0
            WARNING = 1
            INFO = 2
            DEBUG = 3
        ```

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy enum.IntEnum pomocí isinstance()
        2. Neověřuje, zda hodnota patří ke konkrétnímu výčtovému typu

    Použití v kódu:
        - Pro parametry funkcí: def process_status(status: Status) -> None
        - Pro návratové hodnoty: def get_priority() -> Priority
        - Pro typování proměnných: log_level: LogLevel = LogLevel.INFO

    Specifické informace:
        - Kombinuje vlastnosti výčtu a celého čísla
        - Lze porovnávat přímo s celými čísly: Status.ERROR == 0
        - Lze použít v aritmetických operacích: Status.WARNING + 1 == Status.INFO
        - Hodnoty jsou uspořádány podle jejich celočíselných hodnot
        - Všechny hodnoty musí být celá čísla
        - Automaticky se dědí od int, takže instance IntEnum jsou zároveň instancemi int

    Běžné chyby:
        - Opomenutí importu `from enum import IntEnum`
        - Použití neceleho čísla jako hodnoty
        - Předpoklad, že všechny Enum typy jsou IntEnum
        - Přetížení metod, které by narušily chování jako celého čísla

    Reference:
        - https://docs.python.org/3/library/enum.html#enum.IntEnum
        - https://peps.python.org/pep-0435/ (Přidání Enum do standardní knihovny)
    """

    VALIDATOR_KEY = "IntEnum"
    ANNOTATION = IntEnum

    IS_INSTANCE = IntEnum
    DUCK_TYPING = {
        "has_attr": ("__int__", "name", "value"),
    }

    DESCRIPTION = "Celočíselný výčtový typ"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí nebo podtřídou enum.IntEnum, "
            "tedy výčtového typu, jehož hodnoty "
            "jsou celá čísla a lze s nimi provádět číselné operace."
        )
