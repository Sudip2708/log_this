from ._get_styles_str import get_styles_str
from ._get_color_hex import get_color_hex
from ._validate_color import validate_color
from ._validate_style import validate_style

__all__ = [
    "get_styles_str",  # Funkce pro převod tuple se styli na jeden řetězec
    "get_color_hex",  # Funkce pro získání hex kodu barvy na základě jejího názvu
    "validate_color",  # Funkce pro validaci názvu barvy
    "validate_style",  # Funkce pro validaci názvu stylu
]