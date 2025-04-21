import site
import os
from pathlib import Path
from typing import Union

from ._exceptions import VerifyUnexpectedError, InvalidPathInputError
from ._is_path_in_ignore_paths import is_path_in_ignore_paths
from ._is_path_in_ignore_patterns import is_path_in_ignore_patterns


# Definice vzrů které se nemají vyhodnotit kladně
IGNORE_PATTERNS = [
    'site-packages', 'dist-packages', '.venv', 'virtualenv', 'venv'
]


def is_user_code(
        file_path: Union[Path, str],
):
    """Vrací True, pokud soubor nepatří do systémového nebo knihovního kódu"""

    # Ověření vstupních hodnot
    if not isinstance(file_path, (str, Path)):
        raise InvalidPathInputError(
            f"Zadaná cesta neprošla validací!"
            f"Vstup obsahuje nepodporovaný typ: {type(file_path)}"
        )

    try:

        # Získání absolutní cesty
        abs_filename = os.path.abspath(os.fspath(file_path))

        # Kontrola vůči definovaným cestám
        if is_path_in_ignore_paths(abs_filename):
            return False

        # Kontrola vůči definovaným vzorům
        if is_path_in_ignore_patterns(abs_filename):
            return False

        # Pokud není zachyceno výše,
        # jde o cestu k uživatelskému kodu
        return True

    # Propagace výjimek z předchozích funkcí
    except VerifyUnexpectedError:
        raise

    # Ošetření nečekané výjimky
    except Exception as e:
        raise VerifyUnexpectedError(
            f"Neočekávaná chyba zachycená ve funkci 'is_user_code' "
            f"při generování zjednodušeného tracebacku: {e}"
        )


if __name__ == "__main__":

    pass