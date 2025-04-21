# print("abc_helper/__init__.py")
from .abc_singleton_meta import AbcSingletonMeta
from .abc_property import abc_property
from .abc_method import abc_method
from abc import ABC

__all__ = [
    "ABC",
    "AbcSingletonMeta",  # Thread-safe implementace Singleton vzoru pro ABC třídy.
    "abc_property",  # Vytvoří abstraktní property s getterem a setterem.
    "abc_method",  # Vytvoří abstraktní metodu s definovanými parametry.
]