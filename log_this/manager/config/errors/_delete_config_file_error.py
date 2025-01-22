class DeleteConfigFileError(Exception):
    """Vlastní výjimka pro chyby při mazání konfiguračního souboru."""

    def __init__(self, exception_type, config_file_path, error_info: dict):
        self.exception_type = exception_type
        message = f"An error occurred while deleting the config file: '{config_file_path}'."
        super().__init__(message)
        self.extra = {
            "detail": error_info.get("detail", ""),
            "hint": error_info.get("hint", "")
        }