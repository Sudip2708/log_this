from typing import AsyncIterator
from collections.abc import AsyncIterator as AsyncIteratorOrigin

from ...._bases import BaseIsInstanceValidator, T


class AsyncIteratorValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci AsyncIterator[T]

    AsyncIterator reprezentuje asynchronní iterátor, který produkuje hodnoty asynchronně.
    Jedná se o objekt, který implementuje metody __aiter__ a __anext__, přičemž __anext__
    vrací awaitable objekt (coroutine).

    Syntaxe:
        - AsyncIterator[T]      # Preferovaný zápis (vyžaduje import z typing)
        - AsyncIterator         # Obecný asynchronní iterátor bez specifikace typu prvků
        - collections.abc.AsyncIterator  # Třída z collections.abc modulu

    Příklady použití:
        - AsyncIterator[int]    # Asynchronní iterátor produkující celá čísla
        - AsyncIterator[str]    # Asynchronní iterátor produkující řetězce
        - AsyncIterator[bytes]  # Asynchronní iterátor produkující bajty

    Vnitřní typy:
        Anotace AsyncIterator typicky vyžaduje specifikaci typu vnitřních prvků T, které bude
        iterátor produkovat. T může být libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.AsyncIterator
        2. Neprovádí hloubkovou kontrolu typů vrácených hodnot

    Použití v kódu:
        - Pro parametry funkcí: async def process_items(source: AsyncIterator[int]) -> None
        - Pro návratové hodnoty: async def generate_data() -> AsyncIterator[str]
        - Pro typování proměnných: stream: AsyncIterator[bytes] = some_async_stream()

    Protokolové požadavky:
        Pro správnou implementaci AsyncIterator[T] objekt musí:
        - Implementovat metodu '__aiter__', která vrací self
        - Implementovat metodu '__anext__', která vrací awaitable objekt (coroutine)
        - Metoda '__anext__' musí po vyčerpání prvků vyvolat StopAsyncIteration

    Příklad implementace:
        ```python
        class MyAsyncIterator(AsyncIterator[int]):
            def __init__(self, limit: int):
                self.limit = limit
                self.current = 0

            def __aiter__(self):
                return self

            async def __anext__(self):
                if self.current < self.limit:
                    value = self.current
                    self.current += 1
                    return value
                raise StopAsyncIteration
        ```

    Běžné použití:
        ```python
        async def use_async_iterator(ait: AsyncIterator[int]):
            async for item in ait:
                print(item)
        ```

    Srovnání s Iterator:
        Na rozdíl od standardního Iterator, AsyncIterator je určen pro asynchronní kontexty
        a je používán s 'async for' syntaxí místo standardního 'for'. AsyncIterator umožňuje
        provádět asynchronní operace během iterace.

    Běžné chyby:
        - Zapomenutí 'async' klíčového slova při iteraci: použít 'async for' místo 'for'
        - Nesprávná implementace __anext__ bez async/await
        - Vyvolání StopIteration místo StopAsyncIteration
        - Použití AsyncIterator v synchronním kódu bez await

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.AsyncIterator
        - https://peps.python.org/pep-0492/ (coroutines a async/await syntax)
        - https://peps.python.org/pep-0525/ (asynchronní generátory)
    """

    VALIDATOR_KEY = "asynciterator"
    ANNOTATION = AsyncIterator[T]

    IS_INSTANCE = AsyncIteratorOrigin
    HAS_ATTRS = "__aiter__", "__anext__"
    CALLABLE_ATTRS = "__aiter__", "__anext__"

    DESCRIPTION = "Asynchronní iterátor"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní AsyncIterator z collections.abc, "
            "tedy že implementuje metody __aiter__ a __anext__, "
            "které umožňují asynchronní iteraci s využitím korutin."
        )
