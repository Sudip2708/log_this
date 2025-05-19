from typing import Any

from ..._exceptions_base import VerifyValueError


class VerifyAttributeAccessError(VerifyValueError, TypeError):
    """
    Výjimka vyvolaná, když během pokusu o přístup k atributu pomocí `getattr()` dojde k chybě typu.

    Tato výjimka je specifickou variantou `TypeError` (i když může indikovat i jiné problémy související s přístupem k atributům),
    která je vyvolána funkcí `get_attr_safe()`, když standardní volání `getattr()` selže s výjimkou `TypeError`.
    Může to indikovat problémy s implementací speciálních metod jako `__getattribute__` nebo `__getattr__` na daném objektu.

    Klíčové koncepty:
    -----------------
    * Bezpečné získávání atributů - Funkce `get_attr_safe()` obaluje přístup k atributům do try-except bloku.
    * Chyby typu při přístupu - Indikuje problém s typem v kontextu získávání atributu.
    * Speciální metody pro přístup k atributům - `__getattribute__` a `__getattr__` mohou ovlivnit chování `getattr()`.

    Architekturální kontext:
    -----------------------
    Tato výjimka je součástí mechanismu pro bezpečnější přístup k atributům objektů.
    Zachytává potenciální chyby typu, které mohou nastat při standardním pokusu o získání atributu,
    a poskytuje kontext v rámci validačního systému.

    Detaily implementace:
    --------------------
    * Dědí od `VerifyValueError` pro jednotný formát chybových hlášení v knihovně Verify.
    * Dědí od `TypeError`, aby si zachovala typickou sémantiku chyby typu (i když příčina může být hlubší).
    * Obsahuje podrobné informace o objektu, názvu atributu, ke kterému se přistupovalo, a původní chybové zprávě.
    * Nabízí uživateli rady, jak diagnostikovat problém, zejména s ohledem na speciální metody pro přístup k atributům.
    * Má specifický nadpis, který jasně identifikuje typ chyby.

    Povinné atributy:
    ----------------
    * obj (Any): Objekt, u kterého došlo k chybě při přístupu k atributu.
    * attribute (str): Název atributu, ke kterému se pokoušelo přistoupit.
    * error_message (str): Původní chybová zpráva zachycené výjimky `TypeError`.

    Příklady použití:
    ---------------
    ```python
    class ProblematicObject:
        def __getattribute__(self, name):
            if name == "secret":
                raise TypeError("Přístup k 'secret' je zakázán!")
            return super().__getattribute__(name)

    obj = ProblematicObject()

    try:
        from your_module import get_attr_safe
        value = get_attr_safe(obj, "secret")
        print(value)
    except VerifyGetAttrSafeAttributeAccessError as e:
        print(f"Chyba při přístupu k atributu: {e}")
        # Další zpracování chyby
    ```

    Souvislosti s interním chováním objektů:
    ---------------------------------------
    Tato výjimka upozorňuje na to, že způsob, jakým objekt interně spravuje přístup
    ke svým atributům (prostřednictvím speciálních metod), může vést k chybám typu.
    Pochopení implementace těchto metod je klíčové pro řešení těchto problémů.
    """

    # Specifický nadpis pro chyby přístupu k atributům
    title = "\n⚠ NASTALA CHYBA PŘI PŘÍSTUPU K ATRIBUTU!\n"

    def __init__(
            self,
            obj: Any,
            attribute_name: str,
            error_message: str
    ):
        """
        Inicializuje výjimku s informacemi o chybě typu při přístupu k atributu.

        Vytváří detailní zprávu, která informuje o objektu, názvu atributu a
        původní chybové zprávě, která byla zachycena během pokusu o přístup.

        Args:
            obj (Any): Objekt, u kterého došlo k chybě.
            attribute_name (str): Název atributu, ke kterému se přistupovalo.
            error_message (str): Původní chybová zpráva výjimky `TypeError`.

        Algoritmus:
        ----------
        1. Uložení reference na objekt, název atributu a chybovou zprávu.
        2. Vytvoření informativní zprávy s detaily o objektu, atributu a chybě.
        3. Poskytnutí pokynů k nápravě, zaměřených na kontrolu implementace přístupu k atributům.
        4. Inicializace nadřazené výjimky s vytvořenou zprávou a nadpisem.

        Poznámky:
        --------
        Dědění od `TypeError` umožňuje, aby tuto výjimku zachytávaly i obecné
        bloky `except TypeError`, což může být v některých případech žádoucí.
        Nicméně doporučuje se zachytávat specifickou výjimku `VerifyGetAttrSafeAttributeAccessError`
        pro přesnější ošetření tohoto typu chyby v kontextu knihovny Verify.
        """
        # Uložení hodnoty pro diagnostiku
        self.obj = obj
        self.attribute = attribute_name
        self.error_message = error_message

        # Vytvoření popisu problému
        what_happened = [
            f"   - Funkce pro získání atributu objektu zachytila chybu typu při přístupu k atributu.\n",
            f"   - Objekt: {repr(self.obj)}\n",
            f"   - Typ objektu: {type(self.obj).__name__}\n",
            f"   - Požadovaný atribut: {repr(self.attribute)}\n"
            f"   - Chybová zpráva: {error_message}\n"
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj objekt a ověř, zda má správně implementovaný přístup k atributům.\n",
            "   - Důvodem může být nestandardní implementace metod __getattribute__ nebo __getattr__ objektu.\n"
            "   - Pokud jde o objekt s nestandardním chováním, ověř jeho dokumentaci nebo implementaci.\n",
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)