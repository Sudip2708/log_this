from typing import Any

from ..._exceptions_base import VerifyValueError


class VerifyNotCallableError(VerifyValueError, ValueError):
    """
    Výjimka vyvolaná, když ověřovaná hodnota není volatelná.

    Tato výjimka je vyvolána, pokud hodnota předaná k ověření pomocí
    funkce `callable_verifier()` není spustitelný objekt (například funkce,
    metoda nebo objekt s implementovanou metodou `__call__`).

    Klíčové koncepty:
    -----------------
    * Validace volatelnosti - Ověření, zda je objekt možné zavolat pomocí operátoru `()`
    * Typy volatelných objektů v Pythonu - Funkce, metody, generátory, korutiny, objekty s `__call__`
    * Diagnostika nevolatelných hodnot - Identifikace objektů, které nelze spustit

    Architekturální kontext:
    -----------------------
    Tato výjimka je jednou z validačních výjimek v knihovně Verify, která se zaměřuje
    na vlastnosti samotné hodnoty. Je vyvolávána funkcí `callable_verifier()` v
    případě, že ověřovaná hodnota nesplňuje kritérium volatelnosti.

    Detaily implementace:
    --------------------
    * Uchovává referenci na původní, nevolatelnou hodnotu pro účely diagnostiky
    * Poskytuje jasné informace o tom, že hodnota není spustitelná
    * Nabízí příklady typů objektů, které jsou považovány za volatelné
    * Upravuje výchozí nadpis pro zdůraznění, že problém spočívá v nevolatelnosti

    Povinné atributy:
    ----------------
    * value (Any): Původní ověřovaná hodnota, která není volatelná

    Příklady použití:
    ---------------
    ```python
    def my_function():
        pass

    my_variable = 123

    # Přímé vyvolání výjimky
    if not callable(my_variable):
        raise CallableValueError(my_variable)

    # Zachycení výjimky
    try:
        # Předpokládejme, že existuje funkce callable_verifier
        from your_module import callable_verifier
        callable_verifier(my_variable)
    except CallableValueError as e:
        print(f"Chyba: Hodnota není spustitelná: {e}")
        # Další zpracování chyby
    ```

    Souvislosti s dynamickým typováním a first-class funkcemi:
    ---------------------------------------------------------
    V Pythonu jsou funkce objekty první třídy, což znamená, že mohou být
    předávány jako argumenty, vraceny z funkcí a přiřazovány proměnným.
    Ověření volatelnosti je důležité v situacích, kdy kód očekává, že s proměnnou
    bude možné zacházet jako s funkcí nebo jiným spustitelným objektem.
    """

    # Specifický nadpis pro chyby nevolatelných hodnot
    title = "\n⚠ ZACHYCEN OBJEKT KTERÝ NENÍ VOLATELNÝ!\n"

    def __init__(self, value: Any):
        """
        Inicializuje výjimku s informacemi o nevolatelné hodnotě.

        Vytváří detailní zprávu, která informuje o tom, že ověřovaná hodnota
        není spustitelná a poskytuje informace o jejím typu a reprezentaci.

        Args:
            value (Any): Hodnota, která nebyla rozpoznána jako volatelná.

        Algoritmus:
        ----------
        1. Uložení reference na původní, nevolatelnou hodnotu.
        2. Vytvoření informativní zprávy s detaily o nevolatelnosti.
        3. Poskytnutí pokynů k nápravě, včetně příkladů volatelných objektů.
        4. Inicializace nadřazené výjimky s formátovanou zprávou.

        Poznámky:
        --------
        Zpráva výjimky obsahuje reprezentaci hodnoty pomocí `repr()`, což
        pomáhá při identifikaci problému, zvláště u složitějších objektů.
        Důraz je kladen na pochopení, co v Pythonu znamená, že je objekt "callable".
        """
        # Uložení hodnoty pro diagnostiku
        self.value = value

        # Vytvoření popisu problému
        what_happened = [
            f"   - Ověřovaný objekt neprošel kontrolou volatelnosti (`callable`).\n",
            f"   - Ověřovaná objekt: {repr(self.value)}\n",
            f"   - Typ objekt: {type(self.value).__name__}\n",
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj, zda je objekt správně definován jako volatelný objekt.\n",
            "   - Například funkce, metoda, nebo objekt s definovanou metodou __call__.\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)