import abc
from typing import Any, TypeVar


def abc_property(
        name: str,
        prop_type: type = Any
) -> property:
    """
    Vytvoří abstraktní property s flexibilním typováním.

    Args:
        name: Název property
        prop_type: Typ property

    Returns:
        Abstraktní property
    """

    def getter(self) -> Any:
        raise NotImplementedError(
            f"Abstract property {name} musí být implementována")

    def setter(self, value: Any) -> None:
        raise NotImplementedError(
            f"Abstract property {name} musí být implementována")

    getter.__name__ = f"get_{name}"
    setter.__name__ = f"set_{name}"

    return property(
        abc.abstractmethod(getter),
        abc.abstractmethod(setter)
    )
