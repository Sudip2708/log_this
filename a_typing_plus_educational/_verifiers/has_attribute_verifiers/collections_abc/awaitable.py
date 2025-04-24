from typing import Awaitable
from collections.abc import Awaitable as AwaitableOrigin

from ...._bases import IsInstanceValidatorBase, T


class AwaitableValidator(IsInstanceValidatorBase):
    """
    Validátor pro typovou anotaci Awaitable[T]

    Awaitable reprezentuje objekt, který lze použít s klíčovým slovem 'await' v asynchronním
    kontextu. Jedná se o objekt, který implementuje metodu __await__, která vrací iterátor.

    Syntaxe:
        - Awaitable[T]      # Preferovaný zápis (vyžaduje import z typing)
        - Awaitable         # Obecný awaitable objekt bez specifikace návratového typu
        - collections.abc.Awaitable  # Třída z collections.abc modulu

    Příklady použití:
        - Awaitable[int]    # Awaitable objekt, který po dokončení vrátí celé číslo
        - Awaitable[str]    # Awaitable objekt, který po dokončení vrátí řetězec
        - Awaitable[None]   # Awaitable objekt, který po dokončení nevrací hodnotu
        - Awaitable[List[Dict[str, Any]]]  # Awaitable s komplexním návratovým typem

    Vnitřní typy:
        Anotace Awaitable typicky vyžaduje specifikaci typu T, který reprezentuje
        hodnotu, již awaitable objekt vrátí po dokončení. T může být libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní collections.abc.Awaitable
        2. Neprovádí hloubkovou kontrolu návratového typu awaitable objektu

    Použití v kódu:
        - Pro parametry funkcí: async def process_data(source: Awaitable[bytes]) -> None
        - Pro návratové hodnoty: def get_future() -> Awaitable[int]
        - Pro typování proměnných: result: Awaitable[str] = async_function()

    Protokolové požadavky:
        Pro správnou implementaci Awaitable[T] objekt musí:
        - Implementovat metodu '__await__', která vrací iterátor
        - Iterátor vrácený metodou '__await__' musí být generátor nebo implementovat metodu
          '__iter__' a '__next__'

    Příklad implementace:
        ```python
        class MyAwaitable(Awaitable[int]):
            def __init__(self, value: int):
                self.value = value

            def __await__(self):
                yield None
                return self.value
        ```

    Běžné použití:
        ```python
        async def use_awaitable(a: Awaitable[int]) -> int:
            result = await a
            return result
        ```

    Souvislosti s jinými typy:
        - Coroutine: Specifický typ Awaitable, který je vytvořen funkcí definovanou s 'async def'
        - Task: V asyncio je specializovaným typem Awaitable reprezentujícím spuštěnou coroutine
        - Future: Generický awaitable objekt, který bude obsahovat výsledek v budoucnosti

    Běžné chyby:
        - Pokus o použití 'await' mimo asynchronní kontext
        - Nesprávná implementace '__await__' metody, která nevrací iterátor
        - Zaměňování Awaitable s Coroutine (Coroutine je specifickým typem Awaitable)
        - Použití awaitable objektu bez 'await' (nevyčká na jeho dokončení)

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Awaitable
        - https://peps.python.org/pep-0492/ (coroutines a async/await syntax)
        - https://docs.python.org/3/library/asyncio-task.html (asyncio úlohy a coroutines)
    """

    VALIDATOR_KEY = "awaitable"
    ANNOTATION = Awaitable[T]
    INFO = "Definuje, že objekt musí implementovat metodu __await__"
    ORIGIN = AwaitableOrigin