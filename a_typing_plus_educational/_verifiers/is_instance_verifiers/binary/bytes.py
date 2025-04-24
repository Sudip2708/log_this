from ..._bases import IsInstanceValidatorBase


class BytesValidator(IsInstanceValidatorBase):
    """
    Validátor pro typovou anotaci bytes

    Bytes reprezentuje immutabilní (neměnnou) sekvenci bajtů v Pythonu. Používá se pro
    reprezentaci binárních dat, jako jsou obrázky, soubory, komprimovaná data nebo síťová
    komunikace. Každý prvek sekvence je celé číslo v rozsahu 0-255.

    Syntaxe:
        - bytes    # Přímý zápis typu

    Příklady použití:
        - bytes    # Sekvence bajtů

    Validační proces:
        1. Ověřuje, zda hodnota je instance typu bytes
        2. Kontroluje, že hodnota je skutečně objekt typu bytes, nikoliv jiné objekty,
           které lze na bytes převést (jako str s kódováním)

    Použití v kódu:
        - Pro parametry funkcí: def process_image(data: bytes) -> None
        - Pro návratové hodnoty: def download_file() -> bytes
        - Pro typování proměnných: content: bytes = b"binary data"

    Vytváření bytes:
        - Pomocí prefixu b: b"text", b'\x00\x01\x02'
        - Pomocí konstruktoru: bytes([65, 66, 67]) -> b"ABC"
        - Z řetězce s kódováním: "text".encode('utf-8')
        - Z bytových polí: bytes(bytearray([1, 2, 3]))

    Operace:
        - Indexování a krájení: data[0], data[1:5]
        - Iterování: for byte in data
        - Spojování: b"a" + b"b", b"".join([b"a", b"b"])
        - Hledání: b"abc".find(b"b"), b"x" in data
        - Konverze na jiné typy: bytearray(data), data.decode('utf-8')

    Kompatibilita:
        - bytes není kompatibilní s str (pro textová data)
        - bytes je podobný bytearray, ale na rozdíl od něj je immutabilní
        - bytes se často používá s knihovnami pro I/O operace

    Běžné chyby:
        - Zaměňování bytes a str, zejména při zpracování textových dat
        - Přímý přístup k bytes jako k textu bez dekódování
        - Ignorování kódování při převodu mezi str a bytes
        - Předpokládání, že bytes jsou vždy ASCII nebo UTF-8
        - Pokus o modifikaci bytes objektu (je immutabilní)

    Reference:
        - https://docs.python.org/3/library/stdtypes.html#bytes
        - https://docs.python.org/3/library/functions.html#func-bytes
        - https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
    """

    VALIDATOR_KEY = "bytes"
    ANNOTATION = bytes
    INFO = "Definuje, že hodnota může být pouze sekvence bajtů"
    ORIGIN = bytes