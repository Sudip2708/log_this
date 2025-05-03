from pathlib import PosixPath

from ...._bases import BaseIsInstanceValidator


class PosixPathValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci pathlib.PosixPath

    Typ pathlib.PosixPath představuje objekt pro manipulaci s cestami v unixovém formátu,
    který umožňuje provádět I/O operace se soubory a adresáři. Je to konkrétní implementace
    Path specifická pro unixové systémy, která rozšiřuje PurePosixPath o interakci se
    souborovým systémem.

    Syntaxe:
        - PosixPath               # Vyžaduje import z modulu pathlib (from pathlib import PosixPath)
        - pathlib.PosixPath       # Alternativní zápis (import pathlib)

    Příklady použití:
        - def process_unix_file(file: PosixPath) -> None:
        - def find_unix_executable(name: str) -> PosixPath:
        - config_file: PosixPath = PosixPath("/etc/config.ini")

    Implementační detaily:
        PosixPath je konkrétní implementace Path pro unixové systémy, která dědí z PurePosixPath
        a přidává metody pro skutečnou interakci se soubory a adresáři. Na unixových systémech
        je Path implementována jako PosixPath, ale lze ji explicitně vytvořit na jakémkoliv systému.

    Validační proces:
        1. Ověří, zda hodnota je instance třídy pathlib.PosixPath
        2. Validace probíhá pomocí isinstance(value, pathlib.PosixPath)

    Použití v kódu:
        - Pro parametry funkcí: def read_unix_file(path: PosixPath) -> str:
        - Pro návratové hodnoty: def find_unix_config() -> PosixPath:
        - Pro typování proměnných: user_home: PosixPath = PosixPath("/home/user")

    Důležité metody specifické pro PosixPath:
        - path.exists() - Kontrola existence cesty
        - path.is_file() / path.is_dir() - Kontrola typu cesty
        - path.is_symlink() / path.is_socket() / path.is_fifo() / path.is_block_device() / path.is_char_device()
        - path.chmod() - Změna oprávnění souboru
        - path.lchmod() - Změna oprávnění symbolického odkazu
        - path.owner() / path.group() - Získání vlastníka a skupiny souboru
        - path.lstat() - Získání informací o souboru bez následování symlinků
        - Všechny I/O metody zděděné z Path (mkdir, rmdir, unlink, read_text, atd.)

    Specifické vlastnosti a omezení:
        - Funguje plně pouze na unixových systémech
        - Některé operace nemusí být dostupné na Windows, i když vytvoříte instanci PosixPath
        - Na Windows může některé metody vyvolat výjimku NotImplementedError

    Srovnání s podobnými typy:
        - Path: Obecná třída, která se stává PosixPath na unixových systémech
        - PurePosixPath: Poskytuje jen manipulaci s cestami bez I/O operací
        - WindowsPath: Ekvivalent pro Windows cesty

    Typické použití:
        - Explicitní práce s unixovými cestami a souborovým systémem
        - Multiplatformní aplikace vyžadující unixové chování cest
        - Kód specifický pro unixové systémy

    Běžné chyby:
        - Zapomenutí importu: from pathlib import PosixPath
        - Předpoklad funkčnosti všech metod na Windows
        - Míchání WindowsPath a PosixPath v jednom kódu
        - Nevyužívání cross-platformní Path, kde by to bylo vhodnější

    Reference:
        - https://docs.python.org/3/library/pathlib.html#pathlib.PosixPath
        - https://peps.python.org/pep-0428/ (Object-oriented filesystem paths)
    """

    VALIDATOR_KEY = "PosixPath"
    ANNOTATION = PosixPath

    IS_INSTANCE = PosixPath
    DUCK_TYPING = None

    DESCRIPTION = "Objektová reprezentace cesty v POSIXových systémech"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí pathlib.PosixPath, "
            "tedy reprezentuje cestu specifickou pro systémy typu POSIX "
            "(Unix, Linux, macOS). Poskytuje metody pro manipulaci s cestami."
        )
