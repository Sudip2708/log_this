# cli_styler/mixins/_get_current_ids.py
from abc import ABC


class GetCurrentIdsMixin(ABC):
    """
    Mixin přidávající metody a atributy třídě CLIStyler.

    Jedná se o atributy definující možnosti pro zobrazení značek a barev,
    a atributy definující aktuálně vybrané možnosti,
    a metodu vracející tuple s hodnotami aktuálně vybraných možnosti.
    """

    # Atributy pro slovník defuinující možnosti pro zobrazení značek
    _symbols_modes = {"native": None, "set_a": 0, "set_b": 1}

    # Atribut definující aktuálně používaný set značek
    _current_symbols_mode  = "set_a"

    # Atributy pro slovník defuinující možnosti pro zobrazení barevného modu
    _colors_modes = {"native": None, "dark": 0, "light": 1}

    # Atribut definující aktuálně používaný barevný mod
    _current_colors_mode = "dark"

    def get_current_symbols_mode(self):
        return self._current_symbols_mode

    def get_current_colors_mode(self):
        return self._current_colors_mode

    def get_symbols_modes_dict(self):
        return self._symbols_modes

    def get_colors_modes_dict(self):
        return self._colors_modes

    def _get_current_ids(self):
        """
        Metoda vrátí id pro aktuálně vybranou sadu znaků a barevný mod

        Metoda na základě atribtutů _current_symbols_mode a _current_colors_mode,
        které obsahují slovní definici vybraného atributu,
        vrátí jeho id reprezentaci a nebo hodnotu None,
        pokud je vybráno nativní zobrazení bez použití značek,
        nebo barevného modu.
        """

        # Načtení hodnoty pro značky
        signs_set_id = self._symbols_modes[self._current_symbols_mode]

        # Načtení hodnoty pro barvný režim
        colors_mode_id = self._colors_modes[self._current_colors_mode]

        # Navrácení tuple s id hodnotami (značka, barevný režim)
        return signs_set_id, colors_mode_id





