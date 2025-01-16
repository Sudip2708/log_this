from pathlib import Path
import json

class CLIValidateConfigDataError(Exception):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, exception_type, error_info: dict):
        # Inicializace základní výjimky
        self.exception_type = exception_type
        message = f"An error occurred while validate config data."
        super().__init__(message)

        # Přidání extra informací o klíči pro CLI logging
        self.extra = {
            "detail": error_info.get("detail", ""),
            "hint": error_info.get("hint", "")
        }


def validate_config_data(
        config_dict: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Metoda pro ověření klíčů a hodnot konfiguračního slovníku.

    Metoda nejprve ověří přítomnost klíče v defaultním slovníku.
    Následně ověří i správný formát hodnoty.

    Args:
        config (Dict[str, Any]): Konfigurace ke kontrole

    Returns:
        bool: Indikuje validitu celé konfigurace
    """

    try:

        # Cyklus rozebírající slovník na klíč a hodnotu
        for key, value in config_dict.items():
            validate_key_and_value(key, value)

        return config_dict

    except AttributeError as e:
        raise CLIValidateConfigDataError(
            AttributeError,
            error_info={
                "detail": "The provided object is not a dictionary or lacks the .items() method.",
                "hint": "Ensure the input is a dictionary or dictionary-like object.",
            },
        )

    except TypeError as e:
        raise CLIValidateConfigDataError(
            TypeError,
            error_info={
                "detail": "The provided object is not iterable.",
                "hint": "Ensure the input is a dictionary or iterable object.",
            },
        )

    except CLIValidateKeyError as e:
        raise CLIValidateConfigDataError(
            CLIValidateKeyError,
            error_info={
                "detail": f"Invalid key found during validation: {str(e)}",
                "hint": "Check the keys in the config file.",
            },
        )

    except CLIValidateValueError as e:
        raise CLIValidateConfigDataError(
            CLIValidateValueError,
            error_info={
                "detail": f"Invalid value found during validation: {str(e)}",
                "hint": "Check the values in the config file.",
            },
        )

    except Exception as e:
        raise CLIValidateConfigDataError(
            Exception,
            error_info={
                "detail": f"Unexpected error: {type(e).__name__}({str(e)})",
                "hint": "Check the input data for unexpected issues.",
            },
        )
