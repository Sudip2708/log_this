from typing import ByteString
from collections.abc import ByteString as ByteStringOrigin

from ...._bases import BaseIsInstanceValidator


class ByteStringValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci ByteString

    ByteString je typ, který reprezentuje sekvenci bytů. Tento typ je určen pro objekty, které
    jsou v podstatě nečíselné řetězce, a operace nad nimi jsou kompatibilní s operacemi nad
    bajty, jako je čtení, zápis nebo manipulace s binárními daty.

    Syntaxe:
        - ByteString              # Preferovaný zápis
        - collections.abc.ByteString  # Původní třída v collections.abc modulu

    Příklady použití:
        - ByteString              # Obecný zápis pro jakýkoliv ByteString
        - bytearray               # Běžný typ podporující ByteString
        - bytes                   # Další běžně používaný typ podporující ByteString

    Validační proces:
        1. Ověří, zda objekt implementuje collections.abc.ByteString
        2. Neprovádí hloubkovou kontrolu typů uvnitř ByteString

    Použití v kódu:
        - Pro parametry funkcí: def process_data(data: ByteString) -> None
        - Pro návratové hodnoty: def get_binary_data() -> ByteString
        - Pro typování proměnných: my_bytes: ByteString = b"data"

    Protokolové požadavky:
        Objekt musí:
        - Implementovat metody pro manipulaci s bajty, například __getitem__, __len__ a další

    Příklad implementace:
        ```python
        def byte_string_example(data: ByteString) -> None:
            print(data)
            print(len(data))
        ```

    Běžné použití:
        ```python
        data: ByteString = b"hello"
        byte_string_example(data)
        ```

    Srovnání s jinými typy:
        - ByteString je navržen pro práci s binárními daty a bajty
        - Na rozdíl od str je to typ určený pro práci s necharakterovými daty (např. soubory, binární protokoly)
        - Je kompatibilní s typy jako `bytes`, `bytearray`, a podobně

    Běžné chyby:
        - Pokus o použití metod specifických pro `str` na `ByteString`
        - Zaměnění mezi `ByteString` a `str`, které je určené pro textové řetězce

    Reference:
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString
        - https://docs.python.org/3/library/stdtypes.html#bytes
    """

    VALIDATOR_KEY = "bytestring"
    ANNOTATION = ByteString

    IS_INSTANCE = ByteStringOrigin
    DUCK_TYPING = {
        "has_attr": ("__getitem__", "__len__", "__iter__"),
    }

    DESCRIPTION = "Abstraktní sekvence bajtů"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní ByteString z collections.abc, "
            "tedy že implementuje protokol pro bytové sekvence. "
            "Základní typy zahrnují bytes a bytearray."
        )

