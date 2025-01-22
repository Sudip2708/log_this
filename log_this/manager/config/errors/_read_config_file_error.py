class ReadConfigFileError(Exception):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, exception_type, config_file_path, error_info: dict):
        # Inicializace základní výjimky
        self.exception_type = exception_type
        message = f"An error occurred while reading config file: '{config_file_path}'."
        super().__init__(message)

        # Přidání extra informací o klíči pro CLI logging
        self.extra = {
            "detail": error_info.get("detail", ""),
            "hint": error_info.get("hint", "")
        }