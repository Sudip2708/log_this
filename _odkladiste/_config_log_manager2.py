import logging

class ConfigLogManager:
    """Třída pro správu logování"""

    def __init__(self):
        self.logger = logging.getLogger('LogThisConfig')
        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """Vrátí loger pro aplikaci"""
        return self.logger

# Příklad použití
if __name__ == "__main__":
    log_manager = ConfigLogManager()
    logger = log_manager.get_logger()

    logger.debug(
                f"for validate key and value: \n"
                f"- Neplatný klíč: key. \n"
                f"- Klíč není součástí defaultní konfigurace. \n"
                f"- Možnosti: options"
            )
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
"""
class LogThisConfig(ConfigMixin):
    _instance = None
    _config_path = Path(__file__).parent / "config.json"
    DEFAULTS = {...}

    def __new__(cls) -> 'LogThisConfig':
        if not cls._instance:
            if not cls._validate_config_dict(cls.DEFAULTS):
                raise ValueError("Chyba při validaci defaultních hodnot.")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self.config = self._load_config_dict()
            self._initialized = True
            # Inicializace logeru
            self.logger = LogManager().get_logger()
"""