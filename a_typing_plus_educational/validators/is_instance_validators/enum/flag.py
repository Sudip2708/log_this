from enum import Flag

from ...._bases import BaseIsInstanceValidator


class FlagValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci enum.Flag

    Typ enum.Flag reprezentuje výčtový typ pro bitové příznaky, které lze kombinovat pomocí
    bitových operací (OR, AND, XOR). Umožňuje reprezentovat sadu příznaků jako jednu hodnotu.

    Syntaxe:
        - enum.Flag             # Vyžaduje import `from enum import Flag`
        - Flag                  # Když je importováno `from enum import Flag`

    Příklady použití:
        - Flag                  # Obecná typová anotace pro libovolný Flag
        - MyFlag                # Typová anotace pro konkrétní Flag typ

    Typický objekt Flag:
        ```python
        from enum import Flag, auto

        class Permission(Flag):
            READ = auto()       # 1
            WRITE = auto()      # 2
            EXECUTE = auto()    # 4
            # Kombinace
            RW = READ | WRITE   # 3
            RWX = READ | WRITE | EXECUTE  # 7
        ```

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy enum.Flag pomocí isinstance()
        2. Neověřuje, zda hodnota patří ke konkrétnímu výčtovému typu příznaků

    Použití v kódu:
        - Pro parametry funkcí: def set_permissions(perm: Permission) -> None
        - Pro návratové hodnoty: def get_current_permissions() -> Permission
        - Pro typování proměnných: options: Options = Options.VERBOSE | Options.DEBUG

    Specifické informace:
        - Podporuje bitové operace: OR (|), AND (&), XOR (^), NOT (~)
        - Hodnoty jsou typicky mocniny dvou pro snadnou kombinaci
        - Hodnota 0 reprezentuje prázdnou množinu příznaků
        - Lze testovat příslušnost příznaku: Permission.READ in combined_permissions
        - V Pythonu 3.11+ Flag automaticky používá celočíselné hodnoty (není třeba je explicitně zadávat)
        - Funkce auto() automaticky přiřadí další mocninu dvou

    Běžné chyby:
        - Opomenutí importu `from enum import Flag, auto`
        - Nepoužití auto() nebo nepoužití mocnin dvou pro hodnoty
        - Záměna Flag a IntFlag (Flag nepodporuje porovnání s celými čísly)
        - Nesprávné kombinování příznaků pomocí sčítání (+) místo bitového OR (|)
        - Testování příslušnosti pomocí == místo in

    Reference:
        - https://docs.python.org/3/library/enum.html#enum.Flag
        - https://peps.python.org/pep-0435/ (Přidání Enum do standardní knihovny)
    """

    VALIDATOR_KEY = "Flag"
    ANNOTATION = Flag

    IS_INSTANCE = Flag
    DUCK_TYPING = {
        "has_attr": (
            "__or__", "__and__", "__xor__", "__invert__",
            "name", "value"
        ),
    }

    DESCRIPTION = "Výčtový typ podporující bitové operace"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí nebo podtřídou enum.Flag, "
            "tedy výčtového typu, jehož hodnoty "
            "mohou být kombinovány pomocí bitových operací jako OR (|)."
        )
