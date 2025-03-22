from typing import Dict, Optional, List, Tuple

from .._base_menu import BaseMenu


class ShowCategoryMenu(BaseMenu):
    """
    Menu pro výpis aktuální konfigurace dle kategorií.

    Poskytuje možnosti pro zobrazení konfigurace rozdělené podle jednotlivých kategorií.
    """

    # Definice názvu a klíčů menu
    menu_name: str = "Menu pro výpis aktuální konfigurace dle kategorií"
    _menu_key: str = "show_category_menu"
    _previous_menu_key: Optional[str] = "show_configuration_menu"

    # Definice dostupných položek menu
    _menu_items: Dict[str, Dict[str, str]] = {
        "log_this_modes": {
            "label": "Výpis pro mody @log_this",
            "help": "Vypíše aktuální konfiguraci s podrobnostmi "
                    "pro nastavení modů knihovny log_this.",
        },
        "log_this_aspects": {
            "label": "Výpis pro další nastavení @log_this",
            "help": "Vypíše aktuální konfiguraci s podrobnostmi "
                    "pro nastavení výstupů knihovny log_this.",
        },
        "interactive_cli": {
            "label": "Výpis pro nastavení vzhledu CLI",
            "help": "Vypíše aktuální konfiguraci s podrobnostmi "
                    "pro nastavení vzhledu interaktivního režimu.",
        },
    }

    @property
    def items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v menu pro výpis konfigurace dle kategorií.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            self.get_response_offer("log_this_modes"),
            self.get_response_offer("log_this_aspects"),
            self.get_response_offer("interactive_cli"),
            self.get_previous_menu(),
            self.get_close_offer(),
        ]

    def _response_action(self, item_key: str) -> None:
        """
        Spustí akci pro zobrazení konfigurace dané kategorie a ukončí menu.

        :param item_key: Klíč vybrané kategorie konfigurace.
        """
        self.mm.config_manager.print_category_configuration(item_key)
        self.mm.exit_menu()
