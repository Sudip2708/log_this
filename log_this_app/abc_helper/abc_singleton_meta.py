import abc
from typing import Any
from threading import Lock


class AbcSingletonMeta(abc.ABCMeta):
    """
    Metaclass prothread-safe singleton implementaci s podporou abstraktních tříd.

    Umožňuje:
    - Garantovat jedinou instanci třídy
    - Bezpečnou inicializaci v multi-threadovém prostředí
    - Smazání instance pro testovací účely
    """
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> 'AbcSingletonMeta':
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]

    def clear_instance(cls) -> None:
        """Vymaže singleton instanci pro testovací účely."""
        with cls._lock:
            if cls in cls._instances:
                del cls._instances[cls]

