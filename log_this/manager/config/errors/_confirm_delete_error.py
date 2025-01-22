class ConfirmDeleteError(Exception):
    """Vlastní výjimka pro případ, že dojde k pokusu o smazání konfiguračního souboru bez zadání atributu _recreate_config_file na True."""

    def __init__(self, exception_type, config_file_path, error_info: dict):
        message = f"Konfigurační soubor není možné smazat."
        super().__init__(message)
        self.extra = {
            "detail": "Pro smazání konfiguračního souboru je potřeba nejprve nastavit atribut umožňující jeho smazání.",
            "hint": "Nastavit atribut self._recreate_config_file na hodnotu True"
        }