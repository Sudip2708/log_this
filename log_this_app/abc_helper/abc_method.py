import abc
from typing import Any, Callable, TypeVar


def abc_method(
        name: str,
        return_type: type = None,
        *params: str
) -> Callable:
    """
    Vytvoří abstraktní metodu s flexibility pro pojmenování a typování.

    Args:
        name: Název metody
        return_type: Očekávaný návratový typ
        *params: Volitelné parametry metody

    Returns:
        Abstraktní metoda
    """

    def method_stub(self, *args: Any) -> Any:
        pass

    method_stub.__name__ = name
    if return_type:
        method_stub.__annotations__['return'] = return_type

    return abc.abstractmethod(method_stub)
