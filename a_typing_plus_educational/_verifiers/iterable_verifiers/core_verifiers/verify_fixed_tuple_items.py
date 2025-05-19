from typing import Optional, Union

from .._tools import reduce_depth_check
from ...typing_verifiers import typing_verifier


def verify_fixed_tuple_items(
    iterable: tuple,
    annotations: tuple,
    custom_types: Optional[dict],
    inner_check: Union[bool, int],
    duck_typing: bool,
    bool_only: bool
) -> bool:
    """
    Ověřuje položky fixní n-tice, kde každá pozice má jinou typovou anotaci.
    """

    # Kontrola délky
    if len(iterable) != len(annotations):
        raise ValueError(
            f"Očekávaná délka n-tice {len(annotations)}, ale obdrženo {len(iterable)}"
        )

    # Vytvoření kopie parametru definující hloubkovou kontrolu
    current_check = inner_check

    # Kontrola typu každé položky na dané pozici
    for item, expected_type in zip(iterable, annotations):

        # Snížení hloubky kontroly
        current_check = reduce_depth_check(current_check)

        # Rekurzivní validace hodnoty na základě vnitřního typu
        if not typing_verifier(
            item,
            expected_type,
            custom_types,
            current_check,
            duck_typing,
            bool_only
        ):
            return False

        # Přerušení cyklu, pokud se dosáhne maximální hloubky
        if not current_check:
            break

    # Pokud vše projde navrácení úspěšné validace
    return True
