from typing import Generator
from collections.abc import Generator as GeneratorOrigin

from ...._bases import BaseIsInstanceValidator, Y, S, R


class GeneratorValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci Generator[T, T_send, T_return]

    Generator je objekt, který implementuje generátorový protokol – typicky vzniká voláním
    funkce obsahující klíčové slovo 'yield'. Tento objekt umí produkovat hodnoty pomocí `yield`,
    přijímat hodnoty pomocí `send`, a může také vracet finální návratovou hodnotu přes `return`.

    Syntaxe:
        - Generator[Y, S, R]        # Y = yieldovaný typ, S = typ pro send, R = návratová hodnota
        - Generator                 # Bez specifikace typů
        - collections.abc.Generator  # Původní třída v abc

    Příklady použití:
        - Generator[int, None, None]    # Generátor, který yielduje int
        - Generator[str, str, None]     # Přijímá a posílá řetězce
        - Generator[bytes, Any, int]    # Yielduje bytes, přijímá cokoliv, vrací int

    Vnitřní typy:
        - Y: typ yieldovaných hodnot
        - S: typ přijímaný metodou send()
        - R: návratová hodnota po StopIteration

    Validační proces:
        1. Ověří, zda objekt implementuje collections.abc.Generator
        2. Nekontroluje typy yieldovaných, přijímaných ani vrácených hodnot

    Použití v kódu:
        - def counter() -> Generator[int, None, None]:
              yield 1
              yield 2

        - for val in counter():
              print(val)

    Protokolové požadavky:
        Objekt musí:
        - Implementovat '__iter__' → self
        - Implementovat '__next__' (vrací další prvek nebo vyvolá StopIteration)
        - Podporuje také 'send', 'throw', 'close'

    Příklad implementace:
        ```python
        def countdown(start: int) -> Generator[int, None, str]:
            while start > 0:
                yield start
                start -= 1
            return "Done"
        ```

    Běžné použití:
        ```python
        def words() -> Generator[str, None, None]:
            yield "hello"
            yield "world"

        for word in words():
            print(word)
        ```

    Srovnání s Iterator:
        - Iterator má pouze __iter__ a __next__
        - Generator rozšiřuje Iterator o send, return, throw, close
        - Generator obvykle vzniká funkcí s `yield`

    Běžné chyby:
        - Použití `return` místo `yield` → funkce nevrací generátor
        - Zaměnění yield a send typů
        - Záměna s asynchronní verzí – AsyncGenerator

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Generator
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator
        - https://peps.python.org/pep-0255/ (zavedení generátorů)
        - https://peps.python.org/pep-0342/ (rozšíření o send, throw)
    """

    VALIDATOR_KEY = "generator"
    ANNOTATION = Generator[Y, S, R]  # yield, send, return typy (mohou se lišit)

    IS_INSTANCE = GeneratorOrigin
    DUCK_TYPING = {
        "has_callable_attr": ("__iter__", "__next__", "send", "throw", "close")
    }

    DESCRIPTION =  "Generátor s podporou yield a send"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je typu Generator, tj. má metody send, throw, "
            "close, __next__ a __iter__, a je instancí GeneratorType. "
            "Umožňuje obousměrnou komunikaci mezi volajícím a generátorem."
        )
