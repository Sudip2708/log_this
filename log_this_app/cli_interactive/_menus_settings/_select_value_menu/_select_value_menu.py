from functools import partial
from typing import Dict, Optional, List, Tuple

from .._base_menu import BaseMenu


class SelectValueMenu(BaseMenu):
    """
    Obecné menu pro výběr hodnoty konfiguračního klíče.

    Dynamicky generuje položky menu na základě dostupných hodnot pro vybraný klíč.
    """

    # Definice základních atributů menu
    menu_name: Optional[str] = None
    _menu_key: Optional[str] = None
    _previous_menu_key: Optional[str] = None

    @property
    def title(self) -> str:
        """
        Vrací nadpis menu.

        :return: Název menu.
        :raises ValueError: Pokud není vybrán žádný klíč.
        """
        if not self.mm.selected_key:
            raise ValueError("Není zadán klíč, pro který se má zadat hodnota")
        return self.menu_name

    @property
    def menu_items(self) -> List[Tuple[str, callable]]:
        """
        Vrací seznam položek dostupných v menu pro výběr hodnoty.

        :return: Seznam dvojic obsahujících název a metodu spuštění.
        """
        return [
            self.get_help_offer(),
            *self._get_items_offer(),
            self.get_previous_menu(),
            self.get_close_offer(),
        ]

    @property
    def _mode_class(self):
        """
        Vrací třídu obsahující data vybraného klíče.

        :return: Třída s definicí hodnot pro vybraný klíč.
        """
        return self._items_manager.KEYS_DATA[self.mm.selected_key]

    @staticmethod
    def _get_label(label: str, value: str, default_value: str,
                  actual_value: str) -> str:
        """
        Vrací formátovaný label pro danou hodnotu.

        :param label: Název hodnoty.
        :param value: Hodnota.
        :param default_value: Výchozí hodnota.
        :param actual_value: Aktuální nastavená hodnota.
        :return: Formátovaný název hodnoty.
        """
        return (
                f"• {label}"
                + (" (default)" if value == default_value else "")
                + (" (selected)" if value == actual_value else "")
        )

    def _get_items_offer(self) -> Tuple[Tuple[str, callable], ...]:
        """
        Vytvoří seznam položek pro výběr hodnoty.

        :return: N-tice obsahující názvy a metody pro změnu hodnoty.
        """
        values_dict = self._mode_class.VALUES_DICT
        default_value = self._mode_class.DEFAULT_VALUE
        actual_value = self._config_manager.config.get(self.mm.selected_key)
        return tuple(
            (
                self._get_label(label, value, default_value, actual_value),
                partial(self._request_processing, value)
            )
            for value, label in values_dict.items()
        )

    def _request_processing(self, value: str) -> None:
        """
        Zpracuje požadavek na změnu hodnoty.

        :param value: Vybraná hodnota.
        """
        if value == "input":
            self.mm.response = "input_int_value"
            self.mm.exit_menu()
        else:
            self.mm.selected_value = value
            self._config_manager.change_value(
                self.mm.selected_key,
                self.mm.selected_value
            )
            self.mm.exit_menu()
