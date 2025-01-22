class ValidateKeyError(KeyError):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, key: str, defaults: set[str]):
        # Inicializace základní výjimky
        message = f"Byl zadán neplatný klíč: '{key}'."
        super().__init__(message)

        # Přidání extra informací o klíči pro CLI logging
        self.extra = {
            "detail": f"Zde je seznam povolených klíčů: \n{defaults}",
            "hint": f"Pro zobrazení seznamu klíčů i s popisem a nápovědou zadej v terminálu: \n"
                    f"$ log-this-config --help -key"
        }