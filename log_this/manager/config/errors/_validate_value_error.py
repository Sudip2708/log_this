class ValidateValueError(ValueError):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, key: str, value: Union[int, str, bool], key_data: ConfigKey):
        # Inicializace základní výjimky
        message = f"Pro klíč '{key}' byla zadaná neplatná hodnota: '{value}'."
        super().__init__(message)

        # Přidání extra informací o klíči pro CLI logging
        self.extra = {
            "detail": key_data.detail,
            "hint": key_data.hint
        }