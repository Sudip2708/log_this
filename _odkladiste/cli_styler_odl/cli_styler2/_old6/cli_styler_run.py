from .signs.cli_sings import CLISigns
from .colors.cli_colors import CLIColors
from ._cli_styles_base import CLIStylesBase
from ._cli_styler import CLIStyler
from ._cli_printer import CLIPrinter

from ..abc_helper import AbcSingletonMeta

class CLIStylerRun(metaclass=AbcSingletonMeta):

    # Definice singletonu
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialize()
            self._initialized = True

    def _initialize(self):
        self.cli_colors = CLIColors()
        self.cli_signs = CLISigns()
        self.cli_styles = CLIStylesBase(self.cli_signs, self.cli_colors)
        self.cli_styler = CLIStyler(self.cli_styles)
        self.cli_printer = CLIPrinter(self.cli_styler)

    def set_mode(self, mode):
        """
        Metoda pro změnu barevného modu

        Metoda nejprve se pokusí změnit barevný mod ve třídě CLIColor
        - pokud bude zadaný neplatný barevný mod metoda change_mode vyvolá výjimku

        Následně metoda spustí metodu pro změnu hodnot atributů této třídy
        """
        self.cli_colors.change_mode(mode)
        self._apply_changes()

    def set_sign_set(self, sign_set):
        """
        Metoda pro změnu barevného modu

        Metoda nejprve se pokusí změnit sadu znaků ve třídě CLISigns
        - pokud bude zadat neplatný set metoda change_sign_set vyvolá výjimku

        Následně metoda spustí metodu pro změnu hodnot atributů této třídy
        """
        self.cli_signs.change_sign_set(sign_set)
        self._apply_changes()

    def _apply_changes(self):
        """Pomocná metoda pro provedení změn v celém styleru"""
        self.cli_styles.set_style_attributes(self.cli_signs, self.cli_colors)
        self.cli_styler.set_styler_attributes(self.cli_styles)
        self.cli_printer.set_printer_attributes(self.cli_styler)

# Vytvoření instance CLIStyler
cs = CLIStylerRun()
cli_print = cs.cli_printer
cli_style = cs.cli_styler

# Vytvoření stylerů
# Printy
print_intro_title = cli_print.intro_title
print_intro_end = cli_print.intro_end

print_error_title = cli_print.error_title
print_error_text = cli_print.error_text

print_warning_title = cli_print.warning_title
print_warning_text = cli_print.warning_text
print_warning_direction = cli_print.warning_direction

print_info_title = cli_print.info_title
print_info_text = cli_print.info_text

print_success_title = cli_print.success_title
print_success_text = cli_print.success_text

# Styly
get_menu_title = cli_style.menu_title
get_menu_offer = cli_style.menu_offer
get_menu_selected = cli_style.menu_selected

get_hint_title = cli_style.hint_title
get_hint_offer = cli_style.hint_offer

get_prompt_input = cli_style.prompt_input