from ._get_menu_text_methods_mixin import GetMenuMethodsMixin


class GetMenuText(

    GetMenuMethodsMixin

):
    """Mixin pro spuštění, ukončení a obnovení interaktivního menu"""


    def __init__(self, cli):

        # Načtení instance hlvní třídy
        self.cli = cli

        # Získání aktuálního menu
        self.menu = self.cli.menu

        # Získání id pro aktuálně vybraný řádek
        self.selected_line_id = self.cli.current_selection

        # Vytvoření prázdného seznamu pro položky k zobrazení
        self.lines = []

    def get_menu_text(self):
        """Vrací naformátovaný text pro zobrazení menu"""

        # Zobrazení nápovědy (je-li aktivní)
        self._get_help()

        # Přidání nadpisu (je-li)
        self._get_menu_title()

        # Přidání položek menu
        self._get_menu_items()

        return self.lines