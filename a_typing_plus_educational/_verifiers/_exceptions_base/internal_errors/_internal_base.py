from typing import List, Optional, Union

from ..bases import VerifyError


class VerifyInternalError(VerifyError):
    """
    Základní třída pro všechny interní chyby knihovny Verify.

    Tato třída slouží jako společný předek pro všechny výjimky, které reprezentují
    interní chyby v knihovně - tedy chyby, které by za normálních okolností
    neměly nastat a indikují problém v implementaci samotné knihovny.

    Klíčové koncepty:
    -----------------
    * Interní chyby knihovny - Problémy v implementaci, nikoliv v použití
    * Hierarchie výjimek - Kategorizace různých typů chyb
    * Chybové zprávy pro vývojáře - Poskytnutí užitečných informací pro ladění

    Architekturální kontext:
    -----------------------
    Tato třída tvoří mezistupeň v hierarchii výjimek knihovny mezi základní
    třídou `VerifyError` a konkrétními implementacemi interních chyb.
    Umožňuje společné zachytávání všech interních chyb a poskytuje
    konzistentní formát chybových zpráv.

    Detaily implementace:
    --------------------
    * Upravuje výchozí nadpis pro zdůraznění interního charakteru chyby
    * Poskytuje výchozí formát chybové zprávy zaměřený na vývojáře knihovny
    * Udržuje konzistentní rozhraní s ostatními kategoriemi výjimek

    Příklady použití:
    ---------------
    ```python
    # Zachycení všech interních chyb knihovny
    try:
        result = verify_function(value)
    except VerifyInternalError as e:
        logging.error("Interní chyba knihovny: %s", e)
        # Další zpracování interní chyby
    ```

    Poznámky k rozšíření:
    --------------------
    * Při vytváření nových typů interních chyb je třeba dbát na konzistentní
      formát chybových zpráv a poskytnout dostatek informací pro ladění
    * Zvažte přidání dodatečných diagnostických informací specifických pro
      interní chyby (např. verze knihovny, konfigurace, atd.)
    """

    # Výchozí nadpis pro všechny interní chyby
    title = "\n⚠ INTERNÍ CHYBA KNIHOVNY VERIFY!\n"

    def __init__(
            self,
            what_happened: Union[List[str], str],
            what_to_do: Optional[List[str], str],
            title: Optional[str] = None,
    ):
        """
        Inicializuje základní interní výjimku.

        Args:
            what_happened (Union[List[str], str]): Popis problému.
            what_to_do (Union[List[str], str]): Doporučení k nápravě.
            title (Optional[str]): Volitelný nadpis výjimky.
        """
        # Výchozí pokyny pro interní chyby, pokud nejsou specifikovány
        if not what_to_do:
            what_to_do = [
                "   - Tato situace by za běžných okolností neměla nastat a pravděpodobně značí chybu v kódu knihovny.\n",
                "   - Zkontrolujte aktuální verzi knihovny nebo prosím nahlaste chybu s podrobným popisem.\n",
            ]

        # Inicializace základní výjimky
        super().__init__(what_happened, what_to_do, title)


