from ...._bases import BaseIsInstanceValidator


class ByteArrayValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci bytearray

    Bytearray reprezentuje mutable (měnitelnou) sekvenci bajtů v Pythonu. Na rozdíl od
    typu bytes umožňuje úpravy obsahu po vytvoření. Používá se pro binární data, která
    potřebují být modifikována, jako jsou buffery pro I/O operace, postupně budované
    binární struktury nebo dočasné úložiště pro zpracování binárních dat.

    Syntaxe:
        - bytearray    # Přímý zápis typu

    Příklady použití:
        - bytearray    # Měnitelná sekvence bajtů

    Validační proces:
        1. Ověřuje, zda hodnota je instance typu bytearray
        2. Kontroluje, že hodnota je skutečně objekt typu bytearray, nikoliv jiné objekty,
           které lze na bytearray převést (jako bytes nebo seznam celých čísel)

    Použití v kódu:
        - Pro parametry funkcí: def accumulate_data(buffer: bytearray) -> None
        - Pro návratové hodnoty: def create_buffer() -> bytearray
        - Pro typování proměnných: buffer: bytearray = bytearray(10)

    Vytváření bytearray:
        - Prázdný s velikostí: bytearray(10) # 10 nulových bajtů
        - Z iterable: bytearray([65, 66, 67]) -> bytearray(b"ABC")
        - Z bytes: bytearray(b"text")
        - Z řetězce s kódováním: bytearray("text", 'utf-8')

    Operace:
        - Indexování a krájení: buffer[0], buffer[1:5]
        - Iterování: for byte in buffer
        - Modifikace: buffer[0] = 65, buffer.append(66), buffer.extend(b"CD")
        - Metody seznamu: buffer.insert(1, 67), buffer.pop(), buffer.remove(65)
        - Konverze: bytes(buffer), buffer.decode('utf-8')

    Kompatibilita:
        - bytearray není kompatibilní s str (pro textová data)
        - bytearray je podobný bytes, ale je mutable (měnitelný)
        - bytearray implementuje rozhraní mutable sequence, podobně jako list

    Běžné chyby:
        - Zaměňování bytearray a bytes pro neměnná binární data
        - Zaměňování bytearray a str pro textová data
        - Ignorování rozsahu hodnot (0-255) při modifikaci prvků
        - Předpokládání, že bytearray jsou vždy ASCII nebo UTF-8
        - Nepochopení rozdílu mezi modifikací bytearray a bytes (který modifikaci neumožňuje)

    Reference:
        - https://docs.python.org/3/library/stdtypes.html#bytearray
        - https://docs.python.org/3/library/functions.html#func-bytearray
        - https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
    """

    VALIDATOR_KEY = "bytearray"
    ANNOTATION = bytearray

    IS_INSTANCE = bytearray
    DUCK_TYPING = {
        "has_attr": (
            "__getitem__", "__setitem__", "__len__",
            "decode", "append", "extend"
        ),
    }

    DESCRIPTION = "Změnitelné pole bajtů"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je typu bytearray, tedy změnitelná "
            "sekvence bajtů (celých čísel 0-255). "
            "Na rozdíl od bytes lze obsah měnit, přidávat nebo odebírat prvky."
        )
