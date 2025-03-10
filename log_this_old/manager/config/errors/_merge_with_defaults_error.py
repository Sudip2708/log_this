class MergeWithDefaultsError(Exception):
    """Vlastní výjimka pro chyby při slučování slovníků."""

    def __init__(self, exception_type, error_info: dict):
        # Inicializace základní výjimky
        self.exception_type = exception_type
        message = "An error occurred while merging configuration with defaults."
        super().__init__(message)

        # Přidání extra informací o chybě pro podrobnější logging
        self.extra = {
            "detail": error_info.get("detail", ""),
            "hint": error_info.get("hint", ""),
        }