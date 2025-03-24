from ._select_value_menu import SelectValueMenu
from cli_styler import styler


class SelectValueMenuInteractive(SelectValueMenu):
    """
    Menu pro nastavení vzhledu interaktivního režimu.

    Umožňuje změnu vzhledu CLI prostřednictvím výběru přednastavených stylů.
    """

    menu_name: str = "Menu pro nastavení vzhledu interaktivního režimu"
    _menu_key: str = "select_value_menu_interactive"
    _previous_menu_key: str = "select_key_menu_interactive"

    def _request_processing(self, value: str) -> None:
        """
        Zpracuje požadavek na změnu stylu interaktivního režimu.

        :param value: Vybraná hodnota stylu.
        """
        key = self.mm.selected_key

        # Změna stylu v cli_styler
        styler.change_mode(key, value)

        # Uložení změny do souboru, pokud je spravován
        if self._config_manager.file_manager:
            self._config_manager.change_value(key, value, silent=True)

        # Aktualizace výběru v menu
        option_id = self._config_manager.current_id(key)
        self.mm.current_selection = option_id + 1  # plus 1 kvůli položce nápovědy

        # Obnovení menu bez resetu pozice výběru
        self.mm.show_menu(self._menu_key, target_reset=False)


class SelectValueMenuModes(SelectValueMenu):
    """
    Menu pro nastavení módů logování.

    Poskytuje možnost změny úrovní a režimů logování aplikace.
    """

    menu_name: str = "Menu pro nastavení módů logování"
    _menu_key: str = "select_value_menu_modes"
    _previous_menu_key: str = "select_key_menu_modes"


class SelectValueMenuAspects(SelectValueMenu):
    """
    Menu pro nastavení aspektů logování.

    Umožňuje výběr specifických parametrů logování.
    """

    menu_name: str = "Menu pro nastavení aspektů logování"
    _menu_key: str = "select_value_menu_aspects"
    _previous_menu_key: str = "select_key_menu_aspects"
