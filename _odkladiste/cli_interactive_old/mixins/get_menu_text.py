from abc import ABC, abstractmethod

from config.help_instructions import HELP_INSTRUCTION


class GetMenuText(ABC):

    @property
    @abstractmethod
    def menu_title(self):
        pass

    @property
    @abstractmethod
    def menu_items(self):
        pass

    @property
    @abstractmethod
    def show_help(self):
        pass

    @property
    @abstractmethod
    def current_selection(self):
        pass

    def get_menu_text(self):
        """
        Funkce vrátí hlavní menu

        menu_items: seznam položek k zobrazení
        """

        # Seznam pro výsledné řetězce
        lines = []

        # Pokud je požadavek i pro nápovědu
        # (Přideání textu nápovědy)
        if self.show_help:
            lines.extend(HELP_INSTRUCTION)

        # Kontrola zde je použit i nadpis pro menu
        # (Přidání nadpisu)
        if self.menu_title:
            lines.append(("class:selection.title", f"{self.menu_title}\n"))

        # Cyklus pro přidání položek menu
        for i, (text, _) in enumerate(self.menu_items):

            # Pokud je položka i aktuálně vybranou
            # (Zobrazení reverzně a se šipkou)
            if i == self.current_selection:
                lines.append(('class:reverse', f'> {text}\n'))

            # Ve všech ostatních případech
            # (Zobrazení normálně a bez šipky)
            else:
                lines.append(('', f'  {text}\n'))

        return lines