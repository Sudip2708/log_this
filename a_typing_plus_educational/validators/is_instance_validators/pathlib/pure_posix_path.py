from pathlib import PurePosixPath

from ...._bases import BaseIsInstanceValidator


class PurePosixPathValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci pathlib.PurePosixPath

    Typ pathlib.PurePosixPath představuje manipulaci s cestami v unixovém formátu
    bez provádění I/O operací. Je to konkrétní implementace PurePath specifická pro
    unixové cesty nezávisle na aktuálním operačním systému.

    Syntaxe:
        - PurePosixPath           # Vyžaduje import z modulu pathlib (from pathlib import PurePosixPath)
        - pathlib.PurePosixPath   # Alternativní zápis (import pathlib)

    Příklady použití:
        - def validate_unix_path(path: PurePosixPath) -> bool:
        - def convert_to_posix(path: str) -> PurePosixPath:
        - unix_path: PurePosixPath = PurePosixPath("/usr/local/bin")

    Implementační detaily:
        PurePosixPath je konkrétní implementace PurePath pro unixové cesty. Dodržuje pravidla
        pro manipulaci s cestami v unixovém stylu (používá '/' jako oddělovač, podporuje
        absolutní cesty začínající '/', atd.) nezávisle na aktuálním operačním systému.

    Validační proces:
        1. Ověří, zda hodnota je instance třídy pathlib.PurePosixPath
        2. Validace probíhá pomocí isinstance(value, pathlib.PurePosixPath)

    Použití v kódu:
        - Pro parametry funkcí: def validate_web_path(path: PurePosixPath) -> None:
        - Pro návratové hodnoty: def to_web_path(local_path: str) -> PurePosixPath:
        - Pro typování proměnných: url_path: PurePosixPath = PurePosixPath("/api/v1/users")

    Specifické vlastnosti a omezení:
        - Vždy používá '/' jako oddělovač adresářů
        - Absolutní cesty začínají znakem '/'
        - Nepodporuje koncepty specifické pro Windows (např. písmena disků, UNC cesty)
        - Kořenová cesta je reprezentována jako '/'

    Srovnání s podobnými typy:
        - PurePath: Abstraktní základní třída, PurePosixPath je její konkrétní implementace
        - PureWindowsPath: Stejná abstrakce pro Windows cesty
        - PosixPath: Rozšiřuje PurePosixPath o I/O operace pro unixové systémy

    Typické použití:
        - Manipulace s URL cestami (které vždy používají unixový formát)
        - Práce s cestami pro webové aplikace
        - Normalizace cest do unixového formátu pro multiplatformní aplikace
        - Práce s cestami v virtuálních souborových systémech (např. v ZIP archivech)

    Běžné chyby:
        - Zapomenutí importu: from pathlib import PurePosixPath
        - Pokusy o použití I/O metod, které PurePosixPath nemá
        - Nekonzistentní míchání Windows a Posix cest
        - Nesprávné použití metody .as_posix() na PurePosixPath (není potřeba)

    Reference:
        - https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath
        - https://peps.python.org/pep-0428/ (Object-oriented filesystem paths)
    """

    VALIDATOR_KEY = "PurePosixPath"
    ANNOTATION = PurePosixPath

    IS_INSTANCE = PurePosixPath
    DUCK_TYPING = None

    DESCRIPTION = "Čistá cesta pro POSIXové systémy"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí pathlib.PurePosixPath, "
            "což je třída pro reprezentaci a manipulaci "
            "s cestami ve formátu POSIXových systémů bez přístupu k souborovému systému."
        )
