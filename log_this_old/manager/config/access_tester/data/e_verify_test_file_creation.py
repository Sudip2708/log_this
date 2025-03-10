from pathlib import Path
from typing import Union, Optional

from _system_access_error import SystemAccessError


def verify_test_file_creation(test_path):
    """Ověří zda došlo k vytvoření testovacího souboru"""

    if test_path.exist():
        return test_path

    else:
        raise SystemAccessError(
            message="Vytvoření testovacího souboru se nezdařilo.",
            detail=f"Testovací soubor není k dispozici na daném umístění '{test_path}'.",
            hint="Zkontrolujte oprávnění k zápisu. Testovací soubor měl být vytvořen, ale fizicky není přítomen."
        )

