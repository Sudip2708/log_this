from abc import ABC

from abc_helper import abc_property
from texts import HELP_INSTRUCTION, get_help_instruction
from cli_styler import END_LINE, DROPDOWN, SELECTED, UNSELECTED

class GetMenuTextMixin(ABC):

    # Atribut pro zaznamenání nadpisu zobrazeného menu
    menu_title = abc_property("menu_title")

    # Atribut pro zaznamenání položek zobrazeného menu
    menu_items = abc_property("menu_items")

    # Atribut pro zaznamenání zda se mají zobrazit instrukce k ovládání
    show_instruction = abc_property("show_instruction")

    # Atribut pro zaznamenání vybrané položky
    current_selection = abc_property("current_selection")


    def get_menu_text(self):
        """Vrací naformátovaný text pro menu"""

        # Seznam pro výsledné řetězce
        lines = []

        # Zobrazení nápovědy (je-li aktivní)
        if self.show_instruction:
            lines.extend(get_help_instruction())

        # Přídání nadpisu (je-li)
        if self.menu_title:
            lines.append(set_menu_title(self.menu_title))

        # Cyklus pro přidání položek menu
        for i, (text, _) in enumerate(self.menu_items):
            lines.append(
                set_menu_selected_offer(text)
                if i == self.current_selection
                else set_menu_offer(text)
            )

        return lines

def set_menu_title(title):
    return "class:menu.title", f"{DROPDOWN}{title}{END_LINE}"

def set_menu_selected_offer(text):
    return "class:menu.focus", f"{SELECTED}{text}{END_LINE}"

def set_menu_offer(text):
    return "class:menu.offer", f"{UNSELECTED}{text}{END_LINE}"