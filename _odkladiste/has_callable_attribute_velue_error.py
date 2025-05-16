from typing import Any, Iterable, List, Union

from .._bases import VerifyValueError


class VerifyHasCallableAttributeValueError(VerifyValueError):
    """
    Výjimka vyvolaná, když jeden nebo více očekávaných atributů není volatelných.

    Tato výjimka je vyvolána, pokud ověřovaná hodnota obsahuje všechny atributy
    specifikované v `expected_attributes`, ale alespoň jeden z těchto atributů
    není spustitelný objekt (například funkce, metoda nebo objekt s implementovanou
    metodou `__call__`).

    Klíčové koncepty:
    -----------------
    * Validace volatelnosti atributů - Ověření, zda jsou specifické atributy spustitelné
    * Typy volatelných objektů v Pythonu - Funkce, metody, generátory, korutiny, objekty s `__call__`
    * Diagnostika nevolatelných atributů - Identifikace atributů, které nelze zavolat

    Architekturální kontext:
    -----------------------
    Tato výjimka je součástí validačního mechanismu pro ověřování, zda objekt
    poskytuje požadované spustitelné operace. Je vyvolána funkcí
    `callable_attribute_verifier()`, když jsou nalezeny očekávané atributy,
    ale jejich typ neodpovídá volatelnému objektu.

    Detaily implementace:
    --------------------
    * Ukládá původní hodnotu a seznam očekávaných atributů pro diagnostiku
    * Jasně informuje, že problém spočívá v tom, že některé atributy nejsou volatelné
    * Poskytuje rady, jak zkontrolovat definici atributů a zajistit jejich volatelnost
    * Používá specifický nadpis, který zdůrazňuje nesprávnou definici atributů

    Povinné atributy:
    ----------------
    * value (Any): Původní ověřovaná hodnota (objekt)
    * expected (Iterable[str]): Kolekce názvů očekávaných atributů

    Příklady použití:
    ---------------
    ```python
    def my_function():
        pass

    class MyObject:
        def __init__(self):
            self.func = my_function
            self.value = 123

    obj = MyObject()
    expected = ["func", "value"]

    try:
        # Předpokládejme, že existuje funkce callable_attribute_verifier
        from your_module import callable_attribute_verifier
        callable_attribute_verifier(obj, expected)
    except VerifyHasCallableAttributeValueError as e:
        print(f"Chyba: Jeden nebo více atributů není volatelných: {e}")
        # Další zpracování chyby
    ```

    Souvislosti s návrhem rozhraní objektů:
    --------------------------------------
    V mnoha případech se očekává, že objekty budou poskytovat určité operace
    prostřednictvím svých metod (volatelných atributů). Tato výjimka pomáhá
    zajistit, že objekty, které mají implementovat určité rozhraní, skutečně
    poskytují požadované spustitelné metody.
    """

    # Specifický nadpis pro chyby chybějících atributů
    title = "\n⚠ ZACHYCENY NEVOLATELNÉ ATRIBUTY!\n"

    def __init__(
            self,
            value: Any,
            expected_attributes: Union[str, Iterable[str]],
            not_callable_attribute: List[str]
    ):
        """
        Inicializuje výjimku s informacemi o atributech, které nejsou volatelné.

        Vytváří detailní zprávu, která informuje o ověřované hodnotě a seznamu
        očekávaných atributů, přičemž zdůrazňuje, že tyto atributy by měly být
        spustitelné objekty.

        Args:
            value (Any): Hodnota (objekt), u které proběhla validace atributů.
            expected_attributes (Iterable[str]): Seznam názvů atributů, u kterých se
                očekávalo, že budou volatelné.

        Algoritmus:
        ----------
        1. Uložení reference na původní hodnotu a seznam očekávaných atributů.
        2. Vytvoření informativní zprávy, která popisuje problém (atributy nejsou volatelné).
        3. Poskytnutí pokynů k nápravě, zaměřených na kontrolu definice atributů.
        4. Inicializace nadřazené výjimky s vytvořenou zprávou.

        Poznámky:
        --------
        Zpráva výjimky jasně uvádí, že problém není v absenci atributů, ale v jejich
        nesprávném typu (neměly by to být běžné proměnné, ale volatelné objekty).
        """
        # Uložení hodnot pro diagnostiku
        self.value = value
        self.expected = expected_attributes
        self.not_callable = not_callable_attribute

        # Vytvoření popisu problému
        what_happened = [
            "   - Funkce pro ověření volatelnosti atributů zachytila chybu.\n"
            f"   - Ověřovaný objekt: {repr(self.value)}\n",
            f"   - Ověřované atributy na volatelnost: {self._format_items(self.expected)}\n",
            f"   - Atributy které ověřením neprošli: {self._format_items(self.not_callable)}\n",
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj definici hodnoty, kterou předáváš k ověření.\n",
            "   - Zkontroluj, zda je hodnota správně definována jako volatelný objekt.\n",
            "   - Například funkce, metoda, nebo objekt s definovanou metodou __call__.\n"        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)