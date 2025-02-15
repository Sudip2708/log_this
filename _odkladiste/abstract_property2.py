from abc import abstractmethod
from functools import partial
from typing import Any


def abstract_property(name: str) -> property:
    """
    Vytvoří abstraktní property s getterem a setterem.

    Args:
        name: Název property

    Returns:
        property: Abstraktní property s getterem a setterem
    """

    def getter(self) -> Any:
        pass

    def setter(self, value: Any) -> None:
        pass

    return property(
        abstractmethod(getter),
        abstractmethod(setter)
    )


def abstract_method(name: str, *params: str) -> classmethod:
    """
    Vytvoří abstraktní metodu s definovanými parametry.

    Args:
        name: Název metody
        *params: Názvy parametrů metody

    Returns:
        classmethod: Abstraktní metoda
    """

    def method(self, *args, **kwargs) -> Any:
        pass

    # Vytvoříme dokumentaci s parametry
    params_doc = ', '.join(params)
    method.__doc__ = f"Abstract method {name}({params_doc})"

    return abstractmethod(method)


class ABCPropertyDecorator:
    """
    Dekorátor pro automatické přidávání properties a metod do třídy.
    """

    def __init__(self, cls):
        self.cls = cls

    @staticmethod
    def property(name: str) -> None:
        """
        Přidá abstraktní property do třídy.

        Args:
            name: Název property
        """

        def decorator(cls):
            setattr(cls, name, abstract_property(name))
            return cls

        return decorator

    @staticmethod
    def method(name: str, *params: str) -> None:
        """
        Přidá abstraktní metodu do třídy.

        Args:
            name: Název metody
            *params: Názvy parametrů metody
        """

        def decorator(cls):
            setattr(cls, name, abstract_method(name, *params))
            return cls

        return decorator


# Pomocné funkce pro přímé volání
def get_abc_property(name: str) -> None:
    """
    Přidá abstraktní property do aktuální třídy.

    Args:
        name: Název property
    """

    def decorator(cls):
        return ABCPropertyDecorator.property(name)(cls)

    return decorator


def get_abc_method(name: str, *params: str) -> None:
    """
    Přidá abstraktní metodu do aktuální třídy.

    Args:
        name: Název metody
        *params: Názvy parametrů metody
    """

    def decorator(cls):
        return ABCPropertyDecorator.method(name, *params)(cls)

    return decorator