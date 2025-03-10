class SaveConfigFileError(Exception):
    """Vlastní výjimka pro chyby při ukládání konfiguračního souboru."""

    def __init__(self, exception_type, config_file_path, error_info: dict):
        self.exception_type = exception_type
        message = f"An error occurred while saving the config file: '{config_file_path}'."
        super().__init__(message)
        self.extra = {
            "detail": error_info.get("detail", ""),
            "hint": error_info.get("hint", "")
        }