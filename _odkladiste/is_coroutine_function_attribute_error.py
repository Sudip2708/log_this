from typing import Any, Iterable

from ._value_base import VerifyValueError


class VerifyIsCoroutineFunctionAttributeError(VerifyValueError):
    """
    Výjimka vyvolaná, když ověřovaná hodnota postrádá jeden nebo více očekávaných atributů (pro coroutine funkce).

    Tato výjimka je vyvolána, pokud objekt, který má být ověřen, neobsahuje
    všechny atributy specifikované v `expected_attributes`. Tyto atributy jsou
    očekávány, aby byly coroutine funkcemi. Výjimka poskytuje informace o
    chybějících atributech a o tom, které atributy byly požadovány.

    Klíčové koncepty:
    -----------------
    * Validace přítomnosti atributů - Ověření, zda objekt disponuje požadovanými atributy
    * Asynchronní programování v Pythonu - Kontext, ve kterém se očekávají coroutine funkce
    * Diagnostika chybějících atributů - Identifikace atributů, které objektu schází

    Architekturální kontext:
    -----------------------
    Tato výjimka je důležitou součástí ověřování objektů, které mají obsahovat
    asynchronní operace. Je vyvolávána funkcí `is_coroutine_function_verifier()`,
    když se zjistí, že ověřovaný objekt nemá všechny potřebné atributy.

    Detaily implementace:
    --------------------
    * Ukládá původní hodnotu a seznam očekávaných atributů pro účely diagnostiky
    * Využívá interní metodu `_get_missing_attributes()` k detekci chybějících atributů
    * Formátuje zprávu tak, aby jasně zobrazovala očekávané a chybějící atributy
    * Poskytuje užitečné rady pro nápravu problému s chybějícími atributy
    * Používá specifický nadpis pro zdůraznění chyby související s chybějícími atributy

    Povinné atributy:
    ----------------
    * value (Any): Původní ověřovaná hodnota (objekt)
    * expected_attributes (Iterable[str]): Kolekce názvů očekávaných atributů
    * missing (List[str]): Seznam názvů chybějících atributů

    Příklady použití:
    ---------------
    ```python
    async def async_function():
        return "done"

    class MyPartialObject:
        def __init__(self):
            self.async_attr = async_function

    obj = MyPartialObject()
    expected = ["async_attr", "another_async_attr"]

    try:
        # Předpokládejme, že existuje funkce is_coroutine_function_verifier
        from your_module import is_coroutine_function_verifier
        is_coroutine_function_verifier(obj, expected)
    except VerifyIsCoroutineFunctionAttributeError as e:
        print(f"Chyba: Objekt postrádá potřebné atributy pro coroutine funkce: {e}")
        # Další zpracování chyby
    ```

    Souvislosti s asynchronním kódem a strukturou objektů:
    -----------------------------------------------------
    Při práci s asynchronním kódem je často nutné, aby objekty měly specifické
    atributy, které jsou samy o sobě asynchronními funkcemi. Tato výjimka
    pomáhá zajistit, že objekty určené pro asynchronní operace mají správnou
    strukturu a potřebné coroutine funkce.
    """

    # Specifický nadpis pro chyby chybějících atributů
    title = "\n⚠ ZACHYCENA NESHODA OČEKÁVANÝCH ATRIBUTŮ!\n"

    def __init__(self, value: Any, expected_attributes: Iterable[str]):
        """
        Inicializuje výjimku s informacemi o chybějících atributech (pro coroutine funkce).

        Vytváří detailní zprávu, která informuje o ověřované hodnotě, seznamu
        očekávaných atributů a konkrétních atributech, které v objektu chybí.

        Args:
            value (Any): Hodnota (objekt), u které proběhla validace atributů.
            expected_attributes (Iterable[str]): Seznam názvů atributů, které se
                očekávaly, aby byly přítomny a byly coroutine funkcemi.

        Algoritmus:
        ----------
        1. Uložení reference na původní hodnotu a seznam očekávaných atributů.
        2. Volání interní metody `_get_missing_attributes()` pro zjištění chybějících atributů.
        3. Uložení seznamu chybějících atributů.
        4. Vytvoření informativní zprávy s detaily o chybějících atributech.
        5. Poskytnutí pokynů k nápravě, zaměřených na přidání chybějících atributů.
        6. Inicializace nadřazené výjimky s vytvořenou zprávou.

        Poznámky:
        --------
        Interní metoda `_get_missing_attributes()` efektivně zjišťuje, které
        z očekávaných atributů nejsou v daném objektu přítomny pomocí `hasattr()`.
        """
        # Uložení hodnot pro diagnostiku
        self.value = value
        self.expected_attributes = expected_attributes
        self.missing = self._get_missing_attributes()

        # Vytvoření popisu problému
        what_happened = [
            "   - Ověřovaná hodnota na coroutine function nemá všechny potřebné atributy.\n"
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Očekávané atributy: {self._format_items(self.expected_attributes)}\n",
            f"   - Chybějící atributy: {self._format_items(self.missing)}\n"
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj definici hodnoty, kterou předáváš k ověření.\n",
            "   - Ujisti se, že obsahuje všechny potřebné atributy.\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)

    def _get_missing_attributes(self) -> list[str]:
        """
        Vrací seznam atributů, které chybí v ověřované hodnotě.

        Tato metoda prochází očekávané atributy a pomocí `hasattr()` určí,
        které z nich nejsou přítomny v objektu `self.value`.

        Výkonová poznámka:
        ------------------
        Neošetřuje chyby uvnitř `hasattr()`, protože tato výjimka je volána až
        poté, co vstupní hodnota byla ověřena jiným verifikátorem. Pokud by
        vstup nebyl vhodný pro introspekci, došlo by k selhání dříve. Tato metoda
        tedy předpokládá, že vstupní data jsou validní a připravená k použití.

        Returns:
            List[str]: Seznam názvů atributů, které v objektu chybí.
        """
        return [
            attr
            for attr in self.expected_attributes
            if not hasattr(self.value, attr)
        ]