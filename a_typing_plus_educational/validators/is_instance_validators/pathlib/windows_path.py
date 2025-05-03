from pathlib import WindowsPath

from ...._bases import BaseIsInstanceValidator


class WindowsPathValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci pathlib.WindowsPath

    Typ pathlib.WindowsPath představuje objekt pro manipulaci s cestami ve Windows formátu,
    který umožňuje provádět I/O operace se soubory a adresáři. Je to konkrétní implementace
    Path specifická pro systémy Windows, která rozšiřuje PureWindowsPath o interakci se
    souborovým systémem.

    Syntaxe:
        - WindowsPath               # Vyžaduje import z modulu pathlib (from pathlib import WindowsPath)
        - pathlib.WindowsPath       # Alternativní zápis (import pathlib)

    Příklady použití:
        - def process_windows_file(file: WindowsPath) -> None:
        - def find_windows_executable(name: str) -> WindowsPath:
        - program_file: WindowsPath = WindowsPath("C:\\Program Files\\app.exe")

    Implementační detaily:
        WindowsPath je konkrétní implementace Path pro systémy Windows, která dědí z PureWindowsPath
        a přidává metody pro skutečnou interakci se soubory a adresáři. Na Windows systémech
        je Path implementována jako WindowsPath, ale lze ji explicitně vytvořit na jakémkoliv systému.

    Validační proces:
        1. Ověří, zda hodnota je instance třídy pathlib.WindowsPath
        2. Validace probíhá pomocí isinstance(value, pathlib.WindowsPath)

    Použití v kódu:
        - Pro parametry funkcí: def read_windows_file(path: WindowsPath) -> str:
        - Pro návratové hodnoty: def find_windows_config() -> WindowsPath:
        - Pro typování proměnných: desktop: WindowsPath = WindowsPath("C:\\Users\\User\\Desktop")

    Důležité metody specifické pro WindowsPath:
        - Všechny I/O metody zděděné z Path (exists, is_file, mkdir, rmdir, unlink, atd.)
        - path.owner() / path.group() - Neimplementováno na Windows (vyvolá výjimku)
        - path.is_mount() - Kontrola, zda je cesta kořenem souborového systému nebo mounted volume

    Specifické vlastnosti a omezení:
        - Funguje plně pouze na Windows
        - Některé unixové operace nejsou dostupné (chmod, lchmod)
        - Na unixových systémech může některé metody vyvolat výjimku NotImplementedError

    Srovnání s podobnými typy:
        - Path: Obecná třída, která se stává WindowsPath na Windows systémech
        - PureWindowsPath: Poskytuje jen manipulaci s cestami bez I/O operací
        - PosixPath: Ekvivalent pro unixové cesty

    Typické použití:
        - Explicitní práce s Windows cestami a souborovým systémem
        - Multiplatformní aplikace vyžadující Windows chování cest
        - Kód specifický pro Windows systémy

    Běžné chyby:
        - Zapomenutí importu: from pathlib import WindowsPath
        - Předpoklad funkčnosti všech metod na unixových systémech
        - Míchání WindowsPath a PosixPath v jednom kódu
        - Nevyužívání cross-platformní Path, kde by to bylo vhodnější
        - Použití nesprávných oddělovačů nebo nepochopení specifik Windows cest

    Reference:
        - https://docs.python.org/3/library/pathlib.html#pathlib.WindowsPath
        - https://peps.python.org/pep-0428/ (Object-oriented filesystem paths)
    """

    VALIDATOR_KEY = "WindowsPath"
    ANNOTATION = WindowsPath

    IS_INSTANCE = WindowsPath
    DUCK_TYPING = None

    DESCRIPTION = "Objektová reprezentace cesty ve Windows"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí pathlib.WindowsPath, tedy reprezentuje cestu specifickou pro systémy Windows. "
            "Poskytuje metody pro manipulaci s cestami a přístup k souborovému systému."
        )
