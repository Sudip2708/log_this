import inspect
from typing import Optional, Tuple

from ._internal_base import VerifyInternalError
from ._get_caller_context import get_caller_context


class VerifyUnexpectedInternalError(VerifyInternalError):
    """
    Výjimka vyvolaná při neočekávané interní chybě v knihovně.

    Tato výjimka slouží k zachycení a diagnostice neočekávaných chyb,
    které by v normálním provozu knihovny neměly nastat. Poskytuje
    detailní informace o kontextu chyby, včetně názvu funkce a modulu,
    ve kterých k chybě došlo.

    Klíčové koncepty:
    -----------------
    * Zachycení neočekávaných výjimek - Pro odhalení problémů v knihovně
    * Introspekce zásobníku volání - Získání kontextu, kde k chybě došlo
    * Diagnostika chyb - Poskytnutí užitečných informací pro ladění

    Architekturální kontext:
    -----------------------
    Tato výjimka je konkrétní implementací interní chyby knihovny.
    Je určena primárně pro vývojáře knihovny, nikoliv pro koncové uživatele.
    Slouží k zachycení a diagnostice chyb, které by mohly indikovat problémy
    v implementaci samotné knihovny.

    Detaily implementace:
    --------------------
    * Využívá modul `inspect` pro analýzu zásobníku volání a získání kontextu
    * Zachycuje původní výjimku pro úplnou diagnostiku problému
    * Poskytuje informace o funkci a modulu, kde k chybě došlo
    * Přizpůsobuje nadpis výjimky pro zdůraznění neočekávaného charakteru chyby

    Příklady použití:
    ---------------
    ```python
    try:
        # Potenciálně problematický kód
        result = complex_operation()
    except Exception as e:
        # Zachycení neočekávané výjimky
        raise VerifyUnexpectedInternalError(e) from e
    ```
    """

    # Specifický nadpis pro neočekávané chyby
    title = "\n⚠ INTERNÍ CHYBA: DOŠLO K NEOČEKÁVANÉ UDÁLOSTI!\n"

    def __init__(self, original_exception: Exception):
        """
        Inicializuje výjimku s informacemi o neočekávané chybě.

        Načítá informace o kontextu, kde k chybě došlo (funkce a modul),
        a vytváří informativní chybovou zprávu pro vývojáře.

        Args:
            original_exception (Exception): Původní výjimka, která byla neočekávaně vyvolána.

        Algoritmus:
        ----------
        1. Uložení reference na původní výjimku
        2. Získání informací o kontextu, kde k chybě došlo
        3. Vytvoření informativní zprávy s popisem problému
        """
        # Uložení původní výjimky
        self.original_exception = original_exception

        # Získání kontextu, kde k chybě došlo
        self.function, self.module = get_caller_context()

        # Vytvoření popisu chyby
        what_happened = [
            f"   - Výjimku vyvolal: {self.function}() z {self.module}\n",
            f"   - Zachycená výjimka: {type(self.original_exception).__name__} - {str(self.original_exception)}.\n",
        ]

        # Inicializace základní interní výjimky
        # Poznámka: what_to_do není potřeba specifikovat, použije se výchozí hodnota z VerifyInternalError
        super().__init__(what_happened, None, self.title)

