from typing import AsyncGenerator
from collections.abc import AsyncGenerator as AsyncGeneratorOrigin

from ...._bases import BaseIsInstanceValidator, Y, R


class AsyncGeneratorValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci AsyncGenerator[T, T_co]

    AsyncGenerator je protokol reprezentující asynchronní generátor, který produkuje hodnoty
    asynchronně a může přijímat hodnoty skrze 'asend'. Podobně jako u běžného generátoru, ale
    ve světě async.

    Syntaxe:
        - AsyncGenerator[Y, R]       # Y = yieldovaný typ, R = návratová hodnota (po StopAsyncIteration)
        - AsyncGenerator             # Bez specifikace typů
        - collections.abc.AsyncGenerator  # Původní třída v abc

    Příklady použití:
        - AsyncGenerator[int, None]    # Asynchronní generátor vracející int, nic nevrací zpět
        - AsyncGenerator[str, str]     # Vrací str a přijímá str
        - AsyncGenerator[bytes, Any]   # Vrací bytes a přijímá cokoliv

    Vnitřní typy:
        - Y: typ yieldovaných hodnot
        - R: typ hodnot přijímaných přes `asend`, příp. návratová hodnota po vyčerpání

    Validační proces:
        1. Ověří, zda objekt implementuje collections.abc.AsyncGenerator
        2. Nekontroluje typy yieldovaných nebo přijímaných hodnot
        (Nelze synchronně získat ani yield ani return hodnotu bez spuštění async běhu.)

    Použití v kódu:
        - async def produce() -> AsyncGenerator[int, None]:
              yield 1
              yield 2
        - async for val in produce():
              ...

    Protokolové požadavky:
        Objekt musí:
        - Implementovat '__aiter__' → self
        - Implementovat asynchronní '__anext__' (vrací awaitovatelný objekt)
        - Typicky implementuje také 'asend', 'athrow' a 'aclose'

    Příklad implementace:
        ```python
        async def async_range(limit: int) -> AsyncGenerator[int, None]:
            i = 0
            while i < limit:
                yield i
                i += 1
        ```

    Běžné použití:
        ```python
        async def my_gen() -> AsyncGenerator[str, None]:
            yield "A"
            yield "B"

        async for val in my_gen():
            print(val)
        ```

    Srovnání s AsyncIterator:
        - AsyncGenerator je nadstavbou AsyncIterator
        - AsyncGenerator umožňuje yield i return (návratové hodnoty)
        - Má metody jako 'asend', 'athrow' a 'aclose'

    Běžné chyby:
        - Chybějící 'yield' uvnitř async funkce → není generátor
        - Použití 'return' bez typové specifikace návratového typu
        - Zaměnění s běžným synchronním generátorem

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.AsyncGenerator
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncGenerator
        - https://peps.python.org/pep-0525/ (asynchronní generátory)
    """

    VALIDATOR_KEY = "asyncgenerator"
    ANNOTATION = AsyncGenerator[Y, R]  # yield type a return type default stejný
    INFO = "Definuje, že objekt musí být asynchronní generátor"

    IS_INSTANCE = AsyncGeneratorOrigin
    HAS_ATTRS = "__aiter__", "__anext__", "asend", "athrow", "aclose"
    CALLABLE_ATTRS = "__aiter__", "__anext__", "asend", "athrow", "aclose"

    DESCRIPTION = "Asynchronní generátor"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní AsyncGenerator z collections.abc, "
            "tedy že je generátorem vytvořeným pomocí async def a yield. "
            "Umožňuje asynchronní iteraci s podporou await."
        )

