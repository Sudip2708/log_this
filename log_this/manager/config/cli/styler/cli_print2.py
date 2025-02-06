from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from prompt_toolkit.styles import Style
from typing import Union, Tuple

from .config import CLI_STYLE_REGISTRY


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
        style: Typ zprávy ('info', 'warning', etc.)
        info: Hlavní informační text
        detail: Doplňující informace
        hint: Nápověda
        conclusion: Závěrečné doporučení
    """
    style_config = CLI_STYLE_REGISTRY.get(style)

    if not style_config:
        raise ValueError(f"Neznámý styl: {style}")

    get_styles = style_config.get_styles
    texts = []
    style_dict = {}

    def process_text(text_type: str, text_value: Union[Tuple[str, ...], str]):
        """Pomocná funkce pro zpracování tuple vs. string"""
        if text_value:
            style_key = f'class:{style}.{text_type}'
            style_dict[style_key] = get_styles(getattr(style_config, text_type))

            if isinstance(text_value, tuple):
                for line in text_value:
                    texts.append((style_key, f"{line}\n"))
            else:
                texts.append((style_key, f"{text_value}\n"))

    process_text('info', info)
    process_text('detail', detail)
    process_text('hint', hint)
    process_text('conclusion', conclusion)

    print_formatted_text(
        FormattedText(texts),
        style=Style.from_dict(style_dict)
    )
