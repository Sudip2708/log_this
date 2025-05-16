from typing import Any, Callable

from ....special_verifiers import boolean_lambda_verifier


def lambda_command_attribute_verifier(
        value: Any,
        lambda_command: Callable[..., bool],
        bool_only: bool = False
):
    """
    Interní funkce pro duck typing ověření pomocí zadané lambda funkce.

    Umožňuje definovat vlastní logiku pro ověření hodnoty formou lambda výrazu.

    Args:
        value (Any): Hodnota, která se má ověřit.
        lambda_command (Any): Lambda funkce nebo výraz, který bude aplikován na hodnotu.
        bool_only (bool): Pokud je True, vrací pouze bool. Jinak vrací případný výstup z lambda funkce.

    Returns:
        Any: Výsledek ověření atributu. Může být bool nebo výjimka popisující
            zachycený stav a možnost nápravy (v závislosti na hodnotě parametru bool_only).
    """
    return boolean_lambda_verifier(
        lambda_command,
        value,
        bool_only=bool_only
    )
