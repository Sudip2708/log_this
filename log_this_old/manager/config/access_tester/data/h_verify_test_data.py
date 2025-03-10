import json
from typing import Union, Optional

from _system_access_error import SystemAccessError


def verify_test_data(read_data, test_data) -> bool:
    """Ověří přečtená data."""

    if read_data == test_data:
        return True

    else:
        raise SystemAccessError(
            message="Chyba integrity dat.",
            detail=f"Přečtená data neodpovídají zapsaným datům. Zapsaná data: {test_data}. Načtená data po zápisu: {read_data}.",
            hint="Může jít o problém s diskem nebo právy."
        )


