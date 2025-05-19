from typing import Any

from ..._exceptions_base import VerifyParameterError


class VerifyAttributeNotStrError(VerifyParameterError, TypeError):
    """
    Výjimka vyvolaná, když název atributu předaný funkci `get_attr_safe()` není řetězec.

    Tato výjimka je specifickou variantou `TypeError`, která je vyvolána
    funkcí `get_attr_safe()`, když je argument `attribute_name` (očekávající
    název atributu jako řetězec) předán v jiném datovém typu. Název atributu
    musí být vždy řetězcem, aby bylo možné k němu pomocí `getattr()` přistoupit.

    Klíčové koncepty:
    -----------------
    * Validace typu vstupního parametru - Funkce `get_attr_safe()` vyžaduje název atributu jako `str`
    * Očekávaný datový typ - Argument `attribute_name` musí být typu `str`
    * Signalizace chyby typu - Tato výjimka jasně indikuje, že byl předán argument nesprávného typu

    Architekturální kontext:
    -----------------------
    Tato výjimka je součástí mechanismu pro bezpečnější přístup k atributům objektů.
    Zajišťuje, že funkce `get_attr_safe()` je volána se správným typem argumentu
    pro název atributu, čímž se předchází neočekávaným chybám při pokusu o přístup.

    Detaily implementace:
    --------------------
    * Dědí od `VerifyParameterError` pro jednotný formát chybových hlášení v knihovně Verify.
    * Dědí od `TypeError`, aby si zachovala typickou sémantiku chyby typu.
    * Obsahuje podrobné informace o skutečném typu předaného argumentu a o tom, že očekáván byl řetězec.
    * Nabízí uživateli jasné pokyny, jak chybu opravit (zajištění, že název atributu je řetězec).
    * Má specifický nadpis, který jasně identifikuje typ chyby.

    Povinné atributy:
    ----------------
    * attribute (Any): Hodnota, která byla chybně předána jako název atributu.

    Příklady použití:
    ---------------
    ```python
    class MyObject:
        def __init__(self):
            self.name = "Test"

    obj = MyObject()
    attribute = "name"
    invalid_attribute = 123

    try:
        from your_module import get_attr_safe
        name = get_attr_safe(obj, attribute)  # Toto je v pořádku
        invalid_name = get_attr_safe(obj, invalid_attribute)
        print(invalid_name)
    except VerifyGetAttrSafeAttributeNotStrError as e:
        print(f"Chyba: Název atributu musí být řetězec: {e}")
        # Další zpracování chyby
    ```

    Souvislosti s typovou bezpečností:
    ----------------------------------
    Tato výjimka pomáhá udržovat typovou bezpečnost v rámci funkce `get_attr_safe()`.
    Očekávání řetězce pro název atributu je zásadní pro správnou funkčnost `getattr()`
    a pro předejití chybám, které by mohly vzniknout při použití jiného datového typu.
    """

    # Specifický nadpis pro chyby nesprávného typu parametru
    title = "\n⚠ PARAMETR PRO JMÉNO ATRIBUTU BYL ZADÁN V NEVALIDNÍM FORMÁTU!\n"

    def __init__(self, attribute_name: Any):
        """
        Inicializuje výjimku s informacemi o chybně zadaném názvu atributu.

        Vytváří detailní zprávu, která informuje o hodnotě, která byla předána
        jako název atributu, a o tom, že očekáván byl řetězec. Poskytuje také
        rady, jak chybu opravit.

        Args:
            attribute_name (Any): Hodnota, která byla chybně předána jako název atributu.

        Algoritmus:
        ----------
        1. Uložení reference na chybně zadanou hodnotu atributu.
        2. Vytvoření informativní zprávy s detaily o zadané hodnotě a očekávaném typu.
        3. Poskytnutí pokynů k nápravě (zajištění, že název atributu je řetězec).
        4. Inicializace nadřazené výjimky s vytvořenou zprávou a nadpisem.

        Poznámky:
        --------
        Dědění od `TypeError` umožňuje, aby tuto výjimku zachytávaly i obecné
        bloky `except TypeError`, což může být v některých případech žádoucí.
        Nicméně doporučuje se zachytávat specifickou výjimku `VerifyGetAttrSafeAttributeNotStrError`
        pro přesnější ošetření tohoto typu chyby v kontextu knihovny Verify.
        """
        # Uložení hodnoty pro diagnostiku
        self.attribute = attribute_name

        # Vytvoření popisu problému
        what_happened = [
            "   - Funkce pro získání atributu objektu obdržela nesprávně zadaný parametr pro jméno hledaného atributu\n",
            "   - Název atributu může být předán funkci pouze jako řetězec (str).\n",
            f"   - Zadaný atribut: {repr(self.attribute)}\n",
            f"   - Typ atributu: {type(attribute_name).__name__}\n",
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj definici parametru pro jméno hledaného atributu.\n",
            "   - Ujisti se, že je předán jako řetězec.\n",
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)