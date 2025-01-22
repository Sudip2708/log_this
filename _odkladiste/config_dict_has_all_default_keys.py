class ConfigDictHasAllDefaultKeysError(Exception):
    """Vlastní výjimka pro chyby při validaci konfiguračního slovníku."""

    def __init__(self, exception_type, error_info: dict):
        # Inicializace základní výjimky
        self.exception_type = exception_type
        message = "An error occurred during comparison of loaded data with default values."
        super().__init__(message)

        # Přidání extra informací o chybě pro podrobnější logging
        self.extra = {
            "detail": error_info.get("detail", ""),
            "hint": error_info.get("hint", ""),
        }


def config_dict_has_all_default_keys(
        config_dict: Dict[str, Any],
        defaults: Dict[str, Any]
) -> bool:
    """
    Zkontroluje, zda načtený konfigurační slovník obsahuje všechny klíče z výchozího slovníku.

    Args:
        config_dict (Dict[str, Any]): Načtený konfigurační slovník.
        defaults (Dict[str, Any]): Výchozí slovník.

    Returns:
        bool: True, pokud obsahuje všechny klíče; jinak False.

    Raises:
        ConfigDictValidationError: Pokud dojde k chybě při validaci.
    """
    try:
        return set(config_dict.keys()) == set(defaults.keys())

    except AttributeError as e:
        raise ConfigDictHasAllDefaultKeysError(
            AttributeError,
            error_info={
                "detail": "The provided object is not a dictionary or lacks the .keys() method.",
                "hint": "Ensure both inputs are dictionaries or dictionary-like objects.",
            },
        )

    except TypeError as e:
        raise ConfigDictHasAllDefaultKeysError(
            TypeError,
            error_info={
                "detail": "Invalid data type encountered during key comparison.",
                "hint": "Ensure both inputs are of type Dict[str, Any].",
            },
        )

    except Exception as e:
        raise ConfigDictHasAllDefaultKeysError(
            Exception,
            error_info={
                "detail": f"Unexpected error: {type(e).__name__}({str(e)})",
                "hint": "Check the inputs for unexpected issues or invalid data.",
            },
        )
