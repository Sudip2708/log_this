# print("_menu_render/_run_methods_mixins.py")
from abc import ABC

from abc_helper import abc_property

class RunMethodsMixin(ABC):
    """Mixin ppřidávající běhové metody interaktivního menu"""

    # Atribut pro instanci MenuRenderer
    menu_app = abc_property("menu_app")


    def run(self):
        """Spustí interaktivní menu"""
        self.menu_app.run()

    def refresh(self):
        """Aktualizuje zobrazení menu"""
        self.menu_app.invalidate()  # Znovu překreslí obsah

    def exit(self):
        """Ukončí aplikaci"""
        self.menu_app.exit()

    def is_running(self):
        """Vrátí True, pokud je interaktivní menu spuštěné"""
        return not self.menu_app.future.done()
        pass