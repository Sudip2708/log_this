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

    @property
    def style(self):
        """Vrací styl pro dialogy"""
        return self._dialog_style

    def add_style(self, style_name: str, style_definition: str) -> None:
        """Metoda pro dočasné přidání nového stylu"""
        self.print_styles_dict[style_name] = style_definition
        self._print_style = Style.from_dict(self.print_styles_dict)

    def print(self, *args: Union[
        str, Tuple[str, str], List[Tuple[str, str]]]) -> None:
        """
        Univerzální metoda pro tisk textu s různými styly.

        *args: Může být:
            - str: Prostý text k vytištění
            - (str, str): (styl, text) pro stylovaný tisk
            - List[Tuple[str, str]]: Seznam párů (styl, text) pro komplexní formátování
        """
        if not args:
            print()
        elif len(args) == 1:
            self._handle_single_argument(args[0])
        elif len(args) == 2:
            self._handle_styled_text(*args)

    def _print_styled(self, formatted_items: List[Tuple[str, str]]) -> None:
        """Vytiskne formátovaný text"""
        print_formatted_text(FormattedText(formatted_items),
                             style=self._print_style)

    def _handle_single_argument(self, arg):
        """Zpracuje případ, kdy je předán jeden argument"""
        if isinstance(arg, str):
            print(arg)
        elif isinstance(arg, list):
            self._validate_list_arguments(arg)
            formatted_texts = [self._format_text(style, text) for style, text in
                               arg]
            self._print_styled(formatted_texts)

    def _handle_styled_text(self, style: str, text: str):
        """Zpracuje případ, kdy jsou předány dva argumenty: styl a text"""
        self._validate_style_and_text(style, text)
        self._print_styled([self._format_text(style, text)])

    @staticmethod
    def _validate_list_arguments(args):
        """Zkontroluje, zda seznam obsahuje pouze dvojice (style, text)"""
        if not isinstance(args, list) or not all(
                isinstance(item, tuple) and len(item) == 2 for item in args):
            raise ValueError("List must contain only tuples of (style, text)")

    @staticmethod
    def _validate_style_and_text(style, text):
        """Zkontroluje, zda styl i text jsou řetězce"""
        if not isinstance(style, str) or not isinstance(text, str):
            raise ValueError("Styl a text musí být typu 'str'")

    def _format_text(self, style: str, text: str) -> Tuple[str, str]:
        """Formátuje text podle zadaného stylu"""
        return (
        f"class:{style}", text) if style in self.print_styles_dict else (
        "", text)


cli_printer = CliPrinter()
cli_print = cli_printer.print
cli_style = cli_printer.style