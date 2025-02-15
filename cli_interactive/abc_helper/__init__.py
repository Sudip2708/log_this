from .abc_singleton_meta import AbcSingletonMeta
from .abc_property import abc_property
from .abc_method import abc_method

__all__ = [
    "AbcSingletonMeta",  # Thread-safe implementace Singleton vzoru pro ABC třídy.
    "abc_property",  # Vytvoří abstraktní property s getterem a setterem.
    "abc_method",  # Vytvoří abstraktní metodu s definovanými parametry.
]