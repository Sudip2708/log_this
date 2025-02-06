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
    get_styles = style_config.get_styles
    if not style_config:
        raise ValueError(f"Neznámý styl: {style}")

    texts = []
    style_dict = {}

    if info:
        texts.append((f'class:{style}.info', f'{style_config.symbol} {info}\n'))
        style_dict[f'{style}.info'] = get_styles(style_config.info)

    if detail:
        texts.append((f'class:{style}.detail', f'{detail}\n'))
        style_dict[f'{style}.detail'] = get_styles(style_config.detail)

    if hint:
        texts.append((f'class:{style}.hint', f'{hint}\n'))
        style_dict[f'{style}.hint'] = get_styles(style_config.hint)

    if conclusion:
        texts.append((f'class:{style}.hint', f'{hint}\n'))
        style_dict[f'{style}.hint'] = get_styles(style_config.hint)

    print_formatted_text(
        FormattedText(texts),
        style=Style.from_dict(style_dict)
    )

