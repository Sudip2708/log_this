from abc import ABC

from abc_helper import abc_property


class RunMethodsMixin(ABC):
    """
    Mixin přidávající běhové metody interaktivního menu.

    Atributy:
        menu_app (Application): Instance interaktivního menu.
    """

    # Atribut třídy MenuRenderer pro instanci CLI aplikace
    menu_app = abc_property("menu_app")

    def run(self) -> None:
        """Spustí interaktivní menu."""
        self.menu_app.run()

    def refresh(self) -> None:
        """Aktualizuje zobrazení menu."""
        self.menu_app.invalidate()  # Znovu překreslí obsah

    def exit(self) -> None:
        """Ukončí aplikaci."""
        self.menu_app.exit()

    def is_running(self) -> bool:
        """
        Vrátí True, pokud je interaktivní menu spuštěné.

        Returns:
            bool: True, pokud je menu spuštěné, jinak False.
        """
        return not self.menu_app.future.done()

