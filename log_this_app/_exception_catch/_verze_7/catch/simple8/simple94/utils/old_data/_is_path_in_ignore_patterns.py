import site
import os

from ._exceptions import VerifyUnexpectedError

# Definice vzrů které se nemají vyhodnotit kladně
IGNORE_PATTERNS = [
    'site-packages', 'dist-packages', '.venv', 'virtualenv', 'venv'
]

def is_path_in_ignore_patterns(
        abs_filename
):
    """Vrací False, pokud cesta neobsahuje definovaný vzor"""

    # Ověření vstupních hodnot
    if abs_filename:
        pass

    try:

        for pattern in IGNORE_PATTERNS:
            if pattern in abs_filename:
                return True
        return False


    # Ošetření případů, kdy by samotná funkce způsobila chybu
    except Exception as e:
        raise VerifyUnexpectedError(
            f"Neočekávaná chyba zachycená ve funkci 'is_path_in_ignore_patterns' "
            f"při generování zjednodušeného tracebacku: {e}"
        )


if __name__ == "__main__":

    pass