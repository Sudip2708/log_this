# file: cli_styler.py
from ..abc_helper import AbcSingletonMeta
from ._style_class import StyleClass
from .utils import get_class_attributes_set, attributes_check
from .settings import get_styles_dict


class CLIStyler(metaclass=AbcSingletonMeta):
    """Třída obsahující definice všech stylů s kontrolou konzistence."""

    # Úvod a ukončení interaktivního režimu
    intro_title = None
    intro_end = None

    # Položky pro interaktivní menu
    menu_title = None
    menu_offer = None
    menu_selected = None

    # Položky nápovědy pro ovládání interaktivního menu
    hint_title = None
    hint_offer = None

    # Chybové oznamy
    error_title = None
    error_text = None

    # Varování
    warning_title = None
    warning_text = None
    warning_direction = None

    # Informativní oznamy
    info_title = None
    info_text = None

    # Oznamy o úspěchu
    success_title = None
    success_text = None

    # Styl pro vstupní pole
    prompt_input = None

    # Nastavení značek
    _signs_sets = {"native": 0, "set_a": 1, "set_b": 2}
    _current_signs_set  = "set_b"

    # Nastavení barevného modu
    _colors_modes = {"native": 0, "light": 1, "dark": 2}
    _current_colors_mode = "dark"

    def __init__(self):
        """Dinamické načtení atributů a inicializace singleton vzoru"""
        if not hasattr(self, "_initialized"):
            self.get_current_styles_attributes()
            self._initialized = True

    def get_current_styles_dict(self):
        """Metoda pro získání ID vybraného barevného režimu a sady značek"""
        sings_id = self._signs_sets[self._current_signs_set],
        colors_id = self._colors_modes[self._current_colors_mode]
        return get_styles_dict(sings_id, colors_id)

    def get_style_attributes_set(self):
        """
        Metoda pro vytvoření množiny atributů pro styly definované v této třídě

        # Načtení třídních metod a atributů
        # Odstranění atributů začínajících podtržítkem
        # Ujistíme se, že `init` není součástí
        """
        return {key for key in dir(self)
                if not key.startswith("_")
                and key != "init"}

    @staticmethod
    def raise_attributes_error(attributes_set, styles_set):
        message = "Neshoda mezi definovanými styly a atributy třídy CLIStyler\n"
        excess = attributes_set - styles_set
        message += f"Nadytečné atributy třídy CLIStyler: {excess}\n" if excess else ""
        missing = styles_set - attributes_set
        message += f"Chybějící atributy třídy CLIStyler: {missing}\n" if missing else ""
        raise ValueError(message)

    def check_style_attributes(self, styles_dict):
        """
        Metoda pro kontzrolu atributů

        # Získáme seznam atributů třídy (jen ty, které jsou relevantní)
        # Seznam dostupných stylů ve slovníku
        # Kontrola zda se shodují
        """
        attributes_set = self.get_style_attributes_set()
        styles_set = set(styles_dict.keys())
        if attributes_set != styles_set:
            self.raise_attributes_error(attributes_set, styles_set)

    def set_style_attributes(self, styles_dict):
        """Metoda pro dianmické přidání/přepsání atributů"""
        for key, (symbol, style) in styles_dict.items():
            setattr(self, key, StyleClass(symbol, style))

    def validate_colors_mode(self, colors_mode):
        """Metoda pro validaci barevného režimu"""
        if not colors_mode in self._colors_modes.keys():
            raise ValueError(f"Byl zadán neplatný set barvy. "
                             f"Povolené sety: {self._colors_modes.keys()}")

    def set_colors_mode(self, colors_mode):
        """
        Metoda pro změnu barevného modu

        Metoda nejprve se pokusí změnit barevný mod ve třídě CLIColor
        - pokud bude zadaný neplatný barevný mod metoda change_mode vyvolá výjimku

        Následně metoda spustí metodu pro změnu hodnot atributů této třídy
        """
        self.validate_colors_mode(colors_mode)
        self._current_colors_mode = self._colors_modes[colors_mode]
        self.get_current_styles_attributes()

    def validate_signs_set(self, signs_set):
        """Metoda pro validaci setu značek"""
        if not signs_set in self._signs_sets.keys():
            raise ValueError(f"Byl zadán neplatný set pro značky. "
                             f"Povolené sety: {self._signs_sets.keys()}")

    def set_sign_set(self, signs_set):
        """
        Metoda pro změnu barevného modu

        Metoda nejprve se pokusí změnit sadu znaků ve třídě CLISigns
        - pokud bude zadat neplatný set metoda change_sign_set vyvolá výjimku

        Následně metoda spustí metodu pro změnu hodnot atributů této třídy
        """
        self.validate_signs_set(signs_set)
        self._current_signs_set = self._signs_sets[signs_set]
        self.get_current_styles_attributes()

    def get_current_styles_attributes(self):
        """Pomocná metoda pro provedení změn v celém styleru"""
        styles_dict = self.get_current_styles_dict()
        self.check_style_attributes(styles_dict)
        self.set_style_attributes(styles_dict)






# Vytvoření instance CLIStyler
cs = CLIStyler()
# Vytvoření stylerů
# Printy
print_intro_title = cs.intro_title.print_styled
print_intro_end = cs.intro_end.print_styled

print_error_title = cs.error_title.print_styled
print_error_text = cs.error_text.print_styled

print_warning_title = cs.warning_title.print_styled
print_warning_text = cs.warning_text.print_styled
print_warning_direction = cs.warning_direction.print_styled

print_info_title = cs.info_title.print_styled
print_info_text = cs.info_text.print_styled

print_success_title = cs.success_title.print_styled
print_success_text = cs.success_text.print_styled

# Styly
get_menu_title = cs.menu_title.get_styled
get_menu_offer = cs.menu_offer.get_styled
get_menu_selected = cs.menu_selected.get_styled

get_hint_title = cs.hint_title.get_styled
get_hint_offer = cs.hint_offer.get_styled

get_prompt_input = cs.prompt_input.get_styled

