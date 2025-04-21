from typing import Dict, Optional, List, Tuple

from .._base_menu import BaseMenu


class ImportMenu(BaseMenu):
    """
    Menu pro možnosti importování konfigurace z externího souboru.

    Poskytuje volby pro zpúsob výběru tohoto souboru.
    """

    # Definice názvu a klíčů menu
    menu_name = "Menu pro import konfigurace"
    _menu_key = "import_menu"
    _previous_menu_key = "import_export_menu"

    # Definice dostupných položek menu
    _item_texts: Dict[str, Dict[str, str]] = {
        "dialog_import_file_path": {
            "label": "Výběr souboru skrze souborové okno",
            "help": "Otevře souborového managera pro výběr cesty "
                    "k souboru .json s uloženou konfigurací.",
        },
        "input_import_file_path": {
            "label": "Ruční zadání cesty k souboru",
            "help": "Nabídne možnost ručního zadání cesty k souboru .json "
                    "s uloženou konfigurací.",
        },
    }

    @property
    def menu_items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v menu pro import konfigurace.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            self.get_response_offer("dialog_import_file_path"),
            self.get_response_offer("input_import_file_path"),
            self.get_previous_menu(),
            self.get_close_offer(),
        ]

