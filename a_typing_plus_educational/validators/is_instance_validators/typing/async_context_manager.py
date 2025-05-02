from typing import AsyncContextManager, Any, Union

from ...._bases import BaseIsInstanceValidator
from ...._verifiers import has_attribute_verifier, is_coroutine_function_verifier


class AsyncContextManagerValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci AsyncContextManager[T]

    AsyncContextManager reprezentuje asynchronní správce kontextu, což je objekt, který implementuje
    asynchronní protokol správy kontextu (metody __aenter__ a __aexit__). Používá se pro bezpečné
    a efektivní správy zdrojů v asynchronním kódu.

    Syntaxe:
        - AsyncContextManager[T]      # Preferovaný zápis (vyžaduje import z typing)
        - AsyncContextManager         # Obecný asynchronní správce kontextu bez specifikace typu

    Příklady použití:
        - AsyncContextManager[None]                # Asynchronní správce kontextu, který nevrací hodnotu
        - AsyncContextManager[int]                 # Asynchronní správce kontextu, který vrací celé číslo
        - AsyncContextManager[Connection]          # Asynchronní správce kontextu, který vrací připojení
        - AsyncContextManager[AsyncIterator[str]]  # Asynchronní správce vrací asynchronní iterátor řetězců

    Vnitřní typy:
        Anotace AsyncContextManager může obsahovat specifikaci typu T, který reprezentuje typ hodnoty
        vrácené metodou __aenter__. Tento typ může být libovolný podporovaný typ včetně složených typů.

    Validační proces:
        1. Ověří, zda hodnota je instance AsyncContextManager
        2. Kontroluje přítomnost metod __aenter__ a __aexit__ pro zajištění asynchronního protokolu
        3. Pokud je specifikován vnitřní typ a je požadována hloubková kontrola, měla by být ověřena
           kompatibilita návratové hodnoty __aenter__ s požadovaným typem (vyžaduje speciální logiku)

    Použití v kódu:
        - Pro parametry funkcí: async def process_file(file_ctx: AsyncContextManager[TextIO]) -> None
        - Pro návratové hodnoty: def get_connection() -> AsyncContextManager[DBConnection]
        - Pro typování proměnných: ctx: AsyncContextManager[Session] = AsyncSession(engine)

    Vlastnosti a specifika:
        - AsyncContextManager je určen pro použití s asynchronním blokem async with
        - Na rozdíl od synchronního ContextManager používá korutiny pro vstup a výstup z kontextu
        - Výhodou je neblokující chování při získávání a uvolňování zdrojů

    Kompatibilita:
        - Není zaměnitelný s běžným ContextManager (ten používá synchronní metody)
        - Objekt s metodami __aenter__ a __aexit__ je typově kompatibilní s AsyncContextManager

    Běžné chyby:
        - Záměna s ContextManager v asynchronním kódu (vede k nekompatibilitě)
        - Nesprávná implementace metod __aenter__ a __aexit__ (musí být korutiny)
        - Použití v synchronním kódu bez async/await (typová chyba)

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.AsyncContextManager
        - https://peps.python.org/pep-0492/ (Coroutines with async and await syntax)
        - https://docs.python.org/3/reference/datamodel.html#asynchronous-context-managers
    """

    VALIDATOR_KEY = "asynccontextmanager"
    ANNOTATION = AsyncContextManager

    IS_INSTANCE = AsyncContextManager
    HAS_ATTRS = "__aenter__", "__aexit__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Asynchronní správce kontextu"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje protokol asynchronního správce kontextu, "
            "tedy má metody __aenter__ a __aexit__. "
            "Používá se s příkazem 'async with' pro asynchronní práci se zdroji."
        )


    LAMBDA = lambda obj: is_coroutine_function_verifier(obj, HAS_ATTRS, ANNOTATION)
