from typing import Dict, Optional, List, Tuple

from .._base_menu import BaseMenu


class ConfigMenu(BaseMenu):
    """
    Konfigurační menu aplikace.

    Poskytuje přístup k nastavení různých aspektů knihovny log_this.
    """

    # Definice názvu a klíčů menu
    menu_name: str = "Konfigurační menu"
    _menu_key: str = "config_menu"
    _previous_menu_key: Optional[str] = "main_menu"

    # Definice dostupných položek menu
    _item_texts: Dict[str, Dict[str, str]] = {
        "select_key_menu_modes": {
            "label": "Nastavit chování módů",
            "help": "Přístup k menu pro nastavení módů knihovny log_this.",
        },
        "select_key_menu_aspects": {
            "label": "Nastavit výstup",
            "help": "Přístup k menu pro nastavení výstupu knihovny log_this.",
        },
        "reset_config_menu": {
            "label": "Reset nastavení",
            "help": "Přístup k menu pro reset konfigurace knihovny log_this.",
        },
    }

    @property
    def menu_items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v konfiguračním menu.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            self.get_menu_offer("select_key_menu_modes"),
            self.get_menu_offer("select_key_menu_aspects"),
            self.get_menu_offer("reset_config_menu"),
            self.get_previous_menu(),
            self.get_close_offer(),
        ]
