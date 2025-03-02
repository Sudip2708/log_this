from abc import ABC
from typing import List, Tuple
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text

from abc_helper import abc_property


class PrintStyledMixin(ABC):

    # Atribut se styli pro tisk
    _print_style = abc_property("_print_style")


    def _print_styled(self,
            formatted_items: List[Tuple[str, str]]
    ) -> None:
        """Vytiskne formátovaný text"""

        print_formatted_text(
            FormattedText(formatted_items),
            style=self._print_style
        )