#
# from ._colors_and_styles import SUPPORTED_COLORS, SUPPORTED_STYLES
#
# def convert_styles(styles: Tuple[str, ...]) -> Tuple[str, ...]:
#     """
#     Převede definice stylů obsahující 'fg:' a 'bg:' na hex hodnoty.
#
#     Args:
#         styles: Tuple stylů jako řetězce.
#
#     Returns:
#         Tuple stylů, kde jsou 'fg:' a 'bg:' převedeny na hex.
#     """
#
#     convert_styles = []
#
#     for style in styles:
#
#
#
#
#
#     return tuple(
#         SUPPORTED_COLORS[color]
#         if style.startswith(('fg:', 'bg:'))
#            and (color := style.split(':')[1])
#            in SUPPORTED_COLORS
#         else style
#         for style in styles
#     )
