from cli_styler import CliStyler
from config_manager import ConfigManager
from cli_interactive import MenusManager
from log_this_manager_methods_mixin import LogThisManagerMethodsMixin

class LogThisManager(LogThisManagerMethodsMixin):
    """Hlavní mabnager knihovny log_this"""

    config_manager = None
    menus_manager = None

    def __init__(self):

        # Inicializace singleton instance styleru
        # (Používá se napříč aplikací pro ostylování výstupu)
        self.styler = CliStyler()

        # Inicializace konfigurace
        self.config_manager = ConfigManager(self)

        # Inicializace interaktivního menu
        self.menus_manager = MenusManager(self.config_manager)

        # Nastavení styleru
        self.styler_settings()


    def styler_settings(self):
        # Nastavení styleru
        self.styler.change_mode("colors", self.config_manager.config.get("colors"))
        self.styler.change_mode("symbols", self.config_manager.config.get("symbols"))
