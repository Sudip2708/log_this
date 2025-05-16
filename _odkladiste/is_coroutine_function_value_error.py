from typing import Any, Iterable

from ._value_base import VerifyValueError


class VerifyIsCoroutineFunctionValueError(VerifyValueError):
    """
    Výjimka vyvolaná, když jeden nebo více očekávaných atributů není coroutine funkcí.

    Tato výjimka je vyvolána, pokud ověřovaná hodnota obsahuje všechny atributy
    specifikované v `expected_attributes`, ale alespoň jeden z těchto atributů
    není definován jako asynchronní funkce (coroutine function) pomocí `async def`.

    Klíčové koncepty:
    -----------------
    * Validace typu atributů - Ověření, zda jsou specifické atributy určitého typu
    * Asynchronní programování v Pythonu - Koncept coroutine funkcí (`async def`)
    * Diagnostika nesprávného typu atributu - Identifikace atributů, které nejsou coroutine

    Architekturální kontext:
    -----------------------
    Tato výjimka je součástí validačního mechanismu pro asynchronní operace.
    Je vyvolána funkcí `is_coroutine_function_verifier()`, když jsou nalezeny
    očekávané atributy, ale jejich typ neodpovídá asynchronní funkci.

    Detaily implementace:
    --------------------
    * Ukládá původní hodnotu a seznam očekávaných atributů pro diagnostiku
    * Jasně informuje, že problém spočívá v tom, že atributy nejsou coroutine funkcemi
    * Poskytuje rady, jak zkontrolovat definici atributů a zajistit jejich asynchronní charakter
    * Používá specifický nadpis, který zdůrazňuje nesprávnou definici atributů

    Povinné atributy:
    ----------------
    * value (Any): Původní ověřovaná hodnota (objekt)
    * expected_attributes (Iterable[str]): Kolekce názvů očekávaných atributů

    Příklady použití:
    ---------------
    ```python
    async def async_function():
        return "done"

    def sync_function():
        return "not async"

    class MyObject:
        def __init__(self):
            self.async_attr = async_function
            self.sync_attr = sync_function

    obj = MyObject()
    expected = ["async_attr", "sync_attr"]

    try:
        # Předpokládejme, že existuje funkce is_coroutine_function_verifier
        from your_module import is_coroutine_function_verifier
        is_coroutine_function_verifier(obj, expected)
    except VerifyIsCoroutineFunctionValueError as e:
        print(f"Chyba: Jeden nebo více atributů není coroutine funkcí: {e}")
        # Další zpracování chyby
    ```

    Souvislosti s asynchronním kódem:
    ---------------------------------
    V asynchronním programování je klíčové, aby určité operace byly definovány
    jako coroutine funkce, aby mohly být efektivně spouštěny aawaitovány.
    Tato výjimka pomáhá zajistit, že atributy, které mají být použity v asynchronním
    kontextu, jsou skutečně definovány jako coroutine funkce.
    """

    # Specifický nadpis pro chyby chybějících atributů
    title = "\n⚠ ZACHYCENA NESPRÁVNÁ DEFINICE ATRIBUTŮ!\n"

    def __init__(self, value: Any, expected_attributes: Iterable[str]):
        """
        Inicializuje výjimku s informacemi o atributech, které nejsou coroutine funkcemi.

        Vytváří detailní zprávu, která informuje o ověřované hodnotě a seznamu
        očekávaných atributů, přičemž zdůrazňuje, že tyto atributy by měly být
        definovány jako asynchronní funkce.

        Args:
            value (Any): Hodnota (objekt), u které proběhla validace atributů.
            expected_attributes (Iterable[str]): Seznam názvů atributů, u kterých
                se očekávalo, že budou coroutine funkcemi.

        Algoritmus:
        ----------
        1. Uložení reference na původní hodnotu a seznam očekávaných atributů.
        2. Vytvoření informativní zprávy, která popisuje problém.
        3. Poskytnutí pokynů k nápravě, zaměřených na kontrolu definice atributů.
        4. Inicializace nadřazené výjimky s vytvořenou zprávou.

        Poznámky:
        --------
        Zpráva výjimky jasně uvádí, že problém není v absenci atributů, ale v jejich
        nesprávném typu (neměly by to být běžné funkce, ale coroutine funkce).
        """
        # Uložení hodnot pro diagnostiku
        self.value = value
        self.expected = expected_attributes

        # Vytvoření popisu problému
        what_happened = [
            "   - Atributy ověřované hodnoty nejsou coroutine function.\n"
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Očekávané atributy: {self._format_items(self.expected)}\n",
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj definici hodnoty, kterou předáváš k ověření.\n",
            "   - Ověřte, zda obsahuje uvedené atributy a zda jsou coroutine function (definované pomocí `async def`).\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)