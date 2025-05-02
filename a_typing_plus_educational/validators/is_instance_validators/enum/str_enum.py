from enum import StrEnum

from ..._bases import BaseIsInstanceValidator


class StrEnumValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci enum.StrEnum

    Typ enum.StrEnum reprezentuje výčtový typ s řetězcovými hodnotami, který se
    zároveň chová jako řetězec. Na rozdíl od základního Enum lze hodnoty StrEnum
    porovnávat přímo s řetězci a lze je použít všude, kde je očekáván řetězec.

    Poznámka: StrEnum je dostupný od Pythonu 3.11.

    Syntaxe:
        - enum.StrEnum          # Vyžaduje import `from enum import StrEnum`
        - StrEnum               # Když je importováno `from enum import StrEnum`

    Příklady použití:
        - StrEnum               # Obecná typová anotace pro libovolný StrEnum
        - MyStrEnum             # Typová anotace pro konkrétní StrEnum typ

    Typický objekt StrEnum:
        ```python
        from enum import StrEnum

        class Color(StrEnum):
            RED = "red"
            GREEN = "green"
            BLUE = "blue"
        ```

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy enum.StrEnum pomocí isinstance()
        2. Neověřuje, zda hodnota patří ke konkrétnímu výčtovému typu

    Použití v kódu:
        - Pro parametry funkcí: def process_color(color: Color) -> None
        - Pro návratové hodnoty: def get_category() -> Category
        - Pro typování proměnných: theme: Theme = Theme.DARK

    Specifické informace:
        - Kombinuje vlastnosti výčtu a řetězce
        - Lze porovnávat přímo s řetězci: Color.RED == "red"
        - Lze použít ve funkcích pro řetězce: len(Color.RED), Color.RED.upper()
        - Všechny hodnoty musí být řetězce
        - Automaticky se dědí od str, takže instance StrEnum jsou zároveň instancemi str
        - Automatická konverze názvu na hodnotu, pokud není hodnota explicitně uvedena

    Běžné chyby:
        - Opomenutí importu `from enum import StrEnum`
        - Použití ne-řetězcové hodnoty
        - Použití StrEnum v prostředí s Pythonem starším než 3.11
        - Předpoklad, že automatická konverze názvu na hodnotu převede název do jiného formátu než UPPERCASE

    Reference:
        - https://docs.python.org/3/library/enum.html#enum.StrEnum
        - https://peps.python.org/pep-0435/ (Přidání Enum do standardní knihovny)
    """

    VALIDATOR_KEY = "StrEnum"
    ANNOTATION = StrEnum

    IS_INSTANCE = StrEnum
    HAS_ATTRS =  "name", "__str__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Řetězcový výčtový typ"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí nebo podtřídou enum.StrEnum, "
            "tedy výčtového typu, jehož hodnoty "
            "jsou řetězce, se kterými lze provádět řetězcové operace."
        )
