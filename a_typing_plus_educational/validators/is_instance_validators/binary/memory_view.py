from ...._bases import BaseIsInstanceValidator


class MemoryViewValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci memoryview

    Memoryview reprezentuje pohled na paměť jiného objektu podporujícího buffer protokol
    (nejčastěji bytes nebo bytearray) bez kopírování dat. Poskytuje efektivní způsob,
    jak pracovat s binárními daty, protože umožňuje přistupovat k podsekvencím nebo změnit
    formát dat bez fyzického kopírování obsahu paměti.

    Syntaxe:
        - memoryview    # Přímý zápis typu

    Příklady použití:
        - memoryview    # Pohled na paměť objektu podporujícího buffer protokol

    Validační proces:
        1. Ověřuje, zda hodnota je instance typu memoryview
        2. Kontroluje, že hodnota je přímo objekt typu memoryview

    Použití v kódu:
        - Pro parametry funkcí: def process_buffer(view: memoryview) -> None
        - Pro návratové hodnoty: def get_memory_view() -> memoryview
        - Pro typování proměnných: view: memoryview = memoryview(bytearray(10))

    Vytváření memoryview:
        - Z bytes: memoryview(b"data")
        - Z bytearray: memoryview(bytearray([65, 66, 67]))
        - Z jiných objektů implementujících buffer protokol

    Operace:
        - Indexování a krájení: view[0], view[1:5]
        - Iterování: for byte in view
        - Formátování: view.cast('I') # přetypování na unsigned ints
        - Přístup ke struktuře: zobrazení více rozměrů pomocí .shape, .strides
        - Konverze: bytes(view), view.tobytes(), view.tolist()

    Výhody oproti přímému použití bytes/bytearray:
        - Sdílení paměti mezi objekty bez kopírování
        - Efektivní operace krájení a reinterpretace dat (bez kopírování)
        - Schopnost přistupovat k datům různými způsoby (různé formáty)
        - Podpora pro vícerozměrná data

    Omezení:
        - Vyžaduje, aby zdrojový objekt podporoval buffer protokol
        - Méně intuitivní než přímé použití bytes/bytearray
        - Životnost memoryview je závislá na životnosti zdrojového objektu

    Běžné chyby:
        - Předpoklad, že memoryview je samostatná kopie dat (je to jen pohled)
        - Používání po uvolnění zdrojových dat z paměti
        - Nepochopení rozdílu mezi memoryview a bytes/bytearray
        - Přehlížení možnosti formátování a přetypování dat

    Reference:
        - https://docs.python.org/3/library/stdtypes.html#memoryview
        - https://docs.python.org/3/c-api/buffer.html (buffer protokol)
        - https://docs.python.org/3/library/functions.html#memoryview
    """

    VALIDATOR_KEY = "memoryview"
    ANNOTATION = memoryview

    IS_INSTANCE = memoryview
    DUCK_TYPING = {
        "has_attr": ("tobytes", "obj", "nbytes"),
    }

    DESCRIPTION = "Pohled na paměť objektu"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je typu memoryview, což poskytuje přístup "
            "k interní paměti objektu bez kopírování. "
            "Umožňuje efektivní práci s velkými bloky dat."
        )
