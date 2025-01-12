print("log_this/manager/ansi_styler/utils/__init__.py")
from .process_text_with_ansi_styles import process_text
from .get_available_styles import get_available_styles

__all__ = [
    "process_text",  # Funkce pro spracování textu
    "get_available_styles",  # Funkce pro navrácení dostupných stylů
]