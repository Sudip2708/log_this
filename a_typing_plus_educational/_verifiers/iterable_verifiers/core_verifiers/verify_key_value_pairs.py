from typing import Any, Iterable, Optional, Tuple, Union

from ...typing_verifiers import typing_verifier
from .._tools import reduce_depth_check


def verify_key_value_pairs(
    pairs: Iterable[Tuple[Any, Any]],
    key_type: type,
    value_type: type,
    custom_types: Optional[dict],
    inner_check: Union[bool, int],
    duck_typing: bool,
    bool_only: bool
) -> bool:
    """
    Validuje iterovatelný objekt obsahující dvojice (klíč, hodnota) podle zadaných typů.

    Rekurzivně kontroluje každý pár (key, value) podle zadaného typu a úrovně hloubkové kontroly.

    Args:
        pairs (Iterable[Tuple[Any, Any]]): Iterovatelný objekt obsahující dvojice (key, value).
        key_type (type): Očekávaný typ klíče.
        value_type (type): Očekávaný typ hodnoty.
        custom_types (Optional[dict]): Slovník vlastních typů pro validaci.
        inner_check (Union[bool, int]): Hloubka rekurzivní kontroly. True/False nebo celé číslo.
        duck_typing (bool): Povolit kachní typování.
        bool_only (bool): Vrátit pouze bool výsledek, bez výjimek.

    Returns:
        bool: True pokud všechny dvojice projdou kontrolou, jinak False.
    """

    # Vytvoření kopie parametru definující hloubkovou kontrolu
    current_check = inner_check


    # Obalit try except blokem a zachytávat not iterable
    # Nebo jen zkontrolovat hodnotu že je iterable
    # Možná přidat možnost zadání dict a nebo tupet nebo itereble tuple
    # A použít items = items.items() if isinstance(items, dict) else items if isinstance(items, Iterable) and len(items) = 2
    # Definovat výjimku pro neplatný vstup


    # Validace každého klíče a hodnoty
    for key, val in pairs:

        # Snížení hloubky kontroly
        current_check = reduce_depth_check(current_check)

        # Rekurzivní validace hodnoty na základě vnitřního typu
        # Pokud je parametr bool_only=True, pak při negativním výsledku ukončení iterace
        if not typing_verifier(
                key,
                key_type,
                custom_types,
                current_check,
                duck_typing,
                bool_only
        ):
            return False

        # Rekurzivní validace hodnoty
        # Pokud je parametr bool_only=True, pak při negativním výsledku ukončení iterace
        if not typing_verifier(
                val,
                value_type,
                custom_types,
                current_check,
                duck_typing,
                bool_only
        ):
            return False

        # Přerušení cyklu, pokud se dosáhne maximální hloubky
        # Tato poslední iterace s current_check == 0 ještě proběhne,
        # ale dále již nebude následovat žádná hlubší kontrola.
        # Proto po této iteraci přerušíme cyklus.
        if not current_check:
            break

    # Pokud vše proběhne v pořádku a bez chyb
    return True
