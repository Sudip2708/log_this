from abc import ABC
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

from abc_helper import abc_method


class StylePrintMixin(ABC):
    """
    Mixin přidávající metodu třídě StyleClass.

    Jedná se o metodu pro vytištění naformátovaného textu.
    """

    # Interní metody použité v tomto mixinu (musí být již definované)
    style_get = abc_method("style_get")

    def style_print(self, text: str):
        """
        Metoda vytiskne ostylovaný text do konzole.

        Metoda nejprve volá metodu get_styled,
        pro načtení tuple obsahující styl a doplněný text.
        Tuple je pak předáno do metody FormattedText z knihovny prompt_toolkit,
        a následně je tento naformátovaný text vytisknut do konzole přes metodu
        print_styled_formatted_text z knihovny prompt_toolkit.
        """

        # Vytvoření formátovaného textu
        formatted_text = FormattedText([
            self.style_get(text)
        ])

        # Tisk formátovaného textu
        print_formatted_text(formatted_text)

print_formatted_text(FormattedText(["text"]))