from pathlib import PurePath

from ...._bases import BaseIsInstanceValidator


class PurePathValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci pathlib.PurePath

    Typ pathlib.PurePath představuje abstraktní základní třídu pro manipulaci s cestami k souborům
    a adresářům bez provádění I/O operací. Poskytuje nástroje pro čistou manipulaci s cestami
    nezávisle na operačním systému, ale neumožňuje práci se skutečným systémem souborů.

    Syntaxe:
        - PurePath                # Vyžaduje import z modulu pathlib (from pathlib import PurePath)
        - pathlib.PurePath        # Alternativní zápis (import pathlib)

    Příklady použití:
        - def normalize_path(path: PurePath) -> str:
        - def validate_filepath(path: PurePath) -> bool:
        - base_path: PurePath = PurePath("/usr/local")
        - relative_path: PurePath = PurePath("bin/python")

    Implementační detaily:
        PurePath je abstraktní základní třída pro manipulaci s cestami bez I/O operací.
        V závislosti na operačním systému se ve skutečnosti vytvoří instance PurePosixPath nebo
        PureWindowsPath. PurePath implementuje protokol os.PathLike, takže je kompatibilní
        se všemi funkcemi očekávajícími cesty.

    Validační proces:
        1. Ověří, zda hodnota je instance třídy pathlib.PurePath
        2. Validace probíhá pomocí isinstance(value, pathlib.PurePath)
        3. Platné jsou všechny podtřídy PurePath, včetně Path, PurePosixPath, PureWindowsPath

    Použití v kódu:
        - Pro parametry funkcí: def join_paths(base: PurePath, *parts: str) -> PurePath:
        - Pro návratové hodnoty: def get_config_path() -> PurePath:
        - Pro typování proměnných: template_path: PurePath = PurePath("templates/default.html")

    Důležité metody a vlastnosti:
        - path.name - Název souboru nebo složky bez cesty
        - path.parent - Rodičovský adresář jako PurePath
        - path.parents - Posloupnost všech rodičovských adresářů
        - path.suffix - Přípona souboru včetně tečky
        - path.suffixes - Seznam všech přípon pro vícenásobné přípony
        - path.stem - Název souboru bez přípony
        - path.parts - Tuple všech komponent cesty
        - path.joinpath(*other) - Připojení dalších částí k cestě
        - path.match(pattern) - Kontrola, zda cesta odpovídá vzoru
        - path.relative_to(*other) - Vytvoření relativní cesty
        - path.with_name(name) - Vrátí novou cestu se změněným názvem
        - path.with_suffix(suffix) - Vrátí novou cestu se změněnou příponou

    Srovnání s Path:
        - PurePath: Pouze manipulace s cestami, bez I/O operací
        - Path: Rozšiřuje PurePath o I/O operace (exists(), mkdir(), rmdir(), atd.)

    Typické použití:
        - Čistá manipulace s cestami bez potřeby přístupu k souborovému systému
        - Normalizace a validace cest
        - Vytváření a upravování cest nezávisle na operačním systému
        - Použití tam, kde potřebujeme pouze manipulovat s cestami, ale ne číst/zapisovat soubory

    Běžné chyby:
        - Zapomenutí importu: from pathlib import PurePath
        - Pokusy o použití I/O metod, které PurePath nemá (exists(), mkdir(), atd.)
        - Nepochopení, že PurePath samotné může být PurePosixPath nebo PureWindowsPath
        - Předpokládání, že PurePath reprezentuje existující cestu v systému souborů

    Reference:
        - https://docs.python.org/3/library/pathlib.html#pure-paths
        - https://peps.python.org/pep-0428/ (Object-oriented filesystem paths)
    """

    VALIDATOR_KEY = "PurePath"
    ANNOTATION = PurePath

    IS_INSTANCE = PurePath
    DUCK_TYPING = {
        "has_attr": ("parts", "name"),
        "has_callable_attr": ("joinpath", "as_posix")
    }

    DESCRIPTION = "Čistá cesta bez přístupu k souborovému systému"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí pathlib.PurePath, "
            "tedy abstraktní základní třídou pro cesty, "
            "která neposkytuje operace přistupující k souborovému systému."
        )
