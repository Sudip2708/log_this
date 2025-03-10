from dataclasses import dataclass
from typing import Tuple, List

from ..utils import validate_color, validate_style

@dataclass
class CliStyle:
    """Konfigurace pro jednotlivé typy zpráv v CLI.

    Attributes:
        symbol: Znak použitý pro označení zprávy
        info: Tuple stylů pro informační zprávy
        detail: Tuple stylů pro detailní zprávy
        hint: Tuple stylů pro nápovědu
    """

    symbol: str = ''
    info: Tuple[str, ...] = ()
    detail: Tuple[str, ...] = ()
    hint: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        """Validuje všechny zadané styly při inicializaci objektu.

        Raises:
            ValueError: Pokud je detekován neplatný styl nebo barva
        """

        # Cyklus pro každý odstavec
        for style_tuple in (self.info, self.detail, self.hint):

            # Cyklus pro každý styl
            for style in style_tuple:

                # Zachycení stylů s barvou
                if style.startswith("fg:") or style.startswith("bg:"):
                    # Vytažení názvu barvy a validace
                    color = style.split(':')[1]
                    validate_color(color)  # Vyvolá výjimku
                else:
                    validate_style(style)  # Vyvolá výjimku



