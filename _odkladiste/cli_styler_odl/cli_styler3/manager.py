from .cli_styler import CLIStyler
from .cli_printer import CLIPrinter

from ..abc_helper import AbcSingletonMeta
from ._get_mode_mixin import GetModeMixin
from ._get_sign_set_mixin import GetSignSetMixin

class Manager(
    GetModeMixin,
    GetSignSetMixin,
    metaclass=AbcSingletonMeta
):

    # Definice singletonu
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.colors = self.get_sign_set("set_a")
            self.signs = self.get_mode("dark")
            self.styler = CLIStyler(self.signs, self.colors)
            self.printer = CLIPrinter(self.styler)
            self._initialized = True

    # Metoda pro změnu modu
    def set_mode(self, mode):
        """
        Metoda pro změnu barevného modu

        Metoda nejprve se pokusí změnit barevný mod ve třídě CLIColor
        - pokud bude zadaný neplatný barevný mod metoda change_mode vyvolá výjimku

        Následně metoda spustí metodu pro změnu hodnot atributů této třídy
        """
        self.colors = self.get_mode(mode)
        self._apply_changes()

    # Metoda pro změnu značek
    def set_sign_set(self, sign_set):
        """
        Metoda pro změnu barevného modu

        Metoda nejprve se pokusí změnit sadu znaků ve třídě CLISigns
        - pokud bude zadat neplatný set metoda change_sign_set vyvolá výjimku

        Následně metoda spustí metodu pro změnu hodnot atributů této třídy
        """
        self.signs = self.get_sign_set(sign_set)
        self._apply_changes()

    # Pomocná metoda pro plykování změn
    def _apply_changes(self):
        """Pomocná metoda pro provedení změn v celém styleru"""
        self.styler.set_styler_attributes(self.signs, self.colors)
        self.printer.set_printer_attributes(self.styler)


