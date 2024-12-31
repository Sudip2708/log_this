from ._getitem import GetItemMixin
from ._str import StrMixin

__all__ = [
    "StrMixin",  # Vrací čitelnou reprezentaci konfigurace.
    "GetItemMixin",  # Vrací hodnotu pro daný klíč.
]