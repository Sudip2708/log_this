class SignsBase:
    """Definuje všechny dostupné znaky a jejich varianty pro různé režimy."""

    # Název znaku   ["set_a", "set_b", "default"]
    # Znaky pro začátek řádku
    INTRO         = [" ■ ",   " ■ ",   ""]
    INFO          = [" ☐ ",   " ☐ ",  ""]
    LIST          = [" - ",   " - ",   ""]
    SUCCESS       = [" ☑ ",   " ☑ ",  ""]
    DROPDOWN      = [" ▼ ",   " ▼ ",   ""]
    SELECTED      = [" » ",   " » ",   ""]
    UNSELECTED    = ["   ",   "   ",   ""]
    ERROR         = [" ⛝ ",   " ⛝ ",  ""]
    WARNING       = [" ⚠ ",   " ⚠ ",   ""]


    @classmethod
    def get_all_signs(cls):
        """
        Vrátí všechny dostupné definice znaků jako slovník.

        Prochází všechny atributy této třídy a vybírá pouze ty,
        které nejsou speciální (`__dunder__` metody) a obsahují seznam hodnot.

        Návratová hodnota:
            dict[str, list[str]]:
                - Klíč: název znaku jako řetězec (např. `"INTRO"`)
                - Hodnota: seznam znakových variant [set_a, set_b, default]
        """
        return {
            attr: getattr(cls, attr)
            for attr in dir(cls)
            if not attr.startswith("_")
               and isinstance(getattr(cls, attr), list)
        }

