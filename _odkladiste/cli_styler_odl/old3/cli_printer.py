from typing import Union, List, Tuple
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text

from abc_helper import AbcSingletonMeta
from .data.dialog_styles import DIALOG_STYLES
from .data.print_styles import PRINT_STYLES


class CliPrinter(metaclass=AbcSingletonMeta):


    def __init__(self):
        """Inicializuje styly pro tisk"""
        self.print_styles_dict = PRINT_STYLES
        self._print_style = Style.from_dict(self.print_styles_dict)
        self._dialog_style = Style.from_dict(DIALOG_STYLES)
        self._args = None

    @property
    def style(self):
        """Vrací styl pro dialogy"""
        return self._dialog_style

    def add_style(self,
            style_name: str,
            style_definition: str
        ) -> None:
        """Metoda pro dočasné přidání nového stylu"""
        self.print_styles_dict[style_name] = style_definition
        self._print_style = Style.from_dict(self.print_styles_dict)

    def print(self,
            *args: Union[
                str,
                Tuple[str, str],
                List[Tuple[str, str]
            ]
        ]) -> None:
        """
        Univerzální metoda pro tisk textu s různými styly.

        *args: Může být:
            - str: Prostý text k vytištění
            - (str, str): (styl, text) pro stylovaný tisk
            - List[Tuple[str, str]]: Seznam párů (styl, text) pro komplexní formátování


        Použití:
            print("Hello")  # Běžný tisk
            print("success", "Hello")  # Stylovaný tisk
            print([("success", "Hello"), ("error", "World")])  # Komplexní tisk
        """

        # Když není zadán žádný argument
        # Vytiskne se prázdný řádek
        if not args:
            print()

        # Když je zadán jeden argument
        # Prostý text nebo list formátovaných textů
        elif len(args) == 1:
            self._one_args_handler(args)

        # Když jsou zadány dva argumenty
        # Styl a text
        elif len(args) == 2:
            style, text = args
            self._two_args_handler(style, text)

    def _print_styled(self,
            formatted_items: List[Tuple[str, str]],
            list_check = False
        ) -> None:
        """Vytiskne formátovaný text"""

        # Kontrola zda jde o zkontrolovaný obsah
        if not list_check:
            self._list_args_check(formatted_items)

        # Vytištění obsahu
        print_formatted_text(
            FormattedText(formatted_items),
            style=self._print_style
        )

    def _one_args_handler(self, args):
        """Když je zadán jeden argument"""

        # Zachycení zadání samotného textu
        if isinstance(args, str):
            print(args)

        # Spracování seznamu
        elif isinstance(args, list):

            # Kontrola obsahu seznamu
            self._list_args_check(args, list_check=True)

            # Příprava a vytištění obsahu
            formatted_texts = self._formate_list_args(args, list_check=True)
            self._print_styled(formatted_texts, list_check=True)

    @staticmethod
    def _list_args_check(args, list_check=False):
        """Zvaliduje seznam zda obsahuje tuple se str"""

        # Kontrola zda jde o seznam
        if not list_check:
            if not isinstance(args, list):
                raise ValueError(
                    f"Zadaný argument není slovník. "
                    f"Typ zadaného argumentu: {type(args)}"
                )

        # Kontrola zda seznam obsahuje povolené položky
        # Každá položka je tuple se dvouma str
        if not all(isinstance(item, tuple)
                and len(item) == 2 for item in args):
            raise ValueError(
                "List must contain only tuples of (style, text)"
            )

    def _formate_list_args(self, args, list_check=False):
        """Naformátuje obsah seznamu"""

        # Kontrola obsahu
        if not list_check:
            self._list_args_check(args)

        # Výsledný seznam pro naformátované tuple
        formatted_texts = []

        # Cyklus procházející jednotlivá tuple
        for style, text in args:
            formatted_texts.append(
                # Zpracování podporovaných stylů
                self._format_text(style, text)
                if style in self.print_styles_dict
                # Zpracování nepodporovaných stylů
                else ("", text)
            )

        # Navrácení naformátovaných tuple
        return formatted_texts


    @staticmethod
    def _style_and_text_formate_check(style, text):
        """Kontrola zda styl a text jsou str"""

        if not isinstance(style, str) or not isinstance(text, str):
            raise ValueError(
                f"Styl a text musí být typu 'str'. "
                f"Zjištěné typy: styl = '{type(style)}', text = '{type(text)}'"
            )


    def _format_text(self, style, text, format_check=False):
        """Metoda navrací tuple se naformátovaným stylem a textem"""

        # Kontrola formátu
        if not format_check:
            self._style_and_text_formate_check(style, text)

        # Navrácení naformátovaného tuple
        return (f"class:{style}", text) if (
                style in self.print_styles_dict
        ) else ("", text)


    def _two_args_handler(self, style, text):
        """Metoda pro zpracování stylu a textu"""
        self._print_styled(
            [self._format_text(style, text),],
            list_check=True
        )


cli_printer = CliPrinter()
cli_print = cli_printer.print
cli_style = cli_printer.style