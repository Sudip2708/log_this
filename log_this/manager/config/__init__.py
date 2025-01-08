# # file: __init__.py
# from .ansi_formatter import (
#     ANSIFormatter,
#     style,
#     sset,
#     sreset,
# )
#
# # Dynamické vytvoření __all__
# __all__ = [
#     'ANSIFormatter',
#     'style',
#     'sset',
#     'sreset',
# ]
#
# # Přidání všech dostupných stylů a barev do __all__
# for attr_name in dir(style):
#     if not attr_name.startswith('_') and attr_name not in {'set', 'reset'}:
#         globals()[attr_name] = getattr(style, attr_name)
#         __all__.append(attr_name)