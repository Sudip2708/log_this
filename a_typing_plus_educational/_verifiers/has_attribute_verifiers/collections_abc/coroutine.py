from typing import Coroutine
from collections.abc import Coroutine as CoroutineOrigin

from ...._bases import IsInstanceValidatorBase


class CoroutineValidator(IsInstanceValidatorBase):
    """
    Validátor pro typovou anotaci Coroutine

    Coroutine je asynchronní funkce nebo objekt, který implementuje asynchronní operace
    a umožňuje práci s async/await syntaxí. Tento typ je určen pro objekty, které jsou
    coroutine objekty, tedy objekty, které lze spustit pomocí 'await' a které vracejí
    výsledky po asynchronním vykonání.

    Syntaxe:
        - Coroutine           # Preferovaný zápis
        - collections.abc.Coroutine  # Původní třída v collections.abc modulu

    Příklady použití:
        - Coroutine[int, str, bool]    # Asynchronní funkce, která vrací bool, očekává int a str
        - Coroutine[None, int, str]    # Asynchronní funkce, která vrací str a očekává int

    Validační proces:
        1. Ověří, zda objekt je instance Coroutine
        2. Neprovádí hloubkovou kontrolu argumentů či návratového typu

    Použití v kódu:
        - Pro parametry funkcí: async def process_data(coro: Coroutine[int, str, bool]) -> None
        - Pro návratové hodnoty: async def fetch_data() -> Coroutine[None, int, str]
        - Pro typování proměnných: coro: Coroutine[None, int, str] = async_function()

    Protokolové požadavky:
        Objekt musí:
        - Být typu Coroutine
        - Implementovat metody pro async/await operace
        - Být schopen být použit s 'await'

    Příklad implementace:
        ```python
        async def example_coroutine() -> str:
            await asyncio.sleep(1)
            return "Hello"
        ```

    Běžné použití:
        ```python
        async def fetch_data() -> Coroutine[None, str, None]:
            await asyncio.sleep(1)
            return "Fetched Data"
        ```

    Srovnání s jinými asynchronními objekty:
        - Na rozdíl od `AsyncIterator` nebo `AsyncGenerator`, `Coroutine` je určen pro jednorázové asynchronní volání.
        - `Coroutine` se používá hlavně pro funkce, které vrací nějaký výsledek po asynchronním vykonání.

    Běžné chyby:
        - Zapomenutí použít `await` při volání coroutine objektu
        - Nesprávná implementace asynchronní logiky uvnitř coroutine
        - Pokus o čekání na něco, co není coroutine (např. synchronní funkce)

    Reference:
        - https://docs.python.org/3/library/asyncio-task.html#coroutine
        - https://docs.python.org/3/library/asyncio.html#coroutine-objects
    """

    VALIDATOR_KEY = "coroutine"
    ANNOTATION = Coroutine
    INFO = "Definuje, že objekt musí být Coroutine (asynchronní funkce)"
    ORIGIN = CoroutineOrigin
