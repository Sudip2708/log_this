from typing import Dict, Optional, List, Tuple

from .._base_menu import BaseMenu


class ImportExportMenu(BaseMenu):
    """
    Menu pro možnosti import a export konfigurace.

    Poskytuje volby pro importování konfigurace z externího souboru,
    a pro expostování konfigurace do vlastního souboru.
    """

    # Definice názvu a klíčů menu
    menu_name: str  = "Menu pro import a export konfigurace"
    _menu_key: str  = "import_export_menu"
    _previous_menu_key: Optional[str] = "main_menu"

    # Definice dostupných položek menu
    _menu_items = {
        "import_menu": {
            "label": "Možnosti pro import konfigurace",
            "help": "Přístup k menu pro import konfigurace "
                    "pro knihovnu log_this ze souboru .json.",
        },
        "export_menu": {
            "label": "Možnosti pro export konfigurace",
            "help": "Přístup k menu pro export aktuální konfigurace "
                    "do souboru .json.",
        },

    }

    @property
    def items(self):
        """
        Vrací seznam položek dostupných v menu pro reset konfigurace.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            self.get_menu_offer("import_menu"),
            self.get_menu_offer("export_menu"),
            self.get_previous_menu(),
            self.get_close_offer(),
        ]


