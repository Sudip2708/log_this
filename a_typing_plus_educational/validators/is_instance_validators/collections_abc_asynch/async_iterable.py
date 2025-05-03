from typing import AsyncIterable
from collections.abc import AsyncIterable as AsyncIterableOrigin

from ...._bases import BaseIsInstanceValidator, T


class AsyncIterableValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci AsyncIterable[T]

    AsyncIterable reprezentuje objekt, který lze použít v konstrukci 'async for'.
    Jedná se o kolekci nebo objekt, který implementuje metodu __aiter__ vracející
    AsyncIterator. AsyncIterable je základním typem pro asynchronní iterace.

    Syntaxe:
        - AsyncIterable[T]      # Preferovaný zápis (vyžaduje import z typing)
        - AsyncIterable         # Obecný asynchronní iterovatelný objekt bez specifikace typu prvků
        - collections.abc.AsyncIterable  # Třída z collections.abc modulu

    Příklady použití:
        - AsyncIterable[int]    # Asynchronně iterovatelný objekt poskytující celá čísla
        - AsyncIterable[str]    # Asynchronně iterovatelný objekt poskytující řetězce
        - AsyncIterable[bytes]  # Asynchronně iterovatelný objekt poskytující bajty
        - AsyncIterable[Dict[str, Any]]  # Asynchronně iterovatelný objekt poskytující slovníky

    Vnitřní typy:
        Anotace AsyncIterable typicky vyžaduje specifikaci typu vnitřních prvků T, které budou
        produkovány během asynchronní iterace. T může být libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Iterable
        2. Neprovádí hloubkovou kontrolu typů vrácených hodnot

    Použití v kódu:
        - Pro parametry funkcí: async def process_data(source: AsyncIterable[int]) -> None
        - Pro návratové hodnoty: async def get_items() -> AsyncIterable[str]
        - Pro typování proměnných: stream: AsyncIterable[bytes] = some_async_stream()

    Protokolové požadavky:
        Pro správnou implementaci AsyncIterable[T] objekt musí:
        - Implementovat metodu '__aiter__', která vrací objekt AsyncIterator[T]

    Příklad implementace:
        ```python
        class MyAsyncIterable(AsyncIterable[int]):
            def __init__(self, data: List[int]):
                self.data = data

            def __aiter__(self):
                return MyAsyncIterator(self.data)

        class MyAsyncIterator:
            def __init__(self, data: List[int]):
                self.data = data
                self.index = 0

            def __aiter__(self):
                return self

            async def __anext__(self):
                if self.index < len(self.data):
                    value = self.data[self.index]
                    self.index += 1
                    return value
                raise StopAsyncIteration
        ```

    Běžné použití:
        ```python
        async def use_async_iterable(ait: AsyncIterable[int]):
            async for item in ait:
                print(item)
        ```

    Srovnání s Iterable:
        AsyncIterable je asynchronní analogií k Iterable. Zatímco Iterable se používá
        se standardní 'for' smyčkou, AsyncIterable vyžaduje použití 'async for' v rámci
        asynchronní funkce. AsyncIterable umožňuje provádět asynchronní operace během iterace.

    Rozdíl oproti AsyncIterator:
        - AsyncIterable pouze definuje, že objekt lze použít v 'async for' konstrukci
        - AsyncIterable implementuje pouze __aiter__
        - AsyncIterator je konkrétním typem AsyncIterable, který navíc implementuje __anext__
        - Každý AsyncIterator je AsyncIterable, ale ne každé AsyncIterable je AsyncIterator

    Běžné chyby:
        - Zaměňování AsyncIterable a AsyncIterator
        - Zapomenutí 'async' klíčového slova při iteraci (použít 'async for' místo 'for')
        - Nesprávná implementace __aiter__ bez vracení AsyncIterator
        - Použití AsyncIterable v synchronním kódu bez asynchronního kontextu

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.AsyncIterable
        - https://peps.python.org/pep-0492/ (coroutines a async/await syntax)
        - https://peps.python.org/pep-0525/ (asynchronní generátory)
    """

    VALIDATOR_KEY = "asynciterable"
    ANNOTATION = AsyncIterable[T]

    IS_INSTANCE = AsyncIterableOrigin
    DUCK_TYPING = {
        "has_callable_attr": "__aiter__",
    }

    DESCRIPTION = "Objekt podporující asynchronní iteraci"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní AsyncIterable z collections.abc, "
            "tedy že implementuje metodu __aiter__ "
            "a může být použit v asynchronním cyklu 'async for'."
        )
