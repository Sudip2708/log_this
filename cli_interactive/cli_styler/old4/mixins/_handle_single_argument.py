from abc import ABC
from typing import Union, List, Tuple

from abc_helper import abc_method, abc_property
from ..utils import validate_list_arguments


class HandleSingleArgumentMixin(ABC):

    # Metoda pro naformátování stylu a textu
    _format_text = abc_method("_format_text")

    # Metoda pro vytisknutí naformátovaného obsahu
    _print_styled = abc_method("_print_styled")


    def _handle_single_argument(
            self,
            arg: Union[
                str,
                List[Tuple[str, str]]
            ]
    ):
        """Zpracuje případ, kdy je předán jeden argument"""

        # Kontrola zda je argument řetězec
        # Dojde k jeho vytištění
        if isinstance(arg, str):
            print(arg)

        # Pokud je argumentem seznam
        elif isinstance(arg, list):

            # Validace argumentů
            validate_list_arguments(arg)

            # Vytvoření naformátovaného seznamu
            formatted_texts = [
                self._format_text(style, text)
                for style, text in arg
            ]

            # Vytištění naformátovaného obsahu
            self._print_styled(formatted_texts)