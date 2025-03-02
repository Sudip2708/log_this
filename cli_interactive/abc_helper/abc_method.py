# print("abc_helper/abc_method.py")
from abc import abstractmethod
from typing import Any, Callable


def abc_method(name: str, *params: str) -> Callable:
    """
    Vytvoří abstraktní metodu s definovanými parametry.

    Args:
        name: Název metody
        *params: Názvy parametrů metody

    Returns:
        Callable: Abstraktní metoda
    """

    def method_stub(self, *args: Any) -> None:
        pass

    method_stub.__name__ = name
    return abstractmethod(method_stub)
