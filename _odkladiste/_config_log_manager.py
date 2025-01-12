import logging
from colorama import Fore, Style, init

class ConfigLogManager:
    """Třída pro správu logování s použitím Colorama pro barevné výstupy"""

    def __init__(self):
        # Inicializace colorama (pro Windows)
        init(autoreset=True)

        # Vytvoření loggeru
        self.logger = logging.getLogger('LogThisConfig')
        self.logger.setLevel(logging.DEBUG)  # Nastavení minimální úrovně logování

        # Vytvoření StreamHandleru pro výstup do konzole
        console_handler = logging.StreamHandler()

        # Nastavení formátování logu
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Přidání handleru do loggeru
        self.logger.addHandler(console_handler)

    def _colorize_message(self, levelname, message):
        """Funkce pro barevné zvýraznění zprávy na základě úrovně logu"""
        if levelname == "ERROR":
            return f"{Fore.RED}{message}{Style.RESET_ALL}"
        elif levelname == "WARNING":
            return f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
        elif levelname == "INFO":
            return f"{Fore.GREEN}{message}{Style.RESET_ALL}"
        elif levelname == "DEBUG":
            return f"{Fore.CYAN}{message}{Style.RESET_ALL}"
        else:
            return message  # Pro ostatní úrovně (např. NOTSET)

    def get_logger(self):
        """Vrátí loger pro aplikaci"""
        # Vytvoření nového loggeru, který bude používat barevné zprávy
        logger = self.logger

        # Vytvoření nový formatteru, který přidává barevné kódování
        def custom_formatter(record):
            message = record.getMessage()
            colored_message = self._colorize_message(record.levelname, message)
            return colored_message

        # Přiřazení vlastní funkce pro formátování
        def log_func(levelname, msg):
            log_method = getattr(logger, levelname.lower())
            log_method(custom_formatter(logger.makeRecord(logger.name, logging._levelNames[levelname], None, None, msg, None, None)))

        # Nastavení záznamů
        return logger


# Příklad použití
if __name__ == "__main__":
    log_manager = ConfigLogManager()
    logger = log_manager.get_logger()

    logger.debug(
                f"for validate key and value: \n"
                f"Neplatný klíč: key. "
                f"Klíč není součástí defaultní konfigurace. \n"
                f"Možnosti: options"
            )
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")