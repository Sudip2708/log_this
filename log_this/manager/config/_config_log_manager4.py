import logging
from rich.logging import RichHandler


class ConfigLogManager:
    """Třída pro správu logování s použitím Rich pro barevné výstupy"""

    def __init__(self):
        # Vytvoření loggeru
        self.logger = logging.getLogger('LogThisConfig')
        self.logger.setLevel(
            logging.DEBUG)  # Nastavení minimální úrovně logování

        # Nastavení Rich handleru pro barevné logy
        console_handler = RichHandler(rich_tracebacks=True)

        # Nastavení formátování logů (formát bez času, úroveň a zpráva)
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Přidání handleru do loggeru
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """Vrátí loger pro aplikaci"""
        return self.logger


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