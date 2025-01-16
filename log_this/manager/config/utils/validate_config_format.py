from typing import Dict, Any

class CLIValidateConfigFormatError(Exception):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, exception_type, error_info: dict):
        # Inicializace základní výjimky
        self.exception_type = exception_type
        message = f"Obdržená data nejsou validní."
        super().__init__(message)

        # Přidání extra informací o klíči pro CLI logging
        self.extra = {
            "detail": error_info.get("detail", ""),
            "hint": error_info.get("hint", "")
        }


def validate_config_format(config_data: Any) -> Dict[str, Any]:
    """
    Validates that the input data is a dictionary and not empty.
    Raises a custom exception if the validation fails.
    """
    if not isinstance(config_data, dict):
        raise CLIValidateConfigFormatError(
            TypeError,
            error_info={
                "detail": f"Validation failed: Expected a dictionary. "
                          f"Received type: {type(config_data).__name__}",
                "hint": "Ensure the input is a dictionary.",
            },
        )

    if not config_data:
        raise CLIValidateConfigFormatError(
            ValueError,
            error_info={
                "detail": "Validation failed: Received an empty dictionary. "
                          "The configuration dictionary is empty.",
                "hint": "Ensure the configuration contains valid key-value pairs.",
            },
        )

    return config_data


