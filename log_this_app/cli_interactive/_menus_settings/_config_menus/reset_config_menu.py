from typing import Dict, Optional, List, Tuple

from .._base_menu import BaseMenu


class ResetConfigMenu(BaseMenu):
    """
    Menu pro možnosti resetu konfigurace.

    Poskytuje volby pro návrat k předchozímu nebo výchozímu nastavení konfigurace.
    """

    # Definice názvu a klíčů menu
    menu_name: str = "Menu pro možnosti resetu konfigurace"
    _menu_key: str = "reset_config_menu"
    _previous_menu_key: Optional[str] = "config_menu"

    # Definice dostupných položek menu
    _menu_items: Dict[str, Dict[str, str]] = {
        "reset_to_previous": {
            "label": "Resetovat na předchozí nastavení",
            "help": "Provede reset konfigurace na předchozí konfiguraci.",
        },
        "reset_to_default": {
            "label": "Resetovat na defaultní nastavení",
            "help": "Provede reset konfigurace na výchozí hodnoty.",
        },
    }

    @property
    def items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v menu pro reset konfigurace.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            self.get_response_offer("reset_to_previous"),
            self.get_response_offer("reset_to_default"),
            self.get_previous_menu(),
            self.get_close_offer(),
        ]

    def _response_action(self, item_key: str) -> None:
        """
        Zpracuje vybranou akci resetu konfigurace a ukončí menu.

        :param item_key: Klíč vybrané akce resetu.
        """
        if item_key == "reset_to_previous":
            self.mm.config_manager.reset_to_previous_configuration()
        elif item_key == "reset_to_default":
            self.mm.config_manager.reset_to_default_configuration()

        self.mm.exit_menu()
