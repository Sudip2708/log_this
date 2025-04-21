# print("_menus_settings/_key_and_value_config/config_menu.py")
from functools import partial
from typing import Dict, Optional, List, Tuple
from .._base_menu import BaseMenu

class ExportMenu(BaseMenu):
    """
    Menu pro možnosti exportování konfigurace do externího souboru.

    Poskytuje volby pro zpúsob výběru tohoto souboru.
    """

    # Definice názvu a klíčů menu
    menu_name = "Menu pro export konfigurace"
    _menu_key = "export_menu"
    _previous_menu_key = "import_export_menu"

    # Definice dostupných položek menu
    _item_texts: Dict[str, Dict[str, str]] = {
        "dialog_export_directory_path": {
            "label": "Výběr složky skrze souborové okno",
            "help": "Otevře souborového managera pro výběr cesty "
                    "ke složky pro uložení aktuální konfigurace.",
        },
        "dialog_export_file_path": {
            "label": "Výběr skrze souborové okno s definicí jména",
            "help": "Otevře souborového managera pro výběr cesty "
                    "s možností definovat vlastní jméno souboru "
                    "pro uložení aktuální konfigurace.",
        },
        "input_export_directory_path": {
            "label": "Ruční zadání cesty k složce",
            "help": "Nabídne možnost ručního zadání cesty "
                    "ke složce pro uložení aktuální konfigurace.",
        },
        "input_export_file_path": {
            "label": "Ruční zadání cesty s definicí jména souboru",
            "help": "Nabídne možnost ručního zadání cesty "
                    "s možností definovat vlastní jméno souboru "
                    "pro uložení aktuální konfigurace.",
        },
    }

    @property
    def menu_items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v menu pro exposr konfigurace.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            self.get_response_offer("dialog_export_directory_path"),
            self.get_response_offer("dialog_export_file_path"),
            self.get_response_offer("input_export_directory_path"),
            self.get_response_offer("input_export_file_path"),
            self.get_previous_menu(),
            self.get_close_offer(),
        ]

