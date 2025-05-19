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


    Výjimky které může vyvolat duck typing funkce:
        VerifyDuckTypingReturnedFalseError: Pokud validace selže (a bool_only=False).
        VerifyDuckTypingInstructionNotDictError: Pokud `instruction` není slovník.
        VerifyDuckTypingInstructionEmptyError: Pokud `instruction` je prázdný.
        VerifyDuckTypingInstructionInvalidKeyError: Pokud se objeví neznámý klíč.
        VerifyDuckTypingGetExceptionError: Pokud některý test vyhodí ověřovací výjimku.
        VerifyUnexpectedInternalError: Pro neočekávané chyby mimo knihovnu.

    Výjimky které může vyvolat isinstance funkce:
        VerifyIsInstanceReturnedFalseError: Pokud validace selže (a bool_only=False).
        VerifyTypeParameterError: Pokud je špatně zadán parametr `expected`
        VerifyUnexpectedInternalError: Pro neočekávané chyby mimo knihovnu.
    """

    try:

        # Pokud je požadována kontrola přes duck typing a anotace ji podporuje
        if duck_typing and duck_typing_instructions:
            return duck_typing_verifier(
                value,
                duck_typing_instructions,
                bool_only=bool_only
            )

        # Jinak proveď ověření na základě validace základního typu (např. list, set)
        return is_instance_verifier(
            value,
            expected_type,
            bool_only=bool_only
        )

    # Propagace všech vnitřních výjimek vyvolaných při ověřování
    except VerifyDuckTypingReturnedFalseError as e:
        """
        VerifyDuckTypingReturnedFalseError: Pokud validace selže (a bool_only=False).
        """
        raise VerifyIterableBaseType


    # Propagace všech vnitřních výjimek vyvolaných při ověřování
    except VerifyError:
        """
        VerifyDuckTypingInstructionNotDictError: Pokud `instruction` není slovník.
        VerifyDuckTypingInstructionEmptyError: Pokud `instruction` je prázdný.
        VerifyDuckTypingInstructionInvalidKeyError: Pokud se objeví neznámý klíč.
        VerifyDuckTypingGetExceptionError: Pokud některý test vyhodí ověřovací výjimku.
        VerifyUnexpectedInternalError: Pro neočekávané chyby mimo knihovnu.
        """
        raise

