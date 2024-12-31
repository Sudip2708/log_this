from ._context import ThreadContext
from .get_thread import get_thread

__all__ = [
    "ThreadContext",  # Singleton třída spravující vlákno pro logování.
    "get_thread",  # Hlavní funkce vracející singleton instanci třífy ThreadContext
]