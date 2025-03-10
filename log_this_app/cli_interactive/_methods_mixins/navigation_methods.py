# print("_methods_mixins/navigation_methods.py")
from abc import ABC

from abc_helper import abc_property

class NavigationMethodsMixin(ABC):
    """Mixin přidávající atribut a metody navigaci v interaktivním menu"""

    # Atribut pro instanci MenuRenderer
    menu_renderer = abc_property("menu_renderer")

    # Atribut pro data aktuálního menu
    menu = abc_property("menu")

    # Atribut pro hodnotu aktuálně vybrané nabídky
    current_selection = abc_property("current_selection")


    def go_up(self):
        """Posune výběr nahoru"""

        # Příprava hodnot
        first_item_id = 0
        previous_item_id = self.current_selection - 1

        # Přiřazení vyšší hodnoty do atributu pro vybranou nabídku
        self.current_selection = max(first_item_id, previous_item_id)

        # Aktualizace zobrazení
        self.menu_renderer.refresh()


    def go_down(self):
        """Posune výběr dolů"""

        # Příprava hodnot
        items_count = len(self.menu.items)
        last_item_id = items_count - 1
        next_item_id = self.current_selection + 1

        # Přiřazení nižší hodnoty do atributu pro vybranou nabídku
        self.current_selection = min(last_item_id, next_item_id)

        # Aktualizace zobrazení
        self.menu_renderer.refresh()


    def run_current_selection(self):
        """Spustí metodu navázanou na vybraný úkon"""

        # Spustí akci definovanou v aktuální položce
        self.menu.items[self.current_selection][1]()
