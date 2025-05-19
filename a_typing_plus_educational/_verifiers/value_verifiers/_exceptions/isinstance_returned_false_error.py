from typing import Any, Tuple, Union

from ..._exceptions_base import VerifyValueError


class VerifyIsInstanceReturnedFalseError(VerifyValueError, ValueError):
    """
    Výjimka vyvolaná při neshodě typu ověřované hodnoty s očekávaným typem.

    Tato výjimka je vyvolána, když hodnota předaná k ověření neodpovídá
    očekávanému typu nebo typům specifikovaným pomocí parametru `expected`.
    Poskytuje detailní informace o tom, jaký typ byl očekáván a jaký byl skutečně obdržen.

    Klíčové koncepty:
    -----------------
    * Typová validace - Ověření, že hodnota odpovídá očekávanému datovému typu
    * Typový systém Pythonu - Vztah mezi `isinstance()` a hierarchií typů
    * Diagnostika typových neshod - Identifikace rozdílů mezi očekávanými a skutečnými typy

    Architekturální kontext:
    -----------------------
    Tato výjimka je jednou z nejzákladnějších a nejčastěji používaných výjimek
    v knihovně Verify, jelikož typová validace je základním stavebním kamenem
    většiny validačních operací. Je vyvolávána funkcí `is_instance_verifier()`
    při detekci nesouladu mezi typem hodnoty a očekávaným typem.

    Detaily implementace:
    --------------------
    * Uchovává reference na původní hodnotu a očekávané typy pro diagnostiku
    * Využívá pomocnou funkci `format_items()` pro přehledné zobrazení seznamu typů
    * Poskytuje konkrétní pokyny k nápravě problému s typem hodnoty
    * Upravuje výchozí nadpis pro zdůraznění charakteru chyby typu

    Povinné atributy:
    ----------------
    * value (Any): Původní ověřovaná hodnota
    * expected (Union[type, Tuple[type, ...]]): Očekávaný typ nebo typy

    Příklady použití:
    ---------------
    ```python
    # Přímé vyvolání výjimky
    if not isinstance(value, expected_type):
        raise IsInstanceValueError(value, expected_type)

    # Zachycení výjimky
    try:
        is_instance_verifier(value, expected_type)
    except IsInstanceValueError as e:
        print(f"Chyba typu: {e}")
        # Další zpracování chyby typu
    ```

    Souvislosti s typovým systémem Pythonu:
    --------------------------------------
    Tato výjimka úzce souvisí s vestavěnou funkcí `isinstance()` v Pythonu,
    která ověřuje, zda je objekt instancí určitého typu nebo jeho podtřídy.
    Pochopení typové hierarchie Pythonu a dědičnosti tříd je klíčové pro
    správné používání a interpretaci této výjimky.
    """

    # Specifický nadpis pro chyby neshody typu
    title = "\n⚠ ZACHYCENA NESHODA TYPU HODNOTY!\n"

    def __init__(self, value: Any, expected: Union[type, Tuple[type, ...]]):
        """
        Inicializuje výjimku s informacemi o neshodě typu.

        Vytváří detailní zprávu obsahující informace o skutečném typu hodnoty
        a očekávaném typu nebo typech pro snadnou diagnostiku problému.

        Args:
            value (Any): Hodnota, která neprošla validací typu.
            expected (Union[type, Tuple[type, ...]]): Očekávaný typ nebo typy.

        Algoritmus:
        ----------
        1. Uložení reference na původní hodnotu a očekávané typy
        2. Vytvoření informativní zprávy s detaily o typové neshodě
        3. Sestavení praktických pokynů k nápravě problému
        4. Inicializace nadřazené výjimky s formátovanou zprávou

        Poznámky:
        --------
        Zpráva výjimky obsahuje reprezentaci hodnoty pomocí `repr()`,
        což umožňuje lépe diagnostikovat problémy s hodnotami, které
        mají specifickou textovou reprezentaci (např. řetězce vs. čísla).
        """
        # Uložení hodnot pro diagnostiku
        self.value = value
        self.expected = expected

        # Vytvoření popisu problému
        what_happened = [
            f"   - Ověřovaná hodnota není instancí očekávaného typu.\n"
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
            f"   - Požadovaný typ/typy: {self._format_items(self.expected)}\n"
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontrolujte typ hodnoty, kterou předáváte k ověření.\n",
            "   - Ujistěte se, že kontrolujete správnou definici typu.\n",
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)




