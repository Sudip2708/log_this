import site
import os

from ._exceptions import VerifyUnexpectedError


def is_path_in_ignore_paths(
        abs_filename
):
    """
    Vrací False, pokud cesta nepatří do systémového nebo knihovního kódu

    Pomocná funkce pro is_user_code
    """

    try:

        # Cesty pro systémové a knihovní kódy
        ignore_paths = [
            os.path.abspath(os.path.dirname(os.__file__)),
            *map(os.path.abspath, site.getsitepackages()),
            os.path.abspath(site.getusersitepackages())
        ]

        # Návrat boolean vyhodnocení
        return any(
            abs_file_path.startswith(path)
            for path in ignore_paths
        )

    # Ošetření případů, kdy by samotná funkce způsobila chybu
    except Exception as e:
        raise VerifyUnexpectedError(
            f"Neočekávaná chyba zachycená ve funkci 'is_path_in_ignore_patterns' "
            f"při generování zjednodušeného tracebacku: {e}"
        )

