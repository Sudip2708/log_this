from pathlib import Path

from ...._bases import BaseIsInstanceValidator


class PathValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci pathlib.Path

    Typ pathlib.Path představuje objektově orientovanou reprezentaci cesty k souboru nebo adresáři
    v systému souborů. Nabízí komplexní sadu metod pro manipulaci s cestami, metadata souborů a
    základní operace se soubory a adresáři nezávisle na operačním systému.

    Syntaxe:
        - Path                    # Vyžaduje import z modulu pathlib (from pathlib import Path)
        - pathlib.Path            # Alternativní zápis (import pathlib)
        - PurePath               # Abstraktní základní třída pro Path bez I/O operací
        - PosixPath/WindowsPath  # Systémově specifické implementace Path (obvykle se nepoužívají přímo)

    Příklady použití:
        - def read_config(path: Path) -> dict:
        - def save_results(directory: Path, filename: str) -> Path:
        - config_file: Path = Path("/etc/app/config.ini")
        - data_files: List[Path] = list(Path("./data").glob("*.csv"))

    Implementační detaily:
        Path je konkrétní implementace PurePath, která přidává I/O operace. Na rozdíl od prostých
        řetězců poskytuje rozsáhlou sadu metod pro manipulaci s cestami a operace se soubory
        a adresáři. Implementuje protokol os.PathLike a lze ji použít ve všech funkcích,
        které očekávají cestu.

    Validační proces:
        1. Ověří, zda hodnota je instance třídy pathlib.Path
        2. Validace probíhá pomocí isinstance(value, pathlib.Path)

    Použití v kódu:
        - Pro parametry funkcí: def process_file(file_path: Path) -> None:
        - Pro návratové hodnoty: def create_temp_file() -> Path:
        - Pro typování proměnných: log_dir: Path = Path("./logs")

    Důležité metody a vlastnosti:
        - path.name - Název souboru nebo složky bez cesty
        - path.parent - Rodičovský adresář
        - path.suffix - Přípona souboru včetně tečky
        - path.stem - Název souboru bez přípony
        - path.exists() - Kontrola existence cesty
        - path.is_file() / path.is_dir() - Kontrola typu cesty
        - path.mkdir() - Vytvoření adresáře
        - path.touch() - Vytvoření prázdného souboru nebo aktualizace času
        - path.rename() - Přejmenování souboru
        - path.unlink() - Odstranění souboru
        - path.rmdir() - Odstranění prázdného adresáře
        - path.glob() / path.rglob() - Vyhledávání souborů dle vzoru
        - path.read_text() / path.read_bytes() - Čtení obsahu souboru
        - path.write_text() / path.write_bytes() - Zápis do souboru

    Srovnání s podobnými typy:
        - os.PathLike: Protokol pro typy použitelné jako cesty, Path ho implementuje
        - str: Jednoduchá reprezentace cesty, bez metod pro manipulaci s cestami
        - bytes: Binární reprezentace cesty, vhodná pro některé nízkoúrovňové operace
        - os.path: Modul s funkcemi pro práci s cestami, méně objektově orientovaný

    Běžné vzory použití:
        - Manipulace s cestami: path.parent / "new_file.txt"
        - Iterace přes soubory: for file in path.glob("*.py"): ...
        - Čtení/zápis souborů: content = path.read_text(), path.write_text(data)
        - Vytváření adresářové struktury: path.mkdir(parents=True, exist_ok=True)

    Běžné chyby:
        - Zapomenutí importu: from pathlib import Path
        - Pokusy o použití řetězcových metod přímo na Path objektu
        - Zapomenutí, že Path není serializovatelný do JSON
        - Nekonvertování Path na str při předávání knihovnám, které očekávají řetězce

    Reference:
        - https://docs.python.org/3/library/pathlib.html
        - https://peps.python.org/pep-0428/ (Object-oriented filesystem paths)
    """

    VALIDATOR_KEY = "Path"
    ANNOTATION = Path

    IS_INSTANCE = Path
    DUCK_TYPING = {
        "has_attr": "__fspath__",
        "has_callable_attr": ("open", "exists", "is_file")
    }

    DESCRIPTION = "Objektová reprezentace cesty k souboru"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí pathlib.Path, "
            "což je třída poskytující objektově orientované rozhraní "
            "pro práci s cestami k souborům a adresářům."
        )
