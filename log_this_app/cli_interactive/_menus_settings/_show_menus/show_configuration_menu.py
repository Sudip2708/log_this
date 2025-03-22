from typing import Dict, Optional, List, Tuple

from .._base_menu import BaseMenu


class ShowConfigurationMenu(BaseMenu):
    """
    Menu s nabídkou pro výpis aktuální konfigurace.

    Poskytuje možnosti pro zobrazení konfigurace v různých úrovních detailu.
    """

    # Definice názvu a klíčů menu
    menu_name: str = "Menu s nabídkou pro výpis aktuální konfigurace"
    _menu_key: str = "show_configuration_menu"
    _previous_menu_key: Optional[str] = "main_menu"

    # Definice dostupných položek menu
    _menu_items: Dict[str, Dict[str, str]] = {
        "show_config_simple": {
            "label": "Stručný výpis",
            "help": "Vypíše aktuální konfiguraci.",
        },
        "show_category_menu": {
            "label": "Podrobný výpis s popisem",
            "help": "Přístup k menu pro výpis konfigurace s podrobnostmi.",
        },
    }

    @property
    def items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v menu pro výpis konfigurace.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            self.get_response_offer("show_config_simple"),
            self.get_menu_offer("show_category_menu"),
            self.get_previous_menu(),
            self.get_close_offer(),
        ]

    def _response_action(self, _: str) -> None:
        """
        Spustí akci pro zobrazení aktuální konfigurace a ukončí menu.

        Přetížení metody základní třídy BaseMenu.
        """
        self.mm.config_manager.print_actual_configuration()
        self.mm.exit_menu()
