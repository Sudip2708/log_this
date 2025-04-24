from typing import SupportsBytes

from ...._bases import IsInstanceValidatorBase


class SupportsBytesValidator(IsInstanceValidatorBase):
    """
    Validátor pro typovou anotaci SupportsBytes

    SupportsBytes reprezentuje protokol pro objekty, které lze konvertovat na
    bajtový řetězec implementací metody __bytes__. Zahrnuje všechny typy, které lze
    explicitně převést na bajty pomocí funkce bytes().

    Syntaxe:
        - SupportsBytes        # Jediný zápis (vyžaduje import z typing)

    Příklady použití:
        - SupportsBytes        # Jakýkoliv objekt, který lze převést na bajty

    Validační proces:
        1. Ověří, zda objekt je instance SupportsBytes (implementuje metodu '__bytes__')
        2. Neprovádí kontrolu skutečné funkčnosti metody

    Použití v kódu:
        - Pro parametry funkcí: def write_binary(obj: SupportsBytes) -> None
        - Pro návratové hodnoty: def get_serialized_data() -> SupportsBytes
        - Pro typování proměnných: raw_data: SupportsBytes = MyBinaryObject(...)

    Protokolové požadavky:
        Pro správnou implementaci SupportsBytes objekt musí:
        - Implementovat metodu '__bytes__', která vrací hodnotu typu bytes

    Příklad implementace:
        ```python
        class MyBinaryObject(SupportsBytes):
            def __init__(self, data: str):
                self.data = data

            def __bytes__(self) -> bytes:
                return self.data.encode("utf-8")
        ```

    Běžné použití:
        ```python
        def save(obj: SupportsBytes):
            with open("file.bin", "wb") as f:
                f.write(bytes(obj))

        save(MyBinaryObject("hello"))
        save(b"native bytes")
        ```

    Kompatibilní typy:
        - bytes: nativní bajtový řetězec
        - bytearray: přetypovatelný na bytes
        - str: přes vlastní implementaci __bytes__
        - Vlastní typy implementující __bytes__

    Srovnání s jinými protokoly:
        - SupportsInt: pro převod na celé číslo
        - SupportsFloat: pro převod na desetinné číslo
        - SupportsComplex: pro převod na komplexní číslo

    Praktické využití:
        - Serializace objektů
        - Přenos dat mezi procesy
        - Zapisování do binárních souborů
        - Obalování a šifrování dat

    Běžné chyby:
        - Nevrácení hodnoty typu bytes
        - Zaměňování s nativním typem bytes
        - Chybné kódování nebo špatná implementace __bytes__
        - Předpoklad, že každé str automaticky podporuje bytes()

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.SupportsBytes
        - https://docs.python.org/3/reference/datamodel.html#object.__bytes__
        - https://peps.python.org/pep-0544/
    """

    VALIDATOR_KEY = "supportsbytes"
    ANNOTATION = SupportsBytes
    INFO = "Definuje, že objekt musí podporovat metodu __bytes__"
    ORIGIN = SupportsBytes
