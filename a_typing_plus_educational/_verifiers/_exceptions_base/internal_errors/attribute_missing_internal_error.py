from typing import Any

from ._internal_base import VerifyInternalError


class VerifyAttributeMissingInternalError(VerifyInternalError):
    """
    Výjimka vyvolaná při detekci chybějících povinných atributů ve validační třídě.

    Tato interní výjimka slouží jako kontrolní mechanismus při tvorbě a inicializaci
    nových validátorů. Detekuje situace, kdy třída odvozená od základních validačních
    tříd nemá definované všechny povinné atributy, což by vedlo k nesprávnému
    fungování validačního systému.

    Klíčové koncepty:
    -----------------
    * Reflexe a introspekce tříd - Kontrola přítomnosti atributů v době běhu
    * Definice kontraktu - Vynucení dodržování rozhraní pro validační třídy
    * Včasná detekce chyb - Odhalení problémů při inicializaci, nikoliv při použití
    * Dokumentace požadavků - Poskytnutí jasných informací o tom, co chybí

    Architekturální kontext:
    -----------------------
    Tato výjimka je nedílnou součástí kontrolního mechanismu validačního systému.
    Je vyvolávána v konstruktorech základních validačních tříd, když se zjistí,
    že odvozená třída neposkytuje všechny povinné atributy. Tímto způsobem
    zajišťuje, že všechny validátory splňují předepsané rozhraní.

    Detaily implementace:
    --------------------
    * Uchovává název třídy s chybějícími atributy pro identifikaci problému
    * Poskytuje seznam všech požadovaných atributů pro úplnou dokumentaci požadavků
    * Přesně identifikuje chybějící atributy pro snadnou opravu
    * Obsahuje pomocnou metodu pro formátování seznamů atributů v chybové zprávě
    * Upravuje nadpis pro jasné odlišení od jiných interních chyb

    Příklady použití:
    ---------------
    ```python
    # V konstruktoru základní validační třídy
    def __init__(self):
        # Kontrola požadovaných atributů
        required_attrs = ['supported_type', 'error_message_template']
        missing_attrs = [attr for attr in required_attrs if not hasattr(self.__class__, attr)]

        if missing_attrs:
            raise VerifyMissingAttributeInternalError(
                self.__class__.__name__,
                required_attrs,
                missing_attrs
            )
    ```

    Poznámky k rozšíření:
    --------------------
    * Výjimku lze rozšířit o podporu kontroly dalších aspektů validačních tříd,
      jako je správnost typových anotací nebo přítomnost specifických metod
    * Zvažte přidání kontroly nejen přítomnosti atributů, ale i jejich správného
      formátu nebo hodnoty pro komplexnější validační třídy
    * Pro pokročilé použití by mohla být doplněna o automatické návrhy řešení
      specifické pro jednotlivé chybějící atributy
    """

    title = "\n⚠ INTERNÍ CHYBA: ZACHYCENA TŘÍDA S CHYBĚJÍCÍMI POVINNÝMI ATRIBUTY!\n"

    def __init__(self, cls, required, missing):
        """
        Inicializace výjimky pro chybějící povinné atributy.

        Vytváří detailní popis problému zahrnující název třídy, seznam všech
        požadovaných atributů a konkrétní seznam chybějících atributů.

        Args:
            cls (str): Třída s chybějícími atributy
            required (list): Seznam všech povinných atributů
            missing (list): Seznam chybějících atributů

        Algoritmus:
        ----------
        1. Uložení informací o třídě, požadovaných a chybějících atributech
        2. Vytvoření detailního popisu problému včetně formátovaných seznamů atributů
        3. Poskytnutí pokynů k řešení zaměřených na vývojáře
        4. Inicializace nadřazené výjimky s připravenými informacemi

        Souvislosti:
        -----------
        Tato metoda používá pomocnou metodu _format_items(), která musí být
        implementována v této třídě nebo v rodičovské třídě pro správné
        formátování seznamů položek v chybové zprávě.
        """
        self.cls = cls
        self.required = required
        self.missing = missing

        what_happened = [
            f"   - Při inicializaci byla zachycena validační třída, která nemá definovaná všechna potřebná atributy.\n",
            f"   - Jméno třídy: {self.cls.__name__}\n",
            f"   - Očekávané atributy: {self._format_items(self.required)}\n",
            f"   - Chybějící atributy: {self._format_items(self.missing)}\n"
        ]

        what_to_do = [
            "   - Zkontrolujte definici dané třídy a doplňte chybějící atributy.\n",
            "   - Ujistěte se, že všechny atributy mají správný název a jsou definovány na úrovni třídy, ne instance.\n",
            "   - Projděte dokumentaci základní třídy pro pochopení účelu a požadovaného formátu každého atributu.\n",
            "   - Pokud se tato chyba vyskytla v produkci, pravděpodobně se jedná o poškození interních dat a je potřeba knihovnu přeinstalovat.\n"
        ]

        super().__init__(what_happened, what_to_do)
