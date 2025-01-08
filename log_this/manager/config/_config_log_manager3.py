import logging

# ANSI kódy pro barvy
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"


class ConfigLogManager:
    """Třída pro správu logování"""

    def __init__(self):
        self.logger = logging.getLogger('LogThisConfig')
        self.logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()

        # Funkce pro přiřazení barvy na základě úrovně logu
        def colorize(levelname):
            if levelname == "ERROR":
                return RED
            elif levelname == "WARNING":
                return YELLOW
            elif levelname == "INFO":
                return GREEN
            elif levelname == "DEBUG":
                return BLUE
            return RESET

        # Přidání ANSI kódů pro barvy do formátu
        formatter = logging.Formatter(
            f"{colorize('%(levelname)s')}%(levelname)s{RESET} - %(message)s"
        )

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
                f"Neplatný klíč: key. "
                f"Klíč není součástí defaultní konfigurace. \n"
                f"Možnosti: options"
            )
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
