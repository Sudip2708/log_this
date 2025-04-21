from functools import partial
from typing import Dict, Optional, List, Tuple

from .._base_menu import BaseMenu


class SelectKeyMenu(BaseMenu):
    """
    Obecné menu pro výběr klíče konfigurace.

    Dynamicky generuje položky menu na základě dostupných klíčů v dané kategorii.
    """

    # Definice základních atributů menu
    menu_name: Optional[str] = None
    _menu_key: Optional[str] = None
    _previous_menu_key: Optional[str] = None
    _category: Optional[str] = None
    _next_menu: Optional[str] = None

    @property
    def _item_texts(self) -> Dict[str, Dict[str, str]]:
        """
        Dynamicky vytváří položky menu na základě dostupných klíčů v dané kategorii.

        :return: Slovník obsahující klíče a jejich popisy.
        """
        category_dict = self._items_manager.get_category_dict(self._category)
        return {
            key: {"label": key_class.LABEL, "help": key_class.INFO}
            for key, key_class in category_dict.items()
        }

    @property
    def menu_items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v menu pro výběr klíče.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            *self._get_items_offers(),
            self.get_previous_menu(),
            self.get_close_offer(),
        ]

    def _get_items_offers(self) -> Tuple[Tuple[str, callable], ...]:
        """
        Vytvoří seznam položek pro výběr klíče.

        :return: N-tice obsahující názvy a metody pro nastavení hodnoty.
        """
        return tuple(
            (f"• {item['label']}", partial(self._set_new_value, key))
            for key, item in self._item_texts.items()
        )

    def _set_new_value(self, key: str) -> None:
        """
        Uloží vybraný klíč a přepne na výběr hodnoty.

        :param key: Vybraný klíč konfigurace.
        """
        self.mm.selected_key = key
        self.mm.show_menu(self._next_menu)
