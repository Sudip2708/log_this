from typing import Any

from ....attribute_verifiers import has_expected_type_attribute_verifier


def has_int_attribute_verifier(
        value: Any,
        expected_attribute: str,
        bool_only: bool = False
):
    """
    Interní funkce pro duck typing ověření, zda hodnota obsahuje atribut typu int.

    Používá se např. při ověření struktur jako datetime, kde se očekává typ int (např. rok, měsíc, den).

    Args:
        value (Any): Hodnota, která se má ověřit.
        expected_attribute (str): Název atributu, který má být typu int.
        bool_only (bool): Pokud je True, výstup je pouze bool. Jinak vrací detailnější výsledek.

    Returns:
        Any: Výsledek ověření atributu. Může být bool nebo výjimka popisující
            zachycený stav a možnost nápravy (v závislosti na hodnotě parametru bool_only).
    """
    return has_expected_type_attribute_verifier(
        value,
        expected_attribute,
        int,
        bool_only
    )


