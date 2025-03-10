from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from prompt_toolkit.styles import Style
from typing import Union, Tuple

from .config import CLI_STYLE_REGISTRY
from .cli_text_processor import process_text  # Import nové funkce


def cli_print(
        style: str = '',
        info: Union[Tuple[str, ...], str] = None,
        detail: Union[Tuple[str, ...], str] = None,
        hint: Union[Tuple[str, ...], str] = None,
        conclusion: Union[Tuple[str, ...], str] = None
) -> None:
    """
    Vytiskne stylovanou zprávu do konzole.

    Args:
        style: Typ zprávy ('info', 'warning', etc.).
        info: Hlavní informační text.
        detail: Doplňující informace.
        hint: Nápověda.
        conclusion: Závěrečné doporučení.
    """
    style_config = CLI_STYLE_REGISTRY.get(style)

    if not style_config:
        raise ValueError(f"Neznámý styl: {style}")

    get_styles = style_config.get_styles
    texts = []
    style_dict = {}

    # Použití nové funkce pro zpracování textu
    process_text(style, 'info', info, get_styles, style_dict, texts)
    process_text(style, 'detail', detail, get_styles, style_dict, texts)
    process_text(style, 'hint', hint, get_styles, style_dict, texts)
    process_text(style, 'conclusion', conclusion, get_styles, style_dict, texts)

    print_formatted_text(
        FormattedText(texts),
        style=Style.from_dict(style_dict)
    )




from typing import Union, Tuple, List

def process_text(
        style: str,
        text_type: str,
        text_value: Union[Tuple[str, ...], str],
        get_styles,
        style_dict: dict,
        texts: List[tuple]
) -> None:
    """
    Pomocná funkce pro zpracování textu (podpora tuple i stringů).

    Args:
        style: Název stylu zprávy ('info', 'warning', etc.).
        text_type: Typ textu ('info', 'detail', 'hint', 'conclusion').
        text_value: Samotná zpráva (může být tuple nebo string).
        get_styles: Funkce pro získání stylu.
        style_dict: Slovník pro uložení stylů.
        texts: Seznam formátovaných textů pro výpis.
    """
    if text_value:
        style_key = f'class:{style}.{text_type}'
        style_dict[style_key] = get_styles(text_type)

        if isinstance(text_value, tuple):
            for line in text_value:
                texts.append((style_key, f"{line}\n"))
        else:
            texts.append((style_key, f"{text_value}\n"))
