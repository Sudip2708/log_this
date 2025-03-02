# print("abc_helper/abc_property.py")
from abc import abstractmethod
from typing import Any, Callable


def abc_property(name: str) -> property:
    """
    Vytvoří abstraktní property s getterem a setterem.

    Args:
        name: Název property

    Returns:
        property: Abstraktní property
    """

    def getter(self) -> Any:
        pass

    def setter(self, value: Any) -> None:
        pass

    getter.__name__ = f"get_{name}"
    setter.__name__ = f"set_{name}"

    return property(
        abstractmethod(getter),
        abstractmethod(setter)
    )