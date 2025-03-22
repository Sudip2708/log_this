from functools import partial
from typing import Dict, Optional, List, Tuple

from .._base_menu import BaseMenu


class ExitMenu(BaseMenu):
    """
    Ukončovací menu aplikace.

    Poskytuje možnost ukončení interaktivního režimu nebo návratu do hlavního menu.
    """

    # Definice názvu a klíčů menu
    menu_name: str = "Ukončovací menu"
    _menu_key: str = "exit_menu"
    _previous_menu_key: Optional[str] = None

    # Definice dostupných položek menu
    _menu_items: Dict[str, Dict[str, str]] = {
        "main_menu": {
            "label": "Pokračovat v interaktivním režimu",
            "help": "Návrat do hlavního menu interaktivního režimu.",
        }
    }

    # Skrytí nadpisu menu
    title: Optional[str] = None

    @property
    def items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v ukončovacím menu.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_menu_offer("main_menu"),
            self.get_close_offer(),
        ]

    def get_menu_offer(self, item_key: str) -> Tuple[str, callable]:
        """
        Přetěžuje metodu pro přechod na jinou nabídku v menu.

        Dochází k odstranění tečky na začátku labelu.

        :param item_key: Klíč položky menu.
        :return: Dvojice obsahující text a metodu pro přepnutí na zvolené menu.
        """
        return (
            self._menu_items[item_key]["label"],
            partial(self.mm.show_menu, item_key)
        )