from abc import abstractmethod
from functools import partial


def abstract_property(name):
    """
    Vytvoří abstraktní property s getterem a setterem.

    Použití:
    class MyABC:
        show_help = abstract_property('show_help')
        response = abstract_property('response')
    """

    def getter(self):
        pass

    def setter(self, value):
        pass

    # Vytvoříme property s abstraktními metodami
    return property(
        abstractmethod(getter),
        abstractmethod(setter)
    )


# Alternativní řešení pomocí dekorátoru třídy
def with_abstract_properties(*names):
    """
    Dekorátor třídy, který přidá abstraktní properties.

    Použití:
    @with_abstract_properties('show_help', 'response')
    class MyABC:
        pass
    """

    def decorator(cls):
        for name in names:
            setattr(cls, name, abstract_property(name))
        return cls

    return decorator