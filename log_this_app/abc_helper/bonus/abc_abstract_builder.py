import abc
from typing import TypeVar, Generic

T = TypeVar('T')


class AbcAbstractBuilder(Generic[T]):
    """
    Generický abstraktní builder pro flexibilní tvorbu objektů.

    Umožňuje:
    - Definovat abstraktní kroky buildu
    - Flexibilní tvorbu složitých objektů
    """

    @abc.abstractmethod
    def build(self) -> T:
        """Vytvoří finální objekt."""
        pass

    @abc.abstractmethod
    def reset(self) -> None:
        """Resetuje aktuální stav builderu."""
        pass