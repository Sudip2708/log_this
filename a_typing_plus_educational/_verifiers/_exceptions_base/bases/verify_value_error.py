from typing import List, Optional, Union

from ..bases import VerifyError


class VerifyValueError(VerifyError):
    """
    Základní třída pro všechny chyby validace hodnot v knihovně Verify.

    Tato třída slouží jako společný předek pro všechny výjimky, které reprezentují
    situace, kdy ověřovaná hodnota nesplňuje validační kritéria. Na rozdíl od
    strukturálních nebo interních chyb se tyto výjimky týkají přímo obsahu dat.

    Klíčové koncepty:
    -----------------
    * Chyby validace hodnot - Problémy s obsahem nebo formátem ověřovaných dat
    * Uživatelská zpětná vazba - Poskytnutí jasné informace o nesplněných požadavcích
    * Rozlišení od jiných kategorií chyb - Oddělení problémů s hodnotami od problémů struktury

    Architekturální kontext:
    -----------------------
    Tato třída tvoří mezistupeň v hierarchii výjimek knihovny mezi základní
    třídou `VerifyError` a konkrétními implementacemi chyb validace hodnot.
    Umožňuje společné zachytávání všech chyb souvisejících s neplatnými hodnotami
    a poskytuje konzistentní formát chybových zpráv.

    Detaily implementace:
    --------------------
    * Upravuje výchozí nadpis pro zdůraznění charakteru chyby validace hodnoty
    * Poskytuje výchozí formát chybové zprávy zaměřený na uživatele
    * Udržuje konzistentní rozhraní s ostatními kategoriemi výjimek
    * Může být potlačena pomocí parametru `bool_only=True` v ověřovacích funkcích

    Povinné atributy a metody:
    -------------------------
    * title (str): Nadpis chybové zprávy specifický pro chyby validace hodnot
    * __init__(...): Konstruktor přijímající potřebné parametry pro vytvoření informativní zprávy

    Příklady použití:
    ---------------
    ```python
    # Zachycení všech chyb validace hodnot
    try:
        result = verify_function(value)
    except VerifyValueError as e:
        logging.warning("Chyba validace hodnoty: %s", e)
        # Další zpracování chyby validace
    ```

    Poznámky k rozšíření:
    --------------------
    * Při vytváření nových typů chyb validace hodnot je vhodné uchovávat referenci
      na původní hodnotu a očekávaná kritéria pro podrobnější diagnostiku
    * V konkrétních implementacích poskytněte specifické pokyny k nápravě
    * Zvažte přidání metod pro formátování hodnot nebo kritérií pro lepší čitelnost
    """

    # Výchozí nadpis pro všechny chyby validace hodnot
    title = "\n⚠ CHYBA VALIDACE HODNOTY!\n"

    def __init__(
            self,
            what_happened: Union[List[str], str],
            what_to_do: Union[List[str], str],
            title: Optional[str] = None,
    ):
        """
        Inicializuje základní výjimku validace hodnoty.

        Vytváří strukturovanou chybovou zprávu s důrazem na srozumitelnost
        a praktickou použitelnost pro koncového uživatele.

        Args:
            what_happened (Union[List[str], str]): Popis problému s validací hodnoty.
            what_to_do (Union[List[str], str]): Doporučení k nápravě problému.
            title (Optional[str]): Volitelný nadpis výjimky, který přepíše výchozí.

        Algoritmus:
        ----------
        1. Uložení specifických informací o chybě
        2. Inicializace nadřazené výjimky s formátovanou zprávou
        3. Zachování konzistentního rozhraní pro všechny chyby validace

        Poznámky:
        --------
        Tato výjimka může být potlačena v ověřovacích funkcích pomocí parametru
        `bool_only=True`, který místo vyvolání výjimky způsobí vrácení hodnoty False.
        Tato logika je implementována v samotných ověřovacích funkcích, nikoliv
        v této výjimce.
        """
        # Inicializace základní výjimky
        super().__init__(what_happened, what_to_do, title)