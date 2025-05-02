from pathlib import PureWindowsPath

from ..._bases import BaseIsInstanceValidator


class PureWindowsPathValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci pathlib.PureWindowsPath

    Typ pathlib.PureWindowsPath představuje manipulaci s cestami ve Windows formátu
    bez provádění I/O operací. Je to konkrétní implementace PurePath specifická pro
    Windows cesty nezávisle na aktuálním operačním systému.

    Syntaxe:
        - PureWindowsPath           # Vyžaduje import z modulu pathlib (from pathlib import PureWindowsPath)
        - pathlib.PureWindowsPath   # Alternativní zápis (import pathlib)

    Příklady použití:
        - def validate_windows_path(path: PureWindowsPath) -> bool:
        - def convert_to_windows(path: str) -> PureWindowsPath:
        - win_path: PureWindowsPath = PureWindowsPath("C:\\Users\\Admin\\Documents")

    Implementační detaily:
        PureWindowsPath je konkrétní implementace PurePath pro Windows cesty. Dodržuje pravidla
        pro manipulaci s cestami ve stylu Windows (používá '\\' jako oddělovač, podporuje
        písmena disků, UNC cesty, atd.) nezávisle na aktuálním operačním systému.

    Validační proces:
        1. Ověří, zda hodnota je instance třídy pathlib.PureWindowsPath
        2. Validace probíhá pomocí isinstance(value, pathlib.PureWindowsPath)

    Použití v kódu:
        - Pro parametry funkcí: def validate_windows_file(path: PureWindowsPath) -> None:
        - Pro návratové hodnoty: def to_windows_path(local_path: str) -> PureWindowsPath:
        - Pro typování proměnných: app_path: PureWindowsPath = PureWindowsPath("C:\\Program Files\\App")

    Specifické vlastnosti a omezení:
        - Výchozí oddělovač je '\\'  (ale při vytváření akceptuje i '/')
        - Podporuje písmena disků (např. 'C:')
        - Podporuje UNC cesty (např. '\\\\server\\share')
        - Absolutní cesty začínají písmenem disku nebo dvojitým oddělovačem
        - drive a root jsou samostatné komponenty (např. 'C:' a '\\')

    Specifické metody a vlastnosti:
        - path.drive - Vrací písmeno disku s dvojtečkou nebo UNC server
        - path.root - Vrací kořenový oddělovač

    Srovnání s podobnými typy:
        - PurePath: Abstraktní základní třída, PureWindowsPath je její konkrétní implementace
        - PurePosixPath: Stejná abstrakce pro unixové cesty
        - WindowsPath: Rozšiřuje PureWindowsPath o I/O operace pro Windows systémy

    Typické použití:
        - Práce s Windows cestami na jakémkoliv operačním systému
        - Konverze mezi unixovými a Windows cestami
        - Validace cest specifických pro Windows
        - Manipulace s cestami pro aplikace určené pro Windows

    Běžné chyby:
        - Zapomenutí importu: from pathlib import PureWindowsPath
        - Pokusy o použití I/O metod, které PureWindowsPath nemá
        - Nekonzistentní míchání Windows a Posix cest
        - Nesprávné použití zpětných lomítek v řetězcích (potřeba escapovat: '\\\\')

    Reference:
        - https://docs.python.org/3/library/pathlib.html#pathlib.PureWindowsPath
        - https://peps.python.org/pep-0428/ (Object-oriented filesystem paths)
    """

    VALIDATOR_KEY = "PureWindowsPath"
    ANNOTATION = PureWindowsPath

    IS_INSTANCE = PureWindowsPath
    HAS_ATTRS = None  # Nepodporuje validaci přes Duck Typing.
    CALLABLE_ATTRS = None  # Nepodporuje validaci přes Duck Typing.

    DESCRIPTION = "Čistá cesta pro systémy Windows"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí pathlib.PureWindowsPath, "
            "což je třída pro reprezentaci a manipulaci "
            "s cestami ve formátu Windows bez přístupu k souborovému systému."
        )
