from typing import Any, Dict, Optional, Tuple, Union

from ...special_verifiers import duck_typing_verifier
from ...value_verifiers import is_instance_verifier


def verify_base_type(
    value: Any,
    expected_type: Union[type, Tuple[type, ...]],
    duck_typing_instructions: Optional[Dict[str, Any]] = None,
    duck_typing: bool = False,
    bool_only: bool = False
) -> bool:
    """
    Ověří, zda `value` odpovídá `expected_type`, buď přes `is_instance_verifier`,
    nebo přes `duck_typing_verifier`.

    Args:
        value (Any): Hodnota, která má být ověřena.
        expected_type (Union[type, Tuple[type, ...]]): Očekávaný typ nebo typy (např. list, dict).
        duck_typing_instructions (Optional[Dict[str, Any]]): Instrukce pro duck typing, pokud je aktivní.
        duck_typing (bool): Pokud `True`, provede duck typing místo isinstance.
        bool_only (bool): Pokud `True`, namísto výjimek funkce vrací False.

    Returns:
        bool: True, pokud hodnota odpovídá typu. Jinak False nebo výjimka.

    Raises:
        VerifyError: Pokud `bool_only=False` a validace selže.
    """

    # Pokud je požadována kontrola přes duck typing a anotace ji podporuje
    if duck_typing and duck_typing_instructions:
        return duck_typing_verifier(
            value,
            duck_typing_instructions,
            bool_only=bool_only
        )

    # Jinak proveď ověření na základě validace základního typu (např. list, set)
    else:
        return is_instance_verifier(
            value,
            expected_type,
            bool_only=bool_only
        )
