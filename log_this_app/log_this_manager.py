from cli_styler import CliStyler
from config_manager import ConfigManager
from cli_interactive import run_interactive_menu


class LogThisManager:
    """Hlavní mabnager knihovny log_this"""

    def __init__(self):

        # Inicializace singleton instance styleru
        # Používá se napříč aplikací pro ostylování výstupu
        CliStyler()

        # Inicializace konfigurace
        self.config_manager = ConfigManager()

        # Inicializace interaktivního modu
        self.interactive_run = run_interactive_menu

