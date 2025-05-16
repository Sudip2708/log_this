from typing import List, Optional, Union

from ..bases import VerifyError


class VerifyParameterError(VerifyError):
    """
    Základní třída pro všechny chyby nesprávně specifikovaných vstupních parametrů.

    Tato třída slouží jako společný předek pro všechny výjimky, které reprezentují
    situace, kdy jsou nesprávně zadány parametry pro validační funkce. Tyto chyby
    indikují problémy s použitím API knihovny, nikoliv s validovanými hodnotami samotnými.

    Klíčové koncepty:
    -----------------
    * Chyby v použití API - Indikují nesprávné použití validačních funkcí
    * Strukturální chyby - Týkají se struktury a formátu vstupních parametrů
    * Edukativní zpětná vazba - Poskytování informací o správném použití API

    Architekturální kontext:
    -----------------------
    Tato třída tvoří mezistupeň v hierarchii výjimek knihovny mezi základní
    třídou `VerifyError` a konkrétními implementacemi chyb vstupních parametrů.
    Umožňuje společné zachytávání všech chyb souvisejících s nesprávným použitím API
    a poskytuje konzistentní formát chybových zpráv.

    Detaily implementace:
    --------------------
    * Upravuje výchozí nadpis pro zdůraznění charakteru chyby vstupu
    * Poskytuje výchozí formát chybové zprávy zaměřený na vývojáře
    * Udržuje konzistentní rozhraní s ostatními kategoriemi výjimek
    * Na rozdíl od chyb validace hodnot tyto výjimky nemohou být potlačeny parametrem `bool_only`

    Povinné atributy a metody:
    -------------------------
    * title (str): Nadpis chybové zprávy specifický pro chyby vstupních parametrů
    * __init__(...): Konstruktor přijímající potřebné parametry pro vytvoření informativní zprávy

    Příklady použití:
    ---------------
    ```python
    # Zachycení všech chyb vstupních parametrů
    try:
        result = verify_function(value, expected_param)
    except VerifyParameterError as e:
        logging.error("Chyba v použití API: %s", e)
        # Další zpracování chyby API
    ```

    Poznámky k rozšíření:
    --------------------
    * Při vytváření nových typů chyb vstupních parametrů je vhodné poskytovat
      konkrétní příklady správného použití API pro rychlé vyřešení problému
    * Tyto výjimky by měly být jasně odlišeny od chyb validace hodnot,
      aby uživatel mohl snadno identifikovat, zda jde o problém s daty
      nebo s použitím knihovny
    """

    # Výchozí nadpis pro všechny chyby vstupních parametrů
    title = "\n⚠ CHYBA VE SPECIFIKACI PARAMETRŮ!\n"

    def __init__(
            self,
            what_happened: Union[List[str], str],
            what_to_do: Union[List[str], str],
            title: Optional[str] = None,
    ):
        """
        Inicializuje základní výjimku pro nesprávné vstupní parametry.

        Vytváří strukturovanou chybovou zprávu s důrazem na edukativní
        aspekt a vysvětlení správného použití API knihovny.

        Args:
            what_happened (Union[List[str], str]): Popis problému se vstupními parametry.
            what_to_do (Union[List[str], str]): Doporučení k nápravě problému.
            title (Optional[str]): Volitelný nadpis výjimky, který přepíše výchozí.

        Algoritmus:
        ----------
        1. Uložení specifických informací o chybě
        2. Inicializace nadřazené výjimky s formátovanou zprávou
        3. Zachování konzistentního rozhraní pro všechny chyby vstupních parametrů

        Poznámky:
        --------
        Na rozdíl od chyb validace hodnot (VerifyValueError) tyto výjimky
        nemohou být potlačeny parametrem `bool_only`, protože indikují
        nesprávné použití API, které musí být vždy opraveno.
        """
        # Inicializace základní výjimky
        super().__init__(what_happened, what_to_do, title)