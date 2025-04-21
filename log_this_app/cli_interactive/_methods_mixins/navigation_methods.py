# print("_methods_mixins/navigation_methods.py")
from abc import ABC

from abc_helper import abc_property

class NavigationMethodsMixin(ABC):
    """Mixin přidávající atribut a metody navigaci v interaktivním menu"""

    # Atribut pro instanci MenuRenderer
    menu_renderer = abc_property("menu_renderer")

    # Atribut pro data aktuálního menu
    current_menu = abc_property("current_menu")

    # Atribut pro hodnotu aktuálně vybrané nabídky
    selected_item_id  = abc_property("selected_item_id ")


    def go_up(self):
        """Posune výběr nahoru"""

        # Příprava hodnot
        first_item_id = 0
        previous_item_id = self.selected_item_id  - 1

        # Přiřazení vyšší hodnoty do atributu pro vybranou nabídku
        self.selected_item_id  = max(first_item_id, previous_item_id)

        # Aktualizace zobrazení
        self.current_menu.refresh()


    def go_down(self):
        """Posune výběr dolů"""

        # Příprava hodnot
        items_count = len(self.current_menu.menu_items)
        last_item_id = items_count - 1
        next_item_id = self.selected_item_id  + 1

        # Přiřazení nižší hodnoty do atributu pro vybranou nabídku
        self.selected_item_id  = min(last_item_id, next_item_id)

        # Aktualizace zobrazení
        self.current_menu.refresh()


    def run_selected_item_id (self):
        """Spustí metodu navázanou na vybraný úkon"""

        # Spustí akci definovanou v aktuální položce
        self.current_menu.menu_items[self.selected_item_id ][1]()
