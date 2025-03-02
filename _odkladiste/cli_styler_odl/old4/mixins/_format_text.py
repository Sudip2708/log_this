from abc import ABC
from typing import Tuple

from abc_helper import abc_property


class FormatTextMixin(ABC):

    # Atribut uchovávající slovník se styli pro tisk
    print_styles_dict = abc_property("print_styles_dict")


    def _format_text(self, style: str, text: str) -> Tuple[str, str]:
        """Formátuje text podle zadaného stylu"""

        # Návratový formát pro podporované styly
        if style in self.print_styles_dict:
            return f"class:{style}", text

        # Návratový fromát pro nepodporované styly
        else:
            return "", text

