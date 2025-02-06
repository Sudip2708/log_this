from typing import Tuple, List

from ._get_color_hex import get_color_hex
from ._validate_style import validate_style


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
        if style.startswith(('fg:', 'bg:')):

            # Vytažení názvu barvy
            color = style.split(':')[1]
            hex_color = get_color_hex(color)  # Součástí je validace, která vyvolá výjimku
            result.append(hex_color)

        # Zpracování ostatních stylů
        elif validate_style(style):  # Validace vyvolá výjimku
            result.append(style)

    # Vrátit styly jako string oddělený mezerami
    return ' '.join(result)

    # Napsat kod pro try expect zpracováváající výjimky pro validace a nebo zajíisti že budou zachytávané jinde