from abc import ABC

from abc_helper import abc_property
from zatributes import HELP_INSTRUCTION

class GetMenuText(ABC):

    # Atribut pro zaznamenání nadpisu zobrazeného menu
    menu_title = abc_property("menu_title")

    # Atribut pro zaznamenání položek zobrazeného menu
    menu_items = abc_property("menu_items")

    # Boolean atribut pro zobrazení instrukcí ovládání interaktivního menu
    show_instruction = abc_property("show_instruction")

    # Atribut pro zaznamenání vybrané položky
    current_selection = abc_property("current_selection")


    def get_menu_text(self):
        """Vrací naformátovaný text pro menu"""

        # Seznam pro výsledné řetězce
        lines = []

        # Zobrazení nápovědy (je-li aktivní)
        if self.show_instruction:
            lines.extend(HELP_INSTRUCTION)

        # Přídání nadpisu (je-li)
        if self.menu_title:
            lines.append(("class:selection.title", f"{self.menu_title}\n"))

        # Cyklus pro přidání položek menu
        for i, (text, _) in enumerate(self.menu_items):

            # Pokud je položka i aktuálně vybranou (zobrazení reverzně a se šipkou)
            if i == self.current_selection:
                lines.append(('class:selection.focus', f'» {text}\n'))

            # Ve všech ostatních případech (zobrazení normálně a bez šipky)
            else:
                lines.append(("class:selection.offer", f'  {text}\n'))

        return lines

