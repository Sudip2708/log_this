print("log_this/manager/ansi_styler/mixins/__init__.py")
from ._set_mixin import SetMixin
from ._proces_ansi_codes_mixin import ProcesAnsiCodesMixin

__all__ = [
    "SetMixin",  # Metoda pro definici stylů pro úpravu textu
    "ProcesAnsiCodesMixin",  # Mertoda pro zpracování ansi kodu
]