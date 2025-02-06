from dataclasses import dataclass
from typing import Tuple, List

from ._colors_and_styles import SUPPORTED_COLORS, SUPPORTED_STYLES


@dataclass
class CliStyleConfig:

    SUPPORTED_COLORS = SUPPORTED_COLORS
    SUPPORTED_STYLES = SUPPORTED_STYLES

    @staticmethod
    def get_styles_str(style_tuple: Tuple[str, ...]) -> str:
        """Zpracuje tuple stylů a vrátí je jako formátovaný string.

        Args:
            style_tuple: Tuple obsahující řetězce definující styly a barvy

        Returns:
            String obsahující zkontrolované styly oddělené mezerou

        Raises:
            ValueError: Pokud je detekován neplatný styl nebo barva
        """

        # Seznam pro zkontrolované styly
        result: List[str] = []

        # Cyklus pro každý styl
        for style in style_tuple:

            # Zachycení stylů s barvou
            if style.startswith("fg:") or style.startswith("bg:"):

                # Vytažení názvu barvy
                color = style.split(':')[1]
                hex_color = CliStyleConfig.get_color_hex(color)
                result.append(hex_color)

            # Zpracování ostatních stylů
            else:
                checked_style = CliStyleConfig.get_supported_style(style)
                result.append(checked_style)

        # Vrátit styly jako string oddělený mezerami
        return ' '.join(result)

    @staticmethod
    def get_color_hex(color: str) -> str:
        """Vrátí hex kód pro zadaný název barvy.

        Args:
            color: Název barvy k vyhledání

        Returns:
            Hex kód odpovídající barvě

        Raises:
            ValueError: Pokud barva není podporována
        """
        if CliStyleConfig.validate_color(color):
            return SUPPORTED_COLORS[color]
        return ''  # Nikdy se neprovede kvůli raise v validate_color

    @staticmethod
    def get_supported_style(style: str) -> str:
        """Validuje a vrátí podporovaný styl.

        Args:
            style: Název stylu k validaci

        Returns:
            Validovaný název stylu

        Raises:
            ValueError: Pokud styl není podporován
        """
        if CliStyleConfig.validate_style(style):
            return style
        return ''  # Nikdy se neprovede kvůli raise v validate_style

    @staticmethod
    def validate_color(color: str) -> bool:
        """Ověří, zda je barva podporována.

        Args:
            color: Název barvy k validaci

        Returns:
            True pokud je barva podporována

        Raises:
            ValueError: Pokud barva není podporována
        """
        if color not in SUPPORTED_COLORS.keys():
            raise ValueError(f"Neplatná barva: {color}")
        return True

    @staticmethod
    def validate_style(style: str) -> bool:
        """Ověří, zda je styl podporován.

        Args:
            style: Název stylu k validaci

        Returns:
            True pokud je styl podporován

        Raises:
            ValueError: Pokud styl není podporován
        """
        if style not in SUPPORTED_STYLES.keys():
            raise ValueError(f"Neplatný styl: {style}")
        return True