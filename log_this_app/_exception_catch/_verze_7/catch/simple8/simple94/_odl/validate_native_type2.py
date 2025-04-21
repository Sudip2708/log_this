from typing import Any, Union, Tuple


class ValidateError(Exception):
    """Základní třída pro výjimky validace."""
    pass


class ValidateTypingError(ValidateError):
    """Výjimka pro chyby typování při validaci."""
    pass


def validate_native_type(value: Any,
                         expected_type: Union[type, Tuple[type, ...]]):
    """
    Validuje, že hodnota odpovídá očekávanému typu.

    Args:
        value: Hodnota k validaci
        expected_type: Očekávaný typ (type, tuple typů nebo Union)

    Raises:
        ValidateTypingError: Pokud hodnota neodpovídá typu nebo expected_type není platný typ
    """
    # Kontrola, zda je expected_type validní
    if not (isinstance(expected_type, (type, tuple)) or
            (hasattr(expected_type,
                     "__origin__") and expected_type.__origin__ is Union)):
        raise ValidateTypingError(
            f"Parametr expected_type musí být typ, tuple typů nebo Union.\n"
            f"Předaný parametr: {expected_type} typu {type(expected_type).__name__}"
        )

    # Kontrola typové shody
    try:
        if not isinstance(value, expected_type):
            try:
                type_name = expected_type.__name__ if hasattr(expected_type, __name__) else str(expected_type)
                type_name = expected_type.__name__
            except AttributeError:
                type_name = str(expected_type)

            raise ValidateTypingError(
                f"Hodnota {value} typu '{type(value).__name__}' "
                f"neodpovídá požadovanému typu: '{type_name}'."
            )
    except TypeError as e:
        # Zachycení TypeError od samotného isinstance - problém s expected_type
        raise ValidateTypingError(
            f"Chyba při kontrole typu hodnoty: {str(e)}"
        ) from e

    print("Ověření úspěšně prošlo")

validate_native_type("123", "int")