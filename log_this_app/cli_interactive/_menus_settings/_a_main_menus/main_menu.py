from typing import Dict, List, Optional, Tuple

from .._base_menu import BaseMenu


class MainMenu(BaseMenu):
    """
    Hlavní menu aplikace.

    Poskytuje přístup k základním nastavením a konfiguraci aplikace.
    """

    # Definice názvu a klíčů menu
    menu_name: str = "Hlavní menu"
    _menu_key: str = "main_menu"
    _previous_menu_key: Optional[str] = None

    # Definice dostupných položek menu
    _item_texts: Dict[str, Dict[str, str]] = {
        "show_configuration_menu": {
            "label": "Zobrazit konfiguraci",
            "help": "Přístup k menu pro zobrazení aktuální konfigurace.",
        },
        "config_menu": {
            "label": "Nastavit konfiguraci",
            "help": "Přístup k menu pro změnu konfigurace.",
        },
        "import_export_menu": {
            "label": "Import/Export konfigurace",
            "help": "Přístup k menu pro import a export konfigurace.",
        },
        "select_key_menu_interactive": {
            "label": "Nastavení vzhledu interaktivního režimu",
            "help": "Přístup k menu pro nastavení vzhledu dialogových oken.",
        }
    }

    @property
    def menu_items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v hlavním menu.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            self.get_menu_offer("show_configuration_menu"),
            self.get_menu_offer("config_menu"),
            self.get_menu_offer("import_export_menu"),
            self.get_menu_offer("select_key_menu_interactive"),
            self.get_close_offer(),
        ]
