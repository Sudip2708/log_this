from os import PathLike

from ...._bases import BaseIsInstanceValidator


class PathLikeValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci os.PathLike

    Typ os.PathLike reprezentuje abstraktní protokol pro objekty, které lze použít jako cesty
    k souborům nebo adresářům v systému souborů. Zahrnuje objekty, které implementují metodu
    __fspath__, což umožňuje jejich automatickou konverzi na řetězcovou reprezentaci cesty ve
    funkcích pracujících se soubory a adresáři.

    Syntaxe:
        - PathLike               # Vyžaduje import z modulu os (from os import PathLike)
        - os.PathLike            # Alternativní zápis (import os)
        - PathLike[str]          # Typicky pro cesty jako řetězce
        - PathLike[bytes]        # Pro cesty v binárním formátu
        - os.PathLike[str]       # Ekvivalentní zápis s kvalifikovaným jménem

    Příklady použití:
        - def read_file(path: PathLike) -> str:
        - def list_directory(directory: PathLike[str]) -> List[str]:
        - def write_binary(path: PathLike[bytes], data: bytes) -> None:

    Implementační detaily:
        PathLike je abstraktní protokol, který definuje metodu __fspath__() vracející řetězcovou
        reprezentaci cesty. Objekty implementující tento protokol mohou být použity všude, kde je
        očekávána cesta k souboru. Standardní implementace zahrnují str, bytes a objekt Path z
        modulu pathlib.

    Validační proces:
        1. Ověří, zda hodnota je instance kompatibilní s os.PathLike
        2. Validace probíhá pomocí isinstance(value, os.PathLike)
        3. Hodnota se považuje za validní, pokud implementuje metodu __fspath__

    Použití v kódu:
        - Pro parametry funkcí: def save_data(path: PathLike) -> None:
        - Pro návratové hodnoty: def generate_temp_path() -> PathLike:
        - Pro typování proměnných: config_path: PathLike = Path('/etc/config.ini')

    Kompatibilní typy:
        - str - Řetězce jsou implicitně PathLike
        - bytes - Binární reprezentace cest
        - pathlib.Path - Objektově orientovaná reprezentace cest
        - Vlastní typy implementující __fspath__

    Srovnání s podobnými typy:
        - str/bytes: Primitivní reprezentace cest, nezahrnují metody pro práci s cestami
        - pathlib.Path: Komplexní objekty pro práci s cestami, implementují PathLike
        - Čisté textové cesty: Vhodné pro jednoduché použití, ale bez objektově orientovaných výhod

    Běžné vzory použití:
        - Přijímání flexibilních typů cest ve funkcích
        - Zpracování souborů a adresářů bez ohledu na konkrétní reprezentaci cesty
        - Konverze mezi různými reprezentacemi cest (str, bytes, pathlib.Path)

    Běžné chyby:
        - Zapomenutí importu: from os import PathLike
        - Nesprávné předpokládání, že PathLike objekty mají metody jako pathlib.Path
        - Zanedbání typového parametru (str nebo bytes)
        - Smíchání cest v různých formátech (str a bytes) bez explicitní konverze

    Reference:
        - https://docs.python.org/3/library/os.html#os.PathLike
        - https://peps.python.org/pep-0519/ (Protokol souborových cest)
    """

    VALIDATOR_KEY = "PathLike"
    ANNOTATION = PathLike

    IS_INSTANCE = PathLike
    DUCK_TYPING = {
        "has_attr": "__fspath__",
    }

    DESCRIPTION = "Objekt reprezentující cestu k souboru"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje protokol os.PathLike, tedy implementuje "
            "metodu __fspath__, která vrací reprezentaci cesty jako řetězec nebo bytes. "
            "Umožňuje snadnou manipulaci s cestami."
        )
