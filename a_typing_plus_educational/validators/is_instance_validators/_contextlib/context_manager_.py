from typing import ContextManager
from contextlib import AbstractContextManager

from ...._bases import BaseIsInstanceValidator, T


class ContextManagerValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci ContextManager[T]

    ContextManager reprezentuje objekt, který lze použít v konstrukci 'with' pro správu
    kontextu a zdrojů. Jedná se o objekt implementující metody __enter__ a __exit__,
    které zajišťují správnou inicializaci a úklid zdrojů.

    Syntaxe:
        - ContextManager[T]          # Preferovaný zápis (vyžaduje import z typing)
        - ContextManager             # Obecný správce kontextu bez specifikace návratového typu
        - contextlib.AbstractContextManager  # Třída z contextlib modulu

    Příklady použití:
        - ContextManager[File]       # Správce kontextu vracející objekt souboru
        - ContextManager[Connection] # Správce kontextu vracející připojení k databázi
        - ContextManager[None]       # Správce kontextu, který nevrací žádnou hodnotu

    Vnitřní typy:
        Anotace ContextManager typicky vyžaduje specifikaci typu T, který reprezentuje
        návratovou hodnotu metody __enter__, která je dostupná uvnitř bloku with.

    Validační proces:
        1. Ověří, zda hodnota implementuje rozhraní contextlib.AbstractContextManager
        2. Neprovádí hloubkovou kontrolu typů vrácených hodnot

    Použití v kódu:
        - Pro parametry funkcí: def process_file(handler: ContextManager[TextIO]) -> None
        - Pro návratové hodnoty: def temp_directory() -> ContextManager[Path]
        - Pro typování proměnných: db_session: ContextManager[Session] = session_factory()

    Protokolové požadavky:
        Pro správnou implementaci ContextManager[T] objekt musí:
        - Implementovat metodu '__enter__', která vrací objekt typu T pro použití v with bloku
        - Implementovat metodu '__exit__(exc_type, exc_val, exc_tb)', která provádí úklid zdrojů
          a může zpracovat výjimky vzniklé v bloku with

    Příklad implementace:
        ```python
        class MyContextManager(ContextManager[Connection]):
            def __init__(self, connection_string: str):
                self.connection_string = connection_string
                self.connection = None

            def __enter__(self) -> Connection:
                self.connection = create_connection(self.connection_string)
                return self.connection

            def __exit__(self, exc_type, exc_val, exc_tb):
                if self.connection:
                    self.connection.close()
                    self.connection = None
                # Vrácení True potlačí výjimku, False ji propustí dále
                return False
        ```

    Běžné použití:
        ```python
        def use_context_manager(cm: ContextManager[Connection]):
            with cm as conn:
                conn.execute("SELECT * FROM users")
        ```

    Související typy:
        - AsyncContextManager: asynchronní varianta pro použití s 'async with'
        - contextlib.contextmanager: dekorátor pro vytváření správců kontextu z generátorů
        - ExitStack: nástroj pro dynamickou správu více kontextových manažerů

    Praktické využití:
        - Správa souborů (automatické zavírání)
        - Správa databázových transakcí a připojení
        - Správa zámků a synchronizačních primitiv
        - Dočasné změny stavu (např. změna pracovního adresáře)
        - Měření času a profilování kódu

    Běžné chyby:
        - Neuzavření nebo neuvolnění zdrojů v metodě __exit__
        - Nezachycení a neošetření výjimek v metodě __exit__
        - Nevrácení relevantní hodnoty z metody __enter__
        - Záměna s decorator pattern nebo jinými návřhovými vzory
        - Nerespektování konvencí pro návratové hodnoty __exit__ (True/False)

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.ContextManager
        - https://docs.python.org/3/reference/datamodel.html#context-managers
        - https://docs.python.org/3/library/contextlib.html
        - https://peps.python.org/pep-0343/ (the "with" statement)
    """

    VALIDATOR_KEY = "contextmanager"
    ANNOTATION = ContextManager[T]

    IS_INSTANCE = AbstractContextManager
    HAS_ATTRS = "__enter__", "__exit__"
    CALLABLE_ATTRS = HAS_ATTRS

    DESCRIPTION = "Správce kontextu"
    LONG_DESCRIPTION = (
            "Validuje, že objekt implementuje protokol správce "
            "kontextu – má metody __enter__ a __exit__. "
            "Používá se např. s příkazem with."
        )

