from abc import ABC
from typing import Union, List, Tuple

from abc_helper import abc_method, abc_property


class CliPrintMixin(ABC):

    # Metoda pro zpracování zadání jednoho arguentu
    _handle_single_argument = abc_method("_handle_single_argument")

    # Metoda pro zpracování zadání dvou arguentu
    _handle_styled_text = abc_method("_handle_styled_text")


    def cli_print(self,
            *args: Union[
                str,
                Tuple[str, str],
                List[Tuple[str, str]]
            ]
    ) -> None:
        """
        Univerzální metoda pro tisk textu s různými styly.

        *args: Může být:
            - str: Prostý text k vytištění
            - (str, str): (styl, text) pro stylovaný tisk
            - List[Tuple[str, str]]: Seznam párů (styl, text) pro komplexní formátování
        """

        # Pokud není zadán žádný argument vytiskne se prázdný řádek
        if not args:
            print()

        # Zpracování jednoho argumentu (text nebo seznam)
        elif len(args) == 1:
            self._handle_single_argument(args[0])

        # Zpracování zadání dvou argumentů (styl a text)
        elif len(args) == 2:
            self._handle_styled_text(*args)