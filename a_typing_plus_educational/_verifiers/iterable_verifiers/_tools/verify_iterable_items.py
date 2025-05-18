from typing import Any, Optional

from .._tools import reduce_depth_check
from ...typing_verifiers import typing_verifier


def verify_iterable_items(
    iterable: Any,
    item_annotation: Any,
    custom_types: Optional[dict],
    inner_check: bool | int,
    duck_typing: bool,
    bool_only: bool
) -> bool:
    """
    Rekurzivně ověřuje položky v iterovatelném objektu dle zadané typové anotace.

    Args:
        iterable (Any): Iterovatelný objekt (např. list, tuple, set).
        item_annotation (Any): Typová anotace pro prvky (např. `int`, `str`, `CustomType`...).
        custom_types (Optional[dict]): Uživatelsky definované typy a jejich validátory.
        inner_check (Union[bool, int]): Hloubka rekurze. Pokud `False`, rekurze neprobíhá.
        duck_typing (bool): Povolit duck typing při ověřování typů.
        bool_only (bool): Pokud `True`, vrací pouze True/False. Jinak může vyvolat výjimky.

    Returns:
        bool: `True`, pokud jsou všechny položky validní. Jinak `False`.
    """
    current_check = inner_check

    for item in iterable:
        current_check = reduce_depth_check(current_check)

        if not typing_verifier(
            item,
            item_annotation,
            custom_types,
            current_check,
            duck_typing,
            bool_only
        ):
            return False

        if not current_check:
            break

    return True
