import site
import os
from pathlib import Path
from typing import Union

from ._exceptions import VerifyUnexpectedError


def is_user_code(
        filename: Union[Path, str],
):
    """Vrací True, pokud soubor nepatří do systémového nebo knihovního kódu"""

    # Ověření vstupních hodnot
    if not filename or filename == '<string>':
        return False

    try:

        # Cesty pro systémové a knihovní kódy
        ignore_paths = [
            os.path.abspath(os.path.dirname(os.__file__)),
            *map(os.path.abspath, site.getsitepackages()),
            os.path.abspath(site.getusersitepackages())
        ]

        # Vzory pro vyloučení
        ignore_patterns = [
            'site-packages', 'dist-packages', '.venv', 'virtualenv', 'venv'
        ]

        # Získání absolutní cesty
        abs_filename = os.path.abspath(filename)

        # Vyhodnocení získané cety vůči vzorům
        return not (
            any(path and abs_filename.startswith(path) for path in ignore_paths)
            or
            any(pattern in abs_filename for pattern in IGNORE_PATTERNS)
        )

    # Ošetření případů, kdy by samotná funkce způsobila chybu
    except Exception as e:
        raise VerifyUnexpectedError(
            f"Neočekávaná chyba zachycená ve funkci 'is_user_code' "
            f"při generování zjednodušeného tracebacku: {e}"
        )


if __name__ == "__main__":

    pass