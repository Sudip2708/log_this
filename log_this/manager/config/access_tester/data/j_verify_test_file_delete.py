import json
from typing import Union, Optional

from _system_access_error import SystemAccessError


def verify_test_file_delete(test_path):
    """Ověří zda došlo k vytvoření testovacího souboru"""

    if not test_path.exist():
        return True

    else:
        raise SystemAccessError(
            message="Smazání testovacího souboru se nezdařilo.",
            detail=f"Testovací soubor i přes provedení smazání je stále přítomen: '{test_path}'.",
            hint="Zkontrolujte oprávnění k mazání."
        )



