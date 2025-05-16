from typing import Any

from ._internal_base import VerifyInternalError


class VerifyNotStringListInternalError(VerifyInternalError):
    """
    Výjimka vyvolaná, když je očekáván řetězec nebo seznam řetězců, ale je obdržena jiná hodnota.

    Tato interní výjimka slouží k signalizaci chyby v implementaci validačních tříd
    nebo v logice předávání parametrů do základní výjimky `VerifyError`.
    Signalizuje nesprávné použití interních mechanismů knihovny, kdy se
    očekávalo, že parametry budou typu `str` nebo `List[str]`, ale byl obdržen jiný typ.

    Klíčové koncepty:
    -----------------
    * Typová kontrola parametrů - Ověřování správných typů pro interní API
    * Formátování chybových zpráv - Konzistentní zpracování textových i seznamových formátů
    * Diagnostika interních chyb - Poskytnutí detailních informací pro vývojáře

    Architekturální kontext:
    -----------------------
    Tato výjimka je konkrétní specializací `VerifyInternalError` zaměřenou na
    zachycení problémů při zpracování parametrů chybových zpráv. Tvoří důležitou
    součást systému zajišťujícího typovou bezpečnost i v rámci samotné knihovny.
    Je vyvolána výhradně v interních mechanismech zpracování chyb.

    Detaily implementace:
    --------------------
    * Uchovává referenci na problematickou hodnotu pro snazší diagnostiku
    * Poskytuje detailní popis očekávaného a skutečného typu hodnoty
    * Generuje specifické instrukce pro řešení problému zaměřené na vývojáře knihovny
    * Využívá vlastní nadpis pro rychlejší identifikaci typu problému

    Příklady použití:
    ---------------
    ```python
    # Kontrola typů před zpracováním
    if not isinstance(message, (str, list)):
        raise NotStringListInternalError(message)

    # Nebo jako ochrana v konstruktoru jiné výjimky
    def __init__(self, what_happened, what_to_do):
        if not isinstance(what_happened, (str, list)):
            raise NotStringListInternalError(what_happened)
        # Další zpracování...
    ```

    Poznámky k rozšíření:
    --------------------
    * Tuto výjimku lze rozšířit pro kontrolu dalších specifických typových požadavků
      na interní parametry knihovny
    * Při úpravách zvažte přidání dodatečných diagnostických informací o kontextu,
      kde byla problematická hodnota zachycena
    """

    title = "\n⚠ INTERNÍ CHYBA: NESPRÁVNÝ TYP OČEKÁVANÉ HODNOTY!\n"

    def __init__(self, value: Any):
        """
        Inicializuje výjimku s informacemi o nesprávném typu.

        Vytváří detailní popis problému zahrnující skutečný typ předané hodnoty
        a její reprezentaci pro usnadnění diagnostiky problému.

        Args:
            value (Any): Hodnota nesprávného typu, která vyvolala výjimku.

        Algoritmus:
        ----------
        1. Uložení reference na problematickou hodnotu
        2. Vytvoření detailního popisu problému s typem a hodnotou
        3. Poskytnutí pokynů k řešení zaměřených na vývojáře knihovny
        4. Inicializace nadřazené výjimky s připravenými informacemi

        Výjimky:
        -------
        Tato metoda by neměla vyvolávat žádné výjimky, protože slouží jako
        mechanismus pro zpracování chyb. Pokud by došlo k výjimce zde, jednalo
        by se o kritickou chybu v knihovně.
        """
        self.value = value

        what_happened = [
            f"   - Interní logika knihovny obdržela neočekávaný typ.\n",
            f"   - Při vytváření výjimky a zpracování předaných parametrů byl zjištěn neočekávaný typ.\n",
            f"   - Očekáván byl typ 'str' nebo 'List[str]', ale obdržen byl typ '{type(self.value).__name__}'.\n",
            f"   - Předaná hodnota: {repr(self.value)}\n"
        ]

        what_to_do = [
            "   - Tato chyba indikuje problém v implementaci knihovny a neměla by se běžně vyskytovat.\n",
            "   - Zkontrolujte kód, který předává hodnotu pro tento parametr, a ujistěte se, že se jedná o řetězec nebo seznam řetězců.\n",
            "   - Ověřte typové anotace a dokumentaci příslušných metod a tříd.\n",
            "   - Pokud se tato chyba vyskytla v produkčním prostředí, prosím nahlaste ji s podrobným popisem a kontextem.\n"
        ]

        super().__init__(what_happened, what_to_do)


